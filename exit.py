import sys
import pygame
from data import Game
from crypto import save_scores


def exit_program():
    save_scores(Game.hall_of_fame)
    pygame.quit()
    sys.exit()
