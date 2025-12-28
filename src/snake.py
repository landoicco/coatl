import pygame
from pygame.math import Vector2


class Snake:
    def __init__(self, configs):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)
        self.new_block = False
        self.configs = configs

        self.head_up = pygame.image.load(
            self.configs.sprites_path + "head_up.png"
        ).convert_alpha()
        self.head_down = pygame.image.load(
            self.configs.sprites_path + "head_down.png"
        ).convert_alpha()
        self.head_right = pygame.image.load(
            self.configs.sprites_path + "head_right.png"
        ).convert_alpha()
        self.head_left = pygame.image.load(
            self.configs.sprites_path + "head_left.png"
        ).convert_alpha()

        self.tail_up = pygame.image.load(
            self.configs.sprites_path + "tail_up.png"
        ).convert_alpha()
        self.tail_down = pygame.image.load(
            self.configs.sprites_path + "tail_down.png"
        ).convert_alpha()
        self.tail_right = pygame.image.load(
            self.configs.sprites_path + "tail_right.png"
        ).convert_alpha()
        self.tail_left = pygame.image.load(
            self.configs.sprites_path + "tail_left.png"
        ).convert_alpha()

        self.body_vertical = pygame.image.load(
            self.configs.sprites_path + "body_vertical.png"
        ).convert_alpha()
        self.body_horizontal = pygame.image.load(
            self.configs.sprites_path + "body_horizontal.png"
        ).convert_alpha()

        self.body_tr = pygame.image.load(
            self.configs.sprites_path + "body_topright.png"
        ).convert_alpha()
        self.body_tl = pygame.image.load(
            self.configs.sprites_path + "body_topleft.png"
        ).convert_alpha()
        self.body_br = pygame.image.load(
            self.configs.sprites_path + "body_bottomright.png"
        ).convert_alpha()
        self.body_bl = pygame.image.load(
            self.configs.sprites_path + "body_bottomleft.png"
        ).convert_alpha()

        self.head = self.head_up
        self.tail = self.tail_up
        self.body_fragment = self.body_vertical
        self.crunch_sound = pygame.mixer.Sound(
            self.configs.assets_path + "apple_bite.ogg"
        )

    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()

        for index, block in enumerate(self.body):
            block_rect = pygame.Rect(
                int(block.x * self.configs.cell_size),
                int(block.y * self.configs.cell_size),
                self.configs.cell_size,
                self.configs.cell_size,
            )
            if index == 0:
                self.configs.screen.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                self.configs.screen.blit(self.tail, block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    self.configs.screen.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    self.configs.screen.blit(self.body_horizontal, block_rect)
                else:
                    if (
                        previous_block.x == -1
                        and next_block.y == -1
                        or previous_block.y == -1
                        and next_block.x == -1
                    ):
                        self.configs.screen.blit(self.body_tl, block_rect)
                    elif (
                        previous_block.x == -1
                        and next_block.y == 1
                        or previous_block.y == 1
                        and next_block.x == -1
                    ):
                        self.configs.screen.blit(self.body_bl, block_rect)
                    elif (
                        previous_block.x == 1
                        and next_block.y == -1
                        or previous_block.y == -1
                        and next_block.x == 1
                    ):
                        self.configs.screen.blit(self.body_tr, block_rect)
                    elif (
                        previous_block.x == 1
                        and next_block.y == 1
                        or previous_block.y == 1
                        and next_block.x == 1
                    ):
                        self.configs.screen.blit(self.body_br, block_rect)

    def update_tail_graphics(self):
        body_length = len(self.body)
        tail_relation = self.body[body_length - 1] - self.body[body_length - 2]
        if tail_relation == Vector2(1, 0):
            self.tail = self.tail_right
        elif tail_relation == Vector2(-1, 0):
            self.tail = self.tail_left
        elif tail_relation == Vector2(0, 1):
            self.tail = self.tail_down
        elif tail_relation == Vector2(0, -1):
            self.tail = self.tail_up

    def move_snake(self):
        body_copy = self.body[:-1]
        if self.new_block:
            self.new_block = False
            body_copy = self.body[:]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(-1, 0):
            self.head = self.head_right
        elif head_relation == Vector2(1, 0):
            self.head = self.head_left
        elif head_relation == Vector2(0, -1):
            self.head = self.head_down
        elif head_relation == Vector2(0, 1):
            self.head = self.head_up

    def play_crunch_sound(self):
        self.crunch_sound.play()

    def reset(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)
