import pygame

from pygame.locals import *

from random import choice, randint

# Let's set some defaults.
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
FONT_SIZE = 40

# I'm going to put my colors here.
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# All the letters that can appear!
ROW1 = "qwertyuiop[]"
ROW2 = "asdfghjkl;'"
ROW3 = "zxcvbnm,./"

LETTERS = ROW1 + ROW2 + ROW3

# We need to get PyGame ready to use some fonts.
pygame.font.init()
# We're setting our font to the default PyGame font.
FONT = pygame.font.Font(None, FONT_SIZE)

def draw_random(screen):
    ''' I want to draw a random letter on the screen,
        then return that letter so that Python knows what
        key the user should be hitting
    '''
    # Get the letter
    letter = choice(LETTERS)
    # Get a random location on the screen, but make sure that it
    # can't go off the screen
    x = randint(0, WINDOW_WIDTH - FONT_SIZE)
    y = randint(0, WINDOW_HEIGHT - FONT_SIZE)
    # Create the text that we want to put on the screen...
    text = FONT.render(" "+letter+" ", 1, BLACK, RED)
    # Toss the text on the screen!
    screen.blit(text, (x, y))
    # Return the letter.
    return letter

def main():
    ''' This is the main function for the program.
    '''
    # Set up the game screen.
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    
    # Set some values up that will change while the game is being played.
    correct = 0     # How many the user got right
    wrong = 0       # How many the user got wrong
    level = 1       # What level are they on?

    # Let's get that first letter up on the screen
    letter = draw_random(screen)
    pygame.display.flip()
    running = True

    # Main loop for the program
    while running:
        for event in pygame.event.get():
            # Does the user want to close the program?
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.unicode == letter:
                    correct += 1
                    screen.fill(BLACK)
                    letter = draw_random(screen)
                    pygame.display.flip()
                elif event.unicode.isalpha():
                    wrong += 1
            if correct == 20:
                level += 1
                correct = 0
                wrong = 0

if __name__ == '__main__':
    main()