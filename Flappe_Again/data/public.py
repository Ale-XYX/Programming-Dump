# Import modules
import pygame

pygame.init()

# Static
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (66, 138, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 60
SWIDTH = 480
SHEIGHT = 600
PIPE_VEL = 3
GRAVITY = 0.1
FONT_BIG = pygame.font.SysFont(None, 40, False, False)
FONT_SMALL = pygame.font.SysFont(None, 20, False, False)

# Variables
screen = pygame.display.set_mode((SWIDTH, SHEIGHT))
clock = pygame.time.Clock()
score_color = (255, 255, 255)
points = 0
floors = pygame.sprite.Group()
clouds = pygame.sprite.Group()
pipes = pygame.sprite.Group()