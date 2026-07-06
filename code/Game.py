import pygame
import sys
from code.Const import ATTACK_OFFSET, BAR_ENEMY_POS, BAR_HEIGHT, BAR_PLAYER_POS, BAR_WIDTH, BG_COLOR, C_DARK_RED, C_GREEN, C_WHITE, CHAR_DIMENSION, COLLISION_GAP, C_BLUE, C_RED, D_BODY, D_HEAD, D_LEG, DIRECTION_E, DIRECTION_W, FONT_NAME, FONT_SIZE, FPS, G_BOTTOM, G_MID, G_TOP, HEALTH, HUD_SCORE_Y, KNOCKBACK, ROUNDS_TO_WIN, SPAWN_E, SPAWN_P, SPEED, SPEED_MIN, TITLE, WIN_HEIGHT, WIN_WIDTH
from code.State import COMMANDS, MENU, PLAYING, GAME_OVER
from code.Commands import Commands
from code.Enemy import Enemy
from code.Player import Player
from code.Sword import Sword
from code.Menu import Menu

class Game:

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption(TITLE)
        self.font = pygame.font.SysFont(FONT_NAME, FONT_SIZE)

        self.menu = Menu()

        self.clock = pygame.time.Clock()
        self.running = True

        player_image = pygame.Surface((CHAR_DIMENSION))
        player_image.fill((C_BLUE))
        
        self.player_score = 0
        self.enemy_score = 0
        
        self.round_ending = False
        self.round_end_time = 0

        self.state = MENU
        self.winner = None
        self.commands = Commands()

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
            elif event.type == pygame.KEYDOWN:
                
                if self.state == COMMANDS:
                    if event.key == pygame.K_ESCAPE:
                        self.state = MENU

                if self.state == MENU:
                    if event.key == pygame.K_UP:
                        self.menu.move_up()
                    elif event.key == pygame.K_DOWN:
                        self.menu.move_down()
                    elif event.key == pygame.K_RETURN:
                        if self.menu.selected == 0:
                            self.state = PLAYING

                        elif self.menu.selected == 1:
                            self.state = COMMANDS

                        elif self.menu.selected == 2:
                            self.running = False
            
                if self.state == PLAYING:
                    if event.key == pygame.K_j:
                        self.player.change_guard(G_TOP)
                    elif event.key == pygame.K_k:
                        self.player.change_guard(G_MID)
                    elif event.key == pygame.K_l:
                        self.player.change_guard(G_BOTTOM)
                    elif event.key == pygame.K_SPACE:
                        self.player.attack()
            
                if self.state == GAME_OVER:
                    if event.key == pygame.K_RETURN:
                        self.player_score = 0
                        self.enemy_score = 0
                        self.reset_round()

                    self.state = MENU

    def update(self):
        if self.state != PLAYING:
            return
        
        if self.round_ending:
            current_time = pygame.time.get_ticks()

            if current_time - self.round_end_time >= 1000:
                    self.round_ending = False
                    self.reset_round()
            return
    
        self.player.update()
        self.enemy.update(self.player)
        
        self.resolve_collision()

        self.player.sword.update()
        self.enemy.sword.update()

        self.check_hit(self.player, self.enemy)
        self.check_hit(self.enemy, self.player)

        self.check_round()

    def resolve_collision(self):
        if self.player.rect.right >= self.enemy.rect.left - COLLISION_GAP:
            self.player.rect.right = self.enemy.rect.left - COLLISION_GAP

            self.player.update_hitboxes()
            self.enemy.update_hitboxes()

    def check_hit(self, attacker, defender):
        sword = attacker.sword
        
        if not sword.attacking or sword.has_hit:
            return
        
        if sword.rect.colliderect(defender.head_rect):
            # print("HEAD") # Testing Hitbox
            damage = D_HEAD
            hit_guard = G_TOP
        elif sword.rect.colliderect(defender.body_rect):
            # print("BODDY") # Testing Hitbox
            damage = D_BODY
            hit_guard = G_MID
        elif sword.rect.colliderect(defender.leg_rect):
            # print("LEG") # Testing Hitbox
            damage = D_LEG
            hit_guard = G_BOTTOM
        else:
            return
        
        if defender.guard == hit_guard:
            sword.has_hit = True
            print("BLOCK!")
            return
        
        old_health = defender.health
        defender.take_damage(damage)

        if defender.health != old_health:
            sword.has_hit = True
            if attacker.facing == DIRECTION_E:
                defender.rect.x += KNOCKBACK
            else:
                defender.rect.x -= KNOCKBACK
            if hit_guard == G_BOTTOM:
                defender.speed = SPEED_MIN
                defender.backward_speed = max(1, SPEED_MIN - 1)
            print(f"Enemy HP: {self.enemy.health}")

    def draw(self):
        self.screen.fill(BG_COLOR)

        if self.state == MENU:
            self.menu.draw(self.screen, self.font)

        elif self.state == COMMANDS:
            self.commands.draw(
                self.screen,
                self.font
            )

        elif self.state == PLAYING:
            self.player.draw(self.screen)
            self.enemy.draw(self.screen)
            
            self.player.sword.draw(self.screen)
            self.enemy.sword.draw(self.screen)

            self.draw_hud()

        elif self.state == GAME_OVER:
            self.draw_game_over()
        
        pygame.display.flip()
    
    def reset_round(self):
        self.player.health = self.player.max_health
        self.enemy.health = self.enemy.max_health

        self.player.speed = self.player.base_speed
        self.player.backward_speed = self.player.base_backward_speed

        self.enemy.speed = self.enemy.base_speed
        self.enemy.backward_speed = self.enemy.base_backward_speed

        self.player.rect.topleft = SPAWN_P
        self.enemy.rect.topleft = SPAWN_E

        self.player.update_hitboxes()
        self.enemy.update_hitboxes()

        self.player.invincible = False
        self.enemy.invincible = False

        self.player.guard = G_MID
        self.enemy.guard = G_MID

        self.player.sword.attacking = False
        self.enemy.sword.attacking = False

        self.player.sword.attack_offset = ATTACK_OFFSET
        self.enemy.sword.attack_offset = ATTACK_OFFSET

    def check_round(self):
        if not self.enemy.is_alive():
            self.player_score += 1
            print(f"Player {self.player_score} x {self.enemy_score} Enemy")
            
            if self.player_score == ROUNDS_TO_WIN:
                # print("You Win!") # Old way
                self.winner = "PLAYER"
                self.state = GAME_OVER
                return
            
            if not self.round_ending:
                self.round_ending = True
                self.round_end_time = pygame.time.get_ticks()

        elif not self.player.is_alive():
            self.enemy_score += 1
            print(f"Player {self.player_score} x {self.enemy_score} Enemy")
            
            if self.enemy_score == ROUNDS_TO_WIN:
                # print("Nice Try") # Old way
                self.winner = "ENEMY"
                self.state = GAME_OVER
                return
            
            self.round_ending = True
            self.round_end_time = pygame.time.get_ticks()

    def draw_hud(self):

        # Player Life Bar
        pygame.draw.rect(self.screen, C_DARK_RED, (*BAR_PLAYER_POS, BAR_WIDTH, BAR_HEIGHT))
        pygame.draw.rect(
            self.screen, C_GREEN,
            (*BAR_PLAYER_POS, BAR_WIDTH * self.player.health / self.player.max_health, BAR_HEIGHT)
        )

        # Enemy Life Bar
        pygame.draw.rect(self.screen, C_DARK_RED, (*BAR_ENEMY_POS, BAR_WIDTH, BAR_HEIGHT))
        pygame.draw.rect(
            self.screen, C_GREEN,
            (*BAR_ENEMY_POS, BAR_WIDTH * self.enemy.health / self.enemy.max_health, BAR_HEIGHT)
        )
        score = self.font.render(
            f"{self.player_score}  x  {self.enemy_score}",
            True,
            C_WHITE
        )

        self.screen.blit(
            score,
            (
                WIN_WIDTH // 2 - score.get_width() // 2,
                HUD_SCORE_Y
            )
        )

    def draw_game_over(self):

        # Old draw_game_over
        # ------------------------------
        # text = self.font.render(
        #     f"{self.winner} WINS!", True, C_WHITE
        # )

        # restart_text = self.font.render(
        #     "Press ENTER to return to menu",
        #     True,
        #     C_WHITE
        # )
        
        # self.screen.blit(
        #     restart_text,
        #     (WIN_WIDTH // 2 - text.get_width() // 2, WIN_HEIGHT // 2 + 50)
        # )
        # Winner Text
        text = self.font.render(f"{self.winner} WINS!", True, C_WHITE)
        text_rect = text.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2))
        self.screen.blit(text, text_rect)

        restart_text = self.font.render("Press ENTER to return to menu", True, C_WHITE)
        restart_rect = restart_text.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2 + 50))
        self.screen.blit(restart_text, restart_rect)