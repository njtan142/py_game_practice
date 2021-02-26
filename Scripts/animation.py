class Anim:

    def __init__(self, name, image_list, duration):
        self.name = name
        self.image_list = image_list
        self.duration = duration
        self.counter = 0

    def play(self, screen, time_delta, object, x_offset=0, y_offset=0):
        self.counter += time_delta
        self.index = self.counter / self.duration * (len(self.image_list))
        if int(self.index) == 0:
            self.index = 1
        object.image = self.image_list[int(self.index)-1]
        object.offsetx = x_offset
        object.offsety = y_offset
        
        if self.counter >= self.duration:
            self.counter -= self.duration
            self.index = 0
            return True
