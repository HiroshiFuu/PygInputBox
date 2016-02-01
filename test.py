import pygame
from pygame.locals import *
import sys
import PygInputBox

#                 R    G    B
WHITE		= 	(255, 255, 255)
BLACK		= 	(  0,   0,   0)

InputBox = PygInputBox.PygInputBox((10, 10, 200, 30), 'Prompt Text', WHITE)
	
def checkForEvent():
	global selected_mode
	
	for event in pygame.event.get(): # event handling loop
		if event.type == pygame.QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
			pygame.quit()
			sys.exit()
		elif event.type == MOUSEBUTTONUP:	
			if 'click' in InputBox.handleMouseEvent(event):
				pass
		elif event.type == KEYUP:
			InputBox.handleKeyEvent(event)
			
			
def main():
	screen = pygame.display.set_mode((320, 240))
	clock = pygame.time.Clock()
	while True:
		clock.tick(30)
		screen.fill(BLACK)
		InputBox.draw(screen)
		pygame.display.update()
		checkForEvent()
	
	
if __name__ == '__main__':
	main()
