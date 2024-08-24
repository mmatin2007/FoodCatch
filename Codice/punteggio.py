from main import *
import pygame
import random
import sys
from catcher import *
from cibo import *
from game_over import *
from sfondo import *

BLACK = (0, 0, 0) 

class Punteggio:
    def __init__(self):
        self.score = 0
        self.missed_food = 0

    def aumenta_punteggio(self, amount):
        self.score += amount

    def cibo_perso(self):
        self.missed_food += 1

    def reset(self):
        self.score = 0
        self.missed_food = 0

    def draw(self, screen):
        screen.blit(font.render(f"Punteggio: {self.score}", True, BLACK), (10, 10))
        screen.blit(font.render(f"Cibo Perso: {self.missed_food}", True, BLACK), (10, 50))