class Settings:
    #class to store all settings for alien invasion
    def __init__(self):
        #initialize the game's static settings
        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        self.ship_speed = 1.5
        self.ship_limit=1
        
        
        #bullet settings
        self.bullet_speed = 2.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_allowed = 3
        
        
        #Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 100
        #fleet_direction of 1 represent right; -1 represts left
        self.fleet_direction = 1
        
        #How quickly game speeds up
        self.speed_up_scale=1.1
        
        #how quickly alien points speed up
        self.score_scale=1.5
        self.initialize_dynamic_settings()
        
        #scoring settings
        self.alien_points=50
        
    def initialize_dynamic_settings(self):
        self.alien_speed = 1.0
        self.ship_speed = 1.5
        self.bullet_speed = 2.5
        
        #fleet direction of 1 represents right and -1 represents left 
        self.fleet_direction = 1
        
    def increase_speed(self):
        #increase alien ship and bullet speed and point values
        self.alien_speed *= self.speed_up_scale
        self.ship_speed *= self.speed_up_scale
        self.bullet_speed *= self.speed_up_scale 
        
        self.alien_points = int(self.alien_points*self.score_scale)
        
        
        