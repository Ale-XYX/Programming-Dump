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

class Bullet(pygame.sprite.Sprite):

    def __init__(self, image, posX, posY):

        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = posX
        self.rect.y = posY

    def update(self, pixels):
        if self.rect.x <= 500 and self.rect.y <= 500:
            self.rect.x += pixels
        else:
            self.kill()
