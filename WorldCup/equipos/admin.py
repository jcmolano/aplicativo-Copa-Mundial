from django.contrib import admin
from models import Equipo, Continente, Jugador

# Register your models here.

class EquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'continente', 'tecnico',)
    search_fields = ('nombre', 'continente__nombreContinente', )
    list_filter = ('continente',)



class ContinenteAdmin(admin.ModelAdmin):
    lis_display = ('nombreContinente', )


class JugadorAdmin(admin.ModelAdmin):
    lis_display = ('nombreJugador',)
    lis_display = ('posicion',)
    lis_display = ('EquipoJugador',)
    lis_display = ('estatura',)
    lis_display = ('PieJugador',)
    lis_display = ('tarjetaAmarilla',)
    lis_display = ('tarjetaRoja',)
    lis_display = ('lesionado',)
    lis_display = ('titular',)
    lis_display = ('goles',)


admin.site.register(Equipo,EquipoAdmin)
admin.site.register(Continente,ContinenteAdmin)
admin.site.register(Jugador,JugadorAdmin)
