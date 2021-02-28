class HealthBar:
    
    def __init__(self, status):
        self.status = status
        
    def show_healthbar(self, screen, pygame, pos, dimension):

        pygame.draw.rect(screen, (255, 80, 0), pygame.rect.Rect(pos[0], pos[1], dimension[0], dimension[1]))
    
        pygame.draw.rect(screen, (0, 200, 0), pygame.rect.Rect(pos[0], pos[1], dimension[0] * self.status.health/self.status.max_health, dimension[1]))
