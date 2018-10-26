import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { AdmisionesModule } from './admisiones/admisiones.module';
import { CoreModule } from './core/core.module';



@NgModule({
  imports: [
    BrowserModule,
    AppRoutingModule,
    AdmisionesModule,
    CoreModule,
  ],
  declarations: [
    AppComponent,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
