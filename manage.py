from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=250)
    apellido_paterno = models.CharField(max_length=150)
    apellido_materno = models.CharField(max_length=150)
    fecha_nacimiento = models.DateField()
    estado_civil = models.CharField(max_length=150)
    nombre_padre = models.CharField(max_length=150)
    nombre_madre = models.CharField(max_length=150)
    tipo_sangre=models.CharField(max_length=150)
    curp = models.CharField(max_length=200)
    rfc = models.CharField(max_length=30)
    genero = models.CharField(max_length=150)
    correo_electronico = models.EmailField(max_length=250)
    persona_responsable = models.CharField(max_length=150)
    nss = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=150)
    edo_nacionalidad = models.CharField(max_length=150)
    municipio_nacionalidad = models.CharField(max_length=150)
    telefono_local = models.CharField(max_length=10)
    telefono_cel = models.CharField(max_length=10)
    telefono_otro = models.CharField(max_length=10)
    tag = models.CharField(max_length=150)
############################################################################
class Servicios(models.Model):
    pago = models.ForeignKey(Pago,on_delete=models.CASCADE)
    tipo_servicio=models.ForeignKey(TipoServicio,on_delete=models.CASCADE)
	estatus = models.ForeignKey(Estatus,on_delete=models.CASCADE)
    clave = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    salarios_menos = models.FloatField()
    costo = models.FloatField()
    concepto = models.CharField(max_length=150)
    departamento = models.CharField(max_length=150)
    vigencia = models.DateField()
    fecha_vencimiento = models.DateField()    
    autorizacion_flag = models.BooleanField()
    categoria_servicio = models.CharField(max_length=150)


class EstatusServicio(models.Model):
    descripcion=models.CharField(max_length=150)

class TipoServicio(models.Model):
    descripcion = models.CharField()
#################################################################################
class Pago(models.Model):
    persona = models.ForeignKey(Persona,on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo,on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicios,on_delete=models.CASCADE)
    estatus = models.ForeignKey(Estatus,on_delete=models.CASCADE)
    matricula = models.CharField(max_length=10)
    nombre_carrera = models.CharField(max_length=150)
    clave_referencia = models.CharField(max_length=150)
    concepto = models.CharField(max_length=150)
    importe = models.FloatField()
    fecha_efectiva = models.DateField()
    fecha_expiracion = models.DateField()
    adeudo_flag = models.BooleanField()
    convenio_flag = models.CharField(max_length=150)
    recibo_numero = models.BooleanField()
    reembolso_flag = models.BooleanField()
    factura_flag = models.CharField(max_length=150)
    generada_por = models.CharField(max_length=150)
    eliminado_por = models.CharField(max_length=150)

######################################################################################################
class Tarea(models.Model):
    tarea_parent = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=150)
    convocatoria_flag = models.CharField(max_length=150)

###########################################################################################

class Periodo(models.Model):
    tarea = models.ForeignKey(Tarea,on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=150)
    periodo_parent = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=150)
    fecha_inicio=models.DateField()
    fecha_fin=models.DateField()
    estatus = models.ForeignKey(Estatus,on_delete=models.CASCADE)


######################################################################################################
class Aspirante(models.Model):
    persona = models.ForeignKey(Persona,on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo,ondelete=models.CASCADE)
    pago = models.ForeignKey(Pago,on_delete=models.CASCADE)
    pago_curso = models.ForeignKey(PagoCurso,on_delete=models.CASCADE)
    folio_ceneval=models.CharField(max_length=150)
    folio =models.CharField(max_length=150)
    opciones_aspirante = models.OneToOneField(Opciones)
    carrera_seleccionada = models.CharField(max_length=150)
    trabaja = models.BooleanField()
    vive_con = models.CharField(max_length=150)
    depende = models.CharField(max_length=150)
    tsu_flag = models.CharField(max_length=150)
    tsu_carrera=models.CharField(max_length=150)
    tsu_escuela =models.CharField(max_length=150)
    dictar_flag = models.BooleanField()
    dictamen_filename= models.CharField(max_length=150)
    estatus = models.ForeignKey(Estatus,on_delete=models.CASCADE)
    resultado_final = models.IntegerField(max_length=10)    
    oferta_flag = models.CharField(max_length=150)
    tipo_registro = models.CharField(max_length=150)
    localizado = models.CharField(max_length=150)
    evalucaion_flag = models.CharField(max_length=150)
    correo_enviado = models.BooleanField()
    correo_admitido = models.BooleanField()
    control_ficha = models.OneToOneField(ControlFicha)
	

class Opciones(models.Model):  ###Cambiar
    primera_opcion = models.CharField(max_length=150)
    segunda_opcion = models.CharField(max_length=150)
    tercera_opcion = models.CharField(max_length=150)

class ControlFicha(models.Model):
    fecha = models.DateField()

############################################################################################################
class Estado(models.Model):
    clave = models.CharField(max_length=150)
    nombre_estado = models.CharField(max_length=150)
    corto = models.CharField(max_length=150)

class Municipio(models.Model):
    nombre = models.CharField(max_length=150)
    siglas = models.CharField(max_length=150)
    estado = models.ForeignKey(Estado,on_delete=models.CASCADE)


############################################################################################################

class Convocatoria(models.Model):
    tarea = models.ForeignKey(Tarea,on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo,on_delete=models.CASCADE)
    servicio=models.ForeignKey(Servicio,on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=150)
    informacion = models.CharField(max_length=150)
    estatus = models.ForeignKey(Estatus,on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

########################################################################################
class PagoConfig(models.Model):
    nombre_banco = models.CharField(max_length=150)
    convenio_cie = models.CharField(max_length=150)
    salario_minimo = models.FloatField()
    observaciones = models.CharField(max_length=150)
#########################################################################################
class CentroTrabajo(models.Model):
    estatus = models.ForeignKey(Estatus,on_delete=models.CASCADE)
    nombre_oficial =models.CharField(max_length=150)
    nombre_corto = models.CharField(max_length=150)
    clave_cct =models.CharField(max_length=150)
    clave_ceneval = models.CharField(max_length=150)
    turno = models.CharField(max_length=150)
    certificado_valido = models.CharField(max_length=150)
    nivel = models.IntegerField(max_length=10)
    domicilio = models.CharField(max_length=150)
    estado = models.ForeignKey(Estado,on_delete=models.CASCADE)
    localidad = models.CharField(max_length=150)
    cp = models.SmallIntegerField()


#####################################################################################
class Carrera(models.Model):
    nombre_oficial =models.CharField(max_length=150)
    nombre_corto=models.CharField(max_length=150)
    clave = models.CharField(max_length=150)
    siglas = models.CharField(max_length=150)
    objetivo = models.CharField(max_length=150)
    generacion = models.IntegerField(max_length=30)
    total_espacios_ciclo_escolar = models.IntegerField(max_length=40)
####################################################################################
#class NombreOficialCorto(models.Model):
#   oficial = models.CharField(max_length=150)
#  corto = models.CharField(max_length=10)
###############################################################################
class Grupo(models.Model):
    grupo_bloque = models.ForeignKey(GrupoBloque,on_delete=models.CASCADE)
    tipo_grupo = models.ForeignKey(TipoGrupo,on_delete=models.CASCADE)
    carrera = models.ForeignKey(Carrera,on_delete=models.CASCADE)
    numero_grupo = models.CharField(max_length=150)
    clave = models.CharField(max_length=150)
    capacidad = models.CharField(max_length=150)
    nivel = models.IntegerField(max_length=10)
    descripion = models.CharField(max_length=150)
    estatus = models.ForeignKey(Estatus,on_delete=models.CASCADE)

###############################################################################
class GrupoBloque(models.Model):
    descripcion = models.CharField(max_length=150)
    estatus = models.ForeignKey(Estatus,on_delete=models.CASCADE)
    hora_inicio=models.TimeField()
    hora_fin=models.TimeField()


class TipoGrupo(models.Model):
    descripcion = models.CharField(max_length=150)
###############################################################################
class Matricula(models.Model):
    grupo = models.ForeignKey(Grupo,on_delete=models.CASCADE)
    persona = models.ForeignKey(Persona,on_delete=models.CASCADE)
    plan_estudio = models.ForeignKey(PlanEstudio,on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo,on_delete=models.CASCADE)
    tipo_inscripcion = models.ForeignKey(TipoInscripcion,on_delete=models.CASCADE)
    estatus = models.ForeignKey(Estatus,on_delete=models.CASCADE)
    matricula =models.CharField(max_length=150)
    generacion=models.IntegerField()
    total_nc=models.FloatField()
    promedio_total=models.DecimalField()
    grupo_idioma=models.CharField(max_length=150)
    le_nivel=models.CharField(max_length=150)
    clave_grupo=models.CharField(max_length=150)
    inscripcion_flag=models.CharField(max_length=150)
    adeudo_flag=models.CharField(max_length=150)
    servicio_social_flag=models.CharField(max_length=150)
    titulacion_flag=models.CharField(max_length=150)
    foto_flag=models.CharField(max_length=150)
    bachillerato_avanzado_flag=models.CharField(max_length=150)
    materias_y_creditos = models.OneToOneField(MateriasCreditos,on_delete=models.CASCADE)

#Conectada Matricula, Inscripcion
class MateriasCreditos(models.Model):
    materias_reprobadas = models.IntegerField(max_length=50)
    creditos_reprobados = models.IntegerField(max_length=500)
    materias_aprobadas= models.IntegerField(max_length=50)
    creditos_aprobados = models.IntegerField(max_length=500)
    materias_cursadas = models.IntegerField(max_length=50)
    creditos_cursador= models.IntegerField(max_length=500)
    materias_no_cursadas = models.IntegerField(max_length=50)


###################################################################################
class PlanEstudio(models.Model):
    carrera = models.ForeignKey(Carrera,on_delete=models.CASCADE)
    estatus = models.ForeignKey(Estatus,on_delete=models.CASCADE)
    carrera_desc_corta=models.CharField(max_length=150)
    carrera_desc_larga=models.CharField(max_length=150)
    clave_mapa_curricular = models.CharField()
    total_cuatrimestre=models.IntegerField(max_length=15)
    total_horas = models.TimeField()
    total_creditos=models.IntegerField(max_length=500)
    total_materias=models.IntegerField(max_length=100)
    duracion=models.DurationField()
    fecha_revision = models.DateField()
    vigente_flag = models.BooleanField()

####################################################################################
class CicloFormacion(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=150)
    plan_estudio = models.ForeignKey(PlanEstudio,on_delete=models.CASCADE)

####################################################################################

class TipoAsignatura(models.Model):
    clave = models.CharField(max_length=150)
    nombre = models.CharField(max_length=150)

class AreaEstudio(models.Model):
    nombre = models.CharField(max_length=150)

class Materia(models.Model):
    plan_estudio = models.ForeignKey(PlanEstudio,on_delete=models.CASCADE)
    area_estudio = models.ForeignKey(AreaEstudio,on_delete=models.CASCADE)
    ciclo_formacion = models.ForeignKey(CicloFormacion,on_delete=models.CASCADE)
    tipo_asignatura = models.ForeignKey(TipoAsignatrua,on_delete=models.CASCADE)
    nombre_oficial=models.CharField(max_length=150)
    nombre_corto=models.CharField(max_length=150)
    objeto=models.CharField(max_length=150)
    justificacion=models.CharField(max_length=150)
    cuatrimestre=models.IntegerField(max_length=15)
    clave_rh=models.CharField(max_length=150)
    parciales = models.IntegerField()
    materias_horas = models.OneToOneField(HoraMateria,on_delete=models.CASCADE)
    estatus = models.ForeignKey(Estatus,on_delete=models.CASCADE)


class HoraMateria(models.Model):
    presencial = models.TimeField()
    semanal = models.DateField()
    tp = models.TimeField()
    tnp = models.TimeField()
    pp = models.TimeField()
    pnp = models.TimeField()
    cuatrimestre = models.TimeField()
    semanal_rh = models.DateField()
    cuatrimestre_rh = models.TimeField()
####################################################################################
class GrupoMateria(models.Model):
    materia = models.ForeignKey(Materias,on_delete=models.CASCADE)
    grupo = models.ForeignKey(Grupo,on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo,on_delete=models.CASCADE)
    plan_estudio = models.ForeignKey(PlanEstudio,on_delete=models.CASCADE)
    profesor_nombre = models.CharField(max_length=150)
    plan_asignatura = models.CharField(max_length=150)
    horario_aprobado_flag = models.BooleanField()
    folio_acta = models.CharField(max_length=150)
    estatus = models.ForeignKey(Estatus,on_delete=models.CASCADE)
    cuatrimestre = models.CharField(max_length=150)
    parciales_flag = models.BooleanField()
    fecha_firma = models.DateField()
    resultado_evaluacion = models.IntegerField(max_length=150)
    clave_grupo = models.CharField(max_length=30)
    nivel_idiomas = models.CharField(max_length=150)
    promedio = models.FloatField()
    nombre_periodo = models.CharField(max_length=150)
    area_estudio_nombre = models.CharField(max_length=150)
##########################################################################################################
class TipoInscripcion(models.Model):
    descripcion=models.CharField(max_length=150)

class Inscripcion(models.Model):
    pago = models.ForeignKey(Pago,on_delete=models.CASCADE)
    periodo=models.ForeignKey(Periodo,on_delete=models.CASCADE)
    matricula = models.ForeignKey(Matricula,on_delete=models.CASCADE)
    tipo_inscripcion=models.ForeignKey(TipoInscripcion,on_delete=models.CASCADE)
    grupo=models.ForeignKey(Grupo,on_delete=models.CASCADE)
    cuatrimestre=models.CharField(max_length=150)
    nombre_carrera=models.CharField(max_length=150)
    estatus = models.ForeignKey(Estatus,on_delete=models.CASCADE)
    total_materias=models.IntegerField(max_length=100)
    total_creditos=models.DecimalField(max_length=500)
    total_nc=models.IntegerField(max_length=100)
    promedio_total = models.DecimalField()
    carga_academica_tipo = models.CharField(max_length=150)
    carga_academica_flag = models.CharField(max_length=150)
    tipo_pago = models.CharField()
    evaluacion_flag = models.BooleanField()
    beca_flag = models.BooleanField()
    beca_observaciones = models.TextField(max_length=200)
    materias_creditos = models.OneToOneField(MateriasCreditos,on_delete=models.CASCADE)
###################################################################################################################

class CargaAcademica(models.Model):
    pago = models.ForeignKey(Pago,on_delete=models.CASCADE)
    inscripcion = models.ForeignKey(Inscripcion,on_delete=models.CASCADE)
    grupo_materia = models.ForeignKey(GrupoMateria,on_delete=models.CASCADE)
    tipo_materia=models.CharField(max_length=150)
    calificacion_final = models.DecimalField()
    tipo_evalucacion=models.CharField(max_length=150)
    porcentaje_unidades=models.CharField(max_length=150)
    procesada_flag=models.BooleanField()
    evaluada_flag=models.BooleanField()
    estatus = models.ForeignKey(Estatus,on_delete=models.CASCADE)
    evaluacion_inicio_flag=models.BooleanField()
    parciales = models.ManyToManyField(Parciales,primary_key=True,on_delete=models.CASCADE)
    parciales_finales = models.OneToOneField(ParcialesFinales,primary_key=True,on_delete=models.CASCADE)

class Parciales(models.Model):
    ca = models.ForeignKey(CargaAcademica,on_delete=models.CASCADE)
    parcial_1 = models.OneToOneField(Parcial1,primary_key=True,on_delete=models.CASCADE)
    parcial_2 = models.OneToOneField(Parcial2,primary_key=True,on_delete=models.CASCADE)
    parcial_3 = models.OneToOneField(Parcial3,primary_key = True,on_delete=models.CASCADE)

class Parcial1(models.Model):
    fecha_parcial = models.DateField()
    faltas_parcial = models.IntegerField(max_length=50)

class Parcial2(models.Model):
    fecha_parcial = models.DateField()
    faltas_parcial = models.IntegerField(max_length=50)

class Parcial3(models.Model):
    fecha_parcial = models.DateField()
    faltas_parcial = models.IntegerField(max_length=50)


class ParicalesFinales(models.Model):
    parcial1_final = models.OneToOneField(ParcialF1,primary_key=True,on_delete=models.CASCADE)
    parcial2_final = models.OneToOneField(ParcialF2,primary_key=True,on_delete=models.CASCADE)
    parcial3_final = models.OneToOneField(ParcialF3,primary_key=true,on_delete=models.CASCADE)

class ParcialF1(models.Model):
    estatus = models.ForeignKey(Estatus,on_delete=models.CASCADE)
    fecha = models.DateField()


class ParcialF2(models.Model):
    estatus = models.ForeignKey(Estatus,on_delete=models.CASCADE)
    fecha = models.DateField()

class ParcialF3(models.Model):
    estatus = models.ForeignKey(Estatus,on_delete=models.CASCADE)
    fecha = models.DateField()



#####################################################################################################################
class CoordinacionCarrera(models.Model):
    carrera = models.ForeignKey(Carrera,on_delete=models.CASCADE)
    persona = models.ForeignKey(Persona,on_delete=models.CASCADE)
    nombre_coordinador = models.CharField(max_length=150)
    tipo = models.CharField(max_length=150)
    puesto_carrera = models.CharField(max_length=150)

#####################################################################################################################
#                                                                                                                   #
#                                                                                                                   #
#                                                                                                                   #
#                                             En la Segunda Parte                                                   #
#                                                                                                                   #
#                                                                                                                   #
#                                                                                                                   #
#                                                                                                                   #
#####################################################################################################################




class Personal(models.Model):
    persona = models.ForeignKey(Persona,on_delete=models.CASCADE)
    rh_pago_nivel = models.ForeignKey(RhPago,on_delete=models.CASCADE)
    carrera = models.CharField(max_length=150)
    correo_institucional = models.EmailField(max_length=200)
    area_asignacion = models.CharField(max_length0150)
    cedula_profesional = models.CharField(max_length=150)
    no_empleado = models.IntegerField(max_length=100)
    tipo_contrato = models.CharField(max_length=150)
    fecha_ingreso = models.DateField()
    estatus = models.ForeignKey(Estatus,on_delete=models.CASCADE)
    biografia = models.TextField()
    foto = models.ImageField()
    hora_entrada = models.TimeField()
    hora_salida = models.TimeField()



#######################################################################################################################
class RhPago(models.Model):
    monto_por_hora = models.FloatField()
    nivel = models.CharField(max_length=150)
    nivel_abreviado=models.CharField(max_length=150)

########################################################################################################################

class PersonalPeriodo(models.Model):
    periodo = models.ForeignKey(Periodo,on_delete=models.CASCADE)
    personal = models.ForeignKey(Personal,on_delete=models.CASCADE)
    estatus = models.ForeignKey(Estatus,on_delete=models.CASCADE)
    total_horas_semanas = models.DateField()
    fecha_elaboracion = models.DateField()
    nombre_usuario_responsable = models.CharField(max_length=250)
    cantidad_semanas = models.IntegerField(max_length=100)
    comentarios_rh =models.CharField(max_length=150)
    comentarios_usuarios=models.CharField(max_length=150)
    resultado_ultima_evaluacion = models.CharField(max_length=10)
    resultado_clase_muestra = models.CharField(max_length=150)
    resultado_evaluacion = models.CharField(max_legnth=10)

########################################################################################################################

class SolicitudBeca(models.Model):
    persona = models.ForeignKey(Persona,on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo,on_delelte=models.CASCADE)
    tipo_beca = models.ForeignKey(TipoBeca,on_delete=models.CASCADE)
    matricula = models.ForeignKey(Matricula,on_delete=models.CASCADE)
	carrera = models.ForeignKey(Carrera, on_delelte=models.CASCADE)
    folio = models.CharField(max_length=200)
    renovacion = models.CharField(max_length=150)    
    materia_solicitud_beca = models.OneToOneField(MateriaBeca, primary_key=True)
    promedio_general = models.DecimalField()
    cuatrimestre = models.CharField(max_length=150)
    porcentaje = models.DecimalField(max_length=150)
    inscrito_flag = models.BooleanField()
    area_asignacion = models.CharField(max_length=150)
    nombre_proyecto = models.CharField(max_length=150)
    monto =models.DecimalField()
    monto_condonado=models.DecimalField()

class MateriaBeca(models.Model):
    reprobadas_actual = models.IntegerField(max_length=150)
    reprobadas_total = models.IntegerField(max_length=150)
    cursadas = models.IntegerField(max_length=100)
########################################################################################################################
class Beca(models.Model):
    estatus = models.ForeignKey(Estatus,on_delete=models.CASCADE)
    puntos = models.IntegerField(max_length=100)
    monto =models.DecimalField()
    monto_condonado=models.DecimalField()
    porcentaje=models.DecimalField()
    folio=models.CharField(max_length=150)

########################################################################################################################
class TipoBeca(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=150)
    tipo = models.CharField(max_length=150)
    categoria = models.CharField(max_length=150)
    porcentaje = models.DecimalField()
    unica_flag = models.CharField()
    estatus = models.ForeignKey(Estatus,on_delete=models.CASCADE)


########################################################################################################################

class Usuario(models.Model):
    acceso = models.ForeignKey(Acceso,on_delete=models.CASCADE)
    persona = models.ForeignKey(Persona,on_delete=models.CASCADE)
    ultimo_acceso = models.DateField()
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    correo_electronico = models.EmailField(max_length=250)
    expira = models.DateField()
    estatus = models.ForeignKey(Estatus,on_delete=models.CASCADE)
    tipo_cuenta = models.CharField(150)
    no_reinicio = models.IntegerField()


class Acceso(models.Model):
    nombre_completo = models.CharField(max_length=150)
    tipo_cuenta = models.CharField(max_length=150)
    ip = models.GenericIPAddressField(protocol='both', unpack_ipv4=False)
    termino = models.DateField()
    inicio = models.DateField()
########################################################################################################################
class Prospecto(models.Model):
    aspirante = models.ForeignKey(Aspirante,on_delete=models.CASCADE)
    localizado = models.BooleanField()
    correo_enviado = models.BooleanField()
    ulitmo_grado_cursado = models.CharField(max_length=150)
    opinion = models.TextField()
    dudas = models.TextField()
    universidad_opciones = models.OneToOneField(UniversidadOpciones,primary_key=True)

class UniversidadOpciones(models.Model):
    opcion_1=models.CharField(max_length=250)
    opcion_2 = models.CharField(max_length=250)
    opcion_3 = models.CharField(max_length=150)

########################################################################################################################
class AspirantesProyectados(models.Model):
    periodo = models.ForeignKey(Periodo,on_delete=models.CASCADE)
    plan_estudio = models.ForeignKey(PlanEstudio,on_delete=models.CASCADE)
    total = models.IntegerField(max_length=200)

########################################################################################################################

class AspiranteObservacion(models.Model):
    aspirante = models.ForeignKey(Aspirante,on_delete=models.CASCADE)
    nombre_usuario = models.CharField(max_length=200)
    observacion = models.CharField(max_length=250)

########################################################################################################################
class ControlExaminado(models.Model):
    aspirante = models.ForeignKey(Aspirante,on_delete=models.CASCADE)
    folio = models.CharField(max_length=200)
    contador_tomas = models.IntegerField(max_length=100)
    ceneval_flag=models.CharField(max_length=150)
    ov_entrada_flag=models.CharField()
    ov_salida_flag=models.CharField()
########################################################################################################################
class Tutoria(models.Model):
    personal = models.ForeignKey(Personal,on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo,on_delete=models.CASCADE)
    matricula = models.ForeignKey(Matricula,on_delete=models.CASCADE)
    periodo_descripcion = models.TextField()
    edad = models.IntegerField(max_length=100)
    correo_electronico = models.EmailField(max_length=250)
    tipo_motivo_consultas = models.CharField(max_length=150)
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField()
    cuatrimestre = models.CharField(max_length=150)
    referido_por = models.CharField(max_length=150)
    vive_con = models.CharField(max_length=150)
    direccion = models.CharField(max_length=150)
    conclusion = models.TextField()
    fecha = models.DateField()
    nombre_alumno = models.CharField(max_length=250)
    nombre_tutor = models.CharField(max_length=250)
########################################################################################################################

class DhRegistroTalleres(models.Model):
    dh_talleres = models.ForeignKey(Dh_Taller,on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo,on_delete=models.CASCADE)
    carga_academica = models.ForeignKey(CargaAcademica,on_delete=models.CASCADE)
    inscripcion = models.ForeignKey(Inscripcion,on_delete=models.CASCADE)
    presencial_flag = models.BooleanField()
    clave_matricula = models.CharField(max_length=10)
    carrera =models.ForeignKey(Carrera, on_delelte=models.CASCADE)
    telefono = models.CharField(max_length=10)
    correo = electronico = models.EmailField(max_length=250)
    nombre_docente_dh = models.CharField(max_length=250)
    clave_grupo = models.CharField(max_length=20)
    nombre_aula = models.CharField(max_length=5)
    horario_materia = models.FileField(upload_to='user/')
    tipo_materia = models.CharField(max_length=100)
    nombre_usuario = models.CharField(max_length=250)
    estatus = models.ForeignKey(Estatus,on_delete=models.CASCADE)
    dh_nombre = models.OneToOneField(DhNombre,primary_key=True,on_delete=models.CASCADE)
    dh_paricla1 = models.OneToOneField(DhParcial1,primary_key=True,on_delete=models.CASCADE)
    dh_parcial2 = models.OneToOneField(DhParcial2,primary_key=True, on_delete=models.CASCADE)
    dh_parcial3 = models.OneToOneField(DhParicla3,primary_key=True,on_delete=models.CASCADE)

class EstatusDhRegistroTalleres(models.Model):
    descripcion=models.CharField(max_length=150)

class DhParcial1(models.Model):
    usuario = models.CharField(max_length=250)
    fecha = models.DateField()

class DhParcial2(models.Model):
    usuario = models.CharField(max_length=250)
    fecha = models.DateField()

class DhParcial3(models.Model):
    usuario = models.CharField(max_length=250)
    fecha = models.DateField()

########################################################################################################################
class Dh_Taller(models.Model):
    personal = models.ForeignKey(Personal,on_delete=models.CASCADE)
    dh_taller_tipo= models.ForeignKey(Dh_TallerTipo,on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo,on_delete=models.CASCADE)
    nombre_taller = models.CharField(max_length=150)
    descripcion = models.TextField()
    lugar = models.CharField(max_length=150)
    nombre_responsable = models.CharField(max_length=150)
    horario = models.CharField()
    total_lugares = models.IntegerField()
    observaciones = models.TextField()
    registro_alumno_flag = models.CharField(max_length=150)
    estatus = models.ForeignKey(EstatusDhTaller,on_delete=models.CASCADE)

class EstatusDhTaller(models.Model):
    descripcion=models.CharField(max_length=150)
########################################################################################################################
class Dh_TallerTipo(models.Model):
    descripcion = models.TextField()
    estatus = models.CharField(max_length=150)

########################################################################################################################
#                                                                                                                      #
#                                                                                                                      #
#                                          TERCERA PARTE                                                               #
#                                                                                                                      #
#                                                                                                                      #
########################################################################################################################


class HistorialAcademico(models.Model):
    tipo_examen = models.ForeignKey(TipoExamen,on_delete=models.CASCADE)
    matricula = models.ForeignKey(Matricula,on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo,on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia,on_delete=models.CASCADE)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    carga_academica = models.ForeignKey(CargaAcademica, on_delete=models.CASCADE)
    personal_nombre = models.CharField(max_length=150)
    calificacion = models.DecimalField()
    porcentaje = models.DecimalField()
    nivel_dominio = models.CharField(max_length=250)
    estatus = models.ForeignKey(EstatusHistorialAcademico,on_delete=models.CASCADE)

class EstatusHistorialAcademico(models.Model):
    descripcion=models.CharField(max_length=150)
########################################################################################################################
class TipoExamen(models.Model):
    descripcion = models.CharField(max_length=150)
    captura_profesor = models.CharField()
    oportunidad = models.SmallIntegerField()

########################################################################################################################

class Egresado(models.Model):
    matricula = models.ForeignKey(Matricula,on_delete=models.CASCADE)
    datos_actualizado=models.CharField()
    fecha_actualizacion=models.DateField()
    curriculum_actualizado_flag = models.DateField()
    correo_notificar = models.BooleanField()
    estatus = models.ForeignKey(EstatusEgresado,on_delete=models.CASCADE)
    cedula = models.CharField(max_length=150)
    fecha_titulacion=models.DateField()
    usuario_cedula=models.CharField(max_length=150)
    encuesta_flag = models.BooleanField()
    fecha_encuesta=models.DateField()

class EstatusEgresado(models.Model):
    descripcion=models.CharField(max_length=150)
########################################################################################################################
class PersonaDocumentacion(models.Model):
    documentacion = models.ForeignKey(Documentacion,on_delete=models.CASCADE)
    persona = models.ForeignKey(Persona,on_delete=models.CASCADE)
    fecha_registro = models.DateField()
########################################################################################################################
class Documentacion(models.Model):
    clave = models.CharField(max_length=150)
    nombre = models.CharField(max_length=250)
    personal_flag = models.CharField()
    alumno_flag = models.CharField()
    administracion_flag = models.CharField()
    aspirante_flag = models.CharField()

########################################################################################################################
class ArchivosPersonas(models.Model):
    documentacion = models.ForeignKey(Documentacion,on_delete=models.CASCADE)
    persona = models.ForeignKey(Persona,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=250)
    ruta = models.CharField(max_length=250)
    mime = models.CharField(max_length=150)
    tamanio = models.IntegerField(max_length=150)

########################################################################################################################
class ServicioMedico(models.Model):
    matricula = models.ForeignKey(Matricula,on_delete=models.CASCADE)
    persona = models.ForeignKey(Persona,on_delete=models.CASCADE)
    institucion = models.CharField(max_length=250)
    clinica = models.CharField(max_length=250)
    nss = models.CharField(max_length=250)
    proporciona = models.CharField(max_length=250)

########################################################################################################################
class EcontinuaPersona(models.Model):
    persona = models.ForeignKey(Persona,on_delete=models.CASCADE)
    folio = models.CharField(max_length=100)
    empresa_institucion = models.CharField(max_length=250)
    descripcion_empresa = models.TextField()

########################################################################################################################
class EcontinuaCursoEstudiante(models.Model):
    econtinua_persona = models.ForeignKey(EcontinuaPersona,on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicios,on_delete=models.CASCADE)
    pago = models.ForeignKey(Pago,on_delete=models.CASCADE)
    estatus = models.ForeignKey(EstatusEcontinuaCursoEstudiante,on_delete=models.CASCADE)

class EstatusEcontinuaCursoEstudiante(models.Model):
    descripcion=models.CharField(max_length=150)
########################################################################################################################
class EcontinuaFacturacion(models.Model):
    econtinua_persona = models.ForeignKey(EcontinuaPersona,on_delete=models.CASCADE)
    razon_social = models.TextField()
    rfc = models.CharField(max_length=250)
    calle = models.CharField(max_length=250)
    colonia = models.CharField(max_length=250)
    municipio = models.ForeignKey(Municipio,on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado,on_delete=models.CASCADE)
    codigo_postal = models.CharField(max_length=5)
    correo_facturacion = models.EmailField(max_length=250)
    no_interior = models.IntegerField(max_length=100)
    no_exterior = models.IntegerField(max_length=100)

########################################################################################################################

class AdeudosBiblioteca(models.Model):
    persona = models.ForeignKey(Persona,on_delete=models.CASCADE)
    motivo_adeudo = models.TextField()
    tipo_adeudo = models.CharField(max_length=150)
    matricula = models.CharField(max_length=10)
    nombre_usuario = models.CharField(max_length=200)

########################################################################################################################
class PersonaCentroTrabajo(models.Model):
    persona = models.ForeignKey(Persona,on_delete=models.CASCADE)
    centro_trabajo = models.ForeignKey(CentroTrabajo,on_delete=models.CASCADE)
    clave_cct = models.CharField(max_length=150)
    nombre_escuela = models.CharField(max_length=250)
    promedio = models.DecimalField()
    fecha_termino = models.DateField()
    clave_ceneval = models.CharField(max_length=150)
########################################################################################################################
class Direccion(models.Model):
    estado = models.ForeignKey(Estado,on_delete=models.CASCADE)
    municipio = models.ForeignKey(Municipio,on_delete=models.CASCADE)
    persona = models.ForeignKey(Persona,on_delete=models.CASCADE)
    localidad = models.CharField(max_length=250)
    calle = models.CharField(max_lnegth=250)
    numero = models.IntegerField(max_length=500)
    colonia = models.CharField(max_length=200)
    codigo_postal = models.CharField(max_length=10)
    delegacion_municipal = models.CharField(max_length=250)

########################################################################################################################

class EcontinuaInformacionServicio(models.Model):
    servicio = models.ForeignKey(Servicios,on_delete=models.CASCADE)
    nombre_profesor = models.CharField(max_length=150)
    lugar_curso = models.CharField(max_length=150)
    hora = models.TimeField()
    numeros_horas = models.DurationField()
    descripcion = models.TextField()
    fehca_inicio = models.DateField()
    fecha_fin = models.DateField()
########################################################################################################################
class Edificio(models.Model):
    nombre = models.CharField(max_length=150)
########################################################################################################################
class Aula(models.Model):
    edificio = models.ForeignKey(Edificio,on_delete=models.CASCADE)
    numero = models.IntegerField(max_length=500)
    nombre = models.CharField(max_length=250)
    capacidad = models.CharField(max_length=250)
    tipo_espacio = models.CharField(max_length=150)
########################################################################################################################
class TimeSlot(models.Model):
    clave = models.CharField(max_length=150)
    dia_semana = models.DateField()
    turno = models.CharField(max_length=150)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

########################################################################################################################

class HorarioLaboratorio(models.Model):
    time_slot = models.ForeignKey(TimeSlot,on_delete=models.CASCADE)
    aula = models.ForeignKey(Aula,on_delete=models.CASCADE)
    grupo_materia = models.ForeignKey(GrupoMateria,on_delete=models.CASCADE)
    dia_semana = models.DateField()
    tipo_horario = models.CharField(max_length=250)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

########################################################################################################################
class HorarioTutoria(models.Model):
    aula = models.ForeignKey(Aula,on_delete=models.CASCADE)
    persona = models.ForeignKey(Persona,on_delete=models.CASCADE)
    grupo = models.ForeignKey(Grupo,on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo,on_delete=models.CASCADE)
    dia_semana = models.DateField()
    actividad = models.TextField(max_length=250)
    hora_inicio = models.TimeField()
    hora_fin= models.TimeField()

########################################################################################################################
class HorarioClase(models.Model):
    time_slot = models.ForeignKey(TimeSlot,on_delete=models.CASCADE)
    aula = models.ForeignKey(Aula,on_delete=models.CASCADE)
    grupo_materia = models.ForeignKey(GrupoMateria,on_delete=models.CASCADE)
    dia_semana = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    tipo_horario = models.CharField(max_length=150)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()


########################################################################################################################
class AltaBajaMateria(models.Model):
    periodo = models.ForeignKey(Periodo,on_delete=models.CASCADE)
    inscripcion = models.ForeignKey(Inscripcion,on_delete=models.CASCADE)
    grupo_materia = models.ForeignKey(GrupoMateria,on_delete=models.CASCADE)
    carga_academica = models.ForeignKey(CargaAcademica,on_delete=models.CASCADE)
    pago = models.ForeignKey(Pago,on_delete=models.CASCADE)
    oportunidad = models.SmallIntegerField(max_length=3)
    tipo = models.CharField(max_length=150)
    usuario = models.CharField(max_length=150)
########################################################################################################################
class RegistroCambioCapacidad(models.Model):
    grupo = models.ForeignKey(Grupo,on_delete=models.CASCADE)
    capacidad_anterior = models.CharField(max_length=150)
    nueva_capacidad = models.CharField(max_length=150)
    usuario = models.CharField(max_length=150)
#########################################################################################################################
class RegistroTitulado(models.Model):
    matricula = models.ForeignKey(Matricula,on_delete=models.CASCADE)
    usuario = models.CharField(max_length=150)

########################################################################################################################
class Software(models.Model):
    tipo_software = models.ForeignKey(TipoSoftware,on_delete=models.CASCADE)
    nombre_software = models.CharField(max_length=150)
    estatus = models.ForeignKey(EstatusSoftware,on_delete=models.CASCADE)

class EstatusSoftware(models.Model):
    descripcion = models.CharField(max_length=150)

########################################################################################################################
class TipoSoftware(models.Model):
    nombre = models.CharField(max_length=150)
    estatus = models.ForeignKey(EstatusTipoSoftware)

class EstatusTipoSoftware(models.Model):
    descripcion = models.CharField(max_length=150)

########################################################################################################################

class CIE(models.Model):
    pago = models.ForeignKey(Pago,on_delete=models.CASCADE)
    tipo_pago = models.CharField(max_length=150)
    guia_cie = models.CharField(max_length=150)
    importe = models.DecimalField()
    fecha = models.DateField()
    clave_referencia = models.CharField(max_length=30)
    nombre_usuario = models.CharField(max_length=150)
    fecha_contabilidad = models.DateField()

########################################################################################################################

class CargaCIE(models.Model):
    fecha_movimiento = models.DateField()
    nombre_archivos = models.CharField(max_length=150)
    total_registro = models.IntegerField(max_length=150)
    contenido = models.CharField(max_length=150)
    procesado_flag = models.BooleanField()

########################################################################################################################

class MovimientoCIE(models.Model):
    carga_cie = models.ForeignKey(CargaCIE,on_delete=models.CASCADE)
    pago = models.ForeignKey(Pago,on_delete=models.CASCADE)
    fecha_pago = models.DateField()
    guia_cie = models.CharField()
    referencia = models.CharField(max_length=30)
    importe = models.DecimalField()
    tipo_pago = models.CharField(max_length=150)
    procesada_flag = models.BooleanField()
    registro = models.CharField(max_length=150)
########################################################################################################################

#class RHActividadCategoria(models.Model):
#    descripcion = models.CharField(max_length=150)
#    estatus

#class EContinuaTipoCurso(models.Model):
#    descripcion = models.CharField(max_legnth=150)

########################################################################################################################
#                                                                                                                      #
#                                                                                                                      #
#                                             SESION                                                                   #
#                                                                                                                      #
#                                                                                                                      #
########################################################################################################################
class UPQUsuario(models.Model):
    persona = models.ForeignKey(Persona,on_delete=models.CASCADE)
    username = models.CharField(max_length=150)
    algotithm = models.CharField(max_length=150)
    password = models.CharField(max_length0150)
    nombre_completo = models.CharField(max_length=250)
    correo_electronico = models.EmailField(max_length=150)
    is_active = models.BooleanField()
    is_super_admin = models.BooleanField()
    total_reinicios = models.IntegerField(max_length=100)
    last_login = models.DateField()
    salt = models.CharField(max_length=10)

########################################################################################################################
class UPQSesion(models.Model):
    upq_usuario = models.ForeignKey(UPQUsuario,on_delete=models.CASCADE)
    nombre_completo = models.CharField(max_length=150)
    ip = models.models.GenericIPAddressField(protocol='both',unpack_ipv4=False)
    inicio = models.DateField()
    ultimo_acceso = models.DateField()

########################################################################################################################
class UsuarioRecurso(models.Model):
    upq_usuario = models.ForeignKey(UPQUsuario,on_delete=models.CASCADE)
    recurso = models.ForeignKey(Recurs,on_delete=models.CASCADE)
    permiso = models.BooleanField()

########################################################################################################################
class RememberKey(models.Model):
    upq_usuario=models.ForeignKey(UPQUsuario,on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField(protocol='both',unpack_ipv4=False)
    remember_key = models.BooleanField()

########################################################################################################################
class UsuarioRole(models.Model):
    role = models.ForeignKey(Role,on_delete=models.CASCADE)
    upq_usuario = models.ForeignKey(UPQUsuario,on_delete=models.CASCADE)
    last_login = models.DateField()

########################################################################################################################

class Menu(models.Model):
    aplicacion = models.ForeignKey(Aplicacion,on_delete=models.CASCADE)
    tag = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=250)
    deptn = models.CharField(max_length=150)
    utl = models.UrlField(max_length=200)
    tipo = models.CharField(max_length=150)
    icono = models.CharField(max_length=150)
    orden = models.IntegerField(max_length=150)
    modal = models.CharField(max_length=150)
    estatus_menu = models.ForeignKey(EstatusMenu,on_delete=models.CASCADE)

class EstatusMenu(models.Model):
    descripcion = models.CharField(max_length=150)

########################################################################################################################
class Aplicacion(models.Model):
    nombre = models.CharField(max_length=250)
    descripcion = models.CharField(max_length=150)

########################################################################################################################
class Modulo(models.Model):
    aplicacion = models.ForeignKey(Aplicacion,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=150)
    is_active = models.BooleanField()

########################################################################################################################
class Role(models.Model):
    aplicacion = models.ForeignKey(Aplicacion,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=150)

########################################################################################################################
class Recurso(models.Model):
    modulo = models.ForeignKey(Modulo,on_delete=models.CASCADE)
    recurso_nombre = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=250)

########################################################################################################################
class RoleUsuario(models.Model):
    role = models.ForeignKey(Role,on_delete=models.CASCADE)
    recurso = models.ForeignKey(Recurso,on_delete=models.CASCADE)
    permision = models.BooleanField()

########################################################################################################################
class RoleMenu(models.Model):
    role = models.ForeignKey(Role,on_delete=models.CASCADE)
    menu = models.TextField(max_length=400)
########################################################################################################################
#                                                                                                                      #
#                                                                                                                      #
#                                     EVALIACION                                                                       #
#                                                                                                                      #
#                                                                                                                      #
########################################################################################################################
class Pregunta(models.Model):
    pregunta_categoria = models.ForeignKey(PreguntaCategoria,on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=150)
    observaciones = models.CharField(max_length=150)
    requerida_flag = models.BooleanField()
########################################################################################################################

class EncuestaAplicada(models.Model):
    encuesta = models.ForeignKey(Encuesta,on_delete=models.CASCADE)
    tipo_aplicacion = models.CharField(max_length=150)
    examen_descripcion = models.CharField(max_length=150)
    total_reactivos = models.IntegerField(max_length=500)
    fecha_termino = models.DateField()
    total_intentos = models.SmallIntegerField(max_length=4)
    detalle_resultado = models.CharField(max_length=150)
    terminada_flag = models.BooleanField()

########################################################################################################################
class EvaluacionEAlumno(models.Model):
    encuesta_aplicada = models.ForeignKey(EncuestaAplicada,on_delete=models.CASCADE)
    proceso = models.ForeignKey(Proceso,on_delete=models.CASCADE)
    matricula = models.ForeignKey(Matricula,on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo,on_delete=models.CASCADE)
    tipo_proceso = models.CharField(max_length=150)
    carrera = models.CharField(max_length=150)
    nombre_alumno = models.CharField(max_length=250)
########################################################################################################################
class EvaluacionTransporte(models.Model):
    encuesta_aplicada = models.ForeignKey(EncuestaAplicada,on_delete=models.CASCADE)
    matricula = models.ForeignKey(Matricula,on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo,on_delete=models.CASCADE)
    terminada_flag = models.BooleanField()

########################################################################################################################
class InstrumentoServicio(models.Model):
    encuesta_aplicada = models.ForeignKey(EncuestaAplicada,on_delete=models.CASCADE)
    carrera = models.ForeignKey(Carrera,on_delete=models.CASCADE)
    grupo = models.ForeignKey(Grupo,on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo,on_delete=models.CASCADE)
    clave_grupo = models.CharField(max_length=10)
    periodo_instrumento = models.DateField()
    carrera_instrumento = models.CharField(max_length=150)
########################################################################################################################
class EvaluacionDocente(models.Model):
    encuesta_aplicada = models.ForeignKey(EncuestaAplicada,on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia,on_delete=models.CASCADE)
    grupo = models.ForeignKey(Grupo,on_delete=models.CASCADE)
    docente = models.ForeignKey(Docente,on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo,on_delete=models.CASCADE)
    carrera = models.ForeignKey(Carrera,on_delete=models.CASCADE)
    area_estudio = models.ForeignKey(AreaEstudio,on_delete=models.CASCADE)
    carga_academica = models.ForeignKey(CargaAcademica,on_delete=models.CASCADE)
    clave_grupo = models.CharField(max_length=10)

########################################################################################################################

class EvaluacionEasesorUpq(models.Model):
    encuesta_aplicada = models.ForeignKey(EncuestaAplicada,on_delete=models.CASCADE)
    proceso = models.ForeignKey(Proceso,on_delete=models.CASCADE)
    matricula = models.ForeignKey(Matricula,on_delete=models.CASCADE)
    personal = models.ForeignKey(Personal,on_delete=models.CASCADE)
    tipo_proceso = models.ForeignKey(TipoProceso, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo,on_delete=models.CASCADE)
    carrera = models.CharField(max_length=150)
    nombre_docente = models.CharField(max_length=150)

########################################################################################################################
class Encuesta(models.Model):
    examen = models.ForeignKey(Examen, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

########################################################################################################################

class Examen(models.Model):
    nombre_completo = models.CharField(max_length=150)
    nombre_corto = models.CharField(max_length=150)
    version = models.CharField()
    objetivo = models.CharField(max_length=150)
    instrucciones = models.TextField(max_length=250)
    random_question = models.CharField(max_length=150)
    estatus = models.ForeignKey(EstatusExamen,on_delete=models.CASCADE)

class EstatusExamen(models.Model):
    descripcion=models.CharField(max_length=150)

########################################################################################################################
class Habilidades(models.Model):
    examen = models.ForeignKey(Examen,on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=150)

########################################################################################################################
class HabilidadesPreguntas(models.Model):
    habilidades = models.ForeignKey(Habilidades,on_delete=models.CASCADE)
    pregutna = models.ForeignKey(Pregunta,on_delete=models.CASCADE)
########################################################################################################################
class PreguntasAleatorias(models.Model):
    examen = models.ForeignKey(Examen,on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Pregunta,on_delete=models.CASCADE)
########################################################################################################################
class TBLEncuestaResultado(models.Model):
    encuesta_aplicada=models.ForeignKey(EncuestaAplicada,on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Pregunra,on_delete=models.CASCADE)
    pregunsta_descripcion = models.CharField(max_length=150)
    valor = models.IntegerField(max_length=10)

########################################################################################################################
class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=150)
    usuario = models.CharField(max_length=150)
    constrasenia = models.CharField(max_length=250)
    correo_electronico = models.EmailField(max_length=250)
    expira = models.DateField()
    ultimo_acceso = models.DateField()
    estatus = models.ForeignKey(EstatusUsuario,on_delete=models.CASCADE)

class EstatusUsuario(models.Model):
    descripcion = models.CharField(max_length=150)

########################################################################################################################
class wwInstrumentosServicios(models.Model):
    pregunta = models.ForeignKey(Pregunta,on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo,on_delete=models.CASCADE)
    carrera = models.ForeignKey(Carrera,on_delete=models.CASCADE)
    nombre_carrera = models.CharField(max_length=150)
    area = models.CharField(max_length=150)
    comentario = models.CharField(max_length=150)
    pregunsta_descripcion = models.TextField(max_length=300)
########################################################################################################################

class Sesion(models.Model):
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    nombre_usuario = models.CharField(max_length=150)
    ip = models.GenericIPAddressField(protocol='both', unpack_ipv4=False)
    inicio = models.DateField()
    ultimo_acceso = models.DateField()


########################################################################################################################
class PreguntaCategoria(models.Model):
    nombre = models.CharField(max_length=150)

########################################################################################################################

class EncuestaInscripcion(models.Model):
    inscripcion = models.ForeignKey(Inscripcion,on_delete=models.CASCADE)

class EncuestaComentario(models.Model):
    pregunta = models.ForeignKey(Pregunta,on_delete=models.CASCADE)
    encuesta_aplicada = models.ForeignKey(EncuestaAplicada,on_delete=models.CASCADE)
    pregunta_descripcion = models.TextField(max_length=300)
    comentario = models.TextField(max_length=300)

class EncuestaResultadoSD2015(models.Model):
    pregunta = models.ForeignKey(Pregunta,on_delete=models.CASCADE)
    encuesta_aplicada = models.ForeignKey(EncuestaAplicada,on_delete=models.CASCADE)
    valor = models.IntegerField(max_length=50)
    pregunta_descripcion = models.TextField(max_length=150)
    considerar_flag = models.BooleanField()

class EncuestaComentariosEE(models.Model):
    pregunta =models.ForeignKey(Pregunta,on_delete=models.CASCADE)
    encuesta_aplicada = models.ForeignKey(EncuestaAplicada,on_delete=models.CASCADE)
    comentario = models.CharField(max_lengh=150)
    pregunta_descripcion = models.TextField(max_length=250)

class EncuestaResultadoRespaldo(models.Model):
    pregunta = models.ForeignKey(Pregunta,on_delete= models.CASCADE)
    encuesta_aplicada = models.ForeignKey(EncuestaAplicada,on_delete=models.CASCADE)
    valor = models.IntegerField(max_length=50)
    pregunta_descripcion = models.TextField(max_length=150)
    considerar_flag = models.BooleanField()

class ExamenAgrupacion(models.Model):
    examen = models.ForeignKey(Examen,on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=150)
    publicar = models.BooleanField()
    instrucciones = models.TextField(max_length=400)
    orden = models.IntegerField(max_length=200)

class EncuestaResultadosEE(models.Model):
    pregunta = models.ForeignKey(Pregunta,on_delete=models.CASCADE)
    encuesta_aplicada = models.ForeignKey(EncuestaAplicada,on_delete=models.CASCADE)
    pregunta_descripcion = models.TextField(max_length=150)
    valor = models.IntegerField(max_length=200)
    considerar_flag = models.BooleanField()

class EncuestaResultado(models.Model):
    pregunta = models.ForeignKey(Pregunta,on_delete=models.CASCADE)
    encuesta_aplicada = models.ForeignKey(EncuestaAplicada, on_delete=models.CASCADE)
    pregunta_descripcion = models.CharField(max_length=200)
    valor = models.IntegerField(max_length=200)
    considerar_flag = models.BooleanField()

class EvaluacionAspirante(models.Model):
    aspirante = models.ForeignKey(Aspirante,on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    encuesta_aplicada =models.ForeignKey(EncuestaAplicada, on_delete=models.CASCADE)
    terminada_flag = models.BooleanField()

class Test(models.Model):
    descripcion = models.TextField(max_length=150)
    valor = models.IntegerField(max_length=200)
    orden = models.IntegerField(max_length=200)

class ExamenPregunta(models.Model):
    pregunta = models.ForeignKey(Pregunta,on_delete=models.CASCADE)
    examen_agrupacion = models.ForeignKey(ExamenAgrupacion,on_delete=models.CASCADE)
    orden = models.IntegerField(max_length=200)
    consecutivo = models.IntegerField(max_length=200)
    mostrar_flag = models.BooleanField()

class RespuestaValor(models.Model):
    pregunta = models.ForeignKey(Pregunta,on_delete=models.CASCADE)
    descripcion = models.TextField(max_length=150)
    valor = models.IntegerField(max_length=200)
    observaciones = models.TextField(max_length=200)
    orden = models.IntegerField(max_length=200)

########################################################################################################################
#                                                                                                                      #
#                                                                                                                      #
#                                        VINCULACIÓN                                                                   #
#                                                                                                                      #
#                                                                                                                      #
########################################################################################################################
class Oferta(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    tipo_oferta = models.CharField(max_length=150)
    candidatos = models.TextField(max_length=300)
    carrera = models.CharField(max_length=200)
    titulo =models.CharField(max_length=200)
    introduccion = models.CharField(max_length=200)
    detalle_oferta = models.CharField(max_length=200)
    perfil_candidato = models.FileField(upload_to='user/')
    requisitos = models.FileField(upload_to='user/')
    competencias = models.CharField(max_length=150)
    salario = models.FloatField()
    fecha_vigencia = models.DateField()
    activa_flag = models.BooleanField()
    cambio_residencia = models.CharField(max_length=150)
    vehiculo_propio = models.BooleanField()
    licencia_manejo_flag = models.BooleanField()
    tipo_licencia_manejo = models.CharField(max_length=150)
    detalle_experiencia = models.FileField(upload_to='user/')
    conocimiento = models.CharField(max_length=200)
    otras_prestaciones = models.FileField(upload_to='user/')
    tipo_contrato = models.FileField(upload_to='user/')
    estado_civil = models.CharField(max_length=200)
    edad = models.IntegerField(max_length=100)
    autorizada_por = models.CharField(max_length=150)
    fecha_autorizacion = models.DateField(max_length=150)
    comentarios_autorizacion = models.TextField(max_length=200)
    idiomas = models.CharField(max_length=150)
    estatus = models.ForeignKey(EstatusOferta,on_delete=models.CASCADE)

class EstatusOferta(models.Model):
    descripcion = models.CharField(max_length=150)
########################################################################################################################

class ParqueIndustrial(models.Model):
    nombre = models.CharField(max_length=150)
    ubicacion = models.CharField()
    estado = models.ForeignKey(Estado,on_delete=models.CASCADE)

class Sector(models.Model):
    descripcion =models.CharField(max_length=150)

class SubSector(models.Model):
    sector = models.ForeignKey(Sector,on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=150)

class PerfilAlumnos(models.Model):
    proyecto = models.ForeignKey(Proyecto,on_delete=models.CASCADE)
    total_alumnos = models.IntegerField(max_length=200)
    carrera = models.CharField(max_length=150)



########################################################################################################################
class Empresa(models.Model):
    estado = models.ForeignKey(Estado,on_delete=models.CASCADE)
    municipio = models.ForeignKey(Municipio,on_delete=models.CASCADE)
    parque_industrial = models.ForeignKey(ParqueIndustrial,on_delete=models.CASCADE)
    sector = models.ForeignKey(Sector,on_delete=models.CASCADE)
    subsector = models.ForeignKey(SubSector, on_delete=models.CASCADE)
    otro_parque_industrial = models.CharField(max_length=150)
    denominacion = models.CharField(max_length=150)
    informacion_general = models.CharField(max_length=150)
    rfc = models.CharField(max_length=10)
    tipo_rubro = models.CharField(max_length=150)
    actividad_empresarial = models.FileField(upload_to='user/')
    producto_servicio=models.CharField(max_length=150)
    nivel_gobierno = models.CharField(max_length=150)
    total_empleados = models.IntegerField(max_length=500)
    logo = models.ImageField()
    pagina_web = models.URLField(max_length=200)
    croquis = models.ImageField()
    domicilio = models.CharField(max_length=150)
    colonia = models.CharField(max_length=150)
    codigo_postal = models.CharField(max_length=5)
    telefono = models.CharField(max_length=10)
    fax = models.CharField(max_length=10)
    tamanio_empresa = models.CharField(max_length=150)
    autorizada_por = models.CharField(max_length=150)
    fecha_autorizacion = models.DateField()
    comentarios_autorizacion = models.TextField(max_length=150)
    registrado_por = models.CharField(max_length=150)
    estatus = models.ForeignKey(EstatusEmpresa,on_delete=models.CASCADE)
    paises_exportacion = models.CharField(max_length=150)
    paises_importacion = models.CharField(max_length=150)
    origen_inversion = models.FloatField()
    porcentaje_inversion = models.FloatField()
    segundo_origen_inversion = models.FloatField()
    porcentaje_segundo_inversion = models.FloatField()
    certificaciones = models.FileField(upload_to='user/')


class EstatusEmpresa(models.Model):
    descripcion = models.CharField(max_length=150)

########################################################################################################################

class Proyecto(models.Model):
    empresa = models.ForeignKey(Empresa,on_delete=models.CASCADE)
    contacto = models.ForeignKey(Contacto, on_delete=models.CASCADE)
    area_descripcion = models.CharField(max_length=150)
    titulo = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=150)
    sexo = models.CharField(max_length=1)
    objetivos = models.CharField(max_length=250)
    total_alumnos = models.IntegerField(max_length=200)
    carrera = models.CharField(max_length=150)
    perfil_deseado = models.FileField(upload_to = 'user/')
    competencias = models.CharField(max_length=150)
    tipo_horario = models.CharField(max_length=150)
    estatus_disponible = models.BooleanField()
    estatus = models.ForeignKey(EstatusProyecto,on_delete=models.CASCADE)
    apoyo_flag = models.BooleanField()
    tipo_apoyo = models.CharField(max_length=150)
    cantidad_apoyo_economico = models.IntegerField(max_length=100)
    tipo_programa = models.CharField(max_length=150)
    duracion = models.DurationField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    observaciones = models.TextField(max_length=200)
    autorizado_por = models.CharField(max_length=150)
    fecha_autorizacion = models.DateField()
    observacion_autorizacion = models.TextField(max_length=250)
    registrado_por=models.CharField(max_length=150)

class EstatusProyecto(models.Model):
    descripcion = models.CharField(max_length=150)

########################################################################################################################

class AlumnoDetalle(models.Model):
    matricula = models.ForeignKey(Matricula, on_delete=models.CASCADE)
    plan_estudio = models.ForeignKey(PlanEstudio, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    nombre_completo = models.CharField(max_length=250)
    apellido_paterno = models.CharField(max_length=250)
    apellido_materno = models.CharField(max_length=250)
    correo_electronico = models.EmailField(max_length=300)
    nombre_carrera = models.CharField(max_length=150)
    carrera_nombre_oficial = models.CharField(max_length=150)
    carrera_nombre_coordinador = models.CharField(max_length=150)
    carrera_coordinador_proceso = models.BooleanField()
    clave_grupo = models.CharField(max_length=5)
    cuatrimestre = models.CharField(max_length=150)
    generacion = models.IntegerField(max_length=100)
    creditos_aprobados = models.FloatField(max_length=150)
    total_ncs = models.CharField(max_length=150)
    promedio_general = models.FloatField()
    calle = models.CharField(max_length=150)
    no = models.IntegerField(max_length=10)
    colonia = models.CharField(max_length=150)
    localidad = models.CharField(max_length=150)
    codigo_postal = models.CharField(max_lengt=5)
    estado = models.ForeignKey(Estado,on_delete=models.CASCADE)
    municipio = models.ForeignKey(Municipio,on_delete=models.CASCADE)
    tel_local = models.CharField(max_length=10)
    nss = models.CharField(max_length=30)
    institucion = models.CharField(max_length=150)
########################################################################################################################
class TipoProceso(models.Model):
    nombre=models.CharField(max_length=150)
    duracion = models.DurationField()
    descripcion = models.CharField(max_length=150)
    tipo_programa = models.CharField(max_length=150)

########################################################################################################################

class Proceso(models.Model):
    empresa = models.ForeignKey(Empresa,on_delete=models.CASCADE)
    proyecto = models.ForeignKey(Proyecto,on_delete=models.CASCADE)
    tipo_proceso = models.ForeignKey(TipoProceso,on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo,on_delete=models.CASCADE)
    personal = models.ForeignKey(Personal,on_delete=models.CASCADE)
    persona = models.ForeignKey(Persona,on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    calificacion_proyecto = models.IntegerField(max_length=10)
    calificacion_final = models.FloatField()
    fecha_calificacion = models.DateField()
    comentarios_finales = models.CharField(max_length=250)
    estatus = models.ForeignKey(EstatusProceso,on_delete=models.CASCADE)

    metodo_conocimiento = models.TextField(max_length=250)
    responsable_proceso_pe = models.CharField(max_length=150)

    avances_subidos = models.BooleanField()
    vinc_entrego_carta = models.BooleanField()

class EstatusProceso(models.Model):
    descripcion = models.CharField(max_length=150)
    estatus_observaciones = models.CharField(max_length=250)
    estatus_documentation = models.FileField(upload_to='user/')
    estatus_encuesta = models.CharField()
    estatus_alumno = models.CharField()
    estatus_easesor =models.CharField()

########################################################################################################################
class UsuarioEmpresa(models.Model):
    empresa = models.ForeignKey(Empresa,on_delete=models.CASCADE)
    nombre_contacto = models.CharField(max_length=150)
    username = models.CharField(max_length=150)
    password=models.CharField(max_length=150)
    correo_electronico = models.EmailField(max_length=250)
    tipo_cuenta=models.CharField(max_length=150)
    expira = models.DateField()
    estatus = models.ForeignKey(EstatusUsuarioEmpresa,on_delete=models.CASCADE)
    ultimo_acceso = models.DateField()

class EstatusUsuarioEmpresa(models.Model):
    descripcion = models.CharField()

class Contrasenia(models.Model):
    usuario_empresa = models.ForeignKey(UsuarioEmpresa,on_delete=models.CASCADE)
    password=models.CharField(max_length=250)
    pass_mod5 = models.CharField(max_length=250)


########################################################################################################################
class PerfilCarreras(models.Model):
    ofera = models.ForeignKey(Oferta,on_delete=models.CASCADE)
    carrera = models.ForeignKey(Carrera,on_delete=models.CASCADE)
    total_alumnos = models.IntegerField(max_length=200)
    carrera_descripcion=models.CharField(max_length=200)
########################################################################################################################
class Reunion(models.Model):
    reunion_proceso = models.ForeignKey(ReunionProceso,on_delete=models.CASCADE)
    fecha = models.DateField()
    confirmacion = models.BooleanField()
    lugar = models.CharField(max_length=150)
    programada_flag = models.BooleanField()

########################################################################################################################
class EmpresaBaja(models.Model):
    empresa = models.ForeignKey(Empresa,on_delete=models.CASCADE)
    usuario = models.CharField(max_length=250)
    observacion = models.CharField(max_length=150)

class ReunionActividades(models.Model):
    reunion = models.ForeignKey(Reunion,on_delete=models.CASCADE)
    no_actividad = models.IntegerField(max_length=10)
    actividad = models.CharField(max_length=100)
    compromisos = models.CharField(max_length=100)

class VisitaProceso(models.Model):
    tipo_proceso = models.ForeignKey(TipoProceso,on_delete=models.CASCADE)
    no = models.IntegerField(max_length=100)
    descripcion = models.TextField(max_length=150)


class Visita(models.Model):
    proceso = models.ForeignKey(Proceso,on_delete=models.CASCADE)
    visita_proceso = models.ForeignKey(VisitaProceso,on_delete=models.CASCADE)
    visita_fecha = models.DateField()
    visita_confirmacion = models.BooleanField()
    observaciones = models.CharField(max_length=150)
    visita_hora = models.TimeField()

class ReunionProceso(models.Model):
    tipo_proceso = models.ForeignKey(TipoProceso,on_delete=models.CASCADE)
    no = models.IntegerField(max_length=150)
    descripcion = models.CharField(max_length=250)

class ProyectoAsignatura(models.Model):
    proyecto = models.ForeignKey(Proyecto,on_delete=models.CASCADE)
    nombre_asignatura = models.CharField(max_length=150)
    topicos = models.CharField(max_length=200)
    estrategias_didacticas = models.CharField()






class DocumentacionEE(models.Model):
    tipo_proceso = models.ForeignKey(TipoProceso,on_delete=models.CASCADE)
    documento=models.FileField(upload_to='user/')
    descripcion = models.CharField(max_length=250)
    activo_flag = models.BooleanField()

class DocumentacionServicioSocial(models.Model):
    documentacion_ee=models.ForeignKey(DocumentacionEE,on_delete=models.CASCADE)
    proceso = models.ForeignKey(Proceso,on_delete=models.CASCADE)
    archivo = models.ForeignKey(Archivo,on_delete=models.CASCADE)

class ProcesoDocumentacion(models.Model):
    proceso = models.ForeignKey(Proceso,on_delete=models.CASCADE)
    archivo = models.ForeignKey(Archivo,on_delete=models.CASCADE)
    documentacion_ee =models.ForeignKey(DocumentacionEE,on_delete=models.CASCADE)
    revisado_flag=models.BooleanField()
    cargado_por = models.CharField(max_length=250)

###### CAMBIO DE NOMBRE DE SESION A SESIONVINCULACION ################
class SesionVinculacion(models.Model):
    usuario_empresa=models.ForeignKey(UsuarioEmpresa,on_delete=models.CASCADE)
    nombre_contacto =models.CharField(max_length=150)
    tipo_cuenta=models.CharField(max_length=150)
    ip = models.GenericIPAddressField(protocol='both', unpack_ipv4=False)
    inicio = models.DateField()
    ultimo_acceso = models.DateField()

class Etapa(models.Model):
    proceso =models.ForeignKey(Proceso,on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=150)
    duracion = models.DurationField()
    etapa_inicio = models.DateField()
    etapa_fin = models.DateField()

class EtapaServicioSocial(models.Model):
    proceso=models.ForeignKey(Proceso,on_delete=models.CASCADE)
    tipo_reporte=models.CharField(max_length=150)
    descripcion = models.CharField(max_length=150)
    ess_horas = models.TimeField()
    ess_horas_acumuladas = models.TimeField()
    inicio = models.DateField()
    fin = models.DateField()

class CalificacionParcial(models.Model):
    proceso = models.ForeignKey(Proceso,on_delete=models.CASCADE)
    mes = models.DateField()
    calificacion_asesor_interno = models.IntegerField(max_length=10)
    observaciones_asesro_interno = models.CharField(max_length=150)
    fecha_asesor_interno = models.DateField()
    calificacion_asesor_externo = models.IntegerField(max_length=10)
    observaciones_asesro_externo = models.CharField(max_length=150)
    fecha_asesor_externo = models.DateField()

class ProyectoAprendizaje(models.Model):
    proyecto = models.ForeignKey(Proyecto,on_delete=models.CASCADE)
    actividades = models.CharField(max_length=150)
    resultados = models.FloatField()
    evidencias = models.CharField(max_length=150)
    instrumentos_evaluacion = models.CharField()

class ProcesoServicioSocial(models.Model):
    matricula = models.ForeignKey(Matricula,on_delete=models.CASCADE)
    tipo_proceso = models.ForeignKey(TipoProceso,on_delete=models.CASCADE)
    proyecto = models.ForeignKey(Proyecto,on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo,on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa,on_delete=models.CASCADE)
    programa = models.CharField(max_length=150)
    actividades = models.CharField(max_length=200)
    observaciones = models.CharField(max_length=150)
    estatus = models.ForeignKey(EstatusProcesoServicioSocial,on_delete=models.CASCADE)
    inicio = models.DateField()
    fin = models.DateField()

class EstatusProcesoServicioSocial(models.Model):
    descripcion = models.CharField(max_length=150)

class ProyectoActividad(models.Model):
    proyecto = models.ForeignKey(Proyecto,on_delete=models.CASCADE)
    actividad = models.CharField(max_length=150)
    observaciones = models.CharField(max_length=150)
    inicio = models.DateField()
    fin = models.DateField()

class ProyectoCompetencia(models.Model):
    proyecto = models.ForeignKey(Proyecto,on_delete=models.CASCADE)
    competencia = models.CharField(max_length=150)

class Contacto(models.Model):
    empresa = models.ForeignKey(Empresa,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=150)
    puesto = models.CharField(max_length=150)
    telefono = models.CharField(max_length=10)
    fax = models.CharField(max_length=10)
    correo_electronico = models.EmailField(max_length=250)
    principal_flag = models.BooleanField()


class ArchivoCategoria(models.Model):
    nombre = models.CharField(max_length=150)

class Archivo(models.Model):
    archivo_categoria = models.ForeignKey(ArchivoCategoria,on_delete=models.CASCADE)
    persona = models.ForeignKey(Persona,on_delelte=models.CASCADE)
    nombre = models.CharField(max_length=150)
    ruta = models.CharField(max_length=150)
    mime = models.CharField(max_length=150)
    size = models.CharField(max_length=150)
    publico_flag=models.BooleanField()

class ArchivoVersion(models.Model):
    archivo =models.ForeignKey(Archivo,on_delete=models.CASCADE)
    version = models.CharField(max_length=150)
    observaciones = models.CharField(max_length=250)
    #ARCHIVO_HIJO =models.ForeignKey() ??????????????????????

class Descarga(models.Model):
    archivo = models.ForeignKey(Archivo,on_delete=models.CASCADE)
    nombre_usuario = models.CharField(max_length=150)

class MimeTypes(models.Model):
    archivo_categoria = models.ForeignKey(ArchivoCategoria,on_delete=models.CASCADE)
    mime_type = models.CharField(max_length=150)

class ReporteFinal(models.Model):
    proceso=models.ForeignKey(Proceso,on_delete=models.CASCADE)
    archivo = models.ForeignKey(Archivo,on_delete=models.CASCADE)
    tipo_proceso = models.ForeignKey(TipoProceso,on_delete=models.CASCADE)
    titulo = models.CharField(max_length=150)
    autor = models.CharField(max_length=150)
    no_paginas = models.IntegerField(max_length=20)
    ruta = models.CharField(max_length=150)
    fecha_publicacion =models.DateField()


class Curriculum(models.Model):
    matricula = models.ForeignKey(Matricula,on_delete=models.CASCADE)
    estatus_curriculum = models.ForeignKey(EstatusCurriculum,on_delete=models.CASCADE)
    nombre_candidato=models.CharField(max_length=150)
    edad = models.IntegerField(max_length=60)
    correo_electronico = models.EmailField(max_length=250)
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField(max_length=250)
    licencia_manejo = models.FileField(upload_to='user/')
    vehiculo_propio_flag = models.BooleanField()
    situacion_laboral=models.CharField(max_length=150)
    disponibilidad = models.BooleanField()
    total_experiencia = models.TextField(max_length=250)
    idiomas = models.TextField(max_length=150)
    nivel_ingles = models.CharField(max_length=150)
    estado_civil = models.CharField(max_length=150)
    expectativa_salarial=models.CharField(max_length=200)
    tipo_empleo = models.CharField(max_length=150)
    carrera=models.CharField(max_length=150)
    detalle_curriculum = models.CharField(max_length=150)
    conocimiento_especializado=models.CharField(max_length=150)
    experiencia_herramientas = models.CharField(max_length=150)
    formacion_academica=models.CharField(max_length=150)

class EstatusCurriculum(models.Model):
    descripcion = models.CharField(max_length=150)


class CurriculumEmpleos(models.Model):
    curriculum = models.ForeignKey(Curriculum,on_delete=models.CASCADE)
    denominacion_empresa =models.CharField(max_length=150)
    puesto = models.CharField(max_length=150)
    actividades_realizadas=models.CharField(max_length=150)
    nombre_jefe = models.CharField(max_length=250)
    telefono = models.CharField(max_length=10)
    sitio_web = models.URLField(max_length=200)


class OfertaCurriculum(models.Model):
    oferta = models.ForeignKey(Oferta,on_delete=models.CASCADE)
    curriculum = models.ForeignKey(Curriculum,on_delete=models.CASCADE)
    estatus = models.ForeignKey(EstatusOfertaCurriculum,on_delete=models.CASCADE)
    observaciones=models.CharField(max_length=150)

class EstatusOfertaCurriculum(models.Model):
    descripcion =models.CharField(max_length=150)

class CurriculumDireccion(models.Model):
    curriculum = models.ForeignKey(Curriculum,on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado,on_delete=models.CASCADE)
    municipio = models.ForeignKey(Municipio,on_delete=models.CASCADE)
    localidad = models.CharField(max_length=250)
    calle =models.CharField(max_length=150)
    no =models.IntegerField(max_length=10)
    colonia = models.CharField(max_length=150)
    delegacion_municipal = models.CharField(max_length=250)

class AsesorDetalle(models.Model):
    personal = models.ForeignKey(Personal,on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo,on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado,on_delete=models.CASCADE)
    municipio = models.ForeignKey(Municipio,on_delete=models.CASCADE)
    nombre_completo=models.CharField(max_length=150)
    apellido_paterno=models.CharField(max_length=150)
    apellido_materno=models.CharField(max_length=150)
    calle =models.CharField(max_length=150)
    no = models.IntegerField(max_length=50)
    colonia = models.CharField(max_length=150)
    localidad = models.CharField(max_length=150)
    codigo_postal=models.CharField(max_lengt=10)
    tel_local=models.CharField(max_length=10)
    tel_celular=models.CharField(max_length=10)
    correo_alterno = models.EmailField(max_length=250)
    correo_institucional=models.EmailField(max_length=250)
    tipo_contrato = models.CharField(max_length=150)
    no_empleado = models.IntegerField(max_length=200)


class Estatus(models.Model):
    descripcion=models.CharField(max_length=150)


