from main import *
import pygame
import random
import sys

class sfondo:
    def schermo_iniziale(self):
        schermo.fill(Sfondo)
        schermo.blit(font.render("Food Catcher Game", True, BLACK), (200, 250))
        schermo.blit(font.render("Press SPACE to Start", True, BLACK), (200, 300))
        pygame.display.update()
        self.wait_for_start()

    def aspetta_a_partire(self):
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        waiting = False