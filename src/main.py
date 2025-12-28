import sys
import pygame
import random
from pygame.math import Vector2

from snake import Snake
from fruit import Fruit


# Contains all shared data between classes
class Configs:
    # Window settings
    cell_size = 40
    cell_number = 20

    # Paths to assets
    sprites_path = "assets/sprites/"
    assets_path = "assets/"

    # Pygame configs
    pygame.mixer.pre_init(44100, -16, 2, 512)
    pygame.init()

    screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
    snake_icon = pygame.image.load(assets_path + "snake_icon.png")
    pygame.display.set_icon(snake_icon)
    pygame.display.set_caption("Python by Lando | WIP")
    clock = pygame.time.Clock()
    apple = pygame.image.load(sprites_path + "apple.png").convert_alpha()
    game_font = pygame.font.Font(None, 25)


class Main:
    def __init__(self, configs):
        self.configs = configs

        self.snake = Snake(configs)
        self.fruit = Fruit(configs)

    def update(self):
        self.snake.move_snake()
        self.check_collisions()
        self.check_fail()

    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()

    def check_collisions(self):
        if self.fruit.pos == self.snake.body[0]:
            self.snake.play_crunch_sound()
            self.fruit.randomize()
            self.snake.add_block()

        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()

    def check_fail(self):
        if (
            not 0 <= self.snake.body[0].x < self.configs.cell_number
            or not 0 <= self.snake.body[0].y < self.configs.cell_number
        ):
            self.game_over()
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def draw_grass(self):
        grass_color = pygame.Color(167, 99, 61)
        for row in range(self.configs.cell_number):
            if row % 2 == 0:
                for col in range(self.configs.cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(
                            col * self.configs.cell_size,
                            row * self.configs.cell_size,
                            self.configs.cell_size,
                            self.configs.cell_size,
                        )
                        pygame.draw.rect(self.configs.screen, grass_color, grass_rect)
            else:
                for col in range(self.configs.cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(
                            col * self.configs.cell_size,
                            row * self.configs.cell_size,
                            self.configs.cell_size,
                            self.configs.cell_size,
                        )
                        pygame.draw.rect(self.configs.screen, grass_color, grass_rect)

    def game_over(self):
        self.snake.reset()

    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = self.configs.game_font.render(score_text, True, (56, 74, 12))
        score_x = int(
            self.configs.cell_size * self.configs.cell_number
            - ((self.configs.cell_size * self.configs.cell_number) / 2)
        )
        score_y = int(self.configs.cell_size * self.configs.cell_number - 15)
        score_rect = score_surface.get_rect(midbottom=(score_x, score_y))
        apple_rect = self.configs.apple.get_rect(
            midright=(score_rect.left, score_rect.centery)
        )
        bg_rect = pygame.Rect(
            apple_rect.left,
            apple_rect.top,
            apple_rect.width + score_rect.width + 10,
            apple_rect.height,
        )

        pygame.draw.rect(self.configs.screen, pygame.Color(187, 199, 61), bg_rect)
        self.configs.screen.blit(score_surface, score_rect)
        self.configs.screen.blit(self.configs.apple, apple_rect)
        pygame.draw.rect(self.configs.screen, (0, 0, 0), bg_rect, 2)


SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = Main(Configs)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == SCREEN_UPDATE:
            main_game.update()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)

    Configs.screen.fill(pygame.Color((164, 122, 61)))
    main_game.draw_elements()
    pygame.display.update()
    Configs.clock.tick(60)
