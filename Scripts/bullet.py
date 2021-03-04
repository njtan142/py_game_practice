from Scripts.object import Object as Obj
import random


class Bullet:
    def __init__(self, speed, damage, axis, direction, screen, pygame, image, target):
        self.speed = speed
        self.damage = damage
        self.bullets = []
        self.axis = axis
        self.direction = direction
        self.screen = screen
        self.pygame = pygame
        self.image = image
        self.target = target
        self.surface = screen.convert_alpha()



    def spawn(self):
        if self.axis == 0 and self.direction < 0:
            bullet = Obj(self.screen.get_width(),
                         random.randint(0, self.screen.get_height()),
                         self.image, False, 2, False, False
                         )
        elif self.axis == 0 and self.direction > 0:
            bullet = Obj(0,
                         random.randint(0, self.screen.get_height()),
                         self.image, False, 2, False, False
                         )
        elif self.axis == 1 and self.direction > 0:
            bullet = Obj(random.randint(0, self.screen.get_width()),
                         0,
                         self.image, False, 2, False, False
                         )
        else:
            bullet = Obj(random.randint(0, self.screen.get_width()),
                         self.screen.get_height(),
                         self.image, False, 2, False, False
                         )
        bullet.hit = False
        self.bullets.append(bullet)

    def move(self, time_delta):
        for bullet in self.bullets:
            if self.axis == 0:
                bullet.move(self.direction * self.speed * time_delta, 0)
                bullet.update(self.screen, 0)
                if self.direction < 0:
                    self.pygame.draw.line(self.screen,
                                          (25, 0, 0, 100),
                                          (bullet.x, bullet.y + bullet.image.get_height() / 2),
                                          (0, bullet.y + bullet.image.get_height() / 2))
                if self.direction > 0:
                    self.pygame.draw.line(self.screen,
                                          (25, 0, 0, 100),
                                          (bullet.x, bullet.y + bullet.image.get_height()/2),
                                          (self.screen.get_width(), bullet.y + bullet.image.get_height()/2))
                if bullet.x < 0 or bullet.x > self.screen.get_width():
                    self.bullets.remove(bullet)
                try:
                    if bullet.rect.colliderect(self.target.rect) and not bullet.hit:
                        self.target.status.take_damage(self.damage)
                        bullet.hit = True
                except TypeError:
                    return
            else:
                bullet.move(0, self.direction * self.speed * time_delta)
                bullet.update(self.screen, 0)
                if self.direction < 0:
                    self.pygame.draw.line(self.screen,
                                          (25, 0, 0, 100),
                                          (bullet.x + bullet.image.get_width() / 2, bullet.y),
                                          (bullet.x + bullet.image.get_width() / 2, 0))
                if self.direction > 0:
                    self.pygame.draw.line(self.screen,
                                          (25, 0, 0, 100),
                                          (bullet.x + bullet.image.get_width() / 2, bullet.y),
                                          (bullet.x + bullet.image.get_width() / 2, self.screen.get_height()))
                if bullet.y < 0 or bullet.y > self.screen.get_height():
                    self.bullets.remove(bullet)
                try:
                    if bullet.rect.colliderect(self.target.rect) and not bullet.hit:
                        self.target.status.take_damage(self.damage)
                        bullet.hit = True
                except TypeError:
                    return
