class Renderer:

    def __init__(self):
        self.render_dict = {}
        self.render_list = []

    def add(self, objects):
        if type(objects) == list:
            for obj in objects:
                try:
                    self.render_dict[obj.layer]
                except KeyError:
                    self.render_dict[obj.layer] = []
                    self.render_list.append(obj.layer)
                self.render_dict[obj.layer].append(obj)
        else:
            self.render_list.append(objects.layer)
            self.render_dict[objects.layer] = objects
        self.render_list.sort()

    def render(self, screen, time_delta):
        for key in self.render_list:
            for obj in self.render_dict[key]:
                obj.update(screen, time_delta)
