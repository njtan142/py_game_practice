class Stats:

    def __init__(self, health=100, power=5, defense=1):
        self.max_health = health
        self.health = health
        self.power = power
        self.defense = defense

    def take_damage(self, damage):
        self.health -= damage - self.defense

    def recover(self, health):
        self.health += health