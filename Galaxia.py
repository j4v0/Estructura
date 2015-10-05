#!/usr/bin/env python
# coding: utf-8

import pilasengine
import random

pilas = pilasengine.iniciar()

#Creando la nave
nave = pilas.actores.Nave(0, -180)

#Creando los asteroides
enemigos = pilas.actores.Piedra()*8
nave.definir_enemigos(enemigos)

pilas.ejecutar()