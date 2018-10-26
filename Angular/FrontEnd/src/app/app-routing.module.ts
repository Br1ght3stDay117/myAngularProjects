import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';
import { PreRegistroComponent } from './admisiones/pre-registro/pre-registro.component';

const routes: Routes = [
  {path: '', redirectTo: '/admisiones', pathMatch: 'full'},
  {path: 'admisiones', component: PreRegistroComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes), CommonModule ],
  exports: [RouterModule]
})
export class AppRoutingModule { }
