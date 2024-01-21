import sys

import pygame

from time import sleep

from setting import Settings

from ship import Ship

from bullet import Bullet

from alien import Alien

from game_stats import GameStats

from button import Button

from scoreboard import Scoreboard

class AlienInvasion:
    #Overall class to manage game assets and behavior.
    def __init__(self):
        
        #Initialize the game,create game resources
        pygame.init()
        
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        
        pygame.display.set_caption("Alien Invasion")
        #setting background color
        self.bg_color = (200,200,200)
        self.ship = Ship(self)
        
        self.bullets = pygame.sprite.Group()
        
        self.aliens = pygame.sprite.Group()
        
        self._create_fleet()
        
        #make instance of gamestats and create scoreboad
        self.stats = GameStats(self)
        self.sb=Scoreboard(self)
        
        #Start Alien Invasion in an inactive state
        self.game_active = False
        
        #make play button
        self.play_button = Button(self,"PLAY")
        
        
    
    def run_game(self):
        #Start the main loop of the game 
        while True:
            #watch for keyboard and mouse events
            self.checkevents()
            
            if self.game_active:
                #update ship's position
                self.ship.update()
                #get rid of bullets that have disappeared
                self._update_bullets()
                #updating positions of aliens
                self._update_aliens()
            
            # Redraw the screen during each pass through the loop.
            self.update_screen()
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
                
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_play_button(mouse_pos)
                    
    
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
        elif event.key == pygame.K_q:
            sys.exit()                 
    
    #respond to key releases                
    def check_keyup_events(self,event):
        #check if right arrow key is released and stop moving ship by setting flag as false
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right=False
        #check if left arrow key is released and stop moving ship by setting flag as false
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left=False
            
    def _fire_bullet(self):
        #create new bullet and add it to the screen if number of bullets are less than or equal to allowed number of bullets
        if(len(self.bullets)<self.settings.bullet_allowed):
            new_bullet=Bullet(self)
            self.bullets.add(new_bullet)     
            
    def _update_bullets(self):
        self.bullets.update()
        #get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
                if bullet.rect.bottom<=0:
                    self.bullets.remove(bullet)  
                    
        #check for bullets that have hit aliens 
        #if so get rid of the bullet and aliens
        self._check_bullet_alien_collision()    
    
    def _create_fleet(self):
        #create fleet of aliens
        #make an alien and keep adding aliens until there is no room left
        #spacing between aliens is one alien width and one alien height
        alien=Alien(self)
        alien_width,alien_height=alien.rect.width,alien.rect.height
        
        current_x , current_y = alien_width , alien_height
        while current_y < (self.settings.screen_height - 3*alien_height):
            while current_x < (self.settings.screen_width - 2*alien_width):
                self._create_alien(current_x,current_y)
                current_x += 2*alien_width
            
            #Finished a row,reset x value,and increment y value
            current_x=alien_width
            current_y += 2*alien_height
    
    def _create_alien(self,x_position,y_position):
        #create alien and place it in the row
        new_alien = Alien(self)
        new_alien.x = x_position 
        new_alien.rect.x , new_alien.rect.y = x_position , y_position
        self.aliens.add(new_alien)
    
    def _update_aliens(self):
        #check if fleet is at the edge,then update positions
        self._check_fleet_edges()
        #update the positions of all aliens in the fleet.
        self.aliens.update()
        
        #check for alien ship collision
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            self.ship_hit()
            
        #checkfor alien hitting bottom
        self._check_alien_bottom()
        
    
    def _check_fleet_edges(self):
        #respond appropriately if any aliens have reached an edge
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
            
    def _change_fleet_direction(self):
        #drop the entire fleet and change the fleet's direction
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
    
    def _check_bullet_alien_collision(self):
        #remove any aliens and bullets that have colided
        collisions = pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)
        
        if collisions:
            #keeping score
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points *len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
        
        #destroy all bullets and create fleet
        if not self.aliens:
            self.settings.increase_speed()
            self.bullets.empty()
            self._create_fleet()
            
            #increase level
            self.stats.level += 1
            self.sb.prep_level()
    
    def _check_alien_bottom(self):
        #check if any aliens have reached at the botoom
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                #treat it same as ship got hit
                self.ship_hit()
                break
        
    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullets()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        
        #draw scoreboard on screen
        self.sb.show_score()
        
        #draw the play button if game is inactive
        if not self.game_active:
            self.play_button.draw_button()
        
        #Make most recent drawn screen visible
        pygame.display.flip()
                
    def ship_hit(self):
        #respond to ship being hit by an alien
        if self.stats.ship_left > 1:
            #decrement ship left and update scoreboard
            self.stats.ship_left -= 1
            self.sb.prep_ships()
            
            #get rid of any remaining bullets and aliens
            self.bullets.empty()
            self.aliens.empty()
            
            #create new fleet and new ship 
            self._create_fleet()
            self.ship.centre_ship()
            
            #pause
            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)
            

    def _check_play_button(self,mouse_pos):
        #start a new game when player clicks play
        mouse_clicked=self.play_button.rect.collidepoint(mouse_pos)

        if mouse_clicked and not self.game_active:
            #reset the game settings
            self.settings.initialize_dynamic_settings()    
            # Reset the game statistics
            self.stats.reset_stats()
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            self.game_active=True
            
            #get rid of all remaining bullets and aliens
            self.aliens.empty()
            self.bullets.empty()
            
            #create new fleet and center the ship
            self._create_fleet()
            self.ship.centre_ship()
            
            #hide the cursor
            pygame.mouse.set_visible(False)         
            
if __name__=='__main__':
    print("First Prototype Done")
    #make game instance and run game.
    ai=AlienInvasion()
    ai.run_game()
    
        