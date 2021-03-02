class Stats:

    def __init__(self, health=100, power=5, defense=1):
        self.max_health = health
        self.health = health
        self.power = power
        self.defense = defense

    def take_damage(self, damage, is_time=False, time_delta=1):
        if damage == 0:
            damage = self.defense

        self.health -= (damage - self.defense) * time_delta

    def recover(self, health):
        self.health += health
