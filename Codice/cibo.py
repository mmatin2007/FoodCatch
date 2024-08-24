from main import * 
import pygame
import random
import sys

class cibo:
    def __init__(self, image, speed):
        self.x = random.randint(0, SCREEN_WIDTH - 50)
        self.y = 0
        self.image = image
        self.speed = speed
        self.width = image.get_width()
        self.height = image.get_height()

    def move(self):
        self.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)