import pygame
from object import Object as Obj
from camera import Camera as Cam
from datetime import datetime as dt


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
player_img = pygame.image.load("assets/werewolf.png")
player = Obj(screen.get_width() / 2, screen.get_height() / 2, player_img, False, True)

# block image
block_img = pygame.image.load("assets/block.png")
block_list = [
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]


def tile_map(tile_map_array, image):
    tile_map_list = []
    y = 0
    for column in tile_map_array:
        x = 0
        for row in column:
            if row == 1:
                tile = Obj(x, y, image, False)
                tile_map_list.append(tile)
            x += image.get_width()
        y += image.get_height()
    return tile_map_list


block_object_list = tile_map(block_list, block_img)

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
    # clock.tick(60)
    # input handler
    key_state = pygame.key.get_pressed()
    horizontal = key_state[pygame.K_d] - key_state[pygame.K_a]
    vertical = key_state[pygame.K_s] - key_state[pygame.K_w]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # background
    screen.fill((203, 123, 123))
    # player update
    player.move(horizontal * 100 * time_delta, vertical * 100 * time_delta, object_list)

    # fps and time management
    last_time_dt = dt.now()
    last_time_ts = dt.timestamp(last_time_dt)
    time_delta = last_time_ts - current_time_ts
    time_count += time_delta
    current_time_dt = dt.now()
    current_time_ts = dt.timestamp(current_time_dt)

    # camera update
    camera.update(object_list, screen)

    # screen update
    pygame.display.update()

    fps += 1
    if time_count >= 1:
        print(fps)
        fps = 0
        time_count -= 1
