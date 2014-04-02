from django.shortcuts import render
from django.views.generic import ListView
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
