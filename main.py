from datetime import datetime as dt
import pygame
from game import Game
from Scripts.scene import Scene
from Scripts.scenemanager import SceneManager
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
screen = pygame.display.set_mode((640, 480))
scene_manager = SceneManager()
game_scene = Scene(Game(pygame, screen))
scene_manager.scenes["game_scene"] = game_scene




current_time_dt = dt.now()
current_time_ts = dt.timestamp(current_time_dt)
last_time_dt = dt.now()
last_time_ts = dt.timestamp(last_time_dt)
time_count = 0
time_delta = 0.016 #1/60 of a second
time_scale = 1

running = True
timescale = 1
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                scene_manager.active_scene = scene_manager.scenes["game_scene"]
            if event.key == pygame.K_ESCAPE:
                scene_manager.active_scene = None
            if event.key == pygame.K_SPACE:
                if scene_manager.active_scene == scene_manager.scenes["game_scene"]:
                    scene_manager.active_scene.assets.player.attacking = True


    if scene_manager.active_scene is not None:
        scene_manager.active_scene.run(time_delta * time_scale)
        
        
    last_time_dt = dt.now()
    last_time_ts = dt.timestamp(last_time_dt)
    time_delta = last_time_ts - current_time_ts
    time_count += time_delta
    current_time_dt = dt.now()
    current_time_ts = dt.timestamp(current_time_dt)
