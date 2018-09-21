import { Component, OnInit } from '@angular/core';
import { User } from '../models/user';
import { Subscription } from 'rxjs';
import { GlobalService } from '../services/global.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  account: User = new User();
  userSub: Subscription;

  constructor(private router: Router , private globalService: GlobalService) { }

  ngOnInit() {
    this.userSub = this.globalService.user.subscribe(
      account => this.account = account
    );
    console.log('account', this.account);
    if (localStorage.getItem('token') && localStorage.getItem('account')) {
      this.globalService.me = JSON.parse(localStorage.getItem('acount'));
      this.getMovies();
    } else {
      this.router.navigate(['/login']);
    }
  }
  getMovies() {
    console.log('hey');
  }

}
