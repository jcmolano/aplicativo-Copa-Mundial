from django.db import models

# Create your models here.
JORNADA = (
    ('seleccione', 'Seleccione'),       
)
FACULTAD = (
    ('seleccione', 'Seleccione'),
)
CARRERA = (
    ('seleccione', 'Seleccione'),
)
MODALIDAD = (
    ('seleccione', 'Seleccione'),
)
COBERTURA = (
    ('seleccione', 'Seleccione'),
)
EVALUACION = (
    ('seleccione', 'Seleccione'),
) 
ESTRATO = (
    ('seleccione', 'Seleccione'),
)
class Estudiante(models.Model):
    cedulaEstudiante = models.CharField(max_length=30)
    nombreEstudiante = models.CharField(max_length=30)
    apellidosEstudiante = models.CharField(max_length=50)
    telefonoEstudiante = models.CharField(max_length=30)
    celularEstudiante = models.CharField(max_length=30)
    emailPersonalEstudiante = models.CharField(max_length=50)
    emailInstitucionalEstudiante = models.CharField(max_length=50)
    jornadaEstudiante = models.CharField(choices=JORNADA, default='seleccione', max_length=10)
    facultad = models.CharField(choices=FACULTAD, default='seleccione', max_length=20)
    carrera = models.CharField(choices=CARRERA, default='seleccione', max_length=20)

class ProfesorTeorico(models.Model):
    cedulaProfesorT = models.CharField(max_length=30)
    nombreProfesorT = models.CharField(max_length=50)
    apellidosProfesorT = models.CharField(max_length=50)
    telefonoProfesorT = models.CharField(max_length=30)
    celularProfesorT = models.CharField(max_length=30)
    emailPersonalProfesorT = models.CharField(max_length=50)
    emailInstitucionalProfesorT = models.CharField(max_length=50)
    
class ProfesorPractico(models.Model):
    cedulaProfesorP = models.IntegerField(null=True)
    nombreProfesorP = models.CharField(max_length=50)
    apellidosProfesorP = models.CharField(max_length=50)
    telefonoProfesorP = models.IntegerField(null=True)
    celularProfesorP = models.IntegerField(null=True)
    emailPersonalProfesorP = models.CharField(max_length=50)
    emailInstitucionalProfesorP = models.CharField(max_length=50)

class Tiempo(models.Model):
    fechaDeInicio = models.CharField(max_length=50)
    fechaDeFinalizacion = models.CharField(max_length=50)
    ano = models.IntegerField(null=True)
    periodo = models.IntegerField(null=True)
    
class CampoDePractica(models.Model):
    modalidadDeLaPractica = models.CharField(choices=MODALIDAD, default='seleccione', max_length=20)
    institucion = models.CharField(max_length=40)
    area = models.CharField(max_length=40)
    caracter = models.CharField(max_length=40)
    sectorEconomico = models.CharField(max_length=40)
    programas = models.CharField(max_length=40)
    localidad = models.CharField(max_length=40)
    municipio = models.CharField(max_length=40)

class Poblacion(models.Model):
    genero = models.CharField(max_length=40)
    clienteInterno = models.CharField(max_length=40)
    clienteExterno = models.CharField(max_length=40)
    estratoSocioEconomico = models.CharField(choices=ESTRATO, default='seleccione', max_length=20)
    cobertura = models.CharField(max_length=40)
    coberturaGeografica = models.CharField(choices=COBERTURA, default='seleccione', max_length=20)
    Telefono = models.IntegerField(null=True)

class Institucion(models.Model):
    privada = models.CharField(max_length=40)
    publico = models.CharField(max_length=40)

class Proyecto(models.Model):
    nivel = models.CharField(max_length=40)
    titulo = models.CharField(max_length=40)
    logros = models.CharField(max_length=40)
    evaluacion_del_lugar_de_la_practica = models.CharField(choices=EVALUACION, default='seleccione', max_length=20)
    dificultades = models.CharField(max_length=40)
    observaciones = models.CharField(max_length=40)

class ProcesoDePractica(models.Model):
    objetivoGeneral = models.CharField(max_length=40)
    objetivosEspecificos = models.CharField(max_length=40)
    competencias = models.CharField(max_length=40)
    apoyo = models.CharField(max_length=40)
    
