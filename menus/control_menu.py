import pygame
from Data.objects import back_button, left_text, right_text, clockwise_text, counterclockwise_text, \
    soft_drop_text, pause_text, hard_drop_text, left_data_text, right_data_text, clockwise_data_text, \
    counterclockwise_data_text, soft_drop_data_text, hard_drop_data_text, pause_data_text


def control_menu(SCREEN, menu_code, return_code):
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

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Left
                if back_button.rect.collidepoint(mouse_pos):
                    if back_button.down:
                        back_button.down = False
                        return return_code
                back_button.down = False
    return menu_code


def draw_settings_menu(SCREEN):
    left_text.draw(SCREEN)
    right_text.draw(SCREEN)
    clockwise_text.draw(SCREEN)
    counterclockwise_text.draw(SCREEN)
    soft_drop_text.draw(SCREEN)
    hard_drop_text.draw(SCREEN)
    pause_text.draw(SCREEN)

    left_data_text.draw(SCREEN)
    right_data_text.draw(SCREEN)
    clockwise_data_text.draw(SCREEN)
    counterclockwise_data_text.draw(SCREEN)
    soft_drop_data_text.draw(SCREEN)
    hard_drop_data_text.draw(SCREEN)
    pause_data_text.draw(SCREEN)

    back_button.draw(SCREEN)