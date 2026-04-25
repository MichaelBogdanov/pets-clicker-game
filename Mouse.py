from Animal import Animal
import os
from random import choice
import pygame


os.chdir(os.path.dirname(__file__))
pygame.font.init()



 
mouse_names = [
    "Просто крыса",
    "Рататуй",
    "Микки Маус",
    "Ля ты крыса",
    "Шустрик",
    "Норушка"
]


class Mouse(Animal):
    def __init__(self, x, y, name, shift, earning, age=0):
        super().__init__(x, y, name, shift, earning, age)

        
        self.sprites = {
            'left': [],
            'right': [],
            'top': [],
            'bottom': []
        }
        for elem in [self.transformation('images/mouse/' + i, (50,90)) for i in os.listdir('images/mouse/') if 'left' in i]:
            self.sprites['left'].append(elem)
        for elem in [self.transformation('images/mouse/' + i, (50,90)) for i in os.listdir('images/mouse/') if 'right' in i]:
            self.sprites['right'].append(elem)
        for elem in [self.transformation('images/mouse/' + i, (50, 90)) for i in os.listdir('images/mouse/') if 'top' in i]:
            self.sprites['top'].append(elem)
        for elem in [self.transformation('images/mouse/' + i, (50, 90)) for i in os.listdir('images/mouse/') if 'bottom' in i]:
            self.sprites['bottom'].append(elem)
        
        self.life_duration = 2