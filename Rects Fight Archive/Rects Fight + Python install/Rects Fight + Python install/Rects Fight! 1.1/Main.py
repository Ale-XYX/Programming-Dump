# Rects Fight

import pygame
import os
import time
from pygame.math import Vector2


print('''
  _ _ _ _ _
 |  _   _  |
 | | | | | |
 | |_| |_| |
 |   1.1   |
 |_ _ _ _ _|
''')

# Init

pygame.init()
screen = pygame.display.set_mode((500, 500))
playarea = pygame.Rect(5, 5, 490, 490)
black = (0, 0, 0)
white = (255, 255, 255)
grey = (192, 192, 192)
vel_reset = 0
vel = 8
left_vel = (-8, 0)
right_vel = (8, 0)
up_vel = (0, -8)
down_vel = (0, 8)

        
# Loading media

bluestage1 = pygame.image.load(os.path.join('media', 'blue1.png')).convert_alpha()
bluestage2 = pygame.image.load(os.path.join('media', 'blue2.png')).convert_alpha()
bluestage3 = pygame.image.load(os.path.join('media', 'blue3.png')).convert_alpha()
orangestage1 = pygame.image.load(os.path.join('media', 'orange1.png')).convert_alpha()
orangestage2 = pygame.image.load(os.path.join('media', 'orange2.png')).convert_alpha()
orangestage3 = pygame.image.load(os.path.join('media', 'orange3.png')).convert_alpha()
bluebullet = pygame.image.load(os.path.join('media', 'bulletblue.png')).convert_alpha()
orangebullet = pygame.image.load(os.path.join('media', 'bulletorange.png')).convert_alpha()
startlogo = pygame.image.load(os.path.join('media', 'startscreen.png')).convert_alpha()
pausescreen = pygame.image.load(os.path.join('media', 'paused.png')).convert_alpha()
windowicon = pygame.image.load(os.path.join('media', 'icon.png')).convert_alpha()

pausesound = pygame.mixer.Sound(os.path.join('media', 'pause.wav'))
shootsound = pygame.mixer.Sound(os.path.join('media', 'shoot.wav'))
hitsound = pygame.mixer.Sound(os.path.join('media', 'hit.wav'))
diesound = pygame.mixer.Sound(os.path.join('media', 'die.wav'))
fightsound = pygame.mixer.Sound(os.path.join('media', 'fight.wav'))

pygame.display.set_caption('Rects Fight!')
pygame.display.set_icon(windowicon)
    
# Player Sprite

class Player(pygame.sprite.Sprite):

    def __init__(self, pos, enemy_bullets, image, *groups):

        super().__init__(*groups)

        self.image = image
        self.rect = self.image.get_rect(center=pos)
        self.vel = Vector2(0, 0)
        self.pos = Vector2(pos)
        self.fire_direction = (8, 0)
        self.health = 3
        self.enemy_bullets = enemy_bullets
        self.toggle = False

    # Checking for collisions
    
    def update(self):
        self.pos += self.vel
        self.rect.center = self.pos
        self.rect.clamp_ip(playarea)
        
        collided_bullets = pygame.sprite.spritecollide(self, self.enemy_bullets, True)
        for bullet in collided_bullets:
            self.health -= 1
            hitsound.play()
            if self.health <= 0:
                self.kill()
                self.toggle = True
                diesound.play()
        
# Bullet Sprite

class Bullet(pygame.sprite.Sprite):

    def __init__(self, pos, vel, image):

        super().__init__()

        self.image = image
        self.rect = self.image.get_rect(center=pos)
        self.pos = pos
        self.vel = vel
        self.toggle = False

    def update(self):
        if self.toggle == False:
            self.pos += self.vel
            self.rect.center = self.pos
            
            if not playarea.contains(self):
                self.kill()

    def stop(self):
        self.toggle = True

    def start(self):
        self.toggle = False
    
# Start Screen

def start():
    startScreen=False
    pygame.display.set_caption('Rects Fight!')
    
    while startScreen == False:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:              
                    startScreen = True
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    
        screen.fill(black)           
        screen.blit(startlogo, (0, 0))
        
        pygame.display.flip()

# ----- Main Game -----
def main():
    
    # Defining Variables
        
    screen = pygame.display.set_mode((500, 500))
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    bullets1 = pygame.sprite.Group()
    bullets2 = pygame.sprite.Group()
    player1 = Player((35, 35), bullets2, bluestage1, all_sprites)
    player2 = Player((465, 465), bullets1, orangestage1, all_sprites)
    confirm = False
    onStart = True
    loop = True

        
# ---- Game loop -----
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            # Keymap  
            if event.type == pygame.KEYDOWN:

                # Player 1 Shooting
                
                if event.key == pygame.K_e and player1.toggle == False:
                    bullet = Bullet(player1.rect.center, Vector2(player1.fire_direction), bluebullet)
                    shootsound.play()
                    bullets1.add(bullet)
                    all_sprites.add(bullet)
                    
                # Player 2 Shooting
                
                if event.key == pygame.K_SPACE and player2.toggle == False:
                    bullet = Bullet(player2.rect.center, Vector2(player2.fire_direction), orangebullet)
                    shootsound.play()
                    bullets2.add(bullet)
                    all_sprites.add(bullet)

                # Player 1 Movement

                if event.key == pygame.K_d and player1.toggle == False:
                    player1.vel.x = 5
                    player1.fire_direction = (vel, 0)

                if event.key == pygame.K_a and player1.toggle == False:
                    player1.vel.x = -5
                    player1.fire_direction = (-vel, 0)
                    
                if event.key == pygame.K_s and player1.toggle == False:
                    player1.vel.y = 5
                    player1.fire_direction = (0, vel)

                if event.key == pygame.K_w and player1.toggle == False:
                    player1.vel.y = -5
                    player1.fire_direction = (0, -vel)
                
                # Player 2 Movement
                
                if event.key == pygame.K_RIGHT and player2.toggle == False:
                    player2.vel.x = 5
                    player2.fire_direction = (vel, 0)

                if event.key == pygame.K_LEFT and player2.toggle == False:
                    player2.vel.x = -5
                    player2.fire_direction = (-vel, 0)

                if event.key == pygame.K_DOWN and player2.toggle == False:
                    player2.vel.y = 5
                    player2.fire_direction = (0, vel)

                if event.key == pygame.K_UP and player2.toggle == False:
                    player2.vel.y = -5
                    player2.fire_direction = (0, -vel)

                # Toggling off movement
            if event.type == pygame.KEYUP:

                # Player 1 Toggles

                if event.key == pygame.K_d:
                    player1.vel.x = vel_reset

                if event.key == pygame.K_a:
                    player1.vel.x = vel_reset

                if event.key == pygame.K_s:
                    player1.vel.y = vel_reset

                if event.key == pygame.K_w:
                    player1.vel.y = vel_reset

                # Player 2 Toggles

                if event.key == pygame.K_RIGHT:
                    player2.vel.x = vel_reset

                if event.key == pygame.K_LEFT:
                    player2.vel.x = vel_reset

                if event.key == pygame.K_DOWN:
                    player2.vel.y = vel_reset

                if event.key == pygame.K_UP:
                    player2.vel.y = vel_reset
                    
        # Main Game Logic
        
        if onStart == True:
            fightsound.play()
            onStart = False
            
        keys = pygame.key.get_pressed()

        if keys[pygame.K_TAB] and confirm == False:
            pausesound.play()
            player1.toggle = True
            player2.toggle = True
            confirm = True
            for bullet in bullets1:
                bullet.stop()
                
            for bullet in bullets2:
                bullet.stop()
            
        if keys[pygame.K_ESCAPE] and confirm == True:
            loop = False
            
        elif keys[pygame.K_LSHIFT] and confirm == True:
            confirm = False
            player1.toggle = False
            player2.toggle = False
            for bullet in bullets1:
                bullet.start()
                
            for bullet in bullets2:
                bullet.start()

        if player1.health == 2:
            player1.image = bluestage2
            
        elif player1.health == 1:
             player1.image = bluestage3
            
        elif player1.health == 0:
            pygame.display.set_caption('Orange Wins!')
            
            if keys[pygame.K_ESCAPE] and confirm == False:
                loop = False

        if player2.health == 2:
            player2.image = orangestage2
            
        elif player2.health == 1:
            player2.image = orangestage3
                    
        elif player2.health == 0:   
            pygame.display.set_caption('Blue Wins!')                        
            
            if keys[pygame.K_ESCAPE] and confirm == False:
                loop = False               

        if player1.health == 0 and player2.health == 0:
            pygame.display.set_caption('They destroyed eachother!')
            
        # Drawing Code
        
        all_sprites.update()
        screen.fill(black)
        if confirm == True:
            screen.blit(pausescreen, (145, 210))
            
        pygame.draw.rect(screen, grey, pygame.Rect(0, 0, 500, 5))
        pygame.draw.rect(screen, grey, pygame.Rect(0, 0, 5, 500))
        pygame.draw.rect(screen, grey, pygame.Rect(0, 495, 500, 5))
        pygame.draw.rect(screen, grey, pygame.Rect(495, 0, 5, 500))
        all_sprites.draw(screen)
        
        pygame.display.flip()
        clock.tick(60)
        
# Game Sequence

if __name__ == '__main__':
    start()
    main()
    pygame.quit()

# ~SnivyDroid


                
                
