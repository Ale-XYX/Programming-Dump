import pygame
import os
import glob
screen = pygame.display.set_mode((500, 600))
namer = 0
MEDIA = {}
files = glob.glob(os.path.join(os.path.dirname(__file__), 'media', 'image', '*.png'))
files.extend(glob.glob(os.path.join(os.path.dirname(__file__), 'media', 'audio', '*.wav')))

for file_name in files:
    if file_name.endswith('.png'):
        obj = pygame.image.load(file_name).convert_alpha()
        namer += 1
    elif file_name.endswith('.wav'):
        obj = pygame.mixer.Sound(file_name)
    MEDIA[str(namer)] = obj
pygame.display.set_caption('Rects Fight!')
pygame.display.set_icon(MEDIA['17'])

# Quick Media Numbers Guide [If anyone wants to add on this]

             
