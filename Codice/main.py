import pygame
import sys
import random

from catcher import Catcher
from punteggio import Punteggio
from game_over import GameOver
from sfondo import Sfondo
from cibo import Cibo

pygame.init()

LARGHEZZA_SCHERMO = 800
ALTEZZA_SCHERMO = 600

schermo = pygame.display.set_mode((LARGHEZZA_SCHERMO, ALTEZZA_SCHERMO))
pygame.display.set_caption("Gioco Raccogli Cibo")

immagine_mela = pygame.image.load("apple.png")
immagine_banana = pygame.image.load("banana.png")
immagine_melone = pygame.image.load("melon.png")
immagine_non_cibo = pygame.image.load("non_cibo.png")

immagine_mela = pygame.transform.scale(immagine_mela, (50, 50))
immagine_banana = pygame.transform.scale(immagine_banana, (50, 50))
immagine_melone = pygame.transform.scale(immagine_melone, (50, 50))
immagine_non_cibo = pygame.transform.scale(immagine_non_cibo, (50, 50))

class Main:
    def __init__(self):
        self.catcher = Catcher()
        self.punteggio = Punteggio()
        self.lista_cibo = []
        self.lista_non_cibo = []

    def ciclo_gioco(self):
        in_corso = True
        while in_corso:
            schermo.fill((255, 255, 255)) 
            self.gestisci_eventi()
            self.muovi_catcher()
            self.genera_oggetti()
            self.aggiorna_oggetti()
            self.catcher.disegna(schermo)
            self.punteggio.disegna(schermo)

            if self.punteggio.cibo_perso >= 3:
                in_corso = False

            pygame.display.update()
            pygame.time.Clock().tick(30)

        GameOver(self.punteggio).mostra_schermo_game_over(schermo)

    def gestisci_eventi(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def verifica_aumento_velocita(self):
        if self.punteggio.punteggio >= self.soglia_punteggio and self.incremento_velocita_attuale == 0:
            self.aumenta_velocita_cibo()
            self.incremento_velocita_attuale += self.incremento_velocita_cibo
            self.soglia_punteggio += 50  

    def aumenta_velocita_cibo(self):
        for cibo in self.lista_cibo:
            cibo.aumenta_velocita(self.incremento_velocita_cibo)
        for non_cibo in self.lista_non_cibo:
            non_cibo.aumenta_velocita(self.incremento_velocita_cibo)

    def muovi_catcher(self):
        tasti = pygame.key.get_pressed()
        if tasti[pygame.K_LEFT]:
            self.catcher.muovi('sinistra')
        if tasti[pygame.K_RIGHT]:
            self.catcher.muovi('destra')

    def genera_oggetti(self):
        if random.randint(1, 20) == 1:
            tipo_cibo = random.choice([immagine_mela, immagine_banana, immagine_melone])
            self.lista_cibo.append(Cibo(tipo_cibo, 5))

        if random.randint(1, 40) == 1:
            self.lista_non_cibo.append(Cibo(immagine_non_cibo, 7))

    def aggiorna_oggetti(self):
        for cibo in self.lista_cibo[:]:
            cibo.muovi()
            if cibo.y > ALTEZZA_SCHERMO:
                self.punteggio.aumenta_cibo_perso()
                self.lista_cibo.remove(cibo)
            if self.catcher.ottieni_rettangolo().colliderect(cibo.ottieni_rettangolo()):
                self.punteggio.aumenta_punteggio(10)
                self.lista_cibo.remove(cibo)

        for non_cibo in self.lista_non_cibo[:]:
            non_cibo.muovi()
            if non_cibo.y > ALTEZZA_SCHERMO:
                self.lista_non_cibo.remove(non_cibo)
            if self.catcher.ottieni_rettangolo().colliderect(non_cibo.ottieni_rettangolo()):
                pygame.quit()
                sys.exit()

        for cibo in self.lista_cibo:
            cibo.disegna(schermo)

        for non_cibo in self.lista_non_cibo:
            non_cibo.disegna(schermo)


def main():
    gioco = Main()
    sfondo = Sfondo()
    sfondo.mostra_schermo_iniziale(schermo)
    gioco.ciclo_gioco()

if __name__ == "__main__":
    main()
