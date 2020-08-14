import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class EmbraceService {

  constructor(private http: HttpClient) { }

  submitData(formData: any) {
    console.log('Submitting new request on Embrace.');
    return this.http.post('/api/embrace/closeOrder', formData);
  }
}
