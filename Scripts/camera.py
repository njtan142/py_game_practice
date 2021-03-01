from math import sqrt
class Camera:

    def __init__(self, self_object, object_list, follow, bound):
        self.objects = object_list
        self.follow = follow
        self.obj = self_object
        self.bounds = bound

    def update(self, object_list, screen):
        x = self.obj.x - self.follow.x
        y = self.obj.y - self.follow.y

        if abs(x) < screen.get_width()/2:
            x = 0
        if abs(y) < screen.get_height()/2:
            y = 0

        # self.bounds.move(x, y)

        for obj in object_list:
            obj.move(x*1.99999, y*1.99999, object_list)


