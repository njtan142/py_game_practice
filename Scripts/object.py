import pygame
import math


class Object:

    def __init__(self, x, y, image=None, is_player=False, layer=0):
        # core variables
        self.x = x
        self.y = y
        self.collision = True
        self.loop = 1
        self.is_player = is_player
        self.image = image
        
        # variables used by other functons
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
            
        if not self.collision:
            self.rect = None
            
        # for layered rendering
        self.layer = layer


    def update(self, screen):
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
        
        
        # reset the offset so that it wont affect other animations
        self.offsetx = 0
        self.offsety = 0


    def move(self, x, y, walls=None):
        
        if not self.is_player: #performance reasons
            walls = None
        
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
                    if self.rect.colliderect(obj.rect):
                        if dx > 0:  # Moving right; Hit the left side of the wall
                            self.rect.right = obj.rect.left
                        if dx < 0:  # Moving left; Hit the right side of the wall
                            self.rect.left = obj.rect.right
                        if dy > 0:  # Moving down; Hit the top side of the wall
                            self.rect.bottom = obj.rect.top
                        if dy < 0:  # Moving up; Hit the bottom side of the wall
                            self.rect.top = obj.rect.bottom
        if self.collision:
            self.x = self.rect.x
            self.y = self.rect.y
