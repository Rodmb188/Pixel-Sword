import pygame

from code.Entity import Entity
from code.Const import BODY_CHEST, BODY_HEAD, BODY_LEG, COOLDOWN, INVINCIBLE_TIME

class Character(Entity):

    def __init__(self, name, image, position, health, speed, facing):
        super().__init__(name, image, position)

        # Life
        self.max_health = health
        self.health = health

        # Move_Speed
        self.base_speed = speed
        self.speed = speed

        # Combat
        self.guard = None
        self.state = "idle"

        # Weapon
        self.sword = None

        # Cooldown
        self.attack_cooldown = COOLDOWN
        self.last_attack = 0

        # Invincibility
        self.invincible = False
        self.invincible_time = INVINCIBLE_TIME

        self.facing = facing

        self.head_rect = pygame.Rect(0, 0, self.rect.width, BODY_HEAD)
        self.body_rect = pygame.Rect(0, 0, self.rect.width, BODY_CHEST)
        self.leg_rect = pygame.Rect(0, 0, self.rect.width, BODY_LEG)

        self.update_hitboxes()


    def take_damage(self, damage):
        if self.invincible:
            return

        self.health -= damage
        if self.health < 0:
            self.health = 0

        self.invincible = True
        self.invincible_start = pygame.time.get_ticks()


    def is_alive(self):
        return self.health > 0
    
    def update_hitboxes(self):
        self.head_rect.topleft = (
        self.rect.left,
        self.rect.top
    )

        self.body_rect.topleft = (
        self.rect.left,
        self.rect.top + self.head_rect.height
    )

        self.leg_rect.topleft = (
        self.rect.left,
        self.body_rect.bottom
    )

    def attack(self):
        pass

    def update_invincibility(self):

        if not self.invincible:
            return

        current_time = pygame.time.get_ticks()

        if current_time - self.invincible_start >= self.invincible_time:
            self.invincible = False