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
        #pilas.avisar("Pulsa las teclas de direccion y espacio para disparar.")
        texto = pilas.actores.TextoInferior("NIVEL 1"); texto.color = pilas.colores.amarillo
        puntos = pilas.actores.Puntaje(x=-280, y=200,
                                            color=pilas.colores.rojo)
        
        global puntos
        
        estrellas = []
        #piedras = []
        
        self.tiempo = 15
        contador = pilas.actores.Texto("...")
        contador.x = 0
        contador.y = 200
        
    # Esta funcion se ejecutara 1 vez por segundo    
        def descontar_tiempo():
           
            self.tiempo = self.tiempo - 1
        
    # Si puede seguir jugando, reducimos el contador.
            if self.tiempo > 0:
                contador.texto = str(self.tiempo) # tiempo es un numero, asi que lo tenemos que convertir a texto con str.
    
    # Si es tiempo de perder.
            if self.tiempo == 0:
                pilas.escenas.Escena2()
                
        # le indicamos a pilas que llame a la funcion cada 1 segundo
        pilas.tareas.siempre(1, descontar_tiempo)   
        
        
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
            #piedras.append(i)
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
        self.nave.definir_enemigos(self.piedras, puntos.aumentar)
        self.piedras.aprender(pilas.habilidades.PuedeExplotar)
        self.piedras.aprender(pilas.habilidades.LimitadoABordesDePantalla)
        pilas.colisiones.agregar(self.nave, self.piedras, self.perder)
        self.pilas.actores.Sonido()


    def cuando_toca_estrella(self, nave, estrella):
        puntos.escala = 0
        pilas.utils.interpolar(puntos, 'escala', 1, duracion=0.5)
        puntos.aumentar(5)
        self.sound_bonus = pilas.sonidos.cargar('saltar.wav')
        self.sound_bonus.reproducir()
        estrella.eliminar()
       
    
    def cuando_rompe_estrella(self, nave, estrella):
        puntos.escala = 0
        pilas.utils.interpolar(puntos, 'escala', 1, duracion=0.5)
        puntos.aumentar(-5)
        self.sound_smile = pilas.sonidos.cargar('smile.wav')
        self.sound_smile.reproducir()
        estrella.eliminar()
                
        
    def perder(self):
        self.pilas.tareas.eliminar_todas()
        self.nave.eliminar()
        self.pilas.escenas.EscenaFin(puntos.obtener())

   
    
class Escena2(pilasengine.escenas.Escena):
    #Escena 2 del juego
    
    def iniciar(self):
        self.pilas.fondos.Galaxia()
        #pilas.avisar("Pulsa las teclas de direccion y espacio para disparar.")
        texto = pilas.actores.TextoInferior("NIVEL 2"); texto.color = pilas.colores.amarillo
        puntos = pilas.actores.Puntaje(x=-280, y=200,
                                                    color=pilas.colores.rojo)
        
        #global puntos2
        
     
        
        #puntos2 = puntos
        
        estrellas = []
        
        self.tiempo = 15
        contador = pilas.actores.Texto("...")
        contador.x = 0
        contador.y = 200
        
    # Función que decuenta el tiempo   
        def descontar_tiempo():
           
            self.tiempo = self.tiempo - 1
        
    # Si puede seguir jugando, reducimos el contador.
            if self.tiempo > 0:
                contador.texto = str(self.tiempo) # tiempo es un numero, asi que lo tenemos que convertir a texto con str.
    
    # Si el tiempo llega a 0
            if self.tiempo == 0:
                pilas.escenas.EscenaFin()
                
        # le indicamos a pilas que llame a la funcion cada 1 segundo
        pilas.tareas.siempre(1, descontar_tiempo)   
        
        
    #Creando la nave
        self.nave = pilas.actores.Nave(0, 0)
        self.nave.aprender(pilas.habilidades.LimitadoABordesDePantalla)
        
        
   
    #Creando los asteroides
        self.piedras = pilas.actores.Piedra()*15
        for i in self.piedras:
            
            x = random.randrange(-320, 320)
            y = random.randrange(-240, 240)
            while x >=-60 and x <60: 
                x = random.randrange(-320, 320)
            while y >=-60 and y <60:
                y = random.randrange(-240, 240)
          
            i.x = x
            i.y = y
           
        
        self.piedras.empujar(1, 1)    

    #Creando estrella
        self.estrellas = pilas.actores.Estrella()*5
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
        self.nave.definir_enemigos(self.piedras, puntos.aumentar)
        self.piedras.aprender(pilas.habilidades.PuedeExplotar)
        #self.piedras.aprender(pilas.habilidades.LimitadoABordesDePantalla)
        pilas.colisiones.agregar(self.nave, self.piedras, self.perder)
        self.pilas.actores.Sonido()


    def cuando_toca_estrella(self, nave, estrella):
        puntos.escala = 0
        pilas.utils.interpolar(puntos, 'escala', 1, duracion=0.5)
        puntos.aumentar(5)
        self.sound_bonus = pilas.sonidos.cargar('saltar.wav')
        self.sound_bonus.reproducir()
        estrella.eliminar()
       
    
    def cuando_rompe_estrella(self, nave, estrella):
        puntos.escala = 0
        pilas.utils.interpolar(puntos, 'escala', 1, duracion=0.5)
        puntos.aumentar(-5)
        self.sound_smile = pilas.sonidos.cargar('smile.wav')
        self.sound_smile.reproducir()
        estrella.eliminar()
                
        
    def perder(self):
        self.pilas.tareas.eliminar_todas()
        self.nave.eliminar()
        self.pilas.escenas.EscenaFin(puntos.obtener())
        
class EscenaFin(pilasengine.escenas.Escena):

    def iniciar(self, puntaje):
        self.pilas.fondos.Noche()
        if puntaje <=0:
            mensaje = "Muy mal, HAS PERDIDO \n    Sumaste {} puntos".format(puntaje)
        elif puntaje >=1 and puntaje <=10:
            mensaje = "          Bien \n Sumaste {} puntos".format(puntaje)
        elif puntaje >=11 and puntaje <=69:
            mensaje = "        Muy Bien \n Sumaste {} puntos".format(puntaje)
        else:
            mensaje = "Puntaje PERFECTO \n Sumaste {} puntos".format(puntaje)
            
        
        
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
