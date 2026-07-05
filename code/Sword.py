import pygame

from code.Const import ATTACK_START, ATTACK_TIME, C_GRAY, D_BOTTOM, D_MID, D_TOP, DIRECTION_W, G_BOTTOM, G_TOP, SWORD_HB

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
        # Descobre a altura da guarda
        if self.owner.guard == G_TOP:
            offset_y = D_TOP
        elif self.owner.guard == G_BOTTOM:
            offset_y = D_BOTTOM
        else:
            offset_y = D_MID

        # Personagem olhando para a direita
        if self.owner.facing != DIRECTION_W:
            self.rect.midleft = (
                self.owner.rect.right,
                self.owner.rect.centery + offset_y
            )
        # Personagem olhando para a esquerda
        else:
            self.rect.midright = (
                self.owner.rect.left,
                self.owner.rect.centery + offset_y
            )


    def draw(self, screen):
        pygame.draw.rect(screen, (C_GRAY), self.rect)