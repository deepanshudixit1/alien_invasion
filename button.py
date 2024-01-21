import pygame.font

class Button:
    #initialize button attributes
    def __init__(self,ai_game,msg):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        #Set dimensions and properties of button
        self.width , self.height = 200 , 50
        self.button_color=(0,135,0)
        self.text_color=(255,255,255)
        self.font=pygame.font.SysFont(None,48,True)
        
        #build the button's rect and centre it
        self.rect=pygame.Rect(0,0,self.width,self.height)
        self.rect.center=self.screen_rect.center
        
        #The button message needs to be prepared only once
        self._prep_msg(msg)
        
    def _prep_msg(self,msg):
        #turn msg into a rendered button and centre the text on button
        self._msg_image = self.font.render(msg,True,self.text_color,self.button_color)
        self._msg_image_rect = self._msg_image.get_rect()
        self._msg_image_rect.center = self.rect.center
        
    def draw_button(self):
        #Draw blank button and then draw message
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self._msg_image,self._msg_image_rect)