from django.db import models

# Create your models here.

POSICIONES = ( 
    ('seleccione', 'Seleccione'),
    ('arquero', 'Arquero'), 
    ('defensa', 'Defensa'),
    ('volante', 'Volante'),
    ('delantero', 'Delantero'),

)

class Continente(models.Model):
    nombreContinente = models.CharField(max_length=50)
    def __unicode__(self):
        return self.nombreContinente

class Equipo(models.Model):
    nombre = models.CharField(max_length=50)
    continente = models.ForeignKey(Continente)
    tecnico = models.CharField(max_length=60)
    def __unicode__(self):
        return self.nombre

class Jugador(models.Model):
    nombreJugador = models.CharField(max_length=60)
    posicion = models.CharField(choices=POSICIONES, default='seleccione',max_length=10 )
    equipo = models.ForeignKey(Equipo)
    estatura = models.DecimalField(max_digits=5, decimal_places=2)
    pieHabil = models.CharField(max_length=50)
    tarjetaAmarilla = models.SlugField(unique=True)
    tarjetaRoja = models.SlugField(unique=True)
    lesionado = models.SlugField(unique=True)
    titular = models.SlugField(unique=True)
    goles = models.IntegerField(max_length=5)
    foto = models.ImageField(upload_to='imagenes', verbose_name='Foto', null=True,)  
    def __unicode__(self):
        return self.nombreJugador

