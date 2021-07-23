import pygame
from settings import settings
from Data.objects import back_button


def hall_of_fame_menu(SCREEN, ui, matrix):
    mouse_pos = pygame.mouse.get_pos()
    draw_hall_of_fame(SCREEN, ui, matrix)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return 0

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                return 0

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left
                if back_button.rect.collidepoint(mouse_pos):
                    back_button.down = True

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Left
                if back_button.rect.collidepoint(mouse_pos):
                    if back_button.down:
                        back_button.down = False
                        return 0
                back_button.down = False

        elif event.type == pygame.MOUSEWHEEL:
            ui.hall_of_fame_scroll = min(ui.hall_of_fame_scroll + event.y * 20, 0)


    return 3


def draw_hall_of_fame(SCREEN, ui, matrix):
    for score_line in ui.hall_of_fame_objects.values():
        for data in score_line:
            data.draw(SCREEN, y_scroll=ui.hall_of_fame_scroll)

    pygame.draw.rect(SCREEN, (20, 20, 20), (0, 0, settings.screen_size[0], matrix.play_area_rect.y))
    pygame.draw.rect(SCREEN, (20, 20, 20), (0, matrix.play_area_rect.y + matrix.play_area_rect.h + 1,
                                            settings.screen_size[0], settings.screen_size[1]))
    back_button.draw(SCREEN)