import sys

import pygame

from .configs import Color, Configs, Font


#####################
### Splash screen ###
#####################
def show_splash_screen(score=None):
    text_data = [
        # Format (name, font_settings, color, y_position)
        ("Coatl.", Font.HEADER, Color.PRIMARY, 100),
        ("A game by", Font.SUBHEADER, Color.SECONDARY, 170),
        ("Lando Icaza C.", Font.SUBHEADER, Color.SECONDARY, 190),
    ]
    if score is None:
        prompt = "Press any key to start"
    else:
        text_data.append((f"Game over! Score: {score}", Font.GAME, Color.PRIMARY, 350))
        prompt = "Press any key to play again"
    text_data.append((prompt, Font.GAME, Color.SECONDARY, 500))

    # Render text once, horizontally centered
    center_x = Configs.screen.get_width() // 2
    rendered = []
    for text, font, color, y in text_data:
        surf = font.render(text, True, color)
        rendered.append((surf, surf.get_rect(midtop=(center_x, y))))

    # Drop keys pressed before the splash appeared so they don't dismiss it instantly
    pygame.event.clear(pygame.KEYDOWN)

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Any key press exits this loop and starts the game
            if event.type == pygame.KEYDOWN:
                waiting = False

        Configs.screen.fill(Color.BACKGROUND)
        for surf, rect in rendered:
            Configs.screen.blit(surf, rect)

        pygame.display.flip()
        Configs.clock.tick(60)
