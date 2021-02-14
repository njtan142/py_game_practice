class Camera:

    def __init__(self, self_object, object_list, follow):
        self.objects = object_list
        self.follow = follow
        self.obj = self_object

    def update(self, list, follow=None):
        if follow is None:
            follow = self.follow
        self.follow = follow
        horizontal_difference = self.obj.x - self.follow.x - follow.image.get_width()/2
        vertical_difference = self.obj.y - self.follow.y - follow.image.get_height()/2

        for obj in self.objects:
            x = int(horizontal_difference)
            y = int(vertical_difference)
            obj.move(x, y, list)






