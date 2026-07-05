import pygame

from code.Character import Character
from code.Const import WIN_WIDTH


class Player(Character):

    def update(self):
        self.move()


    def move(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rect.x -= self.speed

        if keys[pygame.K_d]:
            self.rect.x += self.speed

        # Impede sair da tela
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > WIN_WIDTH:
            self.rect.right = WIN_WIDTH


    def attack(self):

        if self.sword is not None:
            self.sword.attack()


    def change_guard(self, guard):
        self.guard = guard