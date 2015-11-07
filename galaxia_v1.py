#!/usr/bin/env python
# coding: utf-8

# Explosión Galactica
# Juego Creador por Javier Schunk
# Año 2015

import pilasengine
import random

pilas = pilasengine.iniciar()

#Creación de Menú


class Bienvenida(pilasengine.escenas.Escena):
    pilas.fondos.Noche()
    pilas.actores.Texto("EXPLOSION \n GALACTICA", 
                        magnitud=40, y=120)
    pilas.avisar("Pulsa las teclas de direccion para elegir")

    def iniciar_juego():
        print "Tengo que iniciar el juego"
        e1 = pilas.escenas.Escena1()

    def salir_del_juego():
        pilas.terminar()
    
    def ayuda ():
        eay = pilas.escenas.Escena_ayuda()
        

        
        

    pilas.actores.Menu(
        [
            ("Iniciar Juego", iniciar_juego),
            ("Instrucciones", ayuda),
            ("Salir del Juego", salir_del_juego),
        ])

class Escena_ayuda(pilasengine.escenas.Escena):
    def iniciar (self):
        self.pilas.fondos.Noche()
        mensaje = "BLA BLA BLA BLA BLA"
        self.texto = pilas.actores.Texto(mensaje)
        self.texto.y = 100
        
        pilas.actores.Menu(
            [
            ("Iniciar juego", pilas.escenas.Escena1),
        
            ])
    
    
class Escena1(pilasengine.escenas.Escena):
    def iniciar(self):
        self.pilas.fondos.Galaxia()
        pilas.avisar("Pulsa las teclas de direccion  y espacio para disparar.")
        self.puntos = pilas.actores.Puntaje(x=-280, y=200,
                                            color=pilas.colores.amarillo)
         
            
    #Creando la nave
        self.nave = pilas.actores.Nave(0, 0)
        self.nave.aprender(pilas.habilidades.LimitadoABordesDePantalla)
        

        
        
        #pilas.colisiones.agregar(self.nave, self.estrellas, self.puntos.aumentar(50))

    
    #Creando los asteroides
   
        self.enemigos = pilas.actores.Piedra()*20
        for i in self.enemigos:
            
            x = random.randrange(-320, 320)
            y = random.randrange(-240, 240)
            while x >=-60 and x <60: 
                x = random.randrange(-320, 320)
            while y >=-60 and y <60:
                y = random.randrange(-240, 240)
          
            i.x = x
            i.y = y

    #Creando estrellas
        
        self.estrellas = pilas.actores.Estrella(100, 200)
        self.estrellas.escala = [0.5]
        pilas.colisiones.agregar(self.nave, self.estrellas, self.cuando_colisiona)
        
        self.nave.definir_enemigos(self.enemigos, self.puntos.aumentar)
        self.enemigos.aprender(pilas.habilidades.LimitadoABordesDePantalla)
        pilas.colisiones.agregar(self.nave, self.enemigos, self._perder_)
        self.pilas.actores.Sonido()
        self.enemigos.aprender(pilas.habilidades.PuedeExplotar)
       
        
        
    def cuando_colisiona(self):
        self.puntos.escala = 0
        pilas.utils.interpolar(self.puntos, 'escala', 1, duracion=0.5)
        self.puntos.aumentar(10)
        self.estrellas.eliminar()
        self.fin_de_juego = False
        
        
    
    def _perder_(self):
        self.fin_de_juego = True
        self.pilas.tareas.eliminar_todas()
        self.nave.eliminar()
        self.pilas.escenas.EscenaFin(self.puntos.obtener())


        
class EscenaFin(pilasengine.escenas.Escena):

    def iniciar(self, puntaje):
        self.pilas.fondos.Noche()
        mensaje = "Has perdido, Sumaste {} puntos.".format(puntaje)
        
        self.texto = pilas.actores.Texto(mensaje)
        self.texto.y = 100
        """boton = pilas.interfaz.Boton("Reiniciar")
        boton.y = -70
        boton.conectar(self.volver_juego)
        salir = pilas.interfaz.Boton("Salir")
        salir.y = -120
        salir.conectar(self.salir_del_juego)"""   
        pilas.actores.Menu(
        [
            ("Volver a jugar", self.volver_juego),
            ("Salir del Juego", self.salir_del_juego),
        ])    
    def volver_juego(self):
        pilas.escenas.Escena1()

    def salir_del_juego(self):
        print "Tengo que salir..."
        pilas.terminar()
        print "Gracias por Jugar"
        

        
    
    


    
        
        
        
    




pilas.escenas.vincular(Bienvenida)
pilas.escenas.vincular(Escena_ayuda)
pilas.escenas.vincular(Escena1)
pilas.escenas.vincular(EscenaFin)
pilas.escenas.Bienvenida



pilas.ejecutar()
