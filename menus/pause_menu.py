import pygame
import time
from exit import exit_program
from Data.objects import resume_button, settings_button, controls_button, exit_game_button


def pause_menu(SCREEN, game_data):
    draw_pause_menu(SCREEN)
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_program()

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                time_paused = time.time() - game_data.pause_time
                game_data.prev_time += time_paused
                game_data.start_time += time_paused
                return 1  # back to the game

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left
                if resume_button.rect.collidepoint(mouse_pos):
                    resume_button.down = True
                elif settings_button.rect.collidepoint(mouse_pos):
                    settings_button.down = True
                elif controls_button.rect.collidepoint(mouse_pos):
                    controls_button.down = True
                elif exit_game_button.rect.collidepoint(mouse_pos):
                    exit_game_button.down = True

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Left
                if resume_button.rect.collidepoint(mouse_pos):
                    if resume_button.down:
                        resume_button.down = False
                        time_paused = time.time() - game_data.pause_time
                        game_data.prev_time += time_paused
                        game_data.start_time += time_paused
                        return 1  # back to the game
                elif settings_button.rect.collidepoint(mouse_pos):
                    if settings_button.down:
                        settings_button.down = False
                        return 5
                elif controls_button.rect.collidepoint(mouse_pos):
                    if controls_button.down:
                        controls_button.down = False
                        return 7
                elif exit_game_button.rect.collidepoint(mouse_pos):
                    if exit_game_button.down:
                        exit_program()

                resume_button.down = False
                settings_button.down = False
                controls_button.down = False
                exit_game_button.down = False
    return 2


def draw_pause_menu(SCREEN):
    resume_button.draw(SCREEN)
    settings_button.draw(SCREEN)
    controls_button.draw(SCREEN)
    exit_game_button.draw(SCREEN)
