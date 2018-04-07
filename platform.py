import pygame


class Platform(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("sprites/ground_grass.png")
        self.image = pygame.transform.smoothscale(self.image, (50, 20))
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update(self):
        (width, height) = (pygame.display.Info().current_w, pygame.display.Info().current_h)