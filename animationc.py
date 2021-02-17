from animation import Anim
from states import State


class animationC:

    def __init__(self, states_list):
        self.animation_list = []
        self.state = State(states_list)

    def add_animation(self, name, image_list, duration):
        anim = Anim(name, image_list, duration)
        self.animation_list.append(anim)

    def play_animation(self, name, screen, time_delta, x, y):
        for anim in self.animation_list:
            if anim.name == name:
                anim.play(screen, time_delta, x, y)

    def set_state(self, state):
        self.state.set_state(state)

    def get_state(self):
        return self.state.state
