import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { InstitucionProcedenciaComponent } from './institucion-procedencia.component';

describe('InstitucionProcedenciaComponent', () => {
  let component: InstitucionProcedenciaComponent;
  let fixture: ComponentFixture<InstitucionProcedenciaComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ InstitucionProcedenciaComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(InstitucionProcedenciaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
