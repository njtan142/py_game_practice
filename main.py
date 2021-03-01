from datetime import datetime as dt
import pygame
from game import Game
from menu import Menu
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
screen = pygame.display.set_mode((640, 320), pygame.FULLSCREEN|pygame.SCALED)

scene_manager = SceneManager()
game_scene = Scene(Game(pygame, screen))
menu_scene = Scene(Menu(pygame, screen))
scene_manager.scenes["game_scene"] = game_scene
scene_manager.scenes["menu_scene"] = menu_scene

scene_manager.active_scene = scene_manager.scenes["menu_scene"]

clock = pygame.time.Clock()

current_time_dt = dt.now()
current_time_ts = dt.timestamp(current_time_dt)
last_time_dt = dt.now()
last_time_ts = dt.timestamp(last_time_dt)
time_count = 0
time_delta = 0.016  # 1/60 of a second
time_scale = 1

running = True
timescale = 1
loop = 0
while running:

    rect = None

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if scene_manager.active_scene != scene_manager.scenes["game_scene"]:
                    scene_manager.active_scene = scene_manager.scenes["game_scene"]
                    continue

                if scene_manager.active_scene == scene_manager.scenes["game_scene"]:
                    scene_manager.active_scene.assets.change_level()
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                if scene_manager.active_scene == scene_manager.scenes["game_scene"]:
                    scene_manager.active_scene.assets.player.attacking = True
                    direction = scene_manager.active_scene.assets.player_state

                    if 'down' in direction:
                        rect = scene_manager.active_scene.assets.player.bottom_atk_rect

                    if 'up' in direction:
                        rect = scene_manager.active_scene.assets.player.top_atk_rect

                    if 'left' in direction:
                        rect = scene_manager.active_scene.assets.player.left_atk_rect

                    if 'right' in direction:
                        rect = scene_manager.active_scene.assets.player.right_atk_rect

                    for obj in scene_manager.active_scene.assets.object_list:
                        # print(obj)
                        if obj.entity:
                            if obj.rect is None:
                                continue
                            if obj == scene_manager.active_scene.assets.player:
                                continue
                            if rect.colliderect(obj.rect):
                                obj.status.take_damage(scene_manager.active_scene.assets.player.status.power)
                                if obj.status.health <= 0:
                                    scene_manager.active_scene.assets.kills += 1
                                    scene_manager.active_scene.assets.canvas.texts["kills counter"].change(
                                        str(scene_manager.active_scene.assets.kills) + "/" + str(scene_manager.active_scene.assets.levels.active_level.requirements))

    if scene_manager.active_scene is not None:
        scene_manager.active_scene.run(time_delta * time_scale)

    # pygame.draw.rect(screen, (255, 0, 0), rect or (0,0,0,0))
    pygame.display.flip()
    # pygame.image.save(screen, "record/" + str(loop) + ".jpeg")
    loop += 1
    last_time_dt = dt.now()
    last_time_ts = dt.timestamp(last_time_dt)
    time_delta = last_time_ts - current_time_ts
    time_count += time_delta
    current_time_dt = dt.now()
    current_time_ts = dt.timestamp(current_time_dt)

    # clock.tick(60)
