from Scripts.ui import Text, Image, Rect


class Canvas:
    def __init__(self, pygame, name):
        self.pygame = pygame
        self.name = name
        self.objects = {}
        self.layers = []

    def text(self, name, font, text, color, pos, layer=0):
        if layer not in self.layers:
            self.layers.append(layer)
        self.objects[name] = Text(self.pygame, font, text, color, pos, layer)
        self.layers.sort()

    def image(self, name, path, pos, layer=0):
        if layer not in self.layers:
            self.layers.append(layer)
        self.objects[name] = Image(self.pygame, path, pos, layer)
        self.layers.sort()

    def rect(self, name, pos, dimension, color, layer=0):
        if layer not in self.layers:
            self.layers.append(layer)
        self.objects[name] = Rect(self.pygame, pos, dimension, color, layer)
        self.layers.sort()

    def renderUI(self, screen):
        for layer in self.layers:
            for ui in self.objects:
                if not self.objects[ui].disabled and self.objects[ui].layer is layer:
                    self.objects[ui].update(screen)

