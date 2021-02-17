from datetime import datetime as dt

import pygame

from camera import Camera as Cam
from object import Object as Obj
from animationc import animationC



# stand alone functions
def get_distance(object1, object2, x1, y1):
    x_1 = object1.x + x1 - object2.x
    y_1 = object1.y + y1 - object2.y
    x_1 = x_1 ** 2
    y_1 = y_1 ** 2
    result = x_1 + y_1
    result = result ** 0.5
    return result


pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
# player
player_img = pygame.image.load("assets/idle down1.png")
player_idle_animation = [
    pygame.image.load("assets/walk down2.png"),
    pygame.image.load("assets/walk down2.png"),
    pygame.image.load("assets/walk down3.png"),
    pygame.image.load("assets/walk down4.png")
]
player = Obj(0, screen.get_height() / 2, player_img, False, True)
player_anim_controller = animationC()
player_anim_controller.add_animation("walk down", player_idle_animation, 1)
player.anim_c = player_anim_controller

# block image
block_img_list = [pygame.image.load("assets/grass.png"),
                  pygame.image.load("assets/block.png"),
                  pygame.image.load("assets/block2.png")]

block_collisions = [False, True, True]
block_list = [
    "1111111111111111",
    "1000000000000011",
    "1011100000000011",
    "1000000111000011",
    "1000110000000001s",
    "1111111111111111",
]


def tile_map(tile_map_array, image, width, height, collision_list):
    tile_map_list = []
    y = 0
    for column in tile_map_array:
        x = 0
        last_loop_count = 0
        last_number = 0
        for row in column:
            if row == "s":
                player.x = x
                player.y = y
                row = "0"
            tile = Obj(x, y, image[int(row)], False)
            tile.collision = collision_list[int(row)]
            if last_number == int(row):
                tile.loop += last_loop_count
                tile_map_list.pop()
            tile_map_list.append(tile)
            last_loop_count = tile.loop
            last_number = int(row)
            x += width
        y += height
    return tile_map_list


block_object_list = tile_map(block_list, block_img_list, 32, 32, block_collisions)

# frames counter (FPS)
fps = 0
# time
current_time_dt = dt.now()
current_time_ts = dt.timestamp(current_time_dt)

last_time_dt = dt.now()
last_time_ts = dt.timestamp(last_time_dt)
time_count = 0
time_delta = 1
running = True

rect = pygame.Rect(255, 255, 10, 10)
# object list
object_list = [player]
for block in block_object_list:
    object_list.append(block)

# camera
camera_obj = Obj(screen.get_width() / 2, screen.get_height() / 2, None)
camera = Cam(camera_obj, object_list, player)

while running:
    # clock.tick(600)
    # input handler
    key_state = pygame.key.get_pressed()
    horizontal = key_state[pygame.K_d] - key_state[pygame.K_a]
    vertical = key_state[pygame.K_s] - key_state[pygame.K_w]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # background
    screen.fill((123, 123, 123))
    # player update

    (player.move(horizontal * 100 * time_delta, vertical * 100 * time_delta, object_list))
    # camera update
    (camera.update(object_list, screen))

    # first layer update
    for obj in block_object_list:
        obj.update(screen)

    # second layer update
    player.update(screen)
    if vertical == 1:
        player.anim_c.play_animation("walk down", screen, time_delta, player.x, player.y)

    # fps and time management
    last_time_dt = dt.now()
    last_time_ts = dt.timestamp(last_time_dt)
    time_delta = last_time_ts - current_time_ts
    time_count += time_delta
    current_time_dt = dt.now()
    current_time_ts = dt.timestamp(current_time_dt)

    # screen update
    pygame.display.update()

    fps += 1
    if time_count >= 1:
        print(fps)
        fps = 0
        time_count -= 1
