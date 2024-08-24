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

WHITE = (255, 255, 255)

font = pygame.font.SysFont(None, 55)

schermo = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Food Catcher Game")

Sfondo = pygame.image.load('Immagini\sfondo1.jpg')

apple_image = pygame.image.load("apple.png")
banana_image = pygame.image.load("banana.png")
melon_image = pygame.image.load("melon.png")
non_cibo_image = pygame.image.load("non_cibo.png")

apple_image = pygame.transform.scale(apple_image, (50, 50))
banana_image = pygame.transform.scale(banana_image, (50, 50))
melon_image = pygame.transform.scale(melon_image, (50, 50))
non_cibo_image = pygame.transform.scale(non_cibo_image, (50, 50))

class main:
    def __init__(self):
        self.catcher = catcher()
        self.lista_cibo = []
        self.lista_non_cibo = []
        self.punteggio = Punteggio()  

    def game_loop(self):
        running = True
        while running:
            schermo.fill(WHITE)
            self.gestione_gioco()
            self.spostamento_catcher()
            self.genera_cibo()
            self.aggiorna_cibo()
            self.catcher.draw(schermo)
            self.punteggio.draw(schermo)

            if self.punteggio.cibo_perso >= 3:
                running = False

            pygame.display.update()
            pygame.time.Clock().tick(30)

        GameOver(self.punteggio).game_over()

    def gestione_gioco(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def spostamento_catcher(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.basket.move('left')
        if keys[pygame.K_RIGHT]:
            self.basket.move('right')

    def genera_cibo(self):
        if random.randint(1, 20) == 1:
            tipo_di_cibo = random.choice([apple_image, banana_image, melon_image])
            self.lista_cibo.append(cibo(tipo_di_cibo, 5))
        

        if random.randint(1, 40) == 1:
            non_cibo = pygame.Surface((30, 30))
            non_cibo = ([non_cibo.png])
            self.lista_non_cibo.append(cibo(non_cibo, 7))

    def aggiorna_cibo(self):
        for cibo in self.lista_cibo[:]:
            cibo.move()
            if cibo.y > SCREEN_HEIGHT:
                self.punteggio.cibo_perso()
                self.lista_cibo.remove(cibo)
            if self.catcher.get_rect().colliderect(cibo.get_rect()):
                self.punteggio.aumenta_punteggio(10)
                self.lista_cibo.remove(cibo)

        for non_cibo in self.lista_non_cibo[:]:
            non_cibo.move()
            if non_cibo.y > SCREEN_HEIGHT:
                self.lista_non_cibo.remove(non_cibo)
            if self.catcher.get_rect().colliderect(non_cibo.get_rect()):
                pygame.quit()
                sys.exit()

        for cibo in self.lista_cibo:
            cibo.draw(schermo)

        for non_cibo in self.lista_non_cibo:
            non_cibo.draw(schermo)
                
def main():
    game = main()
    sfondo = sfondo()
    sfondo.schermo_iniziale()
    game.game_loop()

if __name__ == "__main__":
    main()
