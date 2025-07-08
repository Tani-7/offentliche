import pygame

class Ship:
    # Manages the ship.
    def __init__(self, ai_game):
        # Start the ship.
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load and scale the ship image to ~1.5cm (≈ 57x57 pixels).
        original_image = pygame.image.load('images/millenium_falcon.bmp')
        self.image = pygame.transform.smoothscale(original_image, (120, 120))
        self.rect = self.image.get_rect()

        # Set the initial position of the ship.
        self.rect.midbottom = self.screen_rect.midbottom

        #Adjusting the speed to use float values 
        self.x  = float(self.rect.x)

        #Allowing continuous movement on keypress THE FLAGS
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """updating the millenium's position based on the movement flag"""
        #Modifying the ship's x-value, not affecting the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        #updating the Rect from self.x
        self.rect.x = self.x


    def blitme(self):
        # Draw the ship at its current location.
        self.screen.blit(self.image, self.rect)
