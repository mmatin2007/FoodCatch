import pygame

class Punteggio:
    def __init__(self):
        self.punteggio = 0
        self.cibo_perso = 0
        self.font = pygame.font.SysFont(None, 55)

    def aumenta_punteggio(self, quantita):
        self.punteggio += quantita

    def aumenta_cibo_perso(self):
        self.cibo_perso += 1

    def resetta(self):
        self.punteggio = 0
        self.cibo_perso = 0

    def disegna(self, schermo):
        schermo.blit(self.font.render(f"Punteggio: {self.punteggio}", True, (0, 0, 0)), (10, 10))
        schermo.blit(self.font.render(f"Cibo Perso: {self.cibo_perso}", True, (0, 0, 0)), (10, 50))
