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
            self._check_events()
            # update the ships movements 
            self.ship.update() 
            # update the screen 
            self._update_screen()
           

    # these are helper methods with the underscore first 
    # they are meant to do work in a class but not be called as an instance
    def _check_events(self): 
        """respond to key presse and mouse events"""
        # every key press or action a user makes is regersted as an event 
        # each event is picked up by the pygame.event.get() method 
        # sepcify here what you want to check for.
        # every keypres is a KEYDOWN event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN: 
                self._check_keydown_events(event)
                
            # when key up is ifted 
            elif event.type == pygame.KEYUP: 
                # then make movement flag set to False 
                                # check for right key press 
                self._check_keyup_events(event)

    def _check_keydown_events(self,event): 
        """respond to keypresses"""
        if event.key == pygame.K_RIGHT: 
                    # move the ship one space to right 
            self.ship.moving_right = True

        elif event.key == pygame.K_LEFT: 
            self.ship.moving_left = True
        elif event.key == pygame.K_q: 
            sys.exit()


    def _check_keyup_events(self,event): 
        """respond to key up events""" 
        if event.key == pygame.K_RIGHT: 
                    # move the ship one space to right 
                    self.ship.moving_right = False

        elif event.key == pygame.K_LEFT: 
                    self.ship.moving_left = False

    def _update_screen(self): 
        """update the images of the screen and flip to the new screen"""
                    # redraw the screen during each pass through the loop 
        self.screen.fill(self.settings.bg_color)
        self.ship.blit_background()
        self.ship.blitme()

        # make most recently drawn screen visible 
        pygame.display.flip()
    

# running the code 

if __name__ == '__main__': 
    # make game instance and run it 
    ai = SpaceInvaders()
    ai.run_game()
        