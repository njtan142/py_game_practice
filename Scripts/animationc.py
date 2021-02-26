from Scripts.animation import Anim
from Scripts.states import State


class animationC:

    def __init__(self, states_list):
        self.animation_list = []
        self.state = State(states_list)

    def add_animation(self, name, image_list, duration):
        anim = Anim(name, image_list, duration)
        self.animation_list.append(anim)

    def play_animation(self, name, screen, time_delta, object, x_offset=0, y_offset=0):
        for anim in self.animation_list:
            if anim.name == name:
                return anim.play(screen, time_delta, object, x_offset, y_offset)

    def set_state(self, state):
        self.state.set_state(state)

    def get_state(self):
        return self.state.state
