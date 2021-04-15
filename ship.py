import pygame 

class Ship: 

    """A class to model a ship and its attributes and behaviours"""
    def __init__(self, ai_game): 
        """initialise the ship and set its starting position"""
        self.screen = ai_game.screen 
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # load the ship image and get its rect. 
        self.image = pygame.image.load('images/ship.bmp')
        
        self.rect = self.image.get_rect()

        # start each ship at bottom centre of the screen 
        self.rect.midbottom = self.screen_rect.midbottom

        self.background_image = pygame.image.load('images/background.png')

        self.background_rect = self.background_image.get_rect()

        # create a movement flag 
        self.moving_right = False 

        self.moving_left = False


        # store decimanl float for the ships horizontal position 
        self.x = float(self.rect.x)


        

    def blitme(self): 
        """draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def blit_background(self): 
        self.screen.blit(self.background_image, (0,0))

    def update(self): 
        """updaet the ships position based on movement flag""" 
        # no press should have precedence over the over so its an 
        # straight forward conditional check here no need to cycle through 
        # if and elif blocks - if right go right - if left go left thats all
        # updae the ships x value not its rect
        if self.moving_right and self.rect.right < self.screen_rect.right: 
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left >0: 
            self.x -= self.settings.ship_speed

        # update the srect object from self.x 
        self.rect.x = self.x