import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-landing',
  templateUrl: './landing.component.html',
  styleUrls: ['./landing.component.scss']
})
export class LandingComponent implements OnInit {
  router: any;
  valid: string;

  constructor(private http: HttpClient) { }

  ngOnInit(): void {
  }

  onRegister(){
    alert("register")
    this.router.navigateURL(['/register'])
  }

  onLogin(){
    const email = <HTMLInputElement>document.getElementById("email").value;
    alert(email)
    this.http.post<any>("http://localhost:8000/api/users/login",email)
    .subscribe((
      data) => {
        this.valid = data.valid;
      },
      err => alert("ERROR:"+ err.message)
    );
    if(this.valid=="true"){
      this.router.navigateURL(['/home'])
    }
  }


}
