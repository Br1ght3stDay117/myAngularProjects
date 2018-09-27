import { Component, OnInit } from '@angular/core';
import { User } from '../models/user';
import { Subscription } from 'rxjs';
import { GlobalService } from '../services/global.service';
import { Router } from '@angular/router';
import { MovieService } from '../services/movie.service';
import { Movie } from '../models/movie';
import { FormGroup, Validators, FormBuilder } from '@angular/forms';
import { MatSnackBar } from '@angular/material';

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
  movieInput: FormGroup;
  isAddEditMode: boolean;
  isEdit: boolean;

  // tslint:disable-next-line:max-line-length
  constructor(private router: Router , private globalService: GlobalService , private movieService: MovieService, private fb: FormBuilder, public snackBar: MatSnackBar) { }

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
    this.isAddEditMode = false;
    this.movieInput = this.fb.group({
      title: ['', Validators.required],
      description: ['', Validators.required]
    });
  }
  getMovies() {
    this.movieService.getMovies().subscribe(
      response => {
        this.movies = response;
        console.log('movies', response);
      },
      error => {
        console.log('error', error);
        this.snackBar.open('Error getting movies', '', { duration: 3000 });
      }
    );
  }
  movieClicked(movie: Movie) {
    this.selectedMovie = movie;
    this.isAddEditMode = false;
  }
  private doLogout() {
    this.globalService.me = new User();
    localStorage.removeItem('token');
    localStorage.removeItem('user');
    this.router.navigate(['/login']);
  }
  editMovieClicked() {
    this.isEdit = true;
    this.isAddEditMode = true;
    this.movieInput = this.fb.group({
      title: [this.selectedMovie.title, Validators.required],
      description: [this.selectedMovie.description, Validators.required]
    });
  }
  addMovieClicked() {
    this.isEdit = false;
    this.isAddEditMode = true;
    this.selectedMovie = null;
    this.movieInput.reset();
  }
  deleteMovieClicked () {
    this.movieService.deleteMovie(this.selectedMovie.id).subscribe(
      response => {
        const movIndex = this.movies.map(function(e) {return e.id; }).indexOf(this.selectedMovie.id);
        if (movIndex >= 0) {
          this.movies.splice(movIndex, 1);
          this.selectedMovie = null;
        }
        this.isAddEditMode = false;
      },
      error => {
        console.log('error', error);
        this.snackBar.open('Error deleting movies', '', { duration: 3000 });
      }
    );
  }
  submitMovie() {
    if (this.isEdit) {
      this.movieService.editMovie(this.movieInput.value, this.selectedMovie.id).subscribe(
        response => {
          const movIndex = this.movies.map(function(e) {return e.id; }).indexOf(this.selectedMovie.id);
          if (movIndex >= 0) {
            this.movies[movIndex] = response;
            this.selectedMovie = response;
          }
          this.movieInput.reset();
          this.isAddEditMode = false;
        },
        error => {
          console.log('error', error);
          this.snackBar.open('Error editing movie', '', { duration: 3000 });
        }
      );
    } else {
      this.movieService.addMovie(this.movieInput.value).subscribe(
        response => {
          this.movies.push(response);
          this.movieInput.reset();
          this.isAddEditMode = false;
        },
        error => {
          console.log('error', error);
          this.snackBar.open('Error saving movie', '', { duration: 3000 });
        }
      );
    }
  }

}
