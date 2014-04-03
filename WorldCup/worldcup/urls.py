from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
import equipos.views
 
admin.autodiscover()
 
urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^continentes/', equipos.views.ListarContinentes.as_view(), name='lista-continentes',),
    url(r'^jugadores/', equipos.views.ListarJugadores.as_view(), name='lista-jugadores',),
    url(r'^player/(?P<jugador_id>/d+)/player.hmtl$',
                'equipos.views.detalleJugador', name='lista-jugador'),    

    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
                {'document_root':settings.MEDIA_ROOT,}
        ),
)
 
urlpatterns += staticfiles_urlpatterns()
