import pygame
from cell import Cell


class MiniMatrix:
    col = 4
    row = 4
    background_color = (0,0,0)

    def __init__(self, coord, node_size):
        self.node_size = node_size
        self.x = coord[0]
        self.y = coord[1]
        self.background_rect = pygame.Rect(self.x, self.y, MiniMatrix.col * self.node_size, MiniMatrix.row * self.node_size)
        self.cells_dict = {}
        self.create_cells_dict()

    def draw(self, SCREEN):
        pygame.draw.rect(SCREEN, MiniMatrix.background_color, self.background_rect)
        for cell in self.cells_dict.values():
            if cell.color:
                cell.draw(SCREEN)

    def create_cells_dict(self):
        for x in range(4):
            for y in range(4):
                self.cells_dict[(x, y)] = Cell(pygame.Rect(
                    self.x + x * self.node_size,
                    self.y + y * self.node_size, self.node_size, self.node_size), None)

    def update_tetrimino(self, tetrimino):
        for y in range(4):
            for x in range(4):
                if tetrimino.grid[0][y][x] == 1:
                    self.cells_dict[(x, y)].color = tetrimino.color
                else:
                    self.cells_dict[(x, y)].color = None
