class Camera:

    def __init__(self, self_object, object_list, follow):
        self.objects = object_list
        self.follow = follow
        self.obj = self_object

    def update(self, list, screen, follow=None):
        if follow is None:
            follow = self.follow
        self.follow = follow
        horizontal_difference = self.obj.x - self.follow.x 
        vertical_difference = self.obj.y - self.follow.y
        x = (horizontal_difference)
        y = (vertical_difference)
        print(x, y)
        for obj in self.objects:
            if obj.x > 0 - obj.image.get_width() and obj.x < screen.get_width():
                if obj.y > 0 - obj.image.get_height() and obj.y < screen.get_height():
                    obj.update(screen)
            obj.move(x, y, list)







