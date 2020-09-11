import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import {Router} from '@angular/router'
@Component({
  selector: 'app-landing',
  templateUrl: './landing.component.html',
  styleUrls: ['./landing.component.scss']
})
export class LandingComponent implements OnInit {
  valid: string;

  constructor(private route: Router, private http: HttpClient) { }

  ngOnInit(): void {
  }

  onRegister(){
    alert("register")
    this.route.navigate(['/register'])
  }

  onLogin(){
    const email = (<HTMLInputElement>document.getElementById("email")).value;
    const password = (<HTMLInputElement>document.getElementById("password")).value;
    const data = {'email':email, 'password':password};
    alert(email)
    this.http.post<any>("http://localhost:8000/api/users/login",data)
    .subscribe((
      data) => {
        this.valid = data.valid;
      },
      err => alert("ERROR:"+ err.message)
    );
    if(this.valid=="true"){
      this.route.navigate(['/home'])
    }
  }


}
