import pygame, sys, os, time
import constants
import base_game


def main():

    pygame.init()
    clock = pygame.time.Clock()
    # initialize Pygame Fonts. Display and sets game window caption
    font = pygame.font.Font(os.path.join("text",'Inconsolata-Regular.ttf'), 16)
    title_font = pygame.font.Font(os.path.join("text",'Inconsolata-Regular.ttf'), 32)
    screen = pygame.display.set_mode((constants.width,constants.height))
    pygame.display.set_caption("RetroRouter")
    done = False
    # Create an instance of the Game class
    game = base_game.BaseGame(11,font,title_font)

    # Main game loop
    while not done:
        done = game.process_events()
        game.run_logic()
        game.display_frame(screen)
        clock.tick(60)
    pygame.quit()


if __name__ == '__main__':
    main()
