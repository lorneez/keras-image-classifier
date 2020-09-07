import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { FormGroup, FormBuilder } from '@angular/forms';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})

export class HomeComponent implements OnInit {
  selectedFile: File = null;
  url: string;
  uploadform: FormGroup;

  // constructor(private http: HttpClient) { }
  constructor(public fb: FormBuilder){
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
      this.selectedFile = <File>event.target.files[0];
       // this.selectedFile = <File> event.target.files[0];
       // const fd = new FormData();
    // fd.append('image',this.selectedFile,this.selectedFile.name);
    // console.log(event);
    }
   
    


  onUpload(){
    // this.http.post("url",fd)
    // .subscribe(res =>{
    //   console.log(res);
    // });
  }
}
