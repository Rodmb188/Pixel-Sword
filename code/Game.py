import pygame
import sys
from code.Const import BG_COLOR, CHAR_DIMENSION, C_BLUE, C_RED, DIRECTION_E, DIRECTION_W, FPS, G_BOTTOM, G_MID, G_TOP, HEALTH, SPAWN_E, SPAWN_P, SPEED, TITLE, WIN_HEIGHT, WIN_WIDTH
from code.Enemy import Enemy
from code.Player import Player
from code.Sword import Sword

class Game:

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption(TITLE)

        self.clock = pygame.time.Clock()
        self.running = True

        player_image = pygame.Surface((CHAR_DIMENSION))
        player_image.fill((C_BLUE))

        self.player = Player(
            "Player",
            player_image,
            (SPAWN_P),
            HEALTH,
            SPEED,
            DIRECTION_E
        )
        self.player.sword = Sword(self.player)

        enemy_image = pygame.Surface((CHAR_DIMENSION))
        enemy_image.fill((C_RED))

        self.enemy = Enemy(
            "Enemy",
            enemy_image,
            (SPAWN_E),
            HEALTH,
            SPEED,
            DIRECTION_W
        )
        self.enemy.sword = Sword(self.enemy)

    def run(self):
        while self.running:
            self.events()
            self.update()
            self.draw()

            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.player.update()
        self.enemy.update()

        self.player.sword.update()
        self.enemy.sword.update()

    def draw(self):
        self.screen.fill(BG_COLOR)

        self.player.draw(self.screen)
        self.enemy.draw(self.screen)
        
        self.player.sword.draw(self.screen)
        self.enemy.sword.draw(self.screen)

        pygame.display.flip()