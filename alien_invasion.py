import sys

import pygame

from setting import Settings

from ship import Ship

from bullet import Bullet

class AlienInvasion:
    #Overall calss to manage game assets and behavior.
    def __init__(self):
        #Initialize the game,create game resources
        pygame.init()
        
        self.clock=pygame.time.Clock()
        self.settings=Settings()
        
        self.screen=pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        
        self.settings.screen_width=self.screen.get_rect().width
        self.settings.screen_height=self.screen.get_rect().height
        
        pygame.display.set_caption("Alien Invasion")
        #setting background color
        self.bg_color=(200,200,200)
        self.ship=Ship(self)
        
        self.bullets=pygame.sprite.Group()
        
    
    def run_game(self):
        #Start the main loop of the game 
        while True:
            #watch for keyboard and mouse events
            self.checkevents()
            #update ship's position
            self.ship.update()
            #update bullets' groups' positions
            self.bullets.update()
            #get rid of bullets that have disappeared
            self._update_bullets()
            # Redraw the screen during each pass through the loop.
            self.update_screen()
            #Make most recent drawn screen visible
            pygame.display.flip()
            #making the pygame clock run at 60 times per second
            self.clock.tick(60)
            
    def checkevents(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self.check_keydown_events(event)
                
                elif event.type == pygame.KEYUP:
                    self.check_keyup_events(event)
                
                elif event.type == pygame.K_q:
                    sys.exit()
                    
    
    #respond to keypresses
    def check_keydown_events(self,event):
        #check for right arrow key to be pressed down
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right=True
        #check for left arrow key to be pressed down
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left=True    
        #check for space to be pressed down and fire bullets 
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()                    
    
    #respond to key releases                
    def check_keyup_events(self,event):
        #check if right arrow key is released and stop moving ship by setting flag as false
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right=False
        #check if left arrow key is released and stop moving ship by setting flag as false
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left=False
            
    def _fire_bullet(self):
        #crete new bullet and add it to the screen if number of bullets are less than or equal to allowed number of bullets
        if(len(self.bullets)<self.settings.bullet_allowed):
            new_bullet=Bullet(self)
            self.bullets.add(new_bullet)     
            
    def _update_bullets(self):
        #get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
                if bullet.rect.bottom<=0:
                    self.bullets.remove(bullet)       
        
    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullets()
        self.ship.blitme()


            
if __name__=='__main__':
    #make game instance and run game.
    ai=AlienInvasion()
    ai.run_game()
    
        