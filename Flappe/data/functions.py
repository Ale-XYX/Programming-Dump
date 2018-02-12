# Import modules
import pygame
import random
import public
import sprites

def generate_pipes():
	pipes = pygame.sprite.Group()
	checkpoints = pygame.sprite.Group()

	checkpoint = sprites.Checkpoint((530, random.randint(100, 450)), checkpoints)
	pipe_bottom = sprites.Pipe((530, checkpoint.rect.bottom + 200), pipes)
	pipe_top = sprites.Pipe((530, checkpoint.rect.top - 300), pipes)
	
	return pipes, checkpoints