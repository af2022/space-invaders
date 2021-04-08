import pygame 

class Ship: 

    """A class to model a ship and its attributes and behaviours"""
    def __init__(self, ai_game): 
        """initialise the ship and set its starting position"""
        self.screen = ai_game.screen 
        self.screen_rect = ai_game.screen.get_rect()

        # load the ship image and get its rect. 
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()

        # start each ship at bottom centre of the screen 
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self): 
        """draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

        