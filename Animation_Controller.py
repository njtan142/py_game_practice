from animation import Anim

class Animation_Controller:
    
    def __init_(self):
        self.initialized = True
        self.animation_list = []
    
    def add_animation(self, name, image_list, duration)
        anim = Anim(name, image_list, duration)