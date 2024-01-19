import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    #class to represent single alien in fleet 
    def __init__(self,ai_game):
        #initialize the aliean and set its starting position
        super().__init__()
        self.screen=ai_game.screen
        self.settings=ai_game.settings
        
        #load the alien image and set its attribute
        self.image = pygame.image.load("Alien-invasion/images/alien.bmp")
        self.rect= self.image.get_rect()
        
        #start new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        #store the alien's exact horizontal position
        self.x = float(self.rect.x)
    
    def check_edges(self):
        #Return True if alien is at edge of screen
        screen_rect = self.screen.get_rect()
        return(self.rect.right >= screen_rect.right) or (self.rect.left <= 0)
        
    def update(self):
        #move the alien to the right or left   
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x