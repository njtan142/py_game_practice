import pygame


class Object:

    def __init__(self, x, y, image, centered=True, is_player=False):
        self.is_player = is_player
        self.image = image
        self.float_x = 0
        self.float_y = 0
        if image is None:
            self.x = x
            self.y = y
            self.rect = pygame.rect.Rect(x, y, 0, 0)
        elif centered is False:
            self.x = x
            self.y = y
            self.rect = pygame.rect.Rect(x, y, image.get_width(), image.get_height())
        else:
            self.x = x - image.get_width() / 2
            self.y = y - image.get_height() / 2
            self.rect = pygame.rect.Rect(self.x, self.y, image.get_width(), image.get_height())

    def update(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def move(self, x, y, walls):
        
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

        if x != 0:
            self.move_single_axis(x, 0, walls)
        if y != 0:
            self.move_single_axis(0, y, walls)

    def move_single_axis(self, dx, dy, walls):
        self.x += dx
        self.y += dy
        # Move the rect
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

        # If you collide with a wall, move out based on velocity
        if self.is_player:
            for wall in walls:
                if wall == self:
                    continue
                if self.rect.colliderect(wall.rect):
                    if dx > 0:  # Moving right; Hit the left side of the wall
                        self.rect.right = wall.rect.left
                    if dx < 0:  # Moving left; Hit the right side of the wall
                        self.rect.left = wall.rect.right
                    if dy > 0:  # Moving down; Hit the top side of the wall
                        self.rect.bottom = wall.rect.top
                    if dy < 0:  # Moving up; Hit the bottom side of the wall
                        self.rect.top = wall.rect.bottom
                self.x = self.rect.x
                self.y = self.rect.y
        

