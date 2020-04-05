"""
Module with the Base Game Class, thinking of implementing a State Machine, once we have that in place this will make more sense.
"""


import pygame
import constants
import calculations
import game_characters
import channel
from pygame.locals import *



class BaseGame(object):
    """ This class represents an instance of the base game. If we need to
        reset the base game we'd just need to create a new instance of this
        class. """

    def __init__(self,channel_num,font,title_font):
        """ Constructor. Create all our attributes and initialize
        the game. """

        self.game_over = False
        # Create sprite lists
        self.channel_select_list = pygame.sprite.Group()
        self.channel_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()
        self.title_sprite = pygame.sprite.Group()
        self.bandwidth = int((constants.width/(channel_num-1)))
        self.counter = 5
        title = constants.Title(title_font)
        #router = game_characters.Router()
        client = game_characters.Client(font)
        self.all_sprites_list.add(router)
        self.all_sprites_list.add(client)
        self.title_sprite.add(title)

        for i in range(channel_num):
            channel_name = channel.Channel_Name(i+1,self.bandwidth*i,self.bandwidth)
            channel_select = channel.Channel_Select(i+1,self.bandwidth*i,self.bandwidth,font)
            self.channel_list.add(channel_name)
            self.channel_select_list.add(channel_select)
            self.all_sprites_list.add(channel_name)
            self.all_sprites_list.add(channel_select)





    def process_events(self):
        """ Process all of the events. Return a "True" if we need
        to close the window. """

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == KEYDOWN:
                if (event.key == pygame.K_LEFT):
                    self.counter = calculations.button_click(self.counter,-1)
                elif (event.key == pygame.K_RIGHT):
                    self.counter = calculations.button_click(self.counter,1)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x,y = event.pos
                    for sprites in self.all_sprites_list:
                        if sprites.rect.collidepoint(x,y):
                            print (sprites)








        return False

    def run_logic(self):
        """
        This method is run each time through the frame.
        """
        if not self.game_over:
            # Move all the sprites

            self.all_sprites_list.update(self.counter)


    def display_frame(self, screen):
        """ Display everything to the screen for the game. """
        screen.fill(constants.screen_background)

        if self.game_over:
            text = font.render("Game Over", True, constants.GREEN)
            center_x = (constants.width // 2) - (text.get_width() // 2)
            center_y = (constants.height // 2) - (text.get_height() // 2)
            screen.blit(text, [center_x, center_y])

        if not self.game_over:

            self.all_sprites_list.draw(screen)
            self.title_sprite.draw(screen)

        pygame.display.flip()
