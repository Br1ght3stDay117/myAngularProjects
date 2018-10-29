import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PreRegistroComponent } from './pre-registro/pre-registro.component';
import { InstitucionProcedenciaComponent } from './institucion-procedencia/institucion-procedencia.component';
import {CoreModule} from '../core/core.module';


@NgModule({
  imports: [
    CommonModule,
    CoreModule,
  ],
  declarations: [PreRegistroComponent, InstitucionProcedenciaComponent],
  exports: [PreRegistroComponent, InstitucionProcedenciaComponent]
})
export class AdmisionesModule { }
