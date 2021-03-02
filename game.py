from Scripts.camera import Camera as Cam
from Scripts.object import Object as Obj
from Scripts.animationc import animationC
from Scripts.level import Level
from Scripts.levelmanager import LevelManager
from Scripts.renderer import Renderer
from Scripts.canvas import Canvas
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
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.canvas = Canvas(pygame, "canvas")
        self.font = pygame.font.SysFont(None, 24)
        self.canvas.text("kills", self.font, "Kills: ", (255, 0, 0), (self.screen.get_width() * 0.05, 10))
        self.kills = 0
        self.canvas.text("kills counter", self.font, str(self.kills), (255, 255, 255),
                         (self.screen.get_width() * 0.15, 10))
        self.canvas.text("continue to next level", self.font, "", (0, 0, 0),
                         (self.screen.get_width() / 2, self.screen.get_height() * 0.48))
        self.current_level = 0
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
            'ss_iu1': resource_path("assets/ss/idle_01_01.png"),
            'ss_iu2': resource_path("assets/ss/idle_01_02.png"),
            'ss_iu3': resource_path("assets/ss/idle_01_03.png"),
            'ss_iu4': resource_path("assets/ss/idle_01_04.png"),
            'ss_il1': resource_path("assets/ss/idle_02_01.png"),
            'ss_il2': resource_path("assets/ss/idle_02_02.png"),
            'ss_il3': resource_path("assets/ss/idle_02_03.png"),
            'ss_il4': resource_path("assets/ss/idle_02_04.png"),
            'ss_ir1': resource_path("assets/ss/idle_03_01.png"),
            'ss_ir2': resource_path("assets/ss/idle_03_02.png"),
            'ss_ir3': resource_path("assets/ss/idle_03_03.png"),
            'ss_ir4': resource_path("assets/ss/idle_03_04.png"),
            'ss_id1': resource_path("assets/ss/idle_04_01.png"),
            'ss_id2': resource_path("assets/ss/idle_04_02.png"),
            'ss_id3': resource_path("assets/ss/idle_04_03.png"),
            'ss_id4': resource_path("assets/ss/idle_04_04.png"),
            'ss_wu1': resource_path("assets/ss/walk_01_01.png"),
            'ss_wu2': resource_path("assets/ss/walk_01_02.png"),
            'ss_wu3': resource_path("assets/ss/walk_01_03.png"),
            'ss_wu4': resource_path("assets/ss/walk_01_04.png"),
            'ss_wl1': resource_path("assets/ss/walk_02_01.png"),
            'ss_wl2': resource_path("assets/ss/walk_02_02.png"),
            'ss_wl3': resource_path("assets/ss/walk_02_03.png"),
            'ss_wl4': resource_path("assets/ss/walk_02_04.png"),
            'ss_wr1': resource_path("assets/ss/walk_03_01.png"),
            'ss_wr2': resource_path("assets/ss/walk_03_02.png"),
            'ss_wr3': resource_path("assets/ss/walk_03_03.png"),
            'ss_wr4': resource_path("assets/ss/walk_03_04.png"),
            'ss_wd1': resource_path("assets/ss/walk_04_01.png"),
            'ss_wd2': resource_path("assets/ss/walk_04_02.png"),
            'ss_wd3': resource_path("assets/ss/walk_04_03.png"),
            'ss_wd4': resource_path("assets/ss/walk_04_04.png"),
            'ss_au1': resource_path("assets/ss/attack up_01_01.png"),
            'ss_au2': resource_path("assets/ss/attack up_01_02.png"),
            'ss_au3': resource_path("assets/ss/attack up_01_03.png"),
            'ss_au4': resource_path("assets/ss/attack up_01_04.png"),
            'ss_al1': resource_path("assets/ss/attack_01_01.png"),
            'ss_al2': resource_path("assets/ss/attack_01_02.png"),
            'ss_al3': resource_path("assets/ss/attack_01_03.png"),
            'ss_al4': resource_path("assets/ss/attack_01_04.png"),
            'ss_ar1': resource_path("assets/ss/attack right_01_04.png"),
            'ss_ar2': resource_path("assets/ss/attack right_01_03.png"),
            'ss_ar3': resource_path("assets/ss/attack right_01_02.png"),
            'ss_ar4': resource_path("assets/ss/attack right_01_01.png"),
            'ss_ad1': resource_path("assets/ss/attack down_01_04.png"),
            'ss_ad2': resource_path("assets/ss/attack down_01_03.png"),
            'ss_ad3': resource_path("assets/ss/attack down_01_02.png"),
            'ss_ad4': resource_path("assets/ss/attack down_01_01.png"),
            "grass": "assets/grass.png",
            "block": "assets/block.png",
            "block2": "assets/block2.png",
            "dummy": "assets/enemies/dummy.png",
            "11": "assets/dungeon/11.png",
            "12": "assets/dungeon/12.png",
            "13": "assets/dungeon/13.png",
            "14": "assets/dungeon/14.png",
            "15": "assets/dungeon/15.png",
            "21": "assets/dungeon/21.png",
            "22": "assets/dungeon/22.png",
            "23": "assets/dungeon/23.png",
            "24": "assets/dungeon/24.png",
            "25": "assets/dungeon/25.png",
            "31": "assets/dungeon/31.png",
            "32": "assets/dungeon/32.png",
            "33": "assets/dungeon/33.png",
            "34": "assets/dungeon/34.png",
            "35": "assets/dungeon/35.png",
            "41": "assets/dungeon/41.png",
            "42": "assets/dungeon/42.png",
            "43": "assets/dungeon/43.png",
            "44": "assets/dungeon/44.png",
            "45": "assets/dungeon/45.png",
            "51": "assets/dungeon/51.png",
            "52": "assets/dungeon/52.png",
            "53": "assets/dungeon/53.png",
            "54": "assets/dungeon/54.png",
            "55": "assets/dungeon/55.png",
            "61": "assets/dungeon/61.png",
            "62": "assets/dungeon/62.png",
            "63": "assets/dungeon/63.png",
            "64": "assets/dungeon/64.png",
            "65": "assets/dungeon/65.png"

        }
        # player

        self.screen = screen
        self.player_anim_states = [
            'idle up', 'idle left', 'idle right', 'idle down',
            'walk up', 'walk up', 'walk right', 'walk down'
        ]
        player_anim_controller = animationC(self.player_anim_states)
        self.player_walk_up = [  # player idle down animation image list
            pygame.image.load(self.assets['ss_wu1']).convert_alpha(),
            pygame.image.load(self.assets['ss_wu2']).convert_alpha(),
            pygame.image.load(self.assets['ss_wu3']).convert_alpha(),
            pygame.image.load(self.assets['ss_wu4']).convert_alpha()
        ]
        player_anim_controller.add_animation("walk up", self.player_walk_up, 0.5)
        self.player_walk_left = [  # player idle down animation image list
            pygame.image.load(self.assets['ss_wl1']).convert_alpha(),
            pygame.image.load(self.assets['ss_wl2']).convert_alpha(),
            pygame.image.load(self.assets['ss_wl3']).convert_alpha(),
            pygame.image.load(self.assets['ss_wl4']).convert_alpha()
        ]
        player_anim_controller.add_animation("walk left", self.player_walk_left, 0.5)
        self.player_walk_right = [  # player idle down animation image list
            pygame.image.load(self.assets['ss_wr1']).convert_alpha(),
            pygame.image.load(self.assets['ss_wr2']).convert_alpha(),
            pygame.image.load(self.assets['ss_wr3']).convert_alpha(),
            pygame.image.load(self.assets['ss_wr4']).convert_alpha()
        ]
        player_anim_controller.add_animation("walk right", self.player_walk_right, 0.5)
        self.player_walk_down = [  # player idle down animation image list
            pygame.image.load(self.assets['ss_wd1']).convert_alpha(),
            pygame.image.load(self.assets['ss_wd2']).convert_alpha(),
            pygame.image.load(self.assets['ss_wd3']).convert_alpha(),
            pygame.image.load(self.assets['ss_wd4']).convert_alpha()
        ]
        player_anim_controller.add_animation("walk down", self.player_walk_down, 0.5)
        self.alpha_ = [  # player idle left animation image list
            pygame.image.load(self.assets['ss_iu1']).convert_alpha(),
            pygame.image.load(self.assets['ss_iu2']).convert_alpha(),
            pygame.image.load(self.assets['ss_iu3']).convert_alpha(),
            pygame.image.load(self.assets['ss_iu4']).convert_alpha(),
        ]
        player_anim_controller.add_animation("idle up", self.alpha_, 1)
        self.player_idle_left = [  # player idle left animation image list
            pygame.image.load(self.assets['ss_il1']).convert_alpha(),
            pygame.image.load(self.assets['ss_il2']).convert_alpha(),
            pygame.image.load(self.assets['ss_il3']).convert_alpha(),
            pygame.image.load(self.assets['ss_il4']).convert_alpha(),
        ]
        player_anim_controller.add_animation("idle left", self.player_idle_left, 1)
        self.player_idle_right = [  # player idle left animation image list
            pygame.image.load(self.assets['ss_ir1']).convert_alpha(),
            pygame.image.load(self.assets['ss_ir2']).convert_alpha(),
            pygame.image.load(self.assets['ss_ir3']).convert_alpha(),
            pygame.image.load(self.assets['ss_ir4']).convert_alpha(),
        ]
        player_anim_controller.add_animation("idle right", self.player_idle_right, 1)
        self.player_idle_down = [  # player idle left animation image list
            pygame.image.load(self.assets['ss_id1']).convert_alpha(),
            pygame.image.load(self.assets['ss_id2']).convert_alpha(),
            pygame.image.load(self.assets['ss_id3']).convert_alpha(),
            pygame.image.load(self.assets['ss_id4']).convert_alpha()
        ]
        player_anim_controller.add_animation("idle down", self.player_idle_down, 1)

        self.player_idle_down = [  # player attack up animation image list
            pygame.image.load(self.assets['ss_au1']).convert_alpha(),
            pygame.image.load(self.assets['ss_au2']).convert_alpha(),
            pygame.image.load(self.assets['ss_au3']).convert_alpha(),
            pygame.image.load(self.assets['ss_au4']).convert_alpha()
        ]
        player_anim_controller.add_animation("attack up", self.player_idle_down, 0.1)

        self.player_idle_down = [  # player attack left animation image list
            pygame.image.load(self.assets['ss_al1']).convert_alpha(),
            pygame.image.load(self.assets['ss_al2']).convert_alpha(),
            pygame.image.load(self.assets['ss_al3']).convert_alpha(),
            pygame.image.load(self.assets['ss_al4']).convert_alpha()
        ]
        player_anim_controller.add_animation("attack left", self.player_idle_down, 0.1)

        self.player_idle_down = [  # player attack right animation image list
            pygame.image.load(self.assets['ss_ar1']).convert_alpha(),
            pygame.image.load(self.assets['ss_ar2']).convert_alpha(),
            pygame.image.load(self.assets['ss_ar3']).convert_alpha(),
            pygame.image.load(self.assets['ss_ar4']).convert_alpha()
        ]
        player_anim_controller.add_animation("attack right", self.player_idle_down, 0.1)

        self.player_idle_down = [  # player attack right animation image list
            pygame.image.load(self.assets['ss_ad1']).convert_alpha(),
            pygame.image.load(self.assets['ss_ad2']).convert_alpha(),
            pygame.image.load(self.assets['ss_ad3']).convert_alpha(),
            pygame.image.load(self.assets['ss_ad4']).convert_alpha()
        ]
        player_anim_controller.add_animation("attack down", self.player_idle_down, 0.1)

        self.player = Obj(0, 0, pygame.image.load(self.assets["iu1"]).convert_alpha(), True, 2, True)
        self.player.anim_c = player_anim_controller
        self.player.attacking = False
        self.player.bottom_atk_rect = self.pygame.rect.Rect(self.player.x - 15, self.player.y + 8, 45, 30)
        self.player.top_atk_rect = self.pygame.rect.Rect(self.player.x - 15, self.player.y - 8, 45, 30)
        self.player.right_atk_rect = self.pygame.rect.Rect(self.player.x, self.player.y, 35, 40)
        self.player.left_atk_rect = self.pygame.rect.Rect(self.player.x - 20, self.player.y, 35, 40)
        self.player.pygame = pygame
        self.player.status.power = 30
        print(self.player.x, self.player.y)
        print(self.player.is_player, self.player.is_automation)
        self.dummy = Obj(0, 0, pygame.image.load(self.assets["dummy"]).convert_alpha(), True, 1, True, True)
        self.dummy.pygame = pygame
        # block image
        print(self.player.x, self.player.y)
        # level editor s for player positio3

        # tile map creation

        self.block_img_list = [
            pygame.transform.scale(pygame.image.load(self.assets['11']).convert(), (32, 32)),
            pygame.transform.scale(pygame.image.load(self.assets['12']).convert(), (32, 32)),
            pygame.transform.scale(pygame.image.load(self.assets['13']).convert(), (32, 32)),
            pygame.transform.scale(pygame.image.load(self.assets['14']).convert(), (32, 32)),
            pygame.transform.scale(pygame.image.load(self.assets['15']).convert(), (32, 32)),
            pygame.transform.scale(pygame.image.load(self.assets['21']).convert(), (32, 32)),
            pygame.transform.scale(pygame.image.load(self.assets['22']).convert(), (32, 32)),
            pygame.transform.scale(pygame.image.load(self.assets['23']).convert(), (32, 32)),
            pygame.transform.scale(pygame.image.load(self.assets['24']).convert(), (32, 32)),
            pygame.transform.scale(pygame.image.load(self.assets['25']).convert(), (32, 32)),
            pygame.transform.scale(pygame.image.load(self.assets['31']).convert(), (32, 32)),
            pygame.transform.scale(pygame.image.load(self.assets['32']).convert(), (32, 32)),
            pygame.transform.scale(pygame.image.load(self.assets['33']).convert(), (32, 32)),
            pygame.transform.scale(pygame.image.load(self.assets['34']).convert(), (32, 32)),
            pygame.transform.scale(pygame.image.load(self.assets['35']).convert(), (32, 32)),
            pygame.transform.scale(pygame.image.load(self.assets['41']).convert(), (32, 32)),
            pygame.transform.scale(pygame.image.load(self.assets['42']).convert(), (32, 32)),
            pygame.transform.scale(pygame.image.load(self.assets['43']).convert(), (32, 32)),
            pygame.transform.scale(pygame.image.load(self.assets['44']).convert(), (32, 32)),
            pygame.transform.scale(pygame.image.load(self.assets['45']).convert(), (32, 32)),
            pygame.transform.scale(pygame.image.load(self.assets['51']).convert(), (32, 32)),
            pygame.transform.scale(pygame.image.load(self.assets['52']).convert(), (32, 32)),
            pygame.transform.scale(pygame.image.load(self.assets['53']).convert(), (32, 32)),
            pygame.transform.scale(pygame.image.load(self.assets['54']).convert(), (32, 32)),
            pygame.transform.scale(pygame.image.load(self.assets['55']).convert(), (32, 32)),
            pygame.transform.scale(pygame.image.load(self.assets['61']).convert(), (32, 32)),
            pygame.transform.scale(pygame.image.load(self.assets['62']).convert(), (32, 32)),
            pygame.transform.scale(pygame.image.load(self.assets['63']).convert(), (32, 32)),
            pygame.transform.scale(pygame.image.load(self.assets['64']).convert(), (32, 32)),
            pygame.transform.scale(pygame.image.load(self.assets['65']).convert(), (32, 32))
        ]
        self.block_collisions = [True, True, True, True, True,
                                 True, True, True, True, True,
                                 False, False, False, False, False,
                                 False, False, False, False, False,
                                 False, False, False, False, True,
                                 False, False, False, False, False
                                 ]
        self.block_list = get_layout('Levels/0.txt')

        self.levels = LevelManager()
        self.levels.levels_dict["0"] = Level(
            '0', get_layout('Levels/0.txt'),
            self.block_img_list,
            self.block_collisions,
            [('s', self.player, 21, False), ('d', self.dummy, 20, True)],
            4
        )
        self.levels.levels_dict["1"] = Level(
            '0', get_layout('Levels/1.txt'),
            self.block_img_list,
            self.block_collisions,
            [('s', self.player, 21, False), ('d', self.dummy, 20, True)],
            5
        )
        self.levels.levels_dict["2"] = Level(
            '0', get_layout('Levels/2.txt'),
            self.block_img_list,
            self.block_collisions,
            [('s', self.player, 21, False), ('d', self.dummy, 20, True)],
            9
        )

        self.levels.active_level = self.levels.levels_dict["0"]
        self.block_object_list = self.levels.active_level.load()

        # frames counter (FPS)
        self.fps = 0

        self.time_count = 0

        # object list
        self.object_list = [self.player]
        for block in self.block_object_list:
            self.object_list.append(block)
        print(len(self.object_list), len(self.block_object_list))

        # camera
        camera_obj = Obj(self.screen.get_width() / 2, self.screen.get_height() / 2, None)
        self.camera = Cam(camera_obj, self.object_list, self.player)

        # layer rendering
        self.renderer = Renderer()
        self.renderer.add(self.object_list)

        for obj in self.object_list:
            obj.walls = self.object_list

        # self.object_list[3] = None

    def change_level(self, name=None):
        if self.kills is not self.levels.active_level.requirements:
            return
        if name is None:
            name = str(self.current_level + 1)
        self.current_level += 1
        try:
            self.levels.active_level = self.levels.levels_dict[name]
        except KeyError:
            print("uy")
            self.canvas.texts["continue to next level"].change("You finished the game, no more levels")
            return
        self.canvas.texts["continue to next level"].change("")
        self.levels.active_level = self.levels.levels_dict[name]
        self.block_object_list = self.levels.levels_dict[name].load()
        self.kills = 0
        self.canvas.texts["kills counter"].change(str(self.kills) + "/" + str(self.levels.active_level.requirements))
        # frames counter (FPS)
        self.fps = 0

        self.time_count = 0

        # object list
        self.object_list = [self.player]
        for block in self.block_object_list:
            self.object_list.append(block)
        self.renderer = Renderer()
        self.renderer.add(self.object_list)
        print(len(self.object_list), len(self.block_object_list))
        for obj in self.object_list:
            obj.walls = self.object_list

    def run(self, time_delta):
        # for obj in self.object_list:
        #     if obj.entity:
        #         if obj.status.health <= 0:
        #             self.object_list.remove(obj)
        #             obj = None
        #             continue

        self.player.bottom_atk_rect = self.pygame.rect.Rect(self.player.x - 15, self.player.y + 8, 45, 30)
        self.player.top_atk_rect = self.pygame.rect.Rect(self.player.x - 15, self.player.y - 8, 45, 30)
        self.player.right_atk_rect = self.pygame.rect.Rect(self.player.x, self.player.y, 35, 40)
        self.player.left_atk_rect = self.pygame.rect.Rect(self.player.x - 20, self.player.y, 35, 40)

        # input handler
        key_state = self.pygame.key.get_pressed()
        horizontal = key_state[self.pygame.K_d] - key_state[self.pygame.K_a]
        vertical = key_state[self.pygame.K_s] - key_state[self.pygame.K_w]

        # background
        self.screen.fill((0, 0, 0))

        #
        # player animation logics
        if vertical == 1:
            self.player.anim_c.set_state('walk down')
            self.player.anim_c.play_animation("walk down", self.screen, time_delta, self.player, -3, -6)
        elif vertical == -1:
            self.player.anim_c.set_state('walk up')
            self.player.anim_c.play_animation("walk up", self.screen, time_delta, self.player, 0, -4)
        elif horizontal == 1:
            self.player.anim_c.set_state('walk right')
            self.player.anim_c.play_animation("walk right", self.screen, time_delta, self.player, -2, -6)
        elif horizontal == -1:
            self.player.anim_c.set_state('walk left')
            self.player.anim_c.play_animation("walk left", self.screen, time_delta, self.player, -2, -6)

        player_state = self.player.anim_c.get_state()
        self.player_state = player_state

        if vertical == 0 and horizontal == 0:
            if 'down' in player_state:
                self.player.anim_c.set_state('idle down')
                self.player.anim_c.play_animation("idle down", self.screen, time_delta, self.player, -3, -6)
            if 'up' in player_state:
                self.player.anim_c.set_state('idle up')
                self.player.anim_c.play_animation("idle up", self.screen, time_delta, self.player, -2, -4)
            if 'left' in player_state:
                self.player.anim_c.set_state('idle left')
                self.player.anim_c.play_animation("idle left", self.screen, time_delta, self.player, 0, -4)
            if 'right' in player_state:
                self.player.anim_c.set_state('idle right')
                self.player.anim_c.play_animation("idle right", self.screen, time_delta, self.player, -2, -6)

        if self.player.attacking:
            if 'down' in player_state:
                if self.player.anim_c.play_animation("attack down", self.screen, time_delta, self.player, -22, 0):
                    self.player.attacking = False
            if 'up' in player_state:
                if self.player.anim_c.play_animation("attack up", self.screen, time_delta, self.player, -19, -10):
                    self.player.attacking = False
            if 'left' in player_state:
                if self.player.anim_c.play_animation("attack left", self.screen, time_delta, self.player, -22, 0):
                    self.player.attacking = False
            if 'right' in player_state:
                if self.player.anim_c.play_animation("attack right", self.screen, time_delta, self.player, -12, -1):
                    self.player.attacking = False

        # player movement
        self.player.move(horizontal * 100 * time_delta, vertical * 100 * time_delta, self.object_list)

        # camera update
        self.camera.update(self.object_list, self.screen)

        # layered update
        self.renderer.render(self.screen, time_delta)

        self.canvas.renderUI(self.screen)
        if self.kills == self.levels.active_level.requirements:
            self.canvas.texts["continue to next level"].change("Press enter to continue to next level")
        if self.player.status.health <= 0:
            self.canvas.texts["continue to next level"].change("Game Over")

        self.fps += 1
        self.time_count += time_delta
        if self.time_count >= 1:
            print(self.fps)
            self.fps = 0
            self.time_count -= 1
