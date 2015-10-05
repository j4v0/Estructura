#!/usr/bin/env python
# coding: utf-8

import pilasengine
import random

pilas = pilasengine.iniciar()

#Creación de Menú
pilas.fondos.Noche()

class Bienvenida(pilasengine.escenas.Escena):
	def iniciar_juego():
		print "Tengo que iniciar el juego"
		Escena1_juego
	
	def salir_del_juego():
		print "Tengo que salir..."
		pilas.terminar()
	
	pilas.actores.Menu(
		[
			("Iniciar Juego", iniciar_juego),
			("Salir del Juego", salir_del_juego),
		])

class Escena1_juego(pilasengine.escenas.Escena):
	def iniciar(self):
		#Creando la nave
		nave = pilas.actores.Nave(0, -100)

#Creando los asteroides
enemigos = pilas.actores.Piedra()*8
nave.definir_enemigos(enemigos)

pilas.ejecutar()
