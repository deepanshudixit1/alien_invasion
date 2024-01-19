class Settings:
    #class to store all settings for alien invasion
    def __init__(self):
        #initialize the game settings
        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        self.ship_speed = 1.5
        self.ship_limit=3
        
        
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
        