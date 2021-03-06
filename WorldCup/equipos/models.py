from django.db import models

# Create your models here.
POSICIONES = (
    ('seleccione', 'Seleccione'),
    ('arquero', 'Arquero'),
    ('defensa', 'Defensa'),
    ('volante', 'Volante'),
    ('delantero', 'Delantero'),   
)
PIEHABIL = (
    ('seleccione', 'Seleccione'),
    ('derecho', 'Derecho'),
    ('izquierdo', 'Izquierdo'),
)
LETITULAR = (
    ('seleccione', 'Seleccione'),
    ('si', 'Si'),
    ('no', 'No'),
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
    posicion = models.CharField(choices=POSICIONES, default='seleccione', max_length=10)
    equipoJugador = models.ForeignKey(Equipo)
    estatura = models.PositiveIntegerField(null=True)
    pieJugador = models.CharField(choices=PIEHABIL, default='seleccione', max_length=10)
    tarjetaAmarilla = models.IntegerField(null=True)
    tarjetaroja = models.IntegerField(null=True)
    lesionado =  models.CharField(choices=LETITULAR, default='seleccione', max_length=10)
    titular = models.CharField(choices=LETITULAR, default='seleccione', max_length=10)
    goles = models.PositiveIntegerField(null=True)
    foto = models.ImageField(upload_to='images', verbose_name='Foto', blank=True)
    def __unicode__(self):
        return self.nombreJugador


