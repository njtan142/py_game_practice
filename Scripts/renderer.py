class Renderer:
    
    def __init__(self):
        self.render_dict = {}
        self.render_list = []
    
    def add(self, objects):
        if type(objects) == list:
            for object in objects:
                try:
                    self.render_dict[object.layer]
                except KeyError:
                    self.render_dict[object.layer] = []
                    self.render_list.append(object.layer)
                self.render_dict[object.layer].append(object)
        else:
            self.render_list.append(objects.layer)
            self.render_dict[objects.layer] = objects
        self.render_list.sort()
        
        
    def render(self, screen):
        for key in self.render_list:
            for object in self.render_dict[key]:
                object.update(screen)
    
    