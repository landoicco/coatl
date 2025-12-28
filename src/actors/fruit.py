import pygame
import random
from pygame.math import Vector2


class Fruit:
    def __init__(self, configs):
        self.x = 0
        self.y = 0
        self.pos = 0

        self.configs = configs
        self.randomize()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(
            int(self.pos.x * self.configs.cell_size),
            int(self.pos.y * self.configs.cell_size),
            self.configs.cell_size,
            self.configs.cell_size,
        )
        self.configs.screen.blit(self.configs.apple, fruit_rect)

    def randomize(self):
        self.x = random.randint(0, self.configs.cell_number - 1)
        self.y = random.randint(0, self.configs.cell_number - 1)
        self.pos = Vector2(self.x, self.y)
