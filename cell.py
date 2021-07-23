import pygame


class Cell:
    def __init__(self, rect, color):
        self.rect = rect
        self.color = color

    def draw(self, SCREEN):
        if self.color:
            pygame.draw.rect(SCREEN, self.color, self.rect)
