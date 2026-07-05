import pygame

from code.Character import Character
from code.Const import WIN_WIDTH

class Player(Character):

    def update(self):
        self.move()

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]: # Walk backward
            self.rect.x -= self.speed
        if keys[pygame.K_d]: # Walk forward
            self.rect.x += self.speed

        if self.rect.left < 0: # Cannot exit the screen
            self.rect.left = 0
        if self.rect.right > WIN_WIDTH:
            self.rect.right = WIN_WIDTH

    def attack(self):

        if self.sword is not None: # Just while does not have a sword. It can't attack
            self.sword.attack()

    def change_guard(self, guard): 
        self.guard = guard