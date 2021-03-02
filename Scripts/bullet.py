from Scripts.object import Object as Obj
import random


class Bullet:
    def __init__(self, speed, damage, direction, screen, pygame, image, target):
        self.speed = speed
        self.damage = damage
        self.bullets = []
        self.direction = direction
        self.screen = screen
        self.pygame = pygame
        self.image = image
        self.target = target

    def spawn(self):
        bullet = Obj(self.screen.get_width(),
                      random.randint(0, self.screen.get_height()),
                      self.image, False, 2, False, False
                      )
        bullet.hit = False
        self.bullets.append(bullet)

    def move(self, time_delta):
        for bullet in self.bullets:
            if self.direction is 0:
                bullet.move(-self.speed * time_delta, 0)
                bullet.update(self.screen, 0)
                if bullet.x < 0:
                    self.bullets.remove(bullet)
                try:
                    if bullet.rect.colliderect(self.target.rect) and not bullet.hit:
                        self.target.status.take_damage(self.damage)
                        bullet.hit = True
                except TypeError:
                    return
