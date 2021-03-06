import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { environment } from '../../environments/environment';


@Injectable()
export class UserService {

  httpHeaders = new HttpHeaders({'Content-Type' : 'application/json; charset=utf-8'});
  baseUrl: string = environment.apiUrl;

  constructor( private http: HttpClient) { }

  userLogin(userLogin: any): Observable <any> {
    return this.http.post(this.baseUrl + 'authenticate/', userLogin , {headers: this.httpHeaders});
  }

  registerUser(userData: any): Observable<any> {
    console.log('HEADERS: ', this.httpHeaders);
    return this.http.post(this.baseUrl + 'users/', userData , this.getAuthHeaders());
  }
  private getAuthHeaders() {
    const token = localStorage.getItem('token');
    const httpHeaders = new HttpHeaders(
      {'Content-Type': 'application/json; charset=utf-8',
      'Authorization': 'Token ' + token});
    return { headers: httpHeaders};
  }
}
