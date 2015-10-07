#!/usr/bin/env python
# coding: utf-8

import pilasengine
import random

pilas = pilasengine.iniciar()

#Creación de Menú


class Bienvenida(pilasengine.escenas.Escena):
	pilas.fondos.Noche()
	titulo = pilas.actores.Texto("EXPLOSION GALACTICA", magnitud=40, fuente="visitor1.ttf", y=90)	
	def iniciar():
		print "Tengo que iniciar el juego"
		pilas.fondos.Noche()
	
	def _iniciar_juego():
		pilas.escenas.Escena1_juego()
	
	def salir_del_juego():
		print "Tengo que salir..."
		pilas.terminar()
	
	pilas.actores.Menu(
		[
			("Iniciar Juego", _iniciar_juego),
			("Salir del Juego", salir_del_juego),
		])
		
class Escena1_juego(pilasengine.escenas.Escena):
	def _iniciar_(self):
		#Creando la nave
		nave = pilas.actores.Nave(0, -100)
		nave.aprender(pilas.habilidades.LimitadoABordesDePantalla)
		nave.definir_enemigos(enemigos, puntaje.aumentar)
		pilas.colisiones.agregar(nave, enemigos, nave.eliminar)
		#Creando los asteroides
		enemigos = pilas.actores.Piedra()*12
		nave.definir_enemigos(enemigos)

pilas.ejecutar()
