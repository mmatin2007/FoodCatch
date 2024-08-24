from main import *
import pygame
import random
import sys

WHITE = (255, 255, 255)

class GameOver:
    def __init__(self, score):
        self.score = score

    def game_over(self):
        schermo.fill(WHITE)
        schermo.blit(font.render("Game Over", True, BLACK), (300, 250))
        schermo.blit(font.render(f"Punteggio: {self.score.score}", True, BLACK), (300, 300))
        schermo.blit(font.render("Premi R per ricomiciare oppure U per uscire dal gioco", True, BLACK), (100, 350))
        pygame.display.update()
        self.wait_for_input()

    def aspetta_input_utente(self):
        waiting = True
        while waiting:
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    
                    if event.key == pygame.K_r:
                        waiting = False
                    
                    if event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()   
