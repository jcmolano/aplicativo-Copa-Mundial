from django.contrib import admin
from models import Estudiante, ProfesorTeorico, ProfesorPractico, Tiempo, Poblacion, Institucion, Proyecto, ProcesoDePractica 

# Register your models here.

class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('cedulaEstudiante',)

class ProfesorTeoricoAdmin(admin.ModelAdmin):
    list_display = ('cedulaProfesorT',)

class ProfesorPracticoAdmin(admin.ModelAdmin):
    list_display = ('cedulaProfesorP',)

class TiempoAdmin(admin.ModelAdmin):
    list_display = ('fechaDeInicio',)

class PoblacionAdmin(admin.ModelAdmin):
    list_display = ('genero',)

class InstitucionAdmin(admin.ModelAdmin):
    list_display = ('privada',)

class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('nivel',)

class ProcesoDePracticaAdmin(admin.ModelAdmin):
    list_display = ('objetivoGeneral',)


admin.site.register(Estudiante,EstudianteAdmin)
admin.site.register(ProfesorTeorico,ProfesorTeoricoAdmin)
admin.site.register(ProfesorPractico,ProfesorPracticoAdmin)
admin.site.register(Tiempo,TiempoAdmin)
admin.site.register(Poblacion,PoblacionAdmin)
admin.site.register(Institucion,InstitucionAdmin)
admin.site.register(Proyecto,ProyectoAdmin)
admin.site.register(ProcesoDePractica,ProcesoDePracticaAdmin)
