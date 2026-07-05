import pygame
import sys
from code.Const import BG_COLOR, FPS, G_BOTTOM, G_MID, G_TOP, TITLE, WIN_HEIGHT, WIN_WIDTH

class Game:

    def __init__(self):

        pygame.init()

        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption(TITLE)

        self.clock = pygame.time.Clock()

        self.running = True

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

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_j:
                    self.player.change_guard(G_TOP)
                elif event.key == pygame.K_k:
                    self.player.change_guard(G_MID)
                elif event.key == pygame.K_l:
                    self.player.change_guard(G_BOTTOM)
                elif event.key == pygame.K_SPACE:
                    self.player.attack()

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