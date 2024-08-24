import pygame
import random
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BLACK = (0, 0, 0)

class catcher:
    def __init__(self):
        self.width = 100
        self.height = 20
        self.x = SCREEN_WIDTH // 2 - self.width // 2
        self.y = SCREEN_HEIGHT - self.height - 10
        self.speed = 10
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(BLACK)

    def move(self, direction):
        if direction == 'left':
            self.x -= self.speed
        elif direction == 'right':
            self.x += self.speed
        self.x = max(0, min(SCREEN_WIDTH - self.width, self.x))

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)