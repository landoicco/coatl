import pygame
from .configs import Configs, Color


#####################
### Splash screen ###
#####################
def show_splash_screen():
    text_data = [
        # Format (name, font_settings, color, position)
        ("Coatl.", Configs.header_font, Color.PRIMARY, (300, 100)),
        ("Press any key to start", Configs.game_font, Color.SECONDARY, (190, 500)),
        ("A game by", Configs.subheader_font, Color.SECONDARY, (350, 170)),
        ("Lando Icaza C.", Configs.subheader_font, Color.SECONDARY, (330, 190)),
    ]

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            # Any key press exits this loop and starts the game
            if event.type == pygame.KEYDOWN:
                waiting = False

        Configs.screen.fill(Color.BACKGROUND)
        # Render text
        for text, font, color, position in text_data:
            surf = font.render(text, True, color)
            Configs.screen.blit(surf, position)

        pygame.display.flip()
