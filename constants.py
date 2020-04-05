import pygame, sys, os




WHITE =     (255, 255, 255)
BLUE =      (  0,   0, 255)
GREEN =     (  0, 255,   0)
RED =       (255,   0,   0)
BLACK = (  0,   0,  0)
screen_background = BLACK
width = 1000
height = 800
channel_noise_bar_width = 5
router_height = height // 20
router_width = width // 20
client_size = 40


class Title(pygame.sprite.Sprite):
        """
        This Class contains the centered title for the game,
        this is declared in the constants module since we want to use this in all states (when we implement a state machine)
        """
        def __init__(self,title_font):
            super().__init__()
            self.font = title_font
            self.image = self.font.render("RetroRouter", True , GREEN)
            self.rect = self.image.get_rect()
            self.rect.x = (width // 2) - (self.image.get_width() // 2)
            self.rect.y  = 0
