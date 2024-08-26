import pygame
import sys

class GameOver:
    def __init__(self, punteggio):
        self.punteggio = punteggio
        self.font = pygame.font.SysFont(None, 55)

    def mostra_schermo_game_over(self, schermo):
        schermo.fill((255, 255, 255)) 
        schermo.blit(self.font.render("Game Over", True, (255, 0, 0)), (300, 250)) 
        schermo.blit(self.font.render(f"Punteggio: {self.punteggio.punteggio}", True, (0, 0, 0)), (300, 300))  
        schermo.blit(self.font.render("Premi R per Riavviare o Q per Uscire", True, (0, 0, 0)), (100, 350))
        pygame.display.update()
        self.aspetta_input()

    def aspetta_input(self):
        in_attesa = True
        while in_attesa:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_r:
                        in_attesa = False
                    if evento.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()
