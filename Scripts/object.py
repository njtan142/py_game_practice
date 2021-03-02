import pygame
import math
from Scripts.status import Stats
from Scripts.healthbar import HealthBar
from Scripts.enemyMovement import AI


class Object:

    def __init__(self, x, y, image=None, is_player=False, layer=0, entity=False, automation=False):
        self.entity = entity
        # core variables
        self.x = x
        self.y = y
        self.ox = x
        self.oy = y
        self.collision = True
        self.loop = 1
        self.is_player = is_player
        self.image = image

        # variables used by other functions
        self.offsetx = 0
        self.offsety = 0

        self.float_x = 0
        self.float_y = 0

        # define the collision based on the image
        if image is None:
            self.rect = pygame.rect.Rect(x, y, 0, 0)
            self.o_w = 0
            self.o_h = 0

        else:
            self.rect = pygame.rect.Rect(self.x, self.y, image.get_width(), image.get_height())
            self.o_w = image.get_width()
            self.o_h = image.get_height()

        # for layered rendering
        self.layer = layer

        # healthbar and status if it is an entity
        self.status = Stats()
        self.health_bar = HealthBar(self.status)

        self.is_automation = automation
        if self.is_automation:
            self.automation = AI(self, 50)

        self.walls = None

    def update(self, screen, time_delta):
        if self.entity:
            if self.status.health <= 0:
                self.rect = None
                return
        if self.is_automation and self.walls is not None:
            self.automation.movement(time_delta)
        # this is for chunked objects on the horizontal axis but will also work on unchunked obects
        x = self.x
        width = 0
        for i in range(self.loop):
            screen.blit(self.image, (x + self.offsetx, self.y + self.offsety))
            x -= self.image.get_width()
            width += self.o_w

        if self.collision:
            self.rect.x = x + self.image.get_width()
            self.rect.width = width

        if self.entity:
            self.health_bar.show_healthbar(screen, self.pygame, (self.x, self.y - 3), (width, 3))
            self.health_bar.show_healthbar(screen, self.pygame, (self.x, self.y), (width, 0))

        # reset the offset so that it wont affect other animations
        self.offsetx = 0
        self.offsety = 0

    def move(self, x, y, walls=None):
        if self.entity:
            if self.status.health <= 0:
                return
        if not self.is_player:  # performance reasons
            walls = None
        if self.is_player:
            if walls is not None:
                self.walls = walls
            else:
                walls = self.walls

        # moving the objects by integers instead of float because of the way pygame.rect works
        self.float_x += x - int(x)
        self.float_y += y - int(y)
        x = int(x)
        y = int(y)

        if self.float_x > 0 and self.float_x > 1:
            self.float_x -= 1
            x += 1
        if self.float_x < 0 and self.float_x < -1:
            self.float_x -= -1
            x -= 1
        if self.float_y > 0 and self.float_y > 1:
            self.float_y -= 1
            y += 1
        if self.float_y < 0 and self.float_y < -1:
            self.float_y -= -1
            y -= 1

        if math.fabs(x) >= 1:
            self.move_single_axis(x, 0, walls)

        if math.fabs(y) >= 1:
            self.move_single_axis(0, y, walls)

    def move_single_axis(self, dx, dy, walls):

        if self.entity:
            if self.status.health <= 0:
                return

        self.x += dx
        self.y += dy
        # Move the rect

        if self.collision:
            self.rect.x = int(self.x)
            self.rect.y = int(self.y)

        # If you collide with a wall, move out based on velocity
        if self.is_player:
            for obj in walls:
                if obj == self:
                    continue

                if obj.collision:
                    if obj.rect is None:
                        continue
                    if self.rect.colliderect(obj.rect):
                        if self.is_automation:

                            if obj.is_player and not obj.is_automation:
                                obj.status.take_damage(self.automation.attack())
                            else:
                                self.automation.change_direction()

                        if dx > 0:  # Moving right; Hit the left side of the wall
                            self.rect.right = obj.rect.left
                        if dx < 0:  # Moving left; Hit the right side of the wall
                            self.rect.left = obj.rect.right
                        if dy > 0:  # Moving down; Hit the top side of the wall
                            self.rect.bottom = obj.rect.top
                        if dy < 0:  # Moving up; Hit the bottom side of the wall
                            self.rect.top = obj.rect.bottom
                    else:
                        self.ox = self.x
                        self.oy = self.y

        if self.collision:
            self.x = self.rect.x
            self.y = self.rect.y
