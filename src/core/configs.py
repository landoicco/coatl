import pygame


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
    game_font = pygame.font.Font(assets_path + "AtkinsonHyperlegibleMono.ttf", 25)
