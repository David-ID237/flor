#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 18:13:50 2024

@author: deivit
"""

from turtle import *
from colorsys import *

# Configuración de la pantalla
bgcolor("black")
width(5)
speed(15)

# Función para dibujar la flor
def dibujar_flor():
    pu()
    setpos(190, -60)  # Posición de la flor
    pd()
    
    R = 1
    G = 1
    B = 0

    for i in range(150):
        begin_fill()
        color((R, G, B))
        circle(150-i, 50)
        lt(80)
        circle(150-i, 50)
        rt(150)
        R -= 0.0065
        G -= 0.0065
        end_fill()

# Función para dibujar el tallo
def dibujar_tallo():
    pu()
    setpos(190, -55)  # Posición inicial del tallo
    pd()
    color("green")  # Color del tallo
    width(10)  # Grosor del tallo
    setheading(-90)  # Girar hacia abajo
    fd(300)  # Dibujar el tallo hacia abajo

# Dibujar la flor y el tallo
dibujar_tallo()  # Dibujar el tallo primero
dibujar_flor()   # Dibujar la flor después

done()
