from animation import Anim


class animationC:

    def __init__(self):
        self.animation_list = []

    def add_animation(self, name, image_list, duration):
        anim = Anim(name, image_list, duration)
        self.animation_list.append(anim)

    def play_animation(self, name, screen, time_delta, x, y):
        for anim in self.animation_list:
            if anim.name == name:
                anim.play(screen, time_delta, x, y)
