import sys
import pygame
from settings import Settings

class auslander:
    # entry pouint to manage  the games assets and behaviour
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Auslander krieg')

        self.bg_color = (230,230,230)

    def run_game(self):
        #THe games Main loop
        while true:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            #let's redraw the screen  with each pass of the loop
            self.screen.fill(self.bg_fabre)
            #show the most recent drawing
            pygame.display.flip()
            self.clock.tick(60)
            
            

if __name__ == '__main__':
    #initiate a game instance and run the game
    ai = auslander()
    ai.run_game()

               