from textobjects import TextObject
from settings import settings


# Buttons
button_width = 100
button_height = 40
button_size = (button_width, button_height)
x = settings.screen_size[0] / 2
y_dist = button_height + 10


# Main Menu buttons
num_of_buttons = 5
y = settings.screen_size[1] / 2 - button_height / (2 if num_of_buttons % 2 == 1 else 1)

new_game_button = TextObject(position=(x, y + y_dist * -2), size=button_size,
                             color=None, text="New Game", positioning='midtop')

settings_button = TextObject(
    position=(x, y + y_dist * -1), size=button_size, color=None, text="Settings", positioning='midtop')

controls_button = TextObject(
    position=(x, y + y_dist * 0), size=button_size, color=None, text="Controls", positioning='midtop')

score_button = TextObject(
    position=(x, y + y_dist * 1), size=button_size, color=None, text="Hall of Fame", positioning='midtop')

exit_main_menu_button = TextObject(
    position=(x, y + y_dist * 2), size=button_size, color=None, text="Exit", positioning='midtop')


# Pause / Exit Menu buttons
num_of_buttons = 3

resume_button = TextObject(
    position=(x, y + y_dist * -2), size=button_size, color=None, text="Resume", positioning='midtop')

exit_game_button = TextObject(
    position=(x, y + y_dist * 1), size=button_size, color=None, text="Exit", positioning='midtop')


# Display objects
level_text_display = TextObject(
    position=(0, 0), color=None, text="Level")
level_display = TextObject(
    position=(0, 0), color=None, text="1")
timer_text_display = TextObject(
    position=(0, 0), color=None, text="Time")
timer_display = TextObject(
    position=(0, 0), color=None, text="0")
row_text_display = TextObject(
    position=(0, 0), color=None, text="Rows")
row_display = TextObject(
    position=(0, 0), color=None, text="0")


# Score board
score_board = []
score_height = settings.screen_size[1] / 12
for n in range(1, 11):
    score_line = TextObject(
        position=(settings.play_area_rect.x / 2, n * score_height), color=None, text="", font_size=20)
    score_board.append(score_line)


# Hall of Fame
back_button = TextObject(
    position=(settings.screen_size[0] - 100, settings.screen_size[1] - button_height * 2),
    color=None, text="Back...", size=button_size, positioning='midtop')


# Settings menu
size = (40, 30)
x = settings.play_area_rect.x + 30

music_text = TextObject(
    position=(x, y + y_dist * -2), color=None, text="Music:")
volume_text = TextObject(
    position=(x, y + y_dist * -1), color=None, text="Volume:")
ghost_text = TextObject(
    position=(x, y + y_dist * 0), color=None, text="Ghost:")
starting_level_text = TextObject(
    position=(x, y + y_dist * 1), color=None, text="Starting level:")

x = settings.play_area_rect.right - 60
music_button = TextObject(
    position=(x, y + y_dist * -2), color=None, text="On", size=size, positioning='midtop')
volume_num = TextObject(
    position=(x, y + y_dist * -1), color=None, text="5", positioning='midtop')
ghost_button = TextObject(
    position=(x, y + y_dist * 0), color=None, text="On", size=size, positioning='midtop')
starting_level_num = TextObject(
    position=(x, y + y_dist * 1), color=None, text="1", positioning='midtop')

volume_left_button = TextObject(
    position=(x-25, y + y_dist * -1), color=None, text="<", size=size, positioning='midtop')
volume_right_button = TextObject(
    position=(x+25, y + y_dist * -1), color=None, text=">", size=size, positioning='midtop')
starting_level_left_button = TextObject(
    position=(x-25, y + y_dist * 1), color=None, text="<", size=size, positioning='midtop')
starting_level_right_button = TextObject(
    position=(x+25, y + y_dist * 1), color=None, text=">", size=size, positioning='midtop')


# Control menu
x = 30

left_text = TextObject(
    position=(x, y + y_dist * -3), color=None, text="Left:")
right_text = TextObject(
    position=(x, y + y_dist * -2), color=None, text="Right:")
clockwise_text = TextObject(
    position=(x, y + y_dist * -1), color=None, text="Turn clockwise:")
counterclockwise_text = TextObject(
    position=(x, y + y_dist * 0), color=None, text="Turn counterclockwise:")
soft_drop_text = TextObject(
    position=(x, y + y_dist * 1), color=None, text="Soft drop:")
hard_drop_text = TextObject(
    position=(x, y + y_dist * 2), color=None, text="Hard drop:")
pause_text = TextObject(
    position=(x, y + y_dist * 3), color=None, text="Pause:")

x = settings.play_area_rect.x + 30
left_data_text = TextObject(
    position=(x, y + y_dist * -3), color=None, text="LEFT ARROW,  NUM4,  A")
right_data_text = TextObject(
    position=(x, y + y_dist * -2), color=None, text="RIGHT ARROW,  NUM6,  D")
clockwise_data_text = TextObject(
    position=(x, y + y_dist * -1), color=None, text="UP ARROW,  NUM8,  W")
counterclockwise_data_text = TextObject(
    position=(x, y + y_dist * 0), color=None, text="CTRL,  Z")
soft_drop_data_text = TextObject(
    position=(x, y + y_dist * 1), color=None, text="DOWN ARROW,  NUM2,  S")
hard_drop_data_text = TextObject(
    position=(x, y + y_dist * 2), color=None, text="SPACE")
pause_data_text = TextObject(
    position=(x, y + y_dist * 3), color=None, text="PAUSE,  P,  ESC,  F1")


# Naming menu
x = settings.screen_size[0] / 2
y = settings.play_area_rect.y + settings.play_area_rect.h / 2
naming_menu_background = TextObject(
    position=(x, y - 40), color=(20,20,20), size=(settings.play_area_rect.w - 40, 100),
    positioning='midtop')
naming_menu_text = TextObject(
    position=(x, y - 20), text="Please enter your name:", positioning='midtop')
naming_menu = TextObject(
    position=(x, y + 20), color=(0,0,0), text="", size=(settings.play_area_rect.w - 60, 30), positioning='midtop')
