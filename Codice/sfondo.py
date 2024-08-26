import pygame
import sys

class Sfondo:
    def __init__(self):
        self.font = pygame.font.SysFont(None, 55)

    def mostra_schermo_iniziale(self, schermo):
        schermo.fill((255, 255, 255)) 
        schermo.blit(self.font.render("Gioco Raccogli Cibo", True, (0, 0, 0)), (200, 250))
        schermo.blit(self.font.render("Premi SPAZIO per Iniziare", True, (0, 0, 0)), (200, 300))
        pygame.display.update()
        self.aspetta_inizio()

    def aspetta_inizio(self):
        in_attesa = True
        while in_attesa:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_SPACE:
                        in_attesa = False
