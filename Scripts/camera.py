class Camera:

    def __init__(self, self_object, object_list, follow):
        self.objects = object_list
        self.follow = follow
        self.obj = self_object

    def update(self, object_list):
        x = self.obj.x - self.follow.x
        y = self.obj.y - self.follow.y


        for obj in object_list:
            obj.move(x, y, object_list)

