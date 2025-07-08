import pygame

class Ship:
    # Manages the ship.
    def __init__(self, ai_game):
        # Start the ship.
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load and scale the ship image to ~1.5cm (≈ 57x57 pixels).
        original_image = pygame.image.load('images/Marriete of 1915.bmp')
        self.image = pygame.transform.smoothscale(original_image, (256, 256))
        self.rect = self.image.get_rect()

        # Set the initial position of the ship.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        # Draw the ship at its current location.
        self.screen.blit(self.image, self.rect)
