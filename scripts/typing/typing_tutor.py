import pygame

from pygame.locals import *

from random import choice, randint

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
BOX_SIZE = 40

RED = (255, 0, 0)
BLACK = (0, 0, 0)

LETTERS = "abcdef"

pygame.font.init()
FONT = pygame.font.Font(None, 36)

def draw_random():
	letter = choice(LETTERS)
	x = randint(0, WINDOW_WIDTH - BOX_SIZE)
	y = randint(0, WINDOW_HEIGHT - BOX_SIZE)
	#pygame.draw.rect(screen, RED, (x, y, BOX_SIZE, BOX_SIZE))
	text = FONT.render(letter, 1, BLACK, RED)
	screen.blit(text, (x, y))
	return letter

def main():
	screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
	global screen

	while True:
		letter = draw_random()
		pygame.display.flip()
		for event in pygame.event.get():
			

if __name__ == '__main__':
	main()