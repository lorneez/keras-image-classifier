import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { FormGroup, FormBuilder } from '@angular/forms';

interface response{
  label:string;
  prob:number;
}

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})

export class HomeComponent implements OnInit {
  selectedFile: File = null;
  url: string;
  uploadform: FormGroup;
  predictedLabel: string;
  predictedProbability: number;

  constructor(public fb: FormBuilder, private http: HttpClient){
    this.uploadform = this.fb.group({
      avatar: [null],
      name:['']
    })
  }

  ngOnInit(): void {
  }

  onFileSelected(event){
      const file = (event.target as HTMLInputElement).files[0];
      this.uploadform.patchValue({
        avatar: file
      });
      this.uploadform.get('avatar').updateValueAndValidity()
      const reader = new FileReader();
      reader.onload = () =>{
        this.url = reader.result as string;
      }
      reader.readAsDataURL(file)
      this.selectedFile = file;
    }

    onUpload(){
      const fd = new FormData();
      fd.append('image',this.selectedFile,this.selectedFile.name);
      this.http.post<any>("http://localhost:8080/", fd).subscribe(
        (data) => {
          this.predictedProbability = data.prob1;
          this.predictedLabel = data.class1;
          },
        err =>  alert("ERROR: " + err.message)
      );
  }
}
