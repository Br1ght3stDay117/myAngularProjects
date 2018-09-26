import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { environment } from '../../environments/environment';
@Injectable({
  providedIn: 'root'
})
export class MovieService {
  httpHeaders = new HttpHeaders({'Content-Type' : 'application/json; charset=utf-8'});
  baseUrl: string = environment.apiUrl;

  constructor( private http: HttpClient) { }

  getMovies(): Observable <any> {
    return this.http.get(this.baseUrl + 'movies/', this.getAuthHeaders());
  }

  private getAuthHeaders() {
    const token = localStorage.getItem('token');
    const httpHeaders = new HttpHeaders(
      {'Content-Type': 'application/json; charset=utf-8',
      'Authorization': 'Token ' + token});
    return { headers: httpHeaders};
  }
}
