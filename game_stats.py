class GameStats:
    #Track statistics for alien collisons
    
    def __init__(self,ai_game):
        #initialize statistics 
        self.settings = ai_game.settings
        self.reset_stats()
        #high score should never be reset
        self.high_score=0
        self.level=0
        
    def reset_stats(self):
        #initialize statistics that can change during the game 
        self.level=1
        self.ship_left = self.settings.ship_limit
        self.score=0