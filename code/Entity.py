import pygame
from abc import ABC

class Entity(ABC):

    def __init__(self, name, image, position):
        self.name = name
        self.image = image

        self.rect = self.image.get_rect()
        self.rect.topleft = position

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        # pygame.draw.rect(screen, (255, 0, 0), self.head_rect, 2)
        # pygame.draw.rect(screen, (0, 255, 0), self.body_rect, 2)
        # pygame.draw.rect(screen, (0, 0, 255), self.leg_rect, 2)