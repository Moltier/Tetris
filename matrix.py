import pygame
import random
import time
from settings import settings
from cell import Cell
from mini_matrix import MiniMatrix
from Data.tetrimino import cyan_i, blue_j, orange_l, yellow_o, green_s, red_z, purple_t


class Matrix:
    tetriminos = (cyan_i, blue_j, orange_l, yellow_o, green_s, red_z, purple_t)
    grid_col = 14
    grid_row = 23
    hidden_row_top = 1
    hidden_row_bottom = 2
    grid_color = (50, 50, 50)
    background_color = (0, 0, 0)
    border_color = (1, 1, 1)
    spawn_coord = [5, 0]

    def __init__(self, width, height, node_size, play_area_rect):
        self.width = width
        self.height = height
        self.node_size = node_size
        self.play_area_rect = play_area_rect

        self.tetrimino = None
        self.tetrimino_coord = None
        self.ghost = None
        self.ghost_coord = None
        self.next_tetrimino = random.choice(Matrix.tetriminos).__copy__()
        self.movement_speed = 0.1
        self.movement_timer = None

        self.matrix_rect = pygame.Rect(
            settings.screen_size[0] / 2 - self.width / 2,
            settings.screen_size[1] / 2 - self.height / 2 - self.node_size,
            self.width, self.height)

        self.minimatrix_pos = (
            int(settings.screen_size[0] / 2 + self.width / 2 + (settings.screen_size[0] - self.width) / 4 - 2 * self.node_size),
            int(settings.screen_size[1] / 2 - self.node_size * 2))
        self.minimatrix = MiniMatrix(self.minimatrix_pos, self.node_size)

        self.cells_dict = {}

    def tetrimino_to_matrix(self):
        if self.tetrimino:
            for y in range(4):
                for x in range(4):
                    if self.tetrimino.grid[self.tetrimino.grid_id][y][x] == 1:
                        self.cells_dict[(x + self.tetrimino_coord[0], y + self.tetrimino_coord[1])].color = self.tetrimino.color

    def create_cells_dict(self):
        self.tetrimino = None
        self.next_tetrimino = random.choice(Matrix.tetriminos).__copy__()
        for x in range(1, Matrix.grid_col - 1):
            for y in range(Matrix.grid_row):
                if x in (1, Matrix.grid_col - 2) or y >= Matrix.grid_row - Matrix.hidden_row_bottom:
                    self.cells_dict[(x, y)] = Cell(pygame.Rect(
                        self.matrix_rect.x + x * self.node_size,
                        self.matrix_rect.y + y * self.node_size, self.node_size, self.node_size), Matrix.border_color)
                else:
                    self.cells_dict[(x, y)] = Cell(pygame.Rect(
                        self.matrix_rect.x + x * self.node_size,
                        self.matrix_rect.y + y * self.node_size, self.node_size, self.node_size), None)

    def create_tetrimino(self):
        """ returns False if if fails because of a collision """
        self.tetrimino = self.next_tetrimino
        self.tetrimino_coord = Matrix.spawn_coord.copy()
        self.next_tetrimino = random.choice(Matrix.tetriminos).__copy__()
        self.minimatrix.update_tetrimino(self.next_tetrimino)

        if settings.ghost:
            self.ghost = self.tetrimino.__copy__()
            self.ghost_coord = self.tetrimino_coord.copy()
            self.ghost.color = [int(x * 0.25) for x in self.tetrimino.color]
            self.modify_ghost()
        return not self.collision_scan(self.tetrimino_coord)

    def modify_ghost(self):
        self.ghost_coord = self.tetrimino_coord.copy()
        self.ghost.grid_id = self.tetrimino.grid_id
        while not self.collision_scan((self.ghost_coord[0], self.ghost_coord[1] + 1)):
            self.ghost_coord[1] += 1

    def collision_scan(self, coord):
        for y in range(4):
            for x in range(4):
                if self.tetrimino.grid[self.tetrimino.grid_id][y][x] == 1 \
                        and self.cells_dict[(x + coord[0], y + coord[1])].color:
                    return True
        return False

    def move(self, movement):
        self.movement_timer = None
        if not self.collision_scan((self.tetrimino_coord[0] + movement, self.tetrimino_coord[1])):
            self.tetrimino_coord[0] += movement
            self.modify_ghost()

    def continous_move(self, movement):
        if self.movement_timer is None:
            self.movement_timer = time.time()
        elif self.movement_speed + self.movement_timer <= time.time():
            self.movement_timer += self.movement_speed
            if not self.collision_scan((self.tetrimino_coord[0] + movement, self.tetrimino_coord[1])):
                self.tetrimino_coord[0] += movement
                self.modify_ghost()

    def move_down(self):
        if not self.collision_scan((self.tetrimino_coord[0], self.tetrimino_coord[1] + 1)):
            self.tetrimino_coord[1] += 1
            return True
        return False

    def turn_clockwise(self):
        original_id = self.tetrimino.grid_id
        self.tetrimino.grid_id += 1
        if self.tetrimino.grid_id == len(self.tetrimino.grid):
            self.tetrimino.grid_id = 0
        if self.collision_scan(self.tetrimino_coord):
            self.tetrimino.grid_id = original_id
        else:
            self.modify_ghost()

    def turn_counterclockwise(self):
        original_id = self.tetrimino.grid_id
        self.tetrimino.grid_id -= 1
        if self.tetrimino.grid_id < 0:
            self.tetrimino.grid_id = len(self.tetrimino.grid) - 1
        if self.collision_scan(self.tetrimino_coord):
            self.tetrimino.grid_id = original_id
        else:
            self.modify_ghost()

    def hard_drop(self):
        counter = 0
        while not self.collision_scan((self.tetrimino_coord[0], self.tetrimino_coord[1] + 1)):
            counter += 1
            self.tetrimino_coord[1] += 1
        return counter

    def erase_row(self):
        row_to_erase = 0
        for y in range(20, 0, -1):
            full_row = True
            for x in range(2, 12):
                if row_to_erase > 0:
                    self.cells_dict[(x, y + row_to_erase)].color = self.cells_dict[(x, y)].color
                if full_row and not self.cells_dict[(x, y)].color:
                    full_row = False
            else:
                if full_row:
                    row_to_erase += 1

        if row_to_erase > 0:  # bandage to the bug: blocks on top remain after row erase
            for x in range(2, 12):
                self.cells_dict[(x, 1)].color = None
        return row_to_erase

    def draw_tetrimino(self, SCREEN):
        if settings.ghost:
            for y in range(4):
                for x in range(4):
                    if self.ghost.grid[self.ghost.grid_id][y][x] == 1:
                        rect = self.cells_dict[(x + self.ghost_coord[0], y + self.ghost_coord[1])].rect
                        pygame.draw.rect(SCREEN, self.ghost.color, rect)

        for y in range(4):
            for x in range(4):
                if self.tetrimino.grid[self.tetrimino.grid_id][y][x] == 1:
                    rect = self.cells_dict[(x + self.tetrimino_coord[0], y + self.tetrimino_coord[1])].rect
                    pygame.draw.rect(SCREEN, self.tetrimino.color, rect)

    def draw(self, SCREEN):
        pygame.draw.rect(SCREEN, Matrix.background_color, self.play_area_rect)
        for x in range(Matrix.grid_col - 4 + 1):  # fix val to be switched
            pygame.draw.line(
                SCREEN, Matrix.grid_color,
                (self.play_area_rect.x + self.node_size * x, self.play_area_rect.y),
                (self.play_area_rect.x + self.node_size * x, self.play_area_rect.y + self.play_area_rect.height), 1)
        for y in range(Matrix.grid_row - Matrix.hidden_row_bottom):
            pygame.draw.line(
                SCREEN, Matrix.grid_color,
                (self.play_area_rect.x, self.play_area_rect.y + y * self.node_size),
                (self.play_area_rect.x + self.play_area_rect.width, self.play_area_rect.y + y * self.node_size), 1)

        for (x, y), cell in self.cells_dict.items():
            if 1 < x < 12 and Matrix.grid_row - Matrix.hidden_row_bottom > y >= Matrix.hidden_row_top:
                cell.draw(SCREEN)

        self.minimatrix.draw(SCREEN)
