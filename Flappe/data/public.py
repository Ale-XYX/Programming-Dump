# Import and start pygame
import pygame
pygame.init()

# Constants
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 60
SWIDTH = 480
SHEIGHT = 600


# Variables
screen = pygame.display.set_mode((SWIDTH, SHEIGHT))
clock = pygame.time.Clock()
pipe_velocity = 3
gravity = 0.1
