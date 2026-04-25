from random import randint, choice

import pygame
# from PygameShader import hsl_effect


pygame.font.init()
font = pygame.font.SysFont('Comic Sans', 18)


class Animal:
    def __init__(self, x, y, name, shift, earning, age=0):
        self.x, self.y = x, y
        self.speed_x = self.speed_y = 0
        
        self.name = name
        
        self.sprites = {
            'left': [],
            'right': [],
            'top': [],
            'bottom': []
        }
        self.sprite = None
        self.shift = shift
        
        self.earning = earning
        
        self.walk = False
        
        self.age = age
        self.life_duration = None
        self.alive = True
        self.death_chance = 0
        
        self.counter = 0
        
    def transformation(self, sprite, size):
        sprite = pygame.transform.scale(pygame.image.load(sprite), size)
        # hsl_effect(sprite, self.shift)
        return sprite

    def update(self, screen):
        self.age += 0.1 / 60
        if self.age >= self.life_duration:
            self.death_chance += 0.000625       
        
        if randint(1, 100) > 100 - self.death_chance:
            self.alive = False
        
        if not randint(1, 100) > 95.5 and not self.walk:
            return
        elif not self.walk:
            self.walk = True
            self.counter = 0
            self.speed_x = randint(5, 15) / 10 * choice((-1, 1))
            self.speed_y = randint(5, 15) / 10 * choice((-1, 1))
        
        if 0 >= self.x + self.speed_x or \
            self.x + self.speed_x + self.sprite.get_width() >= screen.get_width():
            self.speed_x *= -1
        
        if screen.get_height() / 6 * 3.75 >= self.y + self.speed_y or \
            self.y + self.speed_y + self.sprite.get_height() >= screen.get_height():
            self.speed_y *= -1
        
        self.x += self.speed_x
        self.y += self.speed_y
    
        
    def draw(self, screen: pygame.Surface):
        self.counter += 1
        
        hor_direction = 'right' if self.speed_x > 0 else 'left'
        ver_direction = 'top' if self.speed_y < 0 else 'bottom'
        direction = hor_direction if abs(self.speed_x) > abs(self.speed_y) else ver_direction
        
        try:
            self.sprite = self.sprites[direction][int((self.counter // (18.75 - (7.5 * abs(self.speed_x) if direction in ('right', 'left') else abs(self.speed_y)))) % len(self.sprites[direction]))]
            screen.blit(self.sprite, (self.x, self.y))
        except:
            pass
        
        self.label = font.render(f"{self.name} ({int(self.age)})", 1, (255, 255, 255), (150, 150, 150, 150))
