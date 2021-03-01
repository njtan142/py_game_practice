class Bounds:

    def __init__(self, x, y, objects, min_x, max_x, min_y, max_y):
        self.x = x
        self.y = y
        self.min_x = min_x
        self.min_y = min_y
        self.max_x = max_y
        self.max_y = max_x
        self.objects = objects

    def update(self, objects):
        self.objects = objects

    def move(self, x, y):
        self.x += x
        self.y += y
        self.min_x += x
        self.min_y += y
        self.max_x += y
        self.max_y += x

    def check(self):
        for obj in self.objects:
            if obj.x < self.min_x or obj.x > self.max_x:
                obj.x = obj.ox
            if obj.y < self.min_y or obj.y > self.max_y:
                obj.y = obj.oy
