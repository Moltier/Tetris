import pygame
from music import start_music, stop_music, set_volume


class Settings:
    visible_col = 10
    visible_row = 20
    grid_col = 14
    grid_row = 23

    grid_proportion_range = range(50, 101)
    default_scores = {
        1: [1, 20000, "The Thing"],
        2: [2, 9001, "Vegetas nightmare"],
        3: [3, 667, "A puppy"],
        4: [4, 666, "Satan"],
        5: [5, 123, "Password"],
        6: [6, 69, "Noobmaster"],
        7: [7, 42, "The Answer"],
        8: [8, 0, "Mr. Missclick"]}

    def __init__(self, screen_size=(800, 600), full_screen=False, grid_proportion=90, framerate=60):
        self.screen_size_options = ((600, 400), (800, 600))
        self.screen_size = screen_size
        self.full_screen = full_screen  # if True, it should change the screen_size -> button placements
        self.grid_proportion = grid_proportion
        self.framerate = framerate

        self.music = True
        self.ghost = True
        self.volume = 5
        self.starting_level = 1

        # play area
        self.height = int(self.screen_size[1] * self.grid_proportion / 100)
        self.node_size = int(self.height / Settings.visible_row)
        self.width = self.node_size * Settings.grid_col
        self.play_area_rect = pygame.Rect(
            self.screen_size[0] / 2 - self.node_size / 2 * Settings.visible_col,
            self.screen_size[1] / 2 - self.height / 2,
            self.node_size * Settings.visible_col, self.height)

        # key should be read/saved from/to settings_data file

    @property
    def grid_proportion(self):
        return self._grid_proportion

    @grid_proportion.setter
    def grid_proportion(self, grid_proportion):
        if grid_proportion in Settings.grid_proportion_range:
            self._grid_proportion = grid_proportion
        else:
            raise ValueError('Proportion is out of range (50-100)!')

    def music_switch(self):
        if self.music:
            self.music = False
            stop_music()
            return "Off"
        start_music(settings.volume)
        self.music = True
        return "On"

    def ghost_switch(self):
        if self.ghost:
            self.ghost = False
            return "Off"
        self.ghost = True
        return "On"

    def volume_change(self, n):
        if 0 < self.volume + n < 11:
            self.volume += n
            set_volume(self.volume)
        return str(self.volume)

    def level_change(self, n):
        if 0 < self.starting_level + n < 16:
            self.starting_level += n
        return str(self.starting_level)


settings = Settings(grid_proportion=90)
