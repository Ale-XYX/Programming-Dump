import pygame
import sprites as s
import os
pygame.init()

# Screen Config
screenWidth = 500
screenHeight = 500
screenSize = (screenWidth, screenHeight)
screen = pygame.display.set_mode(screenSize)

# Color Config
white = ( 255, 255, 255)
black = ( 0, 0, 0)

# Image Config
blueImage = pygame.image.load(
    os.path.join('img', 'blue.png')).convert_alpha()
orangeImage = pygame.image.load(os.path.join(
    'img', 'orange.png')).convert_alpha()

# Clock Config
FPS = 60
clock = pygame.time.Clock()

# Sprite Config
blueX = 5
blueY = 5
orangeX = 445
orangeY = 445
sizeX = 50
sizeY = 50
player1 = s.Player(blueImage)
player2 = s.Player(orangeImage)
allSprites = pygame.sprite.Group()
player1.rect.x = blueX
player1.rect.y = blueY
player2.rect.x = orangeX
player2.rect.y = orangeY

# Game Config
loop = True
again = False
checkIfLeave = False
keys = pygame.key.get_pressed()
