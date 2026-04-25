import pygame


# Эффект пикселизации экрана
def pixelation(screen, pixelation=2):
    width, height = screen.get_size()
    small_surf = pygame.transform.scale(screen, (width // pixelation, height // pixelation))
    screen.blit(pygame.transform.scale(small_surf, (width, height)), (0, 0))