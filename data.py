import time
from textobjects import TextObject
from Data.objects import \
    timer_text_display, timer_display, level_text_display, level_display, row_text_display, row_display, score_board


class Game:
    basic_score_table = (40, 100, 300, 1200)  # per level
    hall_of_fame = {}
    speed_curve = {
        1: 1.0,
        2: 0.793,
        3: 0.617796,
        4: 0.472729139,
        5: 0.355196928256,
        6: 0.262003549978125,
        7: 0.18967724533271815,
        8: 0.1347347308155587,
        9: 0.09388224890421265,
        10: 0.06415158495985583,
        11: 0.042976258297035566,
        12: 0.02821767780121165,
        13: 0.018153328543517738,
        14: 0.01143934234680738,
        15: 0.007058616220934218}

    def __init__(self):
        self.name = "Player"
        self.level = None
        self.timer = 0
        self.start_time = None
        self.curr_time = None
        self.prev_time = None
        self.pause_time = None
        self.new_spawn = False

        self.cleared_rows = 0
        self.rows_to_next_level = None
        self.score = 0
        self.rank = None
        self.soft_drop = False
        self.soft_drop_speed = Game.speed_curve[10]

        self.dir = None
        self.continous_move = False
        self.movement_start_timer_base = 0.1
        self.movement_start_timer = self.movement_start_timer_base

    def new_game(self, starting_level):
        level_display.update_text(str(starting_level))
        self.level = starting_level
        self.timer = 0
        self.start_time = None
        self.curr_time = None
        self.prev_time = None
        self.new_spawn = False

        self.cleared_rows = 0
        self.rows_to_next_level = self.level * 10
        self.score = 0
        self.set_rank()

    def timer_start(self):
        self.timer = 0
        speed = min(Game.speed_curve[self.level], self.soft_drop_speed) if self.soft_drop else Game.speed_curve[self.level]
        self.prev_time = time.time() - speed
        self.timer_update()

    def timer_reset(self):
        self.timer = Game.speed_curve[self.level]
        self.prev_time = time.time()

    def timer_update(self):
        """ Returns True if its time to move the piece down """
        self.curr_time = time.time()
        self.timer -= (self.curr_time - self.prev_time)
        if self.dir and self.movement_start_timer > 0:
            self.movement_start_timer -= (self.curr_time - self.prev_time)
            if self.movement_start_timer <= 0:
                self.continous_move = True
        self.prev_time = self.curr_time
        if self.timer <= 0:
            speed = min(Game.speed_curve[self.level], self.soft_drop_speed) if self.soft_drop else Game.speed_curve[self.level]
            self.timer += speed
            return True

    def start_movement_timer(self, direction):
        self.dir = direction
        self.movement_start_timer = self.movement_start_timer_base

    def stop_movement_timer(self):
        self.dir = None

    def generate_score_list(self):
        new_scores = []
        first_pos = max(1, self.rank - 10)
        for i in range(first_pos, first_pos + 10):
            if i <= len(Game.hall_of_fame):
                new_scores.append(Game.hall_of_fame[i])
            else:
                new_scores.append(["","",""])
        return new_scores

    def update(self, rows):
        self.cleared_rows += rows
        row_display.update_text(str(self.cleared_rows))

        self.rows_to_next_level -= rows
        self.score += Game.basic_score_table[rows - 1] * self.level
        if self.rows_to_next_level <= 0 and self.level < 15:
            self.level += 1
            self.rows_to_next_level = self.level * 10
            level_display.update_text(str(self.level))

    def set_rank(self):
        self.rank = len(Game.hall_of_fame) + 1
        Game.hall_of_fame[self.rank] = [str(self.rank), self.score, self.name]

    def update_hall_of_fame(self):
        Game.hall_of_fame[self.rank][1] = self.score
        while self.rank > 1 and self.score > int(Game.hall_of_fame[self.rank - 1][1]):
            Game.hall_of_fame[self.rank][1], Game.hall_of_fame[self.rank - 1][1] = Game.hall_of_fame[self.rank - 1][1], Game.hall_of_fame[self.rank][1]
            Game.hall_of_fame[self.rank][2], Game.hall_of_fame[self.rank - 1][2] = Game.hall_of_fame[self.rank - 1][2], Game.hall_of_fame[self.rank][2]
            self.rank -= 1

    def update_player_name(self):
        self.hall_of_fame[self.rank][2] = self.name


class UserInterface:
    text_color = (255, 255, 255)

    def __init__(self):
        self.mode = 0  # 0=Menu, 1=Game, 2=Pause
        self.hall_of_fame_objects = {}
        self.hall_of_fame_scroll = 0

        self.timer_text_display = timer_text_display
        self.timer_display = timer_display
        self.level_text_display = level_text_display
        self.level_display = level_display
        self.row_text_display = row_text_display
        self.row_display = row_display
        self.score_board = score_board

    def set_ui_pos(self, screen_size, matrix_width):
        x = screen_size[0] / 2 + matrix_width / 2 + (screen_size[0] - matrix_width) / 4
        y = screen_size[1] / 16
        self.timer_text_display.rect.topleft = (
            int(x - self.timer_text_display.rect.width / 2),
            int(y))
        self.timer_display.rect.topleft = (
            int(x - self.timer_display.rect.width / 2),
            int(y + self.timer_text_display.rect.height))

        self.row_text_display.rect.topleft = (
            int(x - self.row_text_display.rect.width / 2),
            int(y * 3))
        self.row_display.rect.topleft = (
            int(x - self.row_display.rect.width / 2),
            int(y * 3 + self.row_text_display.rect.height))

        self.level_text_display.rect.topleft = (
            int(x - self.level_text_display.rect.width / 2),
            int(y * 5))
        self.level_display.rect.topleft = (
            int(x - self.level_display.rect.width / 2),
            int(y * 5 + self.level_text_display.rect.height))

    def update_row(self, new_row):
        self.row_display.update_text(str(new_row))

    def update_level(self, new_level):
        self.level_display.update_text(str(new_level))

    def update_timer(self, start_time):
        new_timer = str(int(time.time() - start_time))
        self.timer_display.update_text(new_timer)

    def update_score_board(self, scores, player_rank):
        for i in range(len(scores)):
            rank, score, name = scores[i]
            if rank == str(player_rank):
                self.score_board[i].text_color = (255, 255, 0)
            else:
                self.score_board[i].text_color = (200, 200, 200)
            self.score_board[i].update_text(f'{rank} - {score} - {name}')

    def create_hall_of_fame_objects(self, settings):  # i know its static :P
        self.hall_of_fame_objects = {}
        height = settings.screen_size[1] / 13
        for line in Game.hall_of_fame.values():
            rank, score, name = line
            self.hall_of_fame_objects[rank] = [
                TextObject(
                    position=(settings.play_area_rect.x + 30, height * int(rank)),
                    color=None, text=f'{rank}.', text_color=(255, 255, 0), font_size=22, positioning='topright'),
                TextObject(
                    position=(settings.play_area_rect.x + 110, height * int(rank)),
                    color=None, text=str(score), text_color=(255, 255, 0), font_size=22, positioning='topright'),
                TextObject(
                    position=(settings.play_area_rect.x + 260, height * int(rank)),
                    color=None, text=name, text_color=(255, 255, 0), font_size=22, positioning='topright')
            ]

    def draw(self, SCREEN):
        for score_line in self.score_board:
            score_line.draw(SCREEN)
        self.timer_text_display.draw(SCREEN)
        self.timer_display.draw(SCREEN)
        self.row_text_display.draw(SCREEN)
        self.row_display.draw(SCREEN)
        self.level_text_display.draw(SCREEN)
        self.level_display.draw(SCREEN)
