import pygame
from settings import settings
from Data.objects import back_button, music_text, music_button, volume_text, volume_left_button, volume_right_button, \
    volume_num, ghost_text, ghost_button, starting_level_text, \
    starting_level_left_button, starting_level_right_button, starting_level_num


def settings_menu(SCREEN, menu_code, return_code):
    mouse_pos = pygame.mouse.get_pos()
    draw_settings_menu(SCREEN)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return return_code

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                return return_code

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left
                if back_button.rect.collidepoint(mouse_pos):
                    back_button.down = True
            if event.button == 1:  # Left
                if music_button.rect.collidepoint(mouse_pos):
                    music_button.down = True
            if event.button == 1:  # Left
                if volume_left_button.rect.collidepoint(mouse_pos):
                    volume_left_button.down = True
            if event.button == 1:  # Left
                if volume_right_button.rect.collidepoint(mouse_pos):
                    volume_right_button.down = True
            if event.button == 1:  # Left
                if ghost_button.rect.collidepoint(mouse_pos):
                    ghost_button.down = True
            if event.button == 1:  # Left
                if starting_level_left_button.rect.collidepoint(mouse_pos):
                    starting_level_left_button.down = True
            if event.button == 1:  # Left
                if starting_level_right_button.rect.collidepoint(mouse_pos):
                    starting_level_right_button.down = True

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Left
                if back_button.rect.collidepoint(mouse_pos):
                    if back_button.down:
                        back_button.down = False
                        return return_code

                if music_button.rect.collidepoint(mouse_pos):
                    if music_button.down:
                        music_button.down = False
                        music_button.update_text(settings.music_switch())

                if ghost_button.rect.collidepoint(mouse_pos):
                    if ghost_button.down:
                        ghost_button.down = False
                        ghost_button.update_text(settings.ghost_switch())

                if volume_left_button.rect.collidepoint(mouse_pos):
                    if volume_left_button.down:
                        volume_left_button.down = False
                        volume_num.update_text(settings.volume_change(-1))
                if volume_right_button.rect.collidepoint(mouse_pos):
                    if volume_right_button.down:
                        volume_right_button.down = False
                        volume_num.update_text(settings.volume_change(1))

                if starting_level_left_button.rect.collidepoint(mouse_pos):
                    if starting_level_left_button.down:
                        starting_level_left_button.down = False
                        new_level = settings.level_change(-1)
                        starting_level_num.update_text(new_level)
                if starting_level_right_button.rect.collidepoint(mouse_pos):
                    if starting_level_right_button.down:
                        starting_level_right_button.down = False
                        new_level = settings.level_change(1)
                        starting_level_num.update_text(new_level)

                back_button.down = False
                music_button.down = False
                volume_left_button.down = False
                volume_right_button.down = False
                ghost_button.down = False
                starting_level_left_button.down = False
                starting_level_right_button.down = False
    return menu_code


def draw_settings_menu(SCREEN):
    music_text.draw(SCREEN)
    music_button.draw(SCREEN)
    volume_text.draw(SCREEN)
    volume_left_button.draw(SCREEN)
    volume_right_button.draw(SCREEN)
    volume_num.draw(SCREEN)
    ghost_text.draw(SCREEN)
    ghost_button.draw(SCREEN)
    starting_level_text.draw(SCREEN)
    starting_level_left_button.draw(SCREEN)
    starting_level_right_button.draw(SCREEN)
    starting_level_num.draw(SCREEN)

    back_button.draw(SCREEN)
