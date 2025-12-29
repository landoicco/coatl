import sys
import pygame
import random
from pygame.math import Vector2

from core import *
from actors import *


#####################
### Splash screen ###
#####################
def show_splash_screen():
    text = Configs.game_font.render("Press Any Key to Start", True, (255, 255, 255))
    text_rect = text.get_rect(
        center=(Configs.screen.get_width() // 2, Configs.screen.get_height() // 2)
    )

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            # Any key press exits this loop and starts the game
            if event.type == pygame.KEYDOWN:
                waiting = False

        Configs.screen.fill((0, 0, 0))  # Background color
        Configs.screen.blit(text, text_rect)
        pygame.display.flip()


SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

# Init Game class
main_game = Game(Configs)


# Show at start
show_splash_screen()
################
## Game Loop ###
################
is_running = True
while is_running:
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

            # Adding... Splash screen
            if event.key == pygame.K_s:
                is_running = False
                show_splash_screen()

    Configs.screen.fill(pygame.Color((164, 122, 61)))
    main_game.draw_elements()
    pygame.display.update()
    Configs.clock.tick(60)
