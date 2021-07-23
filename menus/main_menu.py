import pygame
import time
from exit import exit_program
from Data.objects import new_game_button, settings_button, controls_button, score_button, exit_main_menu_button
from music import start_music


def main_menu(SCREEN, game_data, matrix, ui, settings):
    draw_main_menu(SCREEN)
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_program()

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                exit_program()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left
                if new_game_button.rect.collidepoint(mouse_pos):
                    new_game_button.down = True
                elif settings_button.rect.collidepoint(mouse_pos):
                    settings_button.down = True
                elif controls_button.rect.collidepoint(mouse_pos):
                    controls_button.down = True
                elif score_button.rect.collidepoint(mouse_pos):
                    score_button.down = True
                elif exit_main_menu_button.rect.collidepoint(mouse_pos):
                    exit_main_menu_button.down = True

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Left
                if new_game_button.rect.collidepoint(mouse_pos):
                    if new_game_button.down:
                        new_game_button.down = False
                        game_data.new_game(settings.starting_level)
                        scores = game_data.generate_score_list()
                        ui.update_score_board(scores, game_data.rank)
                        matrix.create_cells_dict()
                        matrix.create_tetrimino()
                        game_data.start_time = time.time()
                        game_data.timer_start()
                        if settings.music:
                            start_music(settings.volume)
                        return 1
                elif settings_button.rect.collidepoint(mouse_pos):
                    if settings_button.down:
                        settings_button.down = False
                        return 4
                elif controls_button.rect.collidepoint(mouse_pos):
                    if controls_button.down:
                        controls_button.down = False
                        return 6
                elif score_button.rect.collidepoint(mouse_pos):
                    if score_button.down:
                        score_button.down = False
                        return 3
                elif exit_main_menu_button.rect.collidepoint(mouse_pos):
                    if exit_main_menu_button.down:
                        exit_program()

                new_game_button.down = False
                settings_button.down = False
                controls_button.down = False
                score_button.down = False
                exit_main_menu_button.down = False
    return 0


def draw_main_menu(SCREEN):
    new_game_button.draw(SCREEN)
    settings_button.draw(SCREEN)
    controls_button.draw(SCREEN)
    score_button.draw(SCREEN)
    exit_main_menu_button.draw(SCREEN)
