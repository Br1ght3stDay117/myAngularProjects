import { Component, OnInit, ViewEncapsulation} from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Validators, FormGroup, FormBuilder } from '@angular/forms';
import { Router } from '@angular/router';

export interface InstitucionProcedenciaDialogo {
  apellidoPaterno: string;
  apellidoMaterno: string;
  nombre: string;
  institucionProcedencia: string;
}
export interface Estado {
  value: string;
  viewValue: string;
}
export interface Municipio {
  value: string;
  viewValue: string;
}
export interface Carrera {
  value: string;
  viewValue: string;
}
export interface Medio {
  value: string;
  viewValue: string;
}
export interface PeriodicElement {
  name: string;
  position: number;
  weight: number;
  symbol: string;
}
const ELEMENT_DATA: PeriodicElement[] = [
  {position: 1, name: 'Hydrogen', weight: 1.0079, symbol: 'H'},
  {position: 2, name: 'Helium', weight: 4.0026, symbol: 'He'},
  {position: 3, name: 'Lithium', weight: 6.941, symbol: 'Li'},
  {position: 4, name: 'Beryllium', weight: 9.0122, symbol: 'Be'},
  {position: 5, name: 'Boron', weight: 10.811, symbol: 'B'},
  {position: 6, name: 'Carbon', weight: 12.0107, symbol: 'C'},
  {position: 7, name: 'Nitrogen', weight: 14.0067, symbol: 'N'},
  {position: 8, name: 'Oxygen', weight: 15.9994, symbol: 'O'},
  {position: 9, name: 'Fluorine', weight: 18.9984, symbol: 'F'},
  {position: 10, name: 'Neon', weight: 20.1797, symbol: 'Ne'},
];

export class Telefono {
  pais: string;
  area: string;
  prefijo: string;
  linea: string;
  /*
    Formatear número com E.164
    E.164 es el nombre del documento que especifíca el formato, la estructura y la jerarquía administrativa de los números telefónicos.
    Un número E.164 está compuesto por el código de país. código de zona o ciudad y un número telefónico
  */
  get e164() {
    const num = this.pais + this.area + this.prefijo + this.linea;
    return `+${num}`;
  }
}

@Component({
  selector: 'app-pre-registro',
  templateUrl: './pre-registro.component.html',
  styleUrls: ['./pre-registro.component.scss']
})
export class PreRegistroComponent implements OnInit {
  closeResult: string;
  startDate = new Date(1990, 0, 1);
  institucionProcedencia: string;
  step = 0;
  estado: string;
  municipio: string;
  carrera1: string;
  carrera2: string;
  medio: string;
  loading: boolean;
  pre_Registro: FormGroup;
  telefono = new Telefono();
  displayedColumns: string[] = ['position', 'name', 'weight', 'symbol'];
  dataSource = ELEMENT_DATA;

  constructor(private modalService: NgbModal, private fb: FormBuilder, private router: Router) {
    this.pre_Registro = this.fb.group({
      apellidoPaterno: ['', Validators.required],
      apellidoMaterno: [''],
      nombre: ['', Validators.required],
      fechaNacimiento: ['', Validators.required],
      genero: ['', Validators.required],
      email: ['', [Validators.required, Validators.email]],
    });
  }

  estados: Estado[] = [
    {value: '1', viewValue: 'Querétaro'},
    {value: '2', viewValue: 'Guanajuato'},
    {value: '3', viewValue: 'Los datos se obtendrán del server'}
  ];

  municipios: Municipio[] = [
    {value: '1', viewValue: 'Cargar datos del server'}
  ];

  carreras: Carrera[] = [
    {value: '1', viewValue: 'Sistemas Rules'},
    {value: '2', viewValue: 'Cargar datos del server'}
  ];

  medios: Medio[] = [
    {value: '1', viewValue: 'Feria'},
    {value: '2', viewValue: 'Facebook'}
  ];

  setStep(index: number) {
    this.step = index;
  }

  nextStep() {
    this.step++;
  }

  prevStep() {
    this.step--;
  }

  preRegistro(content) {
    this.modalService.open(content, { size: 'lg' });
  }
  RegistraProspecto() {
    this.loading = true;
    console.log('I should do something');
  }
  ngOnInit() {
    this.loading = false;
  }

}
