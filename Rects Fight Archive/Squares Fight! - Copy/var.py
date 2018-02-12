import pygame
import os

pygame.init()

screenWidth = 500
screenHeight = 500
screenSize = (screenWidth, screenHeight)
screen = pygame.display.set_mode(screenSize)

white = ( 255, 255, 255)
black = ( 0, 0, 0)

blueImage = IMAGE = pygame.image.load(os.path.join('img', 'blue.png')).convert_alpha()
orangeImage = IMAGE = pygame.image.load(os.path.join('img', 'orange.png')).convert_alpha()

FPS = 60
cooldownTime = 3
clock = pygame.time.Clock()

font = pygame.font.SysFont('berlinsansfb', 72)
text = font.render('Fight!', True, white)

blueX = 5
blueY = 5
orangeX = 445
orangeY = 445

loop = True
again = False
