class HealthBar:
    
    def __init__(self, status):
        self.status = status
        
    def show_healthbar(self, screen, pygame, pos, dimension):
        # Max health
        pygame.draw.line(screen, (255, 0, 0), (pos[0], pos[1]), (pos[0] + dimension[0], pos[1] + dimension[1]))
        
        # Current health
        pygame.draw.line(screen, (0, 200, 0), (pos[0], pos[1]), (pos[0] + (dimension[0] * self.status.health/self.status.max_health), pos[1] + dimension[1]))
        