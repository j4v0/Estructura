#!/usr/bin/env python
# coding: utf-8

import pilasengine
import random

pilas = pilasengine.iniciar()

#Creación de Menú


class Bienvenida(pilasengine.escenas.Escena):
	pilas.fondos.Noche()
	pilas.actores.Texto("EXPLOSION GALACTICA", 
						magnitud=40, fuente="visitor1.ttf", y=90)	
	
	def iniciar_juego():
		print "Tengo que iniciar el juego"
		pilas.escenas.Escena1()
		
	
	def salir_del_juego():
		print "Tengo que salir..."
		pilas.terminar()
	
	pilas.actores.Menu(
		[
			("Iniciar Juego", iniciar_juego),
			("Salir del Juego", salir_del_juego),
		])
		
class Escena1(pilasengine.escenas.Escena):
	def iniciar(self):
		self.pilas.fondos.Galaxia()
		#Creando la nave
		self.nave = pilas.actores.Nave(0, -100)
		self.puntos = pilas.actores.Puntaje(x=230, y=200,
                                            color=pilas.colores.amarillo)
		self.pilas.actores.Sonido()
		nave.aprender(pilas.habilidades.LimitadoABordesDePantalla)
		nave.definir_enemigos(enemigos, puntaje.aumentar)
		pilas.colisiones.agregar(nave, enemigos, nave.eliminar)
		#Creando los asteroides
		enemigos = pilas.actores.Piedra()*12
		nave.definir_enemigos(enemigos)
		
pilas.escenas.vincular(Bienvenida)
pilas.escenas.vincular(Escena1)
pilas.escenas.vincular(EscenaFin)
pilas.escenas.Bienvenida



pilas.ejecutar()
