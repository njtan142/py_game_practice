from Scripts.canvas import Canvas
import pygame.freetype

class Menu:
    def __init__(self, pygame, screen):
        self.pygame = pygame
        self.screen = screen
        self.canvas = Canvas(self.pygame, "canvas")
        self.title_font = pygame.font.SysFont(None, 100)
        self.canvas.text("Title", self.title_font, "Welcome", (0,0,200),(self.screen.get_width()/2,self.screen.get_height() * 0.4))
        self.font = pygame.font.SysFont(None, 30)
        self.canvas.text("play instructions", self.font, "Press Enter to play", (0,0,200),(self.screen.get_width()/2,self.screen.get_height() * 0.6))
    
    def run(self, time_delta):
        self.canvas.renderUI(self.screen)
        
        