import sys
import pygame
from settings import Settings
from ship import Ship

class auslander:
    # entry pouint to manage  the games assets and behaviour
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Auslander Krieg')

        self.bg_color = (230, 230, 230)
        self.ship = Ship(self)


    def run_game(self):
        #THe games Main loop
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)
        
    def _check_events(self):
        """Responds to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    sys.exit()
            #let's redraw the screen  with each pass of the loop
    
    def _update_screen(self):
        """Update the images on the screen and flip on the new screen"""
        
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            #show the most recent drawing
            pygame.display.flip()
            
    

if __name__ == '__main__':
    #initiate a game instance and run the game
    ai = auslander()
    ai.run_game()

               