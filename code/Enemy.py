import random
import pygame
from code.Character import Character
from code.Const import AI_MAX_DISTANCE, AI_MIN_DISTANCE, DECISION_DELAY, DECISION_LAST, G_BOTTOM, G_MID, G_TOP, SPEED_BACKWARD, WIN_WIDTH

class Enemy(Character):

    def __init__(self, name, image, position, health, speed, facing):
        super().__init__(name, image, position, health, speed, facing)
        self.decision_delay = DECISION_DELAY
        self.last_decision = DECISION_LAST

    def move(self, player):
        distance = abs(self.rect.centerx - player.rect.centerx)
        player_is_left = player.rect.centerx < self.rect.centerx

        if distance < AI_MIN_DISTANCE: # Too close
            if player_is_left:
                self.rect.x += self.backward_speed
            else:
                self.rect.x -= self.backward_speed
        elif distance > AI_MAX_DISTANCE: # Too far
            if player_is_left:
                self.rect.x -= self.speed
            else:
                self.rect.x += self.speed
                
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIN_WIDTH:
            self.rect.right = WIN_WIDTH

    def choose_attack_guard(self, player):
        guards = [G_TOP, G_MID, G_BOTTOM]

        guards.remove(player.guard)
        return random.choice(guards)
    
    def think(self, player):
        current_time = pygame.time.get_ticks()

        if current_time - self.last_decision < self.decision_delay:
            return

        self.last_decision = current_time

        action = random.randint(1, 100)

        if action <= 40:
            follow_player = random.randint(1, 100)
            if follow_player <= 70: # 70% To choose guard as player
                self.change_guard(player.guard)
            else: # 30% To choose guard randomly
                self.change_guard(
                random.choice([G_TOP, G_MID, G_BOTTOM])
        )
        elif action <= 70:
            distance = self.rect.centerx - player.rect.centerx

            if distance <= AI_MAX_DISTANCE:
                self.change_guard(
                    self.choose_attack_guard(player)
                )
                print("Enemy decided to attack")
                self.attack()
        else:
            pass

    def update(self, player):
        self.move(player)
        self.think(player)
        self.update_hitboxes()
        self.update_invincibility()