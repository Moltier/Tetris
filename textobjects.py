import pygame
from settings import settings
pygame.font.init()


class TextObject:
    text_color = (255, 255, 255)

    def __init__(self, position, color=None, text="", text_color=None,
                 font_family='comicsansms', font_size=18, positioning='topleft', size=None):
        self.position = position
        self.positioning = positioning
        self.color = color
        self.size = size
        self.font = pygame.font.SysFont(font_family, font_size)
        if text_color:
            self.text_color = text_color
        else:
            self.text_color = TextObject.text_color
        self.text = self.font.render(text, True, self.text_color)
        self.greyed_text = self.font.render(text, True, [int(x * 0.5) for x in self.text_color])

        if self.size:
            self.rect = pygame.Rect(self.position, self.size)
        else:
            self.rect = self.text.get_rect()
        if self.positioning == 'topleft':
            self.rect.topleft = self.position
        elif self.positioning == 'midtop':
            self.rect.midtop = self.position
        elif self.positioning == 'topright':
            self.rect.topright = self.position

        self.down = False

    def update_text(self, new_text):
        self.text = self.font.render(new_text, True, self.text_color)
        self.greyed_text = self.font.render(new_text, True, [int(x * 0.5) for x in self.text_color])

    def draw(self, SCREEN, y_scroll=0):
        if self.color:
            pygame.draw.rect(SCREEN, self.color, self.rect)

        x = self.rect.x + round(self.rect.width / 2) - round(self.text.get_width() / 2)
        y = self.rect.y + round(self.rect.height / 2) - round(self.text.get_height() / 2) + y_scroll
        if y in range(settings.screen_size[1]):
            if self.down:
                SCREEN.blit(self.greyed_text, (x, y))
            else:
                SCREEN.blit(self.text, (x, y))
