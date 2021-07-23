import pygame
import time
from exit import exit_program
from music import stop_music


def game_loop(SCREEN, game_data, matrix, ui):
    draw_game(SCREEN, matrix, ui)

    if game_data.timer_update():
        if not matrix.move_down():
            game_data.new_spawn = True

    if game_data.new_spawn:
        game_data.new_spawn = False
        matrix.tetrimino_to_matrix()
        erased_rows = matrix.erase_row()
        if erased_rows > 0:
            ui.update_row(erased_rows)
            game_data.update(erased_rows)
            game_data.update_hall_of_fame()
            new_scores = game_data.generate_score_list()
            if new_scores:
                ui.update_score_board(new_scores, game_data.rank)
        if not matrix.create_tetrimino():
            matrix.create_cells_dict()
            stop_music()
            game_data.stop_movement_timer()
            game_data.continous_move = False
            game_data.soft_drop = False
            game_data.name = ""
            return 8
        game_data.timer_start()

    if game_data.continous_move:
        matrix.continous_move(game_data.dir)

    # Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_program()

        elif event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_DOWN, pygame.K_s, pygame.K_KP2):  # soft drop
                game_data.soft_drop = True
                game_data.timer_start()

            elif event.key in (pygame.K_LEFT, pygame.K_a, pygame.K_KP4):
                game_data.start_movement_timer(-1)
            elif event.key in (pygame.K_RIGHT, pygame.K_d, pygame.K_KP6):
                game_data.start_movement_timer(1)

        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_ESCAPE, pygame.K_PAUSE, pygame.K_p, pygame.K_F1):
                game_data.pause_time = time.time()
                game_data.soft_drop = False
                game_data.stop_movement_timer()
                game_data.continous_move = False
                return 2  # to the pause menu

            elif event.key in (pygame.K_UP, pygame.K_w, pygame.K_KP8):
                matrix.turn_clockwise()
            elif event.key in (pygame.K_RCTRL, pygame.K_LCTRL, pygame.K_z):
                matrix.turn_counterclockwise()

            elif event.key in (pygame.K_DOWN, pygame.K_s, pygame.K_KP2):  # soft drop
                game_data.soft_drop = False
            elif event.key == pygame.K_SPACE:
                if matrix.hard_drop() > 0:
                    game_data.timer_reset()  # only if moved at least 1 block
                else:
                    game_data.timer_start()

            elif event.key in (pygame.K_LEFT, pygame.K_a, pygame.K_KP4):
                game_data.stop_movement_timer()
                game_data.continous_move = False
                matrix.move(-1)
            elif event.key in (pygame.K_RIGHT, pygame.K_d, pygame.K_KP6):
                game_data.stop_movement_timer()
                game_data.continous_move = False
                matrix.move(1)

    return 1


def draw_game(SCREEN, matrix, ui):
    matrix.draw_tetrimino(SCREEN)
    ui.draw(SCREEN)
