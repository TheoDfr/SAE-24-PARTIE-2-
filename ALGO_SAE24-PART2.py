"""
Reproduction de la figure vortex_2 de  et enregistre la dans un fichier png
Crée le Mardi 12 Mai 2022 - Jeudi 26 Mai 2022
Crée un fichier png et retourne le nom de ce fichier
"""
# Utilise pygame, random, math :
# -*- coding: utf-8 -*-

from pygame import *
import random 
from random import *
from math import *
import time 
import sys 
from pygame.locals import *
import pygame
pygame.init()
BLACK = (0, 0, 0)
WHITE=(255,255,255)
RED=(255,0,0)

couleur=str(sys.argv[5].replace(',','.'))

nombre = randrange(9, 500, 2) #prend un nombre aléatoire entre 9 et 



screen = pygame.display.set_mode((600, 600))
  
  
# Mise en place de la couleur blanche en fond 
screen.fill((0, 0, 0))
  
# Utilisation du module draw.
# pygame pour dessiner le cercle 
#pygame.draw.circle(screen, (0, 0 , 0),
#                    [300, 300], 100, 0)
for i in range(0,15):
    for j in range(0,21):
        angle, longueurfinal , longueur = i*2*pi/15+j/18*pi/15, 600 , 100 
        x = 300 + longueur * cos(angle+0.32)  
        y = 300 + longueur * sin(angle+0.32) 
        x_final = 300 + longueurfinal * cos(angle)  
        y_final = 300 + longueurfinal * sin(angle) 
        pygame.draw.line(screen,WHITE,(x,y),(x_final,y_final),1)
        
        angle, longueurfinal , longueur = i*2*pi/15+j/3*pi/15, 600 , 100
        x = 300 + longueur * cos(angle + 0.32)  
        y = 300 + longueur * sin(angle + 0.32) 
        x_final = 300 + longueurfinal * cos(angle)  
        y_final = 300 + longueurfinal * sin(angle) 
        pygame.draw.line(screen,BLACK,(x,y),(x_final,y_final),1)
        
        
        

        
        angle, longueurfinal , longueur = i*2*pi/15+j/56*pi/15, 25 , 100
        x = 300 + longueur * cos(angle + 0.78)  
        y = 300 + longueur * sin(angle + 0.78) 
        x_final = 300 + longueurfinal * cos(angle)  
        y_final = 300 + longueurfinal * sin(angle + 0.32) 
        pygame.draw.line(screen,BLACK,(x,y),(x_final,y_final),1)
   
        
    

for i in range (150):
    angle, longueurfinal , longueur = i*6.28/150, 300 , 100 
    x = 300 + longueur * cos(angle +0.7)  
    y = 300 + longueur * sin(angle +0.7) 
    x_final = 300 + longueurfinal * cos(angle)  
    y_final = 300 + longueurfinal * sin(angle)  
    #pygame.draw.line(screen,BLACK,(x,y),(x_final,y_final),1)

#Pour dessiner les lignes
  
    
#for i in range (100):
#    angle, longueurfinal , longueur = i*6.28/15, 300 , 100 
#    x = 300 + longueur * cos(angle+0.1)  
#    y = 300 + longueur * sin(angle+0.1) 
#    x_final = 300 + longueurfinal * cos(angle)  
#    y_final = 300 + longueurfinal * sin(angle) 
#    pygame.draw.line(screen,WHITE,(x,y),(x_final,y_final),nombre)

 
    
    
    



# Dessine la forme
pygame.display.update()
# Enregistre la figure
fichier='figuresae24.png'
pygame.image.save(screen,fichier)

print(fichier)

run = True
while run:
    for pyEvent in event.get():
        if pyEvent.type == QUIT:
            run = False

quit()

