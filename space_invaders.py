import sys 
import pygame

from settings import Settings
from ship import Ship

class SpaceInvaders: 

    """overall class to manage the game assets and behaviour"""

    def __init__(self): 
        """initialize the game and create game resources"""
        pygame.init()

        self.settings = Settings()
        # set screen dimensions and caption
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Space Invaders")

        self.ship = Ship(self)

   
    # module to run the game 

    def run_game(self): 
        """Start the main loop for the game"""
        while True: 
            # take in keyboar and moouse events 
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    sys.exit()

            # redraw the screen during each pass through the loop 
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
    
            # make most recently drawn screen visible 
            pygame.display.flip()
    

# running the code 

if __name__ == '__main__': 
    # make game instance and run it 
    ai = SpaceInvaders()
    ai.run_game()
        