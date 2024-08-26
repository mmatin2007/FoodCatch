import pygame

class Catcher:
    def __init__(self):
        self.larghezza = 100
        self.altezza = 20
        self.x = 800 // 2 - self.larghezza // 2
        self.y = 600 - self.altezza - 10
        self.velocita = 10
        self.immagine = pygame.Surface((self.larghezza, self.altezza))
        self.immagine.fill((0, 0, 0))  

    def muovi(self, direzione):
        if direzione == 'sinistra':
            self.x -= self.velocita
        elif direzione == 'destra':
            self.x += self.velocita
        self.x = max(0, min(800 - self.larghezza, self.x))

    def disegna(self, schermo):
        schermo.blit(self.immagine, (self.x, self.y))

    def ottieni_rettangolo(self):
        return pygame.Rect(self.x, self.y, self.larghezza, self.altezza)
