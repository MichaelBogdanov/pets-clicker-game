import sys
import time
import threading

import pygame

from random import randint

from Dog import Dog
from Chinchilla import Chinchilla
from Mouse import Mouse
from Capibara import Capibara
from Dino import Dino
from IronMan import IronMan


ITEMS = {
    Mouse: (0, (150, 150, 150)),
    Capibara: (0, (200, 200, 255)),
    Dog: (0, (0, 0, 255)),
    Chinchilla: (0, (200, 100, 255)),
    IronMan: (50, (255, 0, 0)),
    Dino: (50, (255, 215, 0))
}


def play_sound_async(file_path):
    """Функция для запуска звука в отдельном потоке."""
    sound = pygame.mixer.Sound(file_path)
    sound.play()
    # Ждем завершения звука, чтобы поток не закрылся раньше времени
    time.sleep(sound.get_length()) 


class Casino:
    def __init__(self, screen):
        self.items = {}
        for animal, data in ITEMS.items():
            surface = pygame.Surface((200, 200))
            current_animal = animal(0, 0, '', 0, 0)
            image = current_animal.sprites.get('bottom')[0]
            rect = image.get_rect()
            rect.center = (100, 100)
            surface.fill(data[1])
            surface.blit(image, rect)
            self.items[animal] = surface
            
        self.slots = []
        for _ in range(screen.get_width() // 200 + 2):
            self.slots.append(self.items[self.random_pet()[0]])
        
        self.speed_x = 200
        self.x = 0
        self.shift = 0
        
        self.complete = False
    
        self.screen = screen
    
        self.shadow = pygame.Surface(screen.get_size())
        self.shadow.set_alpha(128)
        self.shadow.fill((0, 0, 0))
    
    def random_pet(self):
        ITEMS = {
            Mouse: (0, (150, 150, 150)),
            Capibara: (0, (200, 200, 255)),
            Dog: (0, (0, 0, 255)),
            Chinchilla: (0, (200, 100, 255)),
            IronMan: (50, (255, 0, 0)),
            Dino: (50, (255, 215, 0))
        }
        chance = randint(1, 100)
        for animal, data in ITEMS.items():
            if chance <= data[0]:
                return animal, data
            else:
                chance -= data[0]

    def update(self):
        self.x -= self.speed_x
        self.shift -= self.speed_x
        if self.speed_x > 0:
            if abs(self.shift) >= 200:
                # Удаляем ту, которую проехали и она ушла за экран
                self.slots.pop(0)
                # Воспроизводим звук
                threading.Thread(target=play_sound_async, args=("music/tick.mp3", )).start()
                # Добавляем новую ячейку
                self.slots.append(self.items[self.random_pet()[0]])
                # Увеличиваем координату X
                self.x -= self.shift
                self.shift = 0
            self.speed_x = max(self.speed_x - 1, 0)
        elif not self.complete:
            self.complete = True
            threading.Thread(target=play_sound_async, args=("music/gambling.mp3", )).start()
        
    def draw(self):
        self.screen.blit(self.shadow, (0, 0))
        
        for i, slot in enumerate(self.slots):
            self.screen.blit(slot, (self.x + i * 200, self.screen.get_rect().centery - 100))
            if self.complete:
                if self.x + i * 200 <= self.screen.get_rect().centerx <= self.x + i * 200 + 200:
                    for animal, surface in self.items.items():
                        if surface == slot:
                            return animal
        
        pygame.draw.polygon(self.screen, (0, 0, 0), [   
                (self.screen.get_rect().centerx - 10, self.screen.get_rect().centery - 100),
                (self.screen.get_rect().centerx + 10, self.screen.get_rect().centery - 100),
                (self.screen.get_rect().centerx, self.screen.get_rect().centery - 75),
            ]
        )
        
        pygame.draw.polygon(self.screen, (0, 0, 0), [   
                (self.screen.get_rect().centerx - 10, self.screen.get_rect().centery + 100),
                (self.screen.get_rect().centerx + 10, self.screen.get_rect().centery + 100),
                (self.screen.get_rect().centerx, self.screen.get_rect().centery + 75),
            ]
        )


if __name__ == "__main__":
    pygame.init()
    pygame.mixer.init()
    
    
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption('Казино')
    
    clock = pygame.time.Clock()
    FPS = 60
    
    casino = Casino(screen)
    
    while True:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen.fill((255, 255, 255))
        
        casino.update()
        if (animal := casino.draw()) is not None:
            print(animal)
            pygame.quit()
            sys.exit()
        
        pygame.display.flip()