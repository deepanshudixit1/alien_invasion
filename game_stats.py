class GameStats:
    #Track statistics for alien collisons
    
    def __init__(self,ai_game):
        #initialize statistics 
        self.settings = ai_game.settings
        self.reset_status()
        
    def reset_status(self):
        #initialize statistics that can change during the game 
        self.ship_left = self.settings.ship_limit