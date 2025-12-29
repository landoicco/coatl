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
    pygame.display.set_caption("Coatl. | Classic snake game")
    clock = pygame.time.Clock()
    apple = pygame.image.load(sprites_path + "apple.png").convert_alpha()


class Font:
    GAME = pygame.font.Font(Configs.assets_path + "AtkinsonHyperlegibleMono.ttf", 30)
    SUBHEADER = pygame.font.Font(
        Configs.assets_path + "AtkinsonHyperlegibleMono.ttf", 15
    )
    HEADER = pygame.font.Font(Configs.assets_path + "AtkinsonHyperlegibleMono.ttf", 50)
    HEADER.set_bold(True)


class Color:
    # Splash
    BACKGROUND = (168, 184, 160)
    PRIMARY = (167, 109, 93)
    SECONDARY = (44, 44, 44)

    # Wall
    WALL_PRIMARY = (219, 217, 183)
    WALL_SECONDARY = (245, 232, 216)
