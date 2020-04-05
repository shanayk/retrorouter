"""
Module that is the repo for Router and Client classes.
"""

import pygame
import constants


class Client(pygame.sprite.Sprite):
    """
    Class describes the client, for now we are using a circle that fills over time to depict it.
    """
    def __init__(self,font):
        super().__init__()
        # Create the surface, give dimensions and set it to be transparent
        self.font = font

    def update(self,counter):
        self.image = pygame.Surface([constants.client_size, constants.client_size])
        pygame.draw.circle(self.image, constants.GREEN, (constants.client_size // 2,constants.client_size // 2), constants.client_size // 2, counter)
        self.rect = self.image.get_rect()
        if counter >= constants.client_size // 4:
            self.kill()
            pass




class Router(pygame.sprite.Sprite):
    """
    This class represents the central Router, we will only create a single object for this particular class. This will be our equivalent of the missile command main silo. For now there will
    be a place holder image before we can make a better one
    """
    def __init__(self):
        """ Constructor. Pass in the size of the initial channel """
        super().__init__()
        self.image = pygame.Surface([constants.router_width,constants.router_height])
        self.image.fill(constants.GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = ((constants.width // 2) - (constants.router_width // 2))
        self.rect.y = ((constants.height // 2) -(constants.router_height // 2))

    def update(self,counter):
        pass
