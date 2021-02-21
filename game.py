from Scripts.camera import Camera as Cam
from Scripts.object import Object as Obj
from Scripts.animationc import animationC
from Scripts.level import Level
from Scripts.levelmanager import LevelManager
import sys
import os


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath("")
    return os.path.join(base_path, relative_path)

def get_layout(path):
    level1 = open(resource_path(path), 'r')
    string = level1.read()
    layout = string.split('\n')
    level1.close()
    return layout
# stand alone functions
def get_distance(object1, object2, x1, y1):
    x_1 = object1.x + x1 - object2.x
    y_1 = object1.y + y1 - object2.y
    x_1 = x_1 ** 2
    y_1 = y_1 ** 2
    result = x_1 + y_1
    result = result ** 0.5
    return result


# assets

# levels
# level 1


class Game:
    # pygame initialization
    def __init__(self, pygame, screen):
        self.name = "game"
        self.pygame = pygame
        self.clock = pygame.time.Clock()
        # Assets
        self.assets = {
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

        self.player_img = pygame.image.load(self.assets["iu1"]).convert_alpha()
        self.screen = screen
        self.player_anim_states = [
            'idle up', 'idle left', 'idle right', 'idle down',
            'walk up', 'walk up', 'walk right', 'walk down'
        ]
        player_anim_controller = animationC(self.player_anim_states)
        self.player_walk_up = [  # player idle down animation image list
            pygame.image.load(self.assets['wu1']).convert_alpha(),
            pygame.image.load(self.assets['wu2']).convert_alpha(),
            pygame.image.load(self.assets['wu3']).convert_alpha(),
            pygame.image.load(self.assets['wu4']).convert_alpha()
        ]
        player_anim_controller.add_animation("walk up", self.player_walk_up, 0.8)
        self.player_walk_left = [  # player idle down animation image list
            pygame.image.load(self.assets['wl1']).convert_alpha(),
            pygame.image.load(self.assets['wl2']).convert_alpha(),
            pygame.image.load(self.assets['wl3']).convert_alpha(),
            pygame.image.load(self.assets['wl4']).convert_alpha()
        ]
        player_anim_controller.add_animation("walk left", self.player_walk_left, 0.8)
        self.player_walk_right = [  # player idle down animation image list
            pygame.image.load(self.assets['wr1']).convert_alpha(),
            pygame.image.load(self.assets['wr2']).convert_alpha(),
            pygame.image.load(self.assets['wr3']).convert_alpha(),
            pygame.image.load(self.assets['wr4']).convert_alpha()
        ]
        player_anim_controller.add_animation("walk right", self.player_walk_right, 0.8)
        self.player_walk_down = [  # player idle down animation image list
            pygame.image.load(self.assets['wd1']).convert_alpha(),
            pygame.image.load(self.assets['wd2']).convert_alpha(),
            pygame.image.load(self.assets['wd3']).convert_alpha(),
            pygame.image.load(self.assets['wd4']).convert_alpha()
        ]
        player_anim_controller.add_animation("walk down", self.player_walk_down, 0.8)
        self.alpha_ = [  # player idle left animation image list
            pygame.image.load(self.assets['iu1']).convert_alpha(),
            pygame.image.load(self.assets['iu2']).convert_alpha(),
            pygame.image.load(self.assets['iu3']).convert_alpha(),
            pygame.image.load(self.assets['iu4']).convert_alpha(),
        ]
        player_anim_controller.add_animation("idle up", self.alpha_, 1)
        self.player_idle_left = [  # player idle left animation image list
            pygame.image.load(self.assets['il1']).convert_alpha(),
            pygame.image.load(self.assets['il2']).convert_alpha(),
            pygame.image.load(self.assets['il3']).convert_alpha(),
            pygame.image.load(self.assets['il4']).convert_alpha(),
        ]
        player_anim_controller.add_animation("idle left", self.player_idle_left, 1)
        self.player_idle_right = [  # player idle left animation image list
            pygame.image.load(self.assets['ir1']).convert_alpha(),
            pygame.image.load(self.assets['ir2']).convert_alpha(),
            pygame.image.load(self.assets['ir3']).convert_alpha(),
            pygame.image.load(self.assets['ir4']).convert_alpha(),
        ]
        player_anim_controller.add_animation("idle right", self.player_idle_right, 1)
        self.player_idle_down = [  # player idle left animation image list
            pygame.image.load(self.assets['id1']).convert_alpha(),
            pygame.image.load(self.assets['id2']).convert_alpha(),
            pygame.image.load(self.assets['id3']).convert_alpha(),
            pygame.image.load(self.assets['id4']).convert_alpha()
        ]
        player_anim_controller.add_animation("idle down", self.player_idle_down, 1)

        self.player = Obj(0, self.screen.get_height() / 2, self.player_img, False, True)
        self.player.anim_c = player_anim_controller

        # block image

        # level editor s for player position

        # tile map creation

        self.block_img_list = [pygame.image.load(self.assets['grass']).convert(),
                               pygame.image.load(self.assets['block']).convert(),
                               pygame.image.load(self.assets['block2']).convert()
                               ]
        self.block_collisions = [False, True, True]
        self.block_list = get_layout('Levels/level0.txt')

        self.levels = LevelManager()
        self.levels.levels_dict["level0"] = Level('level0', get_layout('Levels/level0.txt'), self.block_img_list, self.block_collisions, self.player)
        self.levels.levels_dict["level1"] = Level('level1', get_layout('Levels/level1.txt'), self.block_img_list, self.block_collisions, self.player)
        self.levels.active_level = self.levels.levels_dict["level1"]
        self.block_object_list = self.levels.active_level.objects
        print(len(self.block_object_list))
        # frames counter (FPS)
        self.fps = 0

        self.time_count = 0

        # object list
        self.object_list = [self.player]
        for block in self.block_object_list:
            self.object_list.append(block)

        # camera
        camera_obj = Obj(self.screen.get_width() / 2, self.screen.get_height() / 2, None)
        self.camera = Cam(camera_obj, self.object_list, self.player)
        self.rel = True

    def run(self, time_delta):
        # frames per second handler(optional)
        # clock.tick(60)

        # input handler
        key_state = self.pygame.key.get_pressed()
        horizontal = key_state[self.pygame.K_d] - key_state[self.pygame.K_a]
        vertical = key_state[self.pygame.K_s] - key_state[self.pygame.K_w]

        # background
        self.screen.fill((0, 0, 0))
        # player update

        self.player.move(horizontal * 100 * time_delta, vertical * 100 * time_delta, self.object_list)
        # camera update

        self.camera.update(self.object_list)
        # first layer update
        for obj in self.block_object_list:
            obj.update(self.screen)

        # player update
        # animation logics
        if vertical == 1:
            self.player.anim_c.set_state('walk down')
            self.player.anim_c.play_animation("walk down", self.screen, time_delta, self.player.x, self.player.y)
        elif vertical == -1:
            self.player.anim_c.set_state('walk up')
            self.player.anim_c.play_animation("walk up", self.screen, time_delta, self.player.x, self.player.y)
        elif horizontal == 1:
            self.player.anim_c.set_state('walk right')
            self.player.anim_c.play_animation("walk right", self.screen, time_delta, self.player.x, self.player.y)
        elif horizontal == -1:
            self.player.anim_c.set_state('walk left')
            self.player.anim_c.play_animation("walk left", self.screen, time_delta, self.player.x, self.player.y)

        if vertical == 0 and horizontal == 0:
            player_state = self.player.anim_c.get_state()
            if 'down' in player_state:
                self.player.anim_c.play_animation("idle down", self.screen, time_delta, self.player.x,
                                                  self.player.y)
            if 'up' in player_state:
                self.player.anim_c.play_animation("idle up", self.screen, time_delta, self.player.x, self.player.y)
            if 'left' in player_state:
                self.player.anim_c.play_animation("idle left", self.screen, time_delta, self.player.x,
                                                  self.player.y)
            if 'right' in player_state:
                self.player.anim_c.play_animation("idle right", self.screen, time_delta, self.player.x,
                                                  self.player.y)

        # screen update
        self.pygame.display.update()
        self.fps += 1
        self.time_count += time_delta
        if self.time_count >= 1:
            print(self.fps)
            self.fps = 0
            self.time_count -= 1




