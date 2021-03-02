import random


class AI:
    def __init__(self, obj, speed):
        self.object = obj
        self.speed = speed
        self.directions = ['north', 'west', 'east', 'south']
        self.direction = self.directions[random.randint(0, len(self.directions)-1)]
        self.time_delta = 0
        self.time_to_attack = 0.5
        self.time_to_attack_counter = self.time_to_attack


    def movement(self, time_delta):
        self.time_delta = time_delta
        self.time_to_attack_counter -= time_delta
        if self.direction is 'north':
            x = 0
            y = -1 * time_delta * self.speed
        elif self.direction is 'west':
            x = -1 * time_delta * self.speed
            y = 0
        elif self.direction is 'east':
            x = 1 * time_delta * self.speed
            y = 0
        else:
            x = 0
            y = 1 * time_delta * self.speed
        self.object.move(x, y)

    def change_direction(self):
        self.direction = self.directions[random.randint(0, len(self.directions) - 1)]

    def attack(self):

        if self.time_to_attack_counter <= 0:
            self.time_to_attack_counter = self.time_to_attack
            return self.object.status.power
        else:
            return 0

