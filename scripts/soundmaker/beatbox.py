import pygame, os
from random import choice
from pygame.locals import *

pygame.init()

ALL_NOTES = ('g', 'f', 'e', 'eb', 'd', 'c', 'b', 'bb', 'a')
SQUARE_SIZE = 40
PADDING = 10
NUM_COLS = 9
NUM_ROWS = 9
WINDOW_SIZE = SQUARE_SIZE * NUM_COLS + PADDING

NOTE_LENGTH = 600

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
CYAN = (102, 225, 255)

COLORS = (WHITE, GREEN, BLUE, RED, CYAN)

def create_main_screen():
    ''' This function creates the main screen for the musicbox.
        Note that we use `global`! This means we can use `screen`
        no matter where we are in the scope of the program. It's cool,
        but you should use `global` sparingly~
    '''
    global screen
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    rows = WINDOW_SIZE / (SQUARE_SIZE+PADDING)
    cols = WINDOW_SIZE / (SQUARE_SIZE+PADDING)
    for row in range(NUM_ROWS):
        for col in range(NUM_COLS):
            pygame.draw.rect(screen, CYAN, 
                (col*SQUARE_SIZE + PADDING, row*SQUARE_SIZE + PADDING, 
                 SQUARE_SIZE-PADDING, SQUARE_SIZE-PADDING))
    pygame.display.flip()

def get_song():
    ''' This function creates our beginning song. It's just a list of strings.
        Each string is one chord / column, and each character is one note. 
    '''
    song = [
    "         ",  # column 0
    "         ",  # column 1
    "         ",  # etc, etc
    "         ",
    "         ",
    "         ",
    "         ",
    "         ",
    "         ",]
    return song

def flip_button(song, pos):
    ''' If a user clicks on a block, we turn it to the opposite color,
        then save that button's state in the song variable
    '''
    chord = song[pos[0]]
    chord = list(chord)       # We can't change just one character of a string,
                            # so we make the string a list.
    if chord[pos[1]] == " ":
        char = "*"
        color = WHITE
    else:
        char = " "
        color = CYAN

    # draw the square!
    pygame.draw.rect(screen, 
        color, 
        (pos[0]*SQUARE_SIZE + PADDING, pos[1]*SQUARE_SIZE + PADDING, 
            SQUARE_SIZE-PADDING, SQUARE_SIZE-PADDING))

    # Change the column, then convert the list into a string
    chord[pos[1]] = char
    chord = "".join(chord)
    song[pos[0]] = chord

    pygame.display.flip()

def get_notes(chord):
    ''' We need to get all the notes from a chord.
    '''
    notes = []
    for i in range(NUM_ROWS):
        if chord[i] == "*":
            notes.append(ALL_NOTES[i])
    return notes

def play_chord(chord):
    ''' We get all the notes in our current chord / column and play them
        at once.
    '''
    notes = get_notes(chord)
    for note in notes:
        n = pygame.mixer.Sound('sounds/piano/piano-{}.wav'.format(note))
        n.play(maxtime=NOTE_LENGTH)
    if not notes:
        n = pygame.mixer.Sound('sounds/silent.wav')
        n.play(maxtime=NOTE_LENGTH)

def switch_col(col, notes, bg_color):
    ''' We switch the colors of a column. If the column is the active
        color, we switch it to the inactive color. If the column is inactive,
        we switch it to the active color.
    '''
    for row in range(NUM_ROWS):
        if notes[row] == " ":
            color = bg_color
        else:
            color = WHITE
        pygame.draw.rect(screen, color, 
            (col*SQUARE_SIZE + PADDING, row*SQUARE_SIZE + PADDING, 
             SQUARE_SIZE-PADDING, SQUARE_SIZE-PADDING))
    pygame.display.flip()

def main():
    ''' Our main function!
    '''
    create_main_screen()        # This creates the global variable screen.
                                # Remember that we can now access 'screen'
                                # anywhere in the scope of the program.
    # Get a blank song
    song = get_song()
    song_col = 0
    running = True
    while running:
        # Check for everything that has happened in PyGame.
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == MOUSEBUTTONDOWN:
                # If the user clicked, let's see if they clicked on a square
                col =  event.pos[0] / (SQUARE_SIZE)   
                row = event.pos[1] / (SQUARE_SIZE)
                if col < NUM_COLS and row < NUM_ROWS:
                    # If they clicked on a square, flip its color!
                    flip_button(song, (col, row))
        if not pygame.mixer.get_busy():
            # If the mixer isn't playing any music, it's time to move on to the next 
            # column

            # Change the color of the current column
            switch_col(song_col, song[song_col], GREEN)

            # Change the color of the last active column
            if song_col == 0:
                switch_col(NUM_COLS-1, song[NUM_COLS-1], CYAN)
            else:
                switch_col(song_col - 1, song[song_col-1], CYAN)

            # Play the current column's chord
            play_chord(song[song_col])

            # Move on to the next column. If we're at the end, move to the beginning.
            if song_col == len(song) - 1:
                song_col = 0
            else:
                song_col += 1

if __name__ == '__main__':
    main()