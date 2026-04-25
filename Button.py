import pygame


pygame.font.init()
font = pygame.font.SysFont('Comic Sans', 18)

class Button:
    def __init__(self, text, color, x, y):
        self.color = color
        self.darker = list(map(lambda x: max(0, x - 100), self.color))
        self.value = text
        self.text = font.render(text, 1, self.darker)
        self.x = x
        self.y = y
        self.width = 200
        self.height = 50
        
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), border_radius=10)
        pygame.draw.rect(screen, self.darker, (self.x, self.y, self.width, self.height), 3, border_radius=10)
        screen.blit(self.text, (self.x + (self.width - self.text.get_width()) // 2, self.y + (self.height - self.text.get_height()) // 2))