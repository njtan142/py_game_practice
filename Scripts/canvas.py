from Scripts.ui import Text


class Canvas:
    def __init__(self, pygame, name):
        self.pygame = pygame
        self.name = name
        self.texts = {}

    def text(self, name, font, text, color, pos):
        self.texts[name] = Text(self.pygame, font, text, color, pos)

    def renderUI(self, screen):
        for ui in self.texts:
            self.texts[ui].update(screen)
