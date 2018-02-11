import pygame
import public
import glob
import os

# Media Dictionary
# Loads media into dictionary
MEDIA = {}
image_files = glob.glob(os.path.join(os.path.dirname(__file__), 'media', 'images', '*.png'))
audio_files = glob.glob(os.path.join(os.path.dirname(__file__), 'media', 'audio', '*.wav'))

for file in image_files:
	obj = pygame.image.load(file).convert_alpha()
	MEDIA[os.path.split(file)[-1][:-4]] = obj

for file in audio_files:
	obj = pygame.mixer.Sound(file)
	MEDIA[os.path.split(file)[-1][:-4]] = obj