import pygame.font

from pygame.sprite import Group

from ship import Ship

class Scoreboard:
    def __init__(self,ai_game):
        #initialize scorekeeping attributes
        self.ai_game=ai_game
        self.screen=ai_game.screen
        self.screen_rect=ai_game.screen.get_rect()
        self.settings=ai_game.settings
        self.stats=ai_game.stats
        
        #font settings for scoring information
        self.text_color=(30,30,30)
        self.font=pygame.font.SysFont(None,45)
        
        #prepare the initial score image
        self.prep_score()
        #prepare high score image
        self.prep_high_score()
        #check high score
        self.check_high_score()
        #prepare level 
        self.prep_level()
        #prepare ships
        self.prep_ships()
        
    
    def prep_score(self):
        rounded_score= round(self.stats.score,-1)
        #turn score into a rendered image
        score_str=f"{rounded_score:,}"
        self.score_image=self.font.render(score_str,True,self.text_color,self.settings.bg_color)
        
        #display the score at top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 10
        self.score_rect.top = 10
            
    def prep_high_score(self):
        #turn high score into rendered image
        high_score=round(self.stats.high_score , -1)
        high_score_str=f"{high_score:,}"
        self.high_score_image=self.font.render(high_score_str,True,self.text_color,self.settings.bg_color)
        
        #center the highscore at the top of the screen
        self.high_score_rect=self.high_score_image.get_rect()
        self.high_score_rect.centerx= self.screen_rect.centerx - 30        
        self.high_score_rect.top=10
        
    def check_high_score(self):
        #check to see if there is a new high score
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
    
    def prep_level(self):
        #turn level into rendered image
        
        level_str='LEVEL '+str(self.stats.level)
        self.level_image = self.font.render(level_str,True,self.text_color,self.settings.bg_color)
        
        #left top at top of screen
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right - 10
        self.level_rect.top = 40
        
    def prep_ships(self):
        #show how many ships are left
        self.ships = Group()
        for ship_number in range(self.stats.ship_left):
           ship = Ship(self.ai_game)
           ship.rect.x = 10 + ship_number * ship.rect.width
           ship.rect.y = 10
           self.ships.add(ship) 
                    
    def show_score(self):
        #draw scores and levels to screen
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        self.ships.draw(self.screen)