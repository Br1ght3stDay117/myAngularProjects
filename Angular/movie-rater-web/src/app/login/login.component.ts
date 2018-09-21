import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { UserService } from '../services/user.service';
import { GlobalService } from '../services/global.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
  providers: [UserService],
})
export class LoginComponent implements OnInit {

  userLogin: FormGroup;
  loading: boolean;

  constructor(private fb: FormBuilder , private router: Router , private userService: UserService, private globalService: GlobalService) { }

  ngOnInit() {
    this.loading = false;
    this.userLogin = this.fb.group({
      username: ['', Validators.required],
      password: ['', Validators.required]
    });
  }
  goToHome() {
    this.router.navigate(['/home']);
  }
  onLogin() {
    this.loading = true;
    this.userService.userLogin(this.userLogin.value).subscribe(
      http_response => {
        this.loading = false;
        localStorage.setItem('token', http_response['token']);
        this.globalService.me = http_response['user'];
        console.log('response', http_response);
      },
      http_error => {
        this.loading = false;
        console.log('error', http_error);
      }
    );
    // console.log(this.userLogin.value);
  }
}
