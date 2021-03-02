class Text:
    def __init__(self, pygame, font, text, color, pos):
        self.font = font
        self.color = color
        self.image = self.font.render(text, True, color)
        self.pos = (pos[0] - self.image.get_width() / 2, pos[1] - self.image.get_height() / 2)
        self.pygame = pygame

    def update(self, screen):
        try:
            screen.blit(self.image, self.pos)
        except TypeError:
            screen.blit(self.image[0], self.pos)

    def change(self, text):
        self.pos = (self.pos[0] + self.image.get_width() / 2, self.pos[1] + self.image.get_height() / 2)
        self.image = self.font.render(text, True, self.color)
        self.pos = (self.pos[0] - self.image.get_width() / 2, self.pos[1] - self.image.get_height() / 2)

class Image:
    def __init__(self, pygame, path, pos):
        self.pygame = pygame
        self.image = pygame.image.load(path).convert_alpha()
        self.pos = (pos[0] - self.image.get_width() / 2, pos[1] - self.image.get_height() / 2)


    def update(self, screen):
        try:
            screen.blit(self.image, self.pos)
        except TypeError:
            screen.blit(self.image[0], self.pos)

    def change(self, path):
        self.pos = (self.pos[0] + self.image.get_width() / 2, self.pos[1] + self.image.get_height() / 2)
        self.image = self.pygame.image.load(path).convert_alpha()
        self.pos = (self.pos[0] - self.image.get_width() / 2, self.pos[1] - self.image.get_height() / 2)