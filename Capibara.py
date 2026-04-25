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


class Capibara(Animal):
    def __init__(self, x, y, name, shift, earning, age=0):
        super().__init__(x, y, name, shift, earning, age)

        
        self.sprites = {
            'left': [],
            'right': [],
            'top': [],
            'bottom': []
        }
        for elem in [self.transformation('images/capibara/' + i, (100, 100)) for i in os.listdir('images/capibara/') if 'left' in i]:
            self.sprites['left'].append(elem)
        for elem in [self.transformation('images/capibara/' + i, (100, 100)) for i in os.listdir('images/capibara/') if 'right' in i]:
            self.sprites['right'].append(elem)
        for elem in [self.transformation('images/capibara/' + i, (100, 100)) for i in os.listdir('images/capibara/') if 'top' in i]:
            self.sprites['top'].append(elem)
        for elem in [self.transformation('images/capibara/' + i, (100, 100)) for i in os.listdir('images/capibara/') if 'bottom' in i]:
            self.sprites['bottom'].append(elem)
        
        self.life_duration = 2