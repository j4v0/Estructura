#!/usr/bin/env python
# coding: utf-8

# Explosión de Galaxias
# Juego Creador por Javier Schunk
# Año 2015

import pilasengine
import random

pilas = pilasengine.iniciar()

#Creación de Menú


class Bienvenida(pilasengine.escenas.Escena):
	pilas.fondos.Noche()
	pilas.actores.Texto("EXPLOSION GALACTICA", 
						magnitud=40, fuente="visitor1.ttf", y=80)	
	
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
		pilas.avisar("Pulsa las teclas de direccion  y espacio para disparar.")
	#Creando la nave
		self.nave = pilas.actores.Nave(0, -100)
			
	#Creando los asteroides
		self.enemigos = pilas.actores.Piedra()*15
		self.nave.definir_enemigos(self.enemigos)
		pilas.colisiones.agregar(self.nave, self.enemigos, self.nave.eliminar)
		self.nave.aprender(pilas.habilidades.LimitadoABordesDePantalla)
		self.pilas.actores.Sonido()
		
pilas.escenas.vincular(Bienvenida)
pilas.escenas.vincular(Escena1)
pilas.escenas.Bienvenida



pilas.ejecutar()
