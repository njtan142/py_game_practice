from datetime import datetime as dt
import pygame
from camera import Camera as Cam
from object import Object as Obj
from animationc import animationC
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
screen = pygame.display.set_mode((1440, 840))
clock = pygame.time.Clock()
# Assets
assets = {
    'iu1': resource_path("assets/idle up1.png"),
    'iu2': resource_path("assets/idle up2.png"),
    'iu3': resource_path("assets/idle up3.png"),
    'iu4': resource_path("assets/idle up4.png"),
    'il1': resource_path("assets/idle left1.png"),
    'il2': resource_path("assets/idle left2.png"),
    'il3': resource_path("assets/idle left3.png"),
    'il4': resource_path("assets/idle left4.png"),
    'ir1': resource_path("assets/idle right1.png"),
    'ir2': resource_path("assets/idle right2.png"),
    'ir3': resource_path("assets/idle right3.png"),
    'ir4': resource_path("assets/idle right4.png"),
    'id1': resource_path("assets/idle down1.png"),
    'id2': resource_path("assets/idle down2.png"),
    'id3': resource_path("assets/idle down3.png"),
    'id4': resource_path("assets/idle down4.png"),
    'wu1': resource_path("assets/walk up1.png"),
    'wu2': resource_path("assets/walk up2.png"),
    'wu3': resource_path("assets/walk up3.png"),
    'wu4': resource_path("assets/walk up4.png"),
    'wl1': resource_path("assets/walk left1.png"),
    'wl2': resource_path("assets/walk left2.png"),
    'wl3': resource_path("assets/walk left3.png"),
    'wl4': resource_path("assets/walk left4.png"),
    'wr1': resource_path("assets/walk right1.png"),
    'wr2': resource_path("assets/walk right2.png"),
    'wr3': resource_path("assets/walk right3.png"),
    'wr4': resource_path("assets/walk right4.png"),
    'wd1': resource_path("assets/walk down1.png"),
    'wd2': resource_path("assets/walk down2.png"),
    'wd3': resource_path("assets/walk down3.png"),
    'wd4': resource_path("assets/walk down4.png"),
    "grass": "assets/grass.png",
    "block": "assets/block.png",
    "block2": "assets/block2.png",

}

# player
player_img = pygame.image.load(assets['id1']).convert_alpha()  # player default image

player_idle_up = [  # player idle left animation image list
    pygame.image.load(assets['iu1']).convert_alpha(),
    pygame.image.load(assets['iu2']).convert_alpha(),
    pygame.image.load(assets['iu3']).convert_alpha(),
    pygame.image.load(assets['iu4']).convert_alpha(),
]
player_idle_left = [  # player idle left animation image list
    pygame.image.load(assets['il1']).convert_alpha(),
    pygame.image.load(assets['il2']).convert_alpha(),
    pygame.image.load(assets['il3']).convert_alpha(),
    pygame.image.load(assets['il4']).convert_alpha(),
]
player_idle_right = [  # player idle left animation image list
    pygame.image.load(assets['ir1']).convert_alpha(),
    pygame.image.load(assets['ir2']).convert_alpha(),
    pygame.image.load(assets['ir3']).convert_alpha(),
    pygame.image.load(assets['ir4']).convert_alpha(),
]
player_idle_down = [  # player idle left animation image list
    pygame.image.load(assets['id1']).convert_alpha(),
    pygame.image.load(assets['id2']).convert_alpha(),
    pygame.image.load(assets['id3']).convert_alpha(),
    pygame.image.load(assets['id4']).convert_alpha()
]
player_walk_up = [  # player idle down animation image list
    pygame.image.load(assets['wu1']).convert_alpha(),
    pygame.image.load(assets['wu2']).convert_alpha(),
    pygame.image.load(assets['wu3']).convert_alpha(),
    pygame.image.load(assets['wu4']).convert_alpha()
]
player_walk_left = [  # player idle down animation image list
    pygame.image.load(assets['wl1']).convert_alpha(),
    pygame.image.load(assets['wl2']).convert_alpha(),
    pygame.image.load(assets['wl3']).convert_alpha(),
    pygame.image.load(assets['wl4']).convert_alpha()
]
player_walk_right = [  # player idle down animation image list
    pygame.image.load(assets['wr1']).convert_alpha(),
    pygame.image.load(assets['wr2']).convert_alpha(),
    pygame.image.load(assets['wr3']).convert_alpha(),
    pygame.image.load(assets['wr4']).convert_alpha()
]
player_walk_down = [  # player idle down animation image list
    pygame.image.load(assets['wd1']).convert_alpha(),
    pygame.image.load(assets['wd2']).convert_alpha(),
    pygame.image.load(assets['wd3']).convert_alpha(),
    pygame.image.load(assets['wd4']).convert_alpha()
]

player = Obj(0, screen.get_height() / 2, player_img, False, True)
player_anim_states = [
    'idle up', 'idle left', 'idle right', 'idle down',
    'walk up', 'walk up', 'walk right', 'walk down'
]
player_anim_controller = animationC(player_anim_states)
player_anim_controller.add_animation("walk up", player_walk_up, 0.8)
player_anim_controller.add_animation("walk left", player_walk_left, 0.8)
player_anim_controller.add_animation("walk right", player_walk_right, 0.8)
player_anim_controller.add_animation("walk down", player_walk_down, 0.8)
player_anim_controller.add_animation("idle up", player_idle_up, 1)
player_anim_controller.add_animation("idle left", player_idle_left, 1)
player_anim_controller.add_animation("idle right", player_idle_right, 1)
player_anim_controller.add_animation("idle down", player_idle_down, 1)

player.anim_c = player_anim_controller

# block image
block_img_list = [pygame.image.load(assets['grass']).convert(),
                  pygame.image.load(assets['block']).convert(),
                  pygame.image.load(assets['block2']).convert()
                  ]

# level editor s for player position
block_collisions = [False, True, True]
block_list = [
    "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111",
    "100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001",
    "101110000000000111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111",
    "1000000111000011",
    "1000010000000001",
    "1111001111111111",
    "1000000000000001",
    "1000100000000001",
    "1000s10000000001",
    "1000110000000001",
    "1111111111111111",
    "1111111111111111",

]


# tile map creation
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
print(len(block_object_list))

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
    # frames per second handler(optional)
    # clock.tick(60)

    # input handler
    key_state = pygame.key.get_pressed()
    horizontal = key_state[pygame.K_d] - key_state[pygame.K_a]
    vertical = key_state[pygame.K_s] - key_state[pygame.K_w]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # background
    screen.fill((0, 0, 0))
    # player update

    (player.move(horizontal * 100 * time_delta, vertical * 100 * time_delta, object_list))
    # camera update
    (camera.update(object_list, screen))

    # first layer update
    for obj in block_object_list:
        obj.update(screen)

    # player update
    # animation logics
    if vertical == 1:
        player.anim_c.set_state('walk down')
        player.anim_c.play_animation("walk down", screen, time_delta, player.x, player.y)
    elif vertical == -1:
        player.anim_c.set_state('walk up')
        player.anim_c.play_animation("walk up", screen, time_delta, player.x, player.y)
    elif horizontal == 1:
        player.anim_c.set_state('walk right')
        player.anim_c.play_animation("walk right", screen, time_delta, player.x, player.y)
    elif horizontal == -1:
        player.anim_c.set_state('walk left')
        player.anim_c.play_animation("walk left", screen, time_delta, player.x, player.y)

    if vertical == 0 and horizontal == 0:
        player_state = player.anim_c.get_state()
        if 'down' in player_state:
            player.anim_c.play_animation("idle down", screen, time_delta, player.x, player.y)
        if 'up' in player_state:
            player.anim_c.play_animation("idle up", screen, time_delta, player.x, player.y)
        if 'left' in player_state:
            player.anim_c.play_animation("idle left", screen, time_delta, player.x, player.y)
        if 'right' in player_state:
            player.anim_c.play_animation("idle right", screen, time_delta, player.x, player.y)

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