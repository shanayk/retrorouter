"""
Module that is the repo for all channel related animations
"""

import pygame
import constants
import random



class Channel_Select(pygame.sprite.Sprite):
        """
        This class represents the channel name and selection criteria, we use this to handle all channel selection and channel selection name animatons
        It derives from the "Sprite" class in Pygame
        """
        def __init__(self,channel,x,width,font):
            """ Constructor. Pass in the size of the initial channel """
            pygame.sprite.Sprite.__init__(self)
            self.font = font
            self.x = x
            self.channel = channel
            self.color = constants.GREEN
            self.text = ("Channel {}".format(self.channel))
            self.pos = (self.x,(19*constants.height) // 20)

        def color_selector(self):
            if self.counter == self.channel:
                return constants.WHITE
            else:
                return constants.GREEN

        def update(self,counter):
            self.counter = counter
            self.image = self.font.render(self.text, True , self.color_selector())
            self.rect = self.image.get_rect()
            self.rect.x, self.rect.y = self.pos




class Channel_Name(pygame.sprite.Sprite):
        """
        This class represents each channel, this is to simulate the per channel spectral width and energy.
        Takes channel,x,width as input parameters and
        It derives from the "Sprite" class in Pygame
        """
        def __init__(self,channel,x,width):
            """ Constructor. Pass in the size of the initial channel """
            super().__init__()
            self.image = pygame.Surface([width,constants.channel_noise_bar_width])
            self.image.fill(constants.GREEN)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = (18*constants.height) // 20
            self.y_const = self.rect.y
            self.channel = channel

        def update(self,counter):
            """ Called each frame. """
            if counter == self.channel:
                self.added_noise = constants.height // 10
            elif (counter == self.channel - 1) or (counter == self.channel + 1):
                self.added_noise = constants.height // 40
            else:
                self.added_noise = 0
            self.noise_fluctuation = random.randint(0,int(constants.height/200))
            self.rect.y = self.y_const - self.noise_fluctuation - self.added_noise
