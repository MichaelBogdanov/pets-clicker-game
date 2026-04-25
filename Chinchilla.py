from Animal import Animal

import os
from random import choice

import pygame

os.chdir(os.path.dirname(__file__))
pygame.font.init()

chinchilla_names = [
    "Ибрагим",
    "Стас",
    "Моська",
    "Ольга Владиславовна",
    "Карамыш",
    "[НЕИЗВЕСТНО]",
    "Дигиндыгандыгаооо",
    "Радар 1985-2014гг",
    "Бидиблад",
    "Эпштепяк"
]

class Chinchilla(Animal):
    def __init__(self, x, y, name, shift, earning, age=0):
        super().__init__(x, y, name, shift, earning, age)
        
        self.name = choice(chinchilla_names)

        self.sprites = {
            'left': [],
            'right': [],
            'top': [],
            'bottom': []
        }
        for elem in [self.transformation('images/chinchilla/' + i, (75, 100)) for i in os.listdir('images/chinchilla/') if 'left' in i]:
            self.sprites['left'].append(elem)
        for elem in [self.transformation('images/chinchilla/' + i, (75, 100)) for i in os.listdir('images/chinchilla/') if 'right' in i]:
            self.sprites['right'].append(elem)
        for elem in [self.transformation('images/chinchilla/' + i, (75, 75)) for i in os.listdir('images/chinchilla/') if 'top' in i]:
            self.sprites['top'].append(elem)
        for elem in [self.transformation('images/chinchilla/' + i, (75, 75)) for i in os.listdir('images/chinchilla/') if 'bottom' in i]:
            self.sprites['bottom'].append(elem)
        
        self.life_duration = 15