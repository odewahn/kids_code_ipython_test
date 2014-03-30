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

NOTE_LENGTH = 500

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
CYAN = (102, 225, 255)

COLORS = (WHITE, GREEN, BLUE, RED, CYAN)

def create_main_screen():
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
    # Is this flipped already?
    line = song[pos[0]]
    line = list(line)
    if line[pos[1]] == " ":
        char = "*"
        color = WHITE
    else:
        char = " "
        color = CYAN

    pygame.draw.rect(screen, 
        color, 
        (pos[0]*SQUARE_SIZE + PADDING, pos[1]*SQUARE_SIZE + PADDING, 
            SQUARE_SIZE-PADDING, SQUARE_SIZE-PADDING))
    line[pos[1]] = char
    line = "".join(line)
    song[pos[0]] = line

    pygame.display.flip()

def get_notes(column):
    notes = []
    for i in range(NUM_ROWS):
        if column[i] == "*":
            notes.append(ALL_NOTES[i])
    return notes

def play_chord(chord):
    notes = get_notes(chord)
    for note in notes:
        n = pygame.mixer.Sound('sounds/piano/piano-{}.wav'.format(note))
        n.play(maxtime=NOTE_LENGTH)
    if not notes:
        n = pygame.mixer.Sound('sounds/silent.wav')
        n.play(maxtime=NOTE_LENGTH)

def switch_col(col, notes, bg_color):
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
    create_main_screen()
    song = get_song()
    song_col = 0
    while True:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                col =  event.pos[0] / (SQUARE_SIZE)
                row = event.pos[1] / (SQUARE_SIZE)
                if col < NUM_COLS and row < NUM_ROWS:
                    flip_button(song, (col, row))
        if not pygame.mixer.get_busy():
            switch_col(song_col, song[song_col], GREEN)
            if song_col == 0:
                switch_col(NUM_COLS-1, song[NUM_COLS-1], CYAN)
            else:
                switch_col(song_col - 1, song[song_col-1], CYAN)
            play_chord(song[song_col])
            if song_col == len(song) - 1:
                song_col = 0
            else:
                song_col += 1



if __name__ == '__main__':
    main()