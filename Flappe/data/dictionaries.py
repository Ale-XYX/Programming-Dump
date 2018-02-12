# Import modules
import pygame
import glob
import os
import public

# Media Dictionary
# Uses glob to import media, then stores it in a loop

MEDIA = {}
image_files = glob.glob(os.path.join(os.path.dirname(__file__), 'media_files', 'image_files', '*.png'))

for file in image_files:
    obj = pygame.image.load(file).convert_alpha()
    MEDIA[os.path.split(file)[-1][:-4]] = obj