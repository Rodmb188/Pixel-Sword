import pygame

from code.Const import ATTACK_START, ATTACK_TIME, C_GRAY, DIRECTION_E, SWORD_HB

class Sword:

    def __init__(self, owner):
        self.owner = owner
        self.attacking = False

        self.attack_duration = ATTACK_TIME
        self.attack_start = ATTACK_START

        self.rect = pygame.Rect(SWORD_HB)

    def attack(self):
        if self.attacking:
            return
        
        self.attacking = True
        self.attack_start = pygame.time.get_ticks()

    def update(self):
        self.update_position()

        current_time = pygame.time.get_ticks()

        if current_time - self.attack_start >= self.attack_duration:
            self.attacking = False


    def update_position(self):
        if self.owner.facing == DIRECTION_E:
            self.rect.midleft = self.owner.rect.midright
        else:
            self.rect.midright = self.owner.rect.midleft

    def draw(self, screen):
        pygame.draw.rect(screen, (C_GRAY), self.rect)