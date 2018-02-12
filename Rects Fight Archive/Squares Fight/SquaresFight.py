# Squares Fight!

# ---------- Config ----------

import pygame 
import time

pygame.init()

# Screen Config
ScreenWidth = 500
ScreenHeight = 500
ScreenSize = (ScreenWidth, ScreenHeight)
Screen = pg.display.set_mode(size)
pg.display.set_caption('Squares Fight')

# Color Config
Red = ( 255, 0, 0)
Blue = ( 43, 255, 230)
Orange = ( 255, 170, 0)
Black = ( 0, 0, 0)

# Image Config
BlueImage = pg.image.load('blue2.bmp').convert()
OrangeImage = pg.image.load('orange2.bmp').convert()

# Time config
FPS = 60
CooldownTime = 3
Clock = pg.time.Clock()

# Text Config
Font = pg.font.SysFont("berlinsansfb", 72)
Text = Font.render("Fight!", True, WHITE)

# Draw Config
SpriteWidth = 50
SpriteHeight = 50
BlueSpawnX = 5
BlueSpawnY = 5
OrangeSpawnX = 445
OrangeSpawnY = 445

#Sprite Config
class Player(pg.sprite.Sprite):

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
        self.rect.y

    def dashleft(self, pixels):
        self.rect.x -= pixels
    
    def dashright(self, pixels):
        self.rect.x += pixels

AllSprites = pg.sprite.Group()

Player1 = Player(BlueImage)
Player2 = Player(OrangeImage)

Player1.rect.x = BlueSpawnX
Player1.rect.y = BlueSpawnY
Player2.rect.x = OrangeSpawnX
Player2.rect.y = OrangeSpawnY

AllSprites.add(Player1, Player2)

# Game Config
Loop = True

# ---------- Main Game ----------

while Loop:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            Loop= False
    # Key Logic
    keys = pg.key.get_pressed()
    if keys[pygame.K_LEFT]:
        Player1.left(3)

    if keys[pg.K_RIGHT]:
        Player1.right(3)

    if keys[pg.K_UP]:
        Player1.up(3)

    if keys[pg.K_DOWN]:
        Player1.down(3)

    if keys[pg.K_a]:
        Player2.left(3)

    if keys[pg.K_d]:
        Player2.right(3)

    if keys[pg.K_s]:
        Player2.down(3)

    if keys[pg.K_w]:
        Player2.up(3)
