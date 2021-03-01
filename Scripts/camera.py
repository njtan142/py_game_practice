from math import sqrt
class Camera:

    def __init__(self, self_object, object_list, follow, bound):
        self.objects = object_list
        self.follow = follow
        self.obj = self_object
        self.bounds = bound

    def update(self, object_list, time_delta):
        x = self.obj.x - self.follow.x
        y = self.obj.y - self.follow.y

        # self.bounds.move(x, y)

        for obj in object_list:
            obj.move(x, y, object_list)


