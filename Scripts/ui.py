class Text:
    def __init__(self, pygame, font, text, color, pos):
        self.font = font
        self.color = color
        self.image = self.font.render(text, True, color)
        self.pos = pos
        
    def update(self, screen):
        screen.blit(self.image, self.pos)
        
    def change(self, text):
        self.image = self.font.render(text, True, self.color)