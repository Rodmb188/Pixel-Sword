from code.Entity import Entity
from code.Const import COOLDOWN, INVINCIBLE_TIME


class Character(Entity):

    def __init__(self, name, image, position, health, speed):

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
        self.last_hit = 0


    def receive_damage(self, damage):

        if self.invincible:
            return

        self.health -= damage

        if self.health < 0:
            self.health = 0


    def is_alive(self):
        return self.health > 0


    def attack(self):
        pass