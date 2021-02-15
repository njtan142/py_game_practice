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
            if obj.visible:
                obj.update(screen)
            if 0 - obj.image.get_width() < obj.x < screen.get_width() \
                    and 0 - obj.image.get_height() < obj.y < screen.get_height():
                obj.visible = True
            else:
                obj.visible = False
