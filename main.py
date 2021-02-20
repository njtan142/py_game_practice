from datetime import datetime as dt
import pygame
from GameDevelopment.py_game_practice.game import Game
from GameDevelopment.py_game_practice.Scripts.scene import Scene
from GameDevelopment.py_game_practice.Scripts.scenemanager import SceneManager
import sys
import os


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


# stand alone functions
def get_distance(object1, object2, x1, y1):
    x_1 = object1.x + x1 - object2.x
    y_1 = object1.y + y1 - object2.y
    x_1 = x_1 ** 2
    y_1 = y_1 ** 2
    result = x_1 + y_1
    result = result ** 0.5
    return result


# pygame initialization
pygame.init()
screen = pygame.display.set_mode((1440, 800))
scene_manager = SceneManager()
game_scene = Scene(Game(pygame, screen))
scene_manager.scenes["game_scene"] = game_scene
running = True
is_running = False
current_time_dt = dt.now()
current_time_ts = dt.timestamp(current_time_dt)
last_time_dt = dt.now()
last_time_ts = dt.timestamp(last_time_dt)
time_count = 0
time_delta = 0.016
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    key_input = pygame.key.get_pressed()
    if key_input[pygame.K_RETURN] == 1:
        scene_manager.active_scene = scene_manager.scenes["game_scene"]
    if key_input[pygame.K_ESCAPE] == 1:
        scene_manager.active_scene = None
    if scene_manager.active_scene is not None:
        scene_manager.active_scene.run(time_delta)
    last_time_dt = dt.now()
    last_time_ts = dt.timestamp(last_time_dt)
    time_delta = last_time_ts - current_time_ts
    time_count += time_delta
    current_time_dt = dt.now()
    current_time_ts = dt.timestamp(current_time_dt)
