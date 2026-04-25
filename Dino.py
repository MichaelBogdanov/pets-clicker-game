import os
from random import choice

import pygame
from graphics import pixelation

from Animal import Animal

os.chdir(os.path.dirname(__file__))
pygame.font.init()

dino_names = [
    'Ыбан',
    'TimurByek',
    'Пиво',
    'Баратрум',
    'ПУДЖ',
    '12 ТАНГО',
    'Витэк',
    'Артем Котенко',
    'Данил Колбасенко',
    'Зайчик Джуди Хопс',
    'Шершень',
    "Энгрибертс",
    'Шапокляк',
    'Матвийко',
    'Лис Ник Вайл',
    'Губка боб',
    'Kliiinda',
    'Нет, это Патрик', 
    'Ыбаниха',
    'Эпштейн',
    'Альбэрт',
    'Андреев Артем Олегович',
    'Андреева Ева Вадимовна',
    'Андреева Пивазина Артйомовна',
    'Donk',
    'Zywoo',
    'S0mple',
    'Cmetanka_ZOV_SVO',
    "Мiхiiл Мiхiйлiвiч"
]

class Dino(Animal):
    def __init__(self, x, y, name, shift, earning, age=0):
        super().__init__(x, y, name, shift, earning, age)
        
        self.sprites = {
            'left': [],
            'right': [],
            'top': [],
            'bottom': []
        }
        for elem in [self.transformation('images/dino/' + i, (160, 120)) for i in os.listdir('images/dino/') if 'left' in i and 'stay' not in i and 'cropped' in i]:
            pixelation(elem, 4)
            self.sprites['left'].append(elem)
        for elem in [self.transformation('images/dino/' + i, (160, 120)) for i in os.listdir('images/dino/') if 'right' in i and 'stay' not in i and 'cropped' in i]:
            pixelation(elem, 4)
            self.sprites['right'].append(elem)
        for elem in [self.transformation('images/dino/' + i, (90, 160)) for i in os.listdir('images/dino/') if 'top' in i and 'stay' not in i and 'cropped' in i]:
            pixelation(elem, 4)
            self.sprites['top'].append(elem)
        for elem in [self.transformation('images/dino/' + i, (90, 160)) for i in os.listdir('images/dino/') if 'bottom' in i and 'stay' not in i and 'cropped' in i]:
            pixelation(elem, 4)
            self.sprites['bottom'].append(elem)
        self.sprite = self.sprites['bottom'][0]
        
        self.life_duration = 20