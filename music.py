from pygame import mixer


mixer.init()
mixer.music.load("music/Tetris.mp3")


def start_music(volume):
    set_volume(volume)
    mixer.music.play(-1)


def stop_music():
    mixer.music.stop()


def set_volume(volume):
    mixer.music.set_volume(0.005 * volume)
