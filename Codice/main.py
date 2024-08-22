import pygame
import random
import sys
from catcher import *
from cibo import *
from game_over import *
from punteggio import *
from sfondo import *

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

font = pygame.font.SysFont(None, 55)

schermo = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Food Catcher Game")

Sfondo = pygame.image.load('Immagini\sfondo1.jpg')

apple_image = pygame.image.load("apple.png")
banana_image = pygame.image.load("banana.png")
melon_image = pygame.image.load("melon.png")

apple_image = pygame.transform.scale(apple_image, (50, 50))
banana_image = pygame.transform.scale(banana_image, (50, 50))
melon_image = pygame.transform.scale(melon_image, (50, 50))

class main:
    def __init__(self):
        self.cesto = cesto()
        self.lista_cibo = []
        self.lista_non_cibo = []
        self.punteggio = Punteggio()  

