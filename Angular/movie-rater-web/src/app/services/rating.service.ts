import { Injectable } from '@angular/core';
import { HttpHeaders, HttpClient } from '@angular/common/http';
import { environment } from '../../environments/environment';
import { Observable } from 'rxjs';

@Injectable()
export class RatingService {
  httpHeaders = new HttpHeaders({'Content-Type': 'application/json; charset=utf-8'});
  baseUrl: string = environment.apiUrl;

  constructor(private http: HttpClient) { }

  addRating(user_id: number, movie_id: number, rating: number): Observable<any> {
    const body = {
      user: user_id,
      movie: movie_id,
      stars: rating,
    };
    return this.http.post(this.baseUrl + 'rating/', body, this.getAuthHeaders());
  }

  private getAuthHeaders() {
    const token = localStorage.getItem('token');
    const httpHeaders = new HttpHeaders(
      {'Content-Type': 'application/json; charset=utf-8',
      'Authorization': 'Token ' + token});
    return { headers: httpHeaders};
  }
}
