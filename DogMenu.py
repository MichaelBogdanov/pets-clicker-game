import pygame

from Button import Button


class DogMenu:
    def __init__(self):
        self.width = 1050
        self.height = 200
        self.y = -self.height
        self.speed_y = 0
        
        self.surface = pygame.Surface((self.width, self.height)).convert_alpha()
        
        self.buttons_sprites = [pygame.transform.scale(pygame.image.load(f'images/cases/{i}.webp'), (150, 100)) for i in range(1, 5)]
        
        self.buttons = [
            Button("100", (100, 230, 150, 200), 0, 0),
            Button("500", (100, 230, 150, 200), 0, 0),
            Button("1500", (100, 230, 150, 200), 0, 0),
            Button("150000", (100, 230, 150, 200), 0, 0),
        ]
        for i in range(len(self.buttons)):
            self.buttons[i].x = 50 + 200 * i + 50 * i
            self.buttons[i].y = 130

    def update(self, mouse_pos):
        if mouse_pos[1] <= self.height:
            self.speed_y = 1
        else:
            self.speed_y = -1
        self.y = max(-self.height, min(0, self.y + self.speed_y))
        
    def draw(self, screen):
        self.surface.fill((0, 0, 0, 0))
        pygame.draw.rect(self.surface, (255, 255, 255, 200), self.surface.get_rect(), border_radius=10)
        
        for i in range(len(self.buttons_sprites)):
            self.surface.blit(self.buttons_sprites[i], (75 + 200 * i + 50 * i, 25))
        
        for button in self.buttons:
            button.draw(self.surface)
            
        screen.blit(self.surface, (screen.get_width() / 2 - self.surface.get_width() / 2, self.y))
            