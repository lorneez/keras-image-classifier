import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})
export class RegisterComponent implements OnInit {
  success: String;

  constructor(private route: Router, private http: HttpClient) { }

  ngOnInit(): void {
  }

  onRegisterSubmit(){
    const username = (<HTMLInputElement>document.getElementById("username")).value;
    const email =  (<HTMLInputElement>document.getElementById("email")).value;
    const password = (<HTMLInputElement>document.getElementById("password")).value;
    const data = {"username": username, "email":email, "password":password};
    this.http.post("http://localhost:8000/api/users/register",data)
    .subscribe((
      data) => {
        // this.success = data.success;
      },
      err => alert("ERROR:"+ err.message)
    );
    if(this.success=="true"){
      this.route.navigate(['/landing'])
    }
  }

}
