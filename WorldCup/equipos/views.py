from django.shortcuts import render
from django.views.generic import ListView
from django.http import Http404
from models import Continente, Jugador, Equipo
# Create your views here.


class ListarContinentes(ListView):
    model = Continente
    template_name = 'lista_continentes.html'

class ListarJugadores(ListView):
 
    model = Jugador
    template_name = 'lista_jugadores.html'

class ListarEquipo(ListView):
    model = Equipo
    template_name = 'lista_equipos.html'

def detalleJugador(request, jugador_id):
    try:
        jugador = Jugador.objects.get(pk=jugador_id)
    except Jugador.DoesNotExist:
        raise Http404
    return render(request, 'player.html', {'jugador': jugador})
