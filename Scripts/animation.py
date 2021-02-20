class Anim:

    def __init__(self, name, image_list, duration):
        self.name = name
        self.image_list = image_list
        self.duration = duration
        self.counter = 0

    def play(self, screen, time_delta, x, y):
        self.counter += time_delta
        index = self.counter / self.duration * (len(self.image_list))
        screen.blit(self.image_list[round(index - 1)], (x, y))
        if self.counter >= self.duration:
            self.counter -= self.duration