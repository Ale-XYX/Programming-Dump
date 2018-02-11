import pygame
import sys

if __name__ == '__main__':
	sys.path.insert(0, './data')

	import game

	pygame.init()
	game.title()
	pygame.quit()