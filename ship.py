import pygame

class Ship:
    #class to manage ship
    def __init__(self , ai_game):
        #initialize the ship and set its starting position.
        self.settings=ai_game.settings
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        #load the ship image and its rect
        self.image = pygame.image.load('Alien-invasion\images\spaceship.bmp')
        self.rect = self.image.get_rect()
        
        #start each ship at bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        
        #store a float for ship's exact horizontal position
        self.x=float(self.rect.x)
        
        self.moving_right = False           #movement flag for right key
        self.moving_left = False            #movement flaf for left key
       
        
    def update(self):
        #change the ship's position based on moving_flag
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        #change ship's position based on moving_left
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        #update rect object from self.x
        self.rect.x=self.x
    
    def centre_ship(self):
        #centre the ship on the screen
        self.rect.midbottom = self.screen_rect.midbottom
        self.x=float(self.rect.x)
    
    def blitme(self):
        #draw ship at current location
        self.screen.blit(self.image,self.rect)