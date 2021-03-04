

class Text:
    def __init__(self, pygame, font, text, color, pos, layer):
        self.layer = layer
        self.font = font
        self.color = color
        self.image = self.font.render(text, True, color)
        self.pos = (pos[0] - self.image.get_width() / 2, pos[1] - self.image.get_height() / 2)
        self.pygame = pygame
        self.rect = self.pygame.rect.Rect(self.pos[0], self.pos[1], self.image.get_width(), self.image.get_height())
        self.disabled = False

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
    def __init__(self, pygame, path, pos, layer):
        self.layer = layer
        self.pygame = pygame
        self.image = pygame.image.load(path).convert_alpha()
        self.pos = (pos[0] - self.image.get_width() / 2, pos[1] - self.image.get_height() / 2)
        self.rect = self.pygame.rect.Rect(self.pos[0], self.pos[1], self.image.get_width(), self.image.get_height())
        self.disabled = False
        print(self.pos)

    def update(self, screen):
        try:
            screen.blit(self.image, self.pos)
        except TypeError:
            screen.blit(self.image[0], self.pos)

    def change(self, path):
        self.pos = (self.pos[0] + self.image.get_width() / 2, self.pos[1] + self.image.get_height() / 2)
        self.image = self.pygame.image.load(path).convert_alpha()
        self.pos = (self.pos[0] - self.image.get_width() / 2, self.pos[1] - self.image.get_height() / 2)


class Rect:

    def __init__(self, pygame, pos, dimension, color, layer):
        self.pygame = pygame
        self.rect = pygame.rect.Rect(pos[0], pos[1], dimension[0], dimension[1])
        self.color = color
        self.layer = layer
        self.disabled = False

    def update(self, screen):
        self.pygame.draw.rect(screen, self.color, self.rect)

