import pygame, sys, os, time
import constants
import base_game


def main():

    pygame.init()
    clock = pygame.time.Clock()
    # Create our objects and set the data
    font = pygame.font.Font(os.path.join("text",'Inconsolata-Regular.ttf'), 16)
    title_font = pygame.font.Font(os.path.join("text",'Inconsolata-Regular.ttf'), 32)
    screen = pygame.display.set_mode((constants.width,constants.height))
    pygame.display.set_caption("RetroRouter")
    done = False
    # Create an instance of the Game class
    game = base_game.BaseGame(11,font,title_font)

    # Main game loop
    while not done:

        # Process events (keystrokes, mouse clicks, etc)
        done = game.process_events()

        # Update object positions, check for collisions
        game.run_logic()

        # Draw the current frame
        game.display_frame(screen)

        # Pause for the next frame
        clock.tick(60)

    # Close window and exit
    pygame.quit()


if __name__ == '__main__':
    main()
