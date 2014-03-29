import pygame, os

pygame.init()

files = os.listdir('sounds/piano/')
notes = []
for f in files:
	if f.endswith('.wav'):
		notes.append(f)

for note in notes:
	print note
	effect = pygame.mixer.Sound('sounds/piano/' + note)
	effect.play()
	pygame.time.wait(500)