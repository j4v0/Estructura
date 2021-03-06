#!/usr/bin/env python
# coding: utf-8

# Explosión Galactica
# Juego Creado por Javier Schunk
# Año 2015

import pilasengine
import random

pilas = pilasengine.iniciar()


class Bienvenida(pilasengine.escenas.Escena):
    #Escena de Bienvenida con el menu
    
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
    #Escena 1 del juego 

    def iniciar(self):
        self.pilas.fondos.Galaxia()
        pilas.avisar("Pulsa las teclas de direccion y espacio para disparar.")
        self.puntos = pilas.actores.Puntaje(x=-280, y=200,
                                            color=pilas.colores.rojo)
        estrellas = []
        piedras = []
        
        
        
    #Creando la nave
        self.nave = pilas.actores.Nave(0, 0)
        self.nave.aprender(pilas.habilidades.LimitadoABordesDePantalla)
        
        
   
    #Creando los asteroides
        self.piedras = pilas.actores.Piedra()*10
        for i in self.piedras:
            
            x = random.randrange(-320, 320)
            y = random.randrange(-240, 240)
            while x >=-60 and x <60: 
                x = random.randrange(-320, 320)
            while y >=-60 and y <60:
                y = random.randrange(-240, 240)
          
            i.x = x
            i.y = y
            piedras.append(i)
        #self.piedras.empujar(1, 1)    

    #Creando estrella
        self.estrellas = pilas.actores.Estrella()*4
        self.estrellas.escala = [0.5]
        for e in self.estrellas:
            
            x = random.randrange(-320, 320)
            y = random.randrange(-240, 240)
            while x >=-60 and x <60: 
                x = random.randrange(-320, 320)
            while y >=-60 and y <60:
                y = random.randrange(-240, 240)
          
            e.x = x
            e.y = y
            estrellas.append(e)
        
        

        self.estrellas.aprender(pilas.habilidades.LimitadoABordesDePantalla)    
        pilas.colisiones.agregar(self.nave, self.estrellas, self.cuando_toca_estrella)
        self.estrellas.aprender(pilas.habilidades.PuedeExplotarConHumo)
        self.nave.definir_enemigos(self.estrellas)
        self.nave.habilidades.Disparar.definir_colision(self.estrellas, self.cuando_rompe_estrella)
        self.nave.definir_enemigos(self.piedras, self.puntos.aumentar)
        #self.piedras.aprender(pilas.habilidades.LimitadoABordesDePantalla)
        pilas.colisiones.agregar(self.nave, self.piedras, self.perder)
        self.pilas.actores.Sonido()

        return True     
    def cuando_toca_estrella(self, nave, estrella):
        self.puntos.escala = 0
        pilas.utils.interpolar(self.puntos, 'escala', 1, duracion=0.5)
        self.puntos.aumentar(10)
        self.sound_bonus = pilas.sonidos.cargar('saltar.wav')
        self.sound_bonus.reproducir()
        estrella.eliminar()
       
    
    def cuando_rompe_estrella(self, nave, estrella):
        self.puntos.escala = 0
        pilas.utils.interpolar(self.puntos, 'escala', 1, duracion=0.5)
        self.puntos.aumentar(-5)
        self.sound_smile = pilas.sonidos.cargar('smile.wav')
        self.sound_smile.reproducir()
        estrella.eliminar()
                
        
    def perder(self):
        self.pilas.tareas.eliminar_todas()
        self.nave.eliminar()
        self.pilas.escenas.EscenaFin(self.puntos.obtener())


    
    
class Escena2(pilasengine.escenas.Escena):
    #Escena 2 del juego
    
    def iniciar(self):
        self.pilas.fondos.Galaxia()
        self.puntos = pilas.actores.Puntaje(x=-280, y=200,
                                            color=pilas.colores.rojo)
        estrellas = []

    #Creando la nave
        self.nave = pilas.actores.Nave(0, 0)
        self.nave.aprender(pilas.habilidades.LimitadoABordesDePantalla)
        
        
   
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
            

    #Creando estrella
        self.estrellas = pilas.actores.Estrella()*4
        self.estrellas.escala = [0.5]
        for e in self.estrellas:
            
            x = random.randrange(-320, 320)
            y = random.randrange(-240, 240)
            while x >=-60 and x <60: 
                x = random.randrange(-320, 320)
            while y >=-60 and y <60:
                y = random.randrange(-240, 240)
          
            e.x = x
            e.y = y
            estrellas.append(e)
            

        self.estrellas.aprender(pilas.habilidades.LimitadoABordesDePantalla)    
        pilas.colisiones.agregar(self.nave, self.estrellas, self.cuando_toca_estrella)
        self.estrellas.aprender(pilas.habilidades.PuedeExplotarConHumo)
        self.nave.definir_enemigos(self.estrellas)
        #pilas.colisiones.agregar(self., self.estrellas, self.cuando_rompe_estrella)
        self.nave.habilidades.Disparar.definir_colision(self.estrellas, self.cuando_rompe_estrella)
        self.nave.definir_enemigos(self.enemigos, self.puntos.aumentar)
        self.enemigos.aprender(pilas.habilidades.LimitadoABordesDePantalla)
        pilas.colisiones.agregar(self.nave, self.enemigos, self.perder)
        self.pilas.actores.Sonido()
        self.enemigos.aprender(pilas.habilidades.PuedeExplotar)
        
        
       
        
        
    def cuando_toca_estrella(self, nave, estrella):
        self.puntos.escala = 0
        pilas.utils.interpolar(self.puntos, 'escala', 1, duracion=0.5)
        self.puntos.aumentar(10)
        self.sound_bonus = pilas.sonidos.cargar('saltar.wav')
        self.sound_bonus.reproducir()
        estrella.eliminar()
    
    def cuando_rompe_estrella(self, nave, estrella):
        self.puntos.escala = 0
        pilas.utils.interpolar(self.puntos, 'escala', 1, duracion=0.5)
        self.puntos.aumentar(-5)
        self.sound_smile = pilas.sonidos.cargar('smile.wav')
        self.sound_smile.reproducir()
        estrella.eliminar()
                
        
    
    def perder(self):
        self.pilas.tareas.eliminar_todas()
        self.nave.eliminar()
        self.pilas.escenas.EscenaFin(self.puntos.obtener())
        
class EscenaFin(pilasengine.escenas.Escena):

    def iniciar(self, puntaje):
        self.pilas.fondos.Noche()
        if puntaje <=0:
            mensaje = "Muy mal, has perdido, Sumaste {} puntos.".format(puntaje)
        elif puntaje >1 and puntaje <=10:
            mensaje = "Bien, Sumaste {} puntos.".format(puntaje)
        else:
            mensaje = "Muy bien, Sumaste {} puntos.".format(puntaje)
            
        
        
        self.texto = pilas.actores.Texto(mensaje)
        self.texto.y = 100
      
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
pilas.escenas.vincular(Escena2)
pilas.escenas.vincular(EscenaFin)
pilas.escenas.Bienvenida



pilas.ejecutar()
