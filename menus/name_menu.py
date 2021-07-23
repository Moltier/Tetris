import pygame
from settings import settings
from Data.objects import naming_menu_text, naming_menu, naming_menu_background


def name_menu(SCREEN, game_data, ui):
    draw_name_menu(SCREEN)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ui.create_hall_of_fame_objects(settings)
            return 0

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                ui.create_hall_of_fame_objects(settings)
                return 0

        elif event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_KP_ENTER, pygame.K_RETURN):
                if game_data.name == "":
                    game_data.name = "Player"
                game_data.update_player_name()
                ui.create_hall_of_fame_objects(settings)
                return 0
            elif event.key == pygame.K_BACKSPACE:
                game_data.name = game_data.name[:-1]
                naming_menu.update_text(game_data.name)
            else:
                if len(game_data.name) < 20:
                    game_data.name += event.unicode
                    naming_menu.update_text(game_data.name)
    return 8


def draw_name_menu(SCREEN):
    naming_menu_background.draw(SCREEN)
    naming_menu_text.draw(SCREEN)
    naming_menu.draw(SCREEN)
