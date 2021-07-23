import pygame
from menus.main_menu import main_menu
from menus.hall_of_fame_menu import hall_of_fame_menu
from menus.settings_menu import settings_menu
from menus.pause_menu import pause_menu
from menus.game import game_loop
from menus.control_menu import control_menu
from menus.name_menu import name_menu
from settings import Settings, settings
from matrix import Matrix
from data import Game, UserInterface
from crypto import *


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()

    SCREEN = pygame.display.set_mode(settings.screen_size, pygame.HWSURFACE | pygame.DOUBLEBUF)

    matrix = Matrix(settings.width, settings.height, settings.node_size, settings.play_area_rect)
    ui = UserInterface()
    ui.set_ui_pos(settings.screen_size, settings.width)
    game_data = Game()
    Game.hall_of_fame = load_scores(get_key(), Settings.default_scores)
    ui.create_hall_of_fame_objects(settings)

    while True:
        pygame.display.update()
        clock.tick(settings.framerate)

        SCREEN.fill((20, 20, 20))
        matrix.draw(SCREEN)

        if ui.mode == 0:  # Menu
            ui.mode = main_menu(SCREEN, game_data, matrix, ui, settings)
        elif ui.mode == 1:  # Game
            ui.update_timer(game_data.start_time)
            ui.mode = game_loop(SCREEN, game_data, matrix, ui)
        elif ui.mode == 2:  # Pause
            ui.mode = pause_menu(SCREEN, game_data)
        elif ui.mode == 3:  # Hall of Fame
            ui.mode = hall_of_fame_menu(SCREEN, ui, matrix)
        elif ui.mode == 4:  # Settings from Main menu
            ui.mode = settings_menu(SCREEN, ui.mode, 0)
        elif ui.mode == 5:  # Settings from Pause menu
            ui.mode = settings_menu(SCREEN, ui.mode, 2)
        elif ui.mode == 6:  # Control from Main menu
            ui.mode = control_menu(SCREEN, ui.mode, 0)
        elif ui.mode == 7:  # Control from Pause menu
            ui.mode = control_menu(SCREEN, ui.mode, 2)
        elif ui.mode == 8:  # Name for the record
            ui.mode = name_menu(SCREEN, game_data, ui)
