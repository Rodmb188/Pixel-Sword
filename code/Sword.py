import pygame

from code.Const import ATTACK_RANGE, ATTACK_START, ATTACK_TIME, C_GRAY, D_BOTTOM, D_MID, D_TOP, DIRECTION_E, G_BOTTOM, G_TOP, SWORD_HB

class Sword:

    def __init__(self, owner):
        self.owner = owner
        self.attacking = False
        self.has_hit = False

        self.attack_duration = ATTACK_TIME
        self.attack_start = ATTACK_START
        self.attack_offset = 0

        self.rect = pygame.Rect(SWORD_HB)

    def attack(self):
        if self.attacking:
            return
        
        self.attacking = True
        self.attack_start = pygame.time.get_ticks()
        self.has_hit = False

    def update(self):
        current_time = pygame.time.get_ticks()

        if self.attacking:
            self.attack_offset = ATTACK_RANGE
            if current_time - self.attack_start >= self.attack_duration:
                self.attacking = False
                self.attack_offset = 0

        self.update_position()

    def update_position(self):
        # Descobre a altura da guarda
        if self.owner.guard == G_TOP:
            offset_y = D_TOP
        elif self.owner.guard == G_BOTTOM:
            offset_y = D_BOTTOM
        else:
            offset_y = D_MID

        # Personagem olhando para a direita
        if self.owner.facing == DIRECTION_E:
            self.rect.midleft = (
                self.owner.rect.right + self.attack_offset,
                self.owner.rect.centery + offset_y
            )
        # Personagem olhando para a esquerda
        else:
            self.rect.midright = (
                self.owner.rect.left - self.attack_offset,
                self.owner.rect.centery + offset_y
            )

    def draw(self, screen):
        pygame.draw.rect(screen, C_GRAY, self.rect)