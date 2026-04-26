import sys
from random import random, randint

import pygame
import threading

from server import *
from graphics import pixelation
from Dog import Dog
from Chinchilla import Chinchilla
from Mouse import Mouse
from Capibara import Capibara
from Dino import Dino
from IronMan import IronMan
from DogMenu import DogMenu
from Casino import Casino



login = menu()
if not login:
    sys.exit()

pygame.init()
pygame.font.init()

font = pygame.font.SysFont('Comic Sans', 36)

FPS = 120
WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
clock = pygame.time.Clock()
frame_counter = 0

score = get_score(login)

wallpaper = pygame.image.load('images/background.jfif')
wallpaper = pygame.transform.scale(wallpaper, (WIDTH, HEIGHT))
floor = pygame.image.load('images/floor.png').convert_alpha()
floor = pygame.transform.scale(floor, (WIDTH, HEIGHT))

dog_menu = DogMenu()

def post_request(earn):
    if earn >= 0:
        add_score(login, earn)
    else:
        reduce_score(login, earn)

def add_animal_request(animal):
    add_animal(login, animal)

animals = get_animals(login)
pets = []
for animal in animals:
    pos = randint(0, WIDTH - 200), randint(int(HEIGHT / 6 * 3.75), HEIGHT - 200)
    match animal[2]:
        case 'Dog':
            pet = Dog(*pos, animal[0], random(), 1, animal[1])
            pet.life_duration = animal[3]
            pets.append(pet)
        case 'Chinchilla':
            pet = Chinchilla(*pos, animal[0], random(), 1, animal[1])
            pet.life_duration = animal[3]
            pets.append(pet)
        case 'Mouse':
            pet = Mouse(*pos, animal[0], random(), 1, animal[1])
            pet.life_duration = animal[3]
            pets.append(pet)
        case 'Capibara':
            pet = Capibara(*pos, animal[0], random(), 1, animal[1])
            pet.life_duration = animal[3]
            pets.append(pet)
        case 'Dino':
            pet = Dino(*pos, animal[0], random(), 1, animal[1])
            pet.life_duration = animal[3]
            pets.append(pet)
        case 'IronMan':
            pet = IronMan(*pos, animal[0], random(), 1, animal[1])
            pet.life_duration = animal[3]
            pets.append(pet)

while True:
    clock.tick(FPS)
        
    pixelation(wallpaper, 8)
    screen.blit(wallpaper, (0, 0))
    pixelation(floor, 8)
    screen.blit(floor, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = event.pos
                for button in dog_menu.buttons:
                    price = int(button.value)
                    if ((screen.get_width() / 2 - dog_menu.surface.get_width() / 2) + button.x <= x <= (screen.get_width() / 2 - dog_menu.surface.get_width() / 2) + button.x + button.width and \
                        dog_menu.y + button.y <= y <= dog_menu.y + button.y + button.height) and score >= price:
                            threading.Thread(target=post_request, args=(price, )).start()
                            score -= price
                            pos = randint(0, WIDTH - 200), randint(int(HEIGHT / 6 * 3.75), HEIGHT - 200)
                            # Создаём казино
                            casino = Casino(screen)
                            break
                else:
                    threading.Thread(target=post_request, args=(1, )).start()
                    score += 1
                for dog in [i for i in pets if not i.alive]:
                    if (dog.x + dog.sprite.get_width() / 2 - 25 <= x <= dog.x + dog.sprite.get_width() / 2 + 25 and \
                    dog.y + dog.sprite.get_height() / 2 - 25 <= y <= dog.y + dog.sprite.get_height() / 2 + 25):
                        threading.Thread(target=post_request, args=(50, )).start()
                        score += 50
                        pets.remove(dog)
                        

                        
    for pet in sorted(pets, key=lambda x: x.y):
        if pet.alive:
            try:
                pet.update(screen)
            except:
                pass
            pet.draw(screen)
            if frame_counter % FPS == 0:

                threading.Thread(target=post_request, args=(pet.earning, )).start()
                score += pet.earning
        else:
            pygame.draw.circle(screen, (0, 0, 0), (pet.x + pet.sprite.get_width() / 2, pet.y + pet.sprite.get_height() / 2), 25)
    
    for pet in pets:
        if pet.alive:
            screen.blit(pet.label, (pet.x + ((pet.sprite.get_width() - pet.label.get_width()) // 2), pet.y - 32))
    
    score_label = font.render(str(int(score)), 1, (255, 215, 0), (100, 100, 100))
    screen.blit(score_label, (15, 15))
    
    for _ in range(5):
        dog_menu.update(pygame.mouse.get_pos())
        dog_menu.draw(screen)
    
    try:
        if not casino.complete:
            casino.update()
            if (animal := casino.draw()) is not None:
                animal_type_name = type(animal(0, 0, '', 0, 0)).__name__
                pets.append(animal(*pos, threading.Thread(target=add_animal_request, args=(animal_type_name, )).start(), random(), 1))
    except:
        pass
    
    pygame.display.flip()
    frame_counter += 1
    