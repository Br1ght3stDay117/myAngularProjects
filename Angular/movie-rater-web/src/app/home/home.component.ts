import { Component, OnInit } from '@angular/core';
import { User } from '../models/user';
import { Subscription } from 'rxjs';
import { GlobalService } from '../services/global.service';
import { Router } from '@angular/router';
import { MovieService } from '../services/movie.service';
import { Movie } from '../models/movie';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css'],
  providers: [MovieService]
})
export class HomeComponent implements OnInit {

  account: User = new User();
  userSub: Subscription;
  username;
  movies;
  selectedMovie: Movie;

  constructor(private router: Router , private globalService: GlobalService , private movieService: MovieService) { }

  ngOnInit() {
    this.userSub = this.globalService.user.subscribe(
      me => this.account = me
    );
    if ( localStorage.getItem('token') && localStorage.getItem('account')) {
      this.username = localStorage.getItem('account');
      // console.log('username', this.username);
      this.username = JSON.parse(this.username);
      // console.log('JSON parse', this.username);
      this.globalService.me = this.username;
      // console.log('Global Service', localStorage.getItem('account'));
      // this.globalService.me = JSON.parse(localStorage.getItem('account'));
      this.getMovies();
    } else {
      this.router.navigate(['/login']);
    }
  }
  getMovies() {
    this.movieService.getMovies().subscribe(
      response => {
        this.movies = response;
        console.log('movies', response);
      },
      error => {
        console.log('error', error);
      }
    );
  }
  movieClicked(movie: Movie) {
    this.selectedMovie = movie;
    console.log('movie clicked: ', movie);
  }
  private doLogout() {
    this.globalService.me = new User();
    localStorage.removeItem('token');
    localStorage.removeItem('user');
    this.router.navigate(['/login']);
  }

}
