from Scripts.ui import Text, Image


class Canvas:
    def __init__(self, pygame, name):
        self.pygame = pygame
        self.name = name
        self.texts = {}
        self.images = {}

    def text(self, name, font, text, color, pos):
        self.texts[name] = Text(self.pygame, font, text, color, pos)

    def image(self, name, path, pos):
        self.images[name] = Image(self.pygame, path, pos)

    def renderUI(self, screen):
        for ui in self.texts:
            self.texts[ui].update(screen)
        for ui in self.images:
            self.images[ui].update(screen)
