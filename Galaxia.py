#!/usr/bin/env python
# coding: utf-8

import pilasengine
import random

pilas = pilasengine.iniciar()

#Creando la nave
nave = pilas.actores.Nave()

#Creando los asteroides
enemigos = pilas.actores.Piedra() * 10
nave.definir.enemigos(enemigos)