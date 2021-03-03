class Anim:

    def __init__(self, name, image_list, duration):
        self.name = name
        self.image_list = image_list
        self.duration = duration
        self.counter = 0

    def play(self, screen, time_delta, object, x_offset=0, y_offset=0):
        # if time_delta <= 0:
        #     return
        
        self.counter += time_delta # for the animation to continue where it left
        
        self.index = self.counter / self.duration * (len(self.image_list)) # choose what index of the image list to display


        object.image = self.image_list[max(min(round(self.index)-1, len(self.image_list) -1), 0)] # change the image of the object, I could use pygame.Surface.blit but I will use this because of the way the layered rendering works.
        
        # because of the way the pygame positioning works, adding offsetting the pygame.Surface.blit will help make the animation look seamless without messing up or breaking the collision
        object.offsetx = x_offset
        object.offsety = y_offset

        # Resets the counter
        if self.counter >= self.duration:
            self.counter -= self.duration
            return True
