import pygame
import random

class Cibo:
    def __init__(self, immagine, velocita):
        self.x = random.randint(0, 800 - 50)
        self.y = 0
        self.immagine = immagine
        self.velocita = velocita
        self.larghezza = immagine.get_width()
        self.altezza = immagine.get_height()

    def muovi(self):
        self.y += self.velocita

    def disegna(self, schermo):
        schermo.blit(self.immagine, (self.x, self.y))

    def ottieni_rettangolo(self):
        return pygame.Rect(self.x, self.y, self.larghezza, self.altezza)
    
    def aumenta_velocita(self, incremento):
        self.velocita += incremento
