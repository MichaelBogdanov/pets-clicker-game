import os
from random import choice

import pygame

from Animal import Animal

os.chdir(os.path.dirname(__file__))
pygame.font.init()

breeds = [
    'Такса', 
    "Корги",
    "Овчарка",
    "Дворняжка",
    "Терьер",
    "Спаниель"
]

class Dog(Animal):
    def __init__(self, x, y, name, shift, earning, age=0):
        super().__init__(x, y, name, shift, earning, age)

        self.breed = choice(breeds) 
        
        for elem in [self.transformation('images/dog/' + i, (160, 120)) for i in os.listdir('images/dog/') if 'left' in i and 'stay' not in i and 'cropped' in i]:
            self.sprites['left'].append(elem)
        for elem in [self.transformation('images/dog/' + i, (160, 120)) for i in os.listdir('images/dog/') if 'right' in i and 'stay' not in i and 'cropped' in i]:
            self.sprites['right'].append(elem)
        for elem in [self.transformation('images/dog/' + i, (90, 160)) for i in os.listdir('images/dog/') if 'top' in i and 'stay' not in i and 'cropped' in i]:
            self.sprites['top'].append(elem)
        for elem in [self.transformation('images/dog/' + i, (90, 160)) for i in os.listdir('images/dog/') if 'bottom' in i and 'stay' not in i and 'cropped' in i]:
            self.sprites['bottom'].append(elem)
        
        self.life_duration = 10