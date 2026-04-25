import os
from random import choice

import pygame

from Animal import Animal

os.chdir(os.path.dirname(__file__))
pygame.font.init()



dragon_names = [
    'Тони Старк'
]



class IronMan(Animal):
    def __init__(self, x, y, name, shift, earning, age=0):
        super().__init__(x, y, name, shift, earning, age)


        
        for elem in [self.transformation('images/ironman/' + i, (160, 120)) for i in os.listdir('images/ironman/') if 'left' in i and 'stay' not in i and 'cropped' in i]:
            self.sprites['left'].append(elem)
        for elem in [self.transformation('images/ironman/' + i, (160, 120)) for i in os.listdir('images/ironman/') if 'right' in i and 'stay' not in i and 'cropped' in i]:
            self.sprites['right'].append(elem)
        for elem in [self.transformation('images/ironman/' + i, (90, 160)) for i in os.listdir('images/ironman/') if 'top' in i and 'stay' not in i and 'cropped' in i]:
            self.sprites['top'].append(elem)
        for elem in [self.transformation('images/ironman/' + i, (90, 160)) for i in os.listdir('images/ironman/') if 'bottom' in i and 'stay' not in i and 'cropped' in i]:
            self.sprites['bottom'].append(elem)
        
        self.life_duration = 10