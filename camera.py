class Camera:

    def __init__(self, self_object, object_list, follow):
        self.objects = object_list
        self.follow = follow
        self.obj = self_object

    def update(self, object_list, screen, follow=None):
        if follow is None:
            follow = self.follow
        self.follow = follow
        horizontal_difference = self.obj.x - self.follow.x
        vertical_difference = self.obj.y - self.follow.y
        x = horizontal_difference
        y = vertical_difference
        print(x, y)
        for obj in self.objects:
            if 0 - obj.image.get_width() < obj.x < screen.get_width()\
                    and 0 - obj.image.get_height() < obj.y < screen.get_height():
                obj.update(screen)
            obj.move(x, y, object_list)
