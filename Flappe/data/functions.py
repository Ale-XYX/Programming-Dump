import pygame
import random
import public
import sprites

def generate_pipes(pipes):
	checkpoint = sprites.Checkpoint((550, random.randint(100, 450)), pipes)
	pipe_top = sprites.Pipe((550, checkpoint.rect.top - 250), 1, pipes)
	pipe_bottom = sprites.Pipe((550, checkpoint.rect.bottom + 250), 0, pipes)


def generate_clouds(clouds, fbool):
	if fbool:
		for i in range(10):
			cloud = sprites.Cloud((random.randint(50, 430), random.randint(100, 500)), random.randint(0, 3), clouds)
	elif not fbool:
		if len(clouds.sprites()) < 10:
			cloud = sprites.Cloud((500, random.randint(100, 500)), random.randint(0, 3), clouds)