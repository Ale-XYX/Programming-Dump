# MEDIA
import pygame
import os
import glob

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((500, 600))
MEDIA = {}
FILES = glob.glob(os.path.join(os.path.dirname(__file__), 'MEDIA_DATA', 'IMAGE', '*.png'))
FILES2 = glob.glob(os.path.join(os.path.dirname(__file__), 'MEDIA_DATA', 'AUDIO', '*.wav'))

for FILE_NAME in FILES:
    OBJ = pygame.image.load(FILE_NAME).convert_alpha()
    MEDIA[os.path.split(FILE_NAME)[-1][:-4]] = OBJ

print('MEDIA: Loaded Images')

for FILE_NAME in FILES2:
    OBJ = pygame.mixer.sound(FILE_NAME)
    MEDIA[os.path.split[FILE_NAME][-1][:-4]] = OBJ

print('MEDIA: Loaded Audio')

pygame.display.set_caption('Rects Fight')
pygame.display.set_icon(MEDIA['icon'])
