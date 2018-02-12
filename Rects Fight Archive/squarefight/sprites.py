import pygame
import var as v
pygame.init()

class Player(pygame.sprite.Sprite):

    def __init__(self, image):

        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()

    def right(self, pixels):
        self.rect.x += pixels
        
    def left (self, pixels):
        self.rect.x -= pixels

    def up(self, pixels):
        self.rect.y -= pixels

    def down(self, pixels):
        self.rect.y += pixels

    def dashleft(self, pixels):
        self.rect.x -= pixels
    
    def dashright(self, pixels):
        self.rect.x += pixels

    
