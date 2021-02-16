
class Camera:

    def __init__(self, self_object, object_list, follow):
        self.objects = object_list
        self.follow = follow
        self.obj = self_object

    def update(self, object_list, screen, follow=None):
        if follow is None:
            follow = self.follow
        self.follow = follow
        x = self.obj.x - self.follow.x
        y = self.obj.y - self.follow.y
        for obj in self.objects:
            obj.move(x, y, object_list)
            if obj != self.follow:
                obj.update(screen)
        self.follow.update(screen)
