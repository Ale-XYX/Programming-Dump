import pygame
import var as v
import media as m

pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, enemy_bullets, direction, color, *groups):
        super().__init__(*groups)
        self.image = m.PLAYER_MEDIA[color]['player_image']
        self.rect = self.image.get_rect(center = pos)
        self.vel = pygame.math.Vector2(0, 0)
        self.pos = pygame.math.Vector2(pos)
        self.fire_direction = pygame.math.Vector2(direction)
        self.health = 3
        self.enemy_bullets = enemy_bullets
        self.toggle = False
        self.color = m.PLAYER_MEDIA[color]['color']
        self.bullet_image = m.PLAYER_MEDIA[color]['bullet_image']
    def update(self):
        self.pos += self.vel
        self.rect.center = self.pos
        self.rect.clamp_ip(v.playarea)
        collided = pygame.sprite.spritecollide(self, self.enemy_bullets, True)
        for bullet in collided:
            self.health -= 1
            m.MEDIA['hit'].play()
            if self.health <= 0:
                m.MEDIA['die'].play()
                self.kill()
                self.toggle = True
                
print('SPRITES: Loaded Player Sprite')

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, vel, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center = pos)
        self.vel = pygame.math.Vector2(vel)
        self.pos = pygame.math.Vector2(pos)
        self.toggle = False
    def update(self):
        if self.toggle == False:
            self.pos += self.vel
            self.rect.center = self.pos
            if not v.playarea.contains(self):
                self.kill()
                
print('SPRITES: Loaded Bullet Sprite')
                
