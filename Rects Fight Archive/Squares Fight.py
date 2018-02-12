import pygame
from pygame.math import Vector2

class Player(pygame.sprite.Sprite):

    def __init__(self, pos, *groups):

        super().__init__(*groups)

        self.image = pygame.Surface((50, 50))
        self.image.fill(pygame.Color('steelblue2'))
        self.rect = self.image.get_rect(center=pos)
        self.vel = Vector2(0, 0)
        self.pos = Vector2(pos)
        self.fire_direction = (8, 0)        

    def update(self):
        self.pos += self.vel
        self.rect.center = self.pos
        
    
class Bullet(pygame.sprite.Sprite):

    def __init__(self, pos, vel):

        super().__init__()

        self.image = pygame.Surface((10, 10))
        self.image.fill(pygame.Color('aquamarine1'))
        self.rect = self.image.get_rect(center=pos)
        self.pos = pos
        self.vel = vel

    def update(self):
        self.pos += self.vel
        self.rect.center = self.pos

def main():

    # Defining Variables
    screen = pygame.display.set_mode((500, 500))
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    player1 = Player((35, 35), all_sprites)
    player2 = Player((465, 465), all_sprites)
    loop = True
    pygame.display.set_caption('Squares Fight!')
    
# ---- Game loop -----
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            # Keymap  
            if event.type == pygame.KEYDOWN:

                # Player 1 Shooting
                if event.key == pygame.K_e:
                    bullet = Bullet(player1.rect.center, Vector2(player1.fire_direction))
                    bullets.add(bullet)
                    all_sprites.add(bullet)
                # Player 2 Shooting
                if event.key == pygame.K_SPACE:
                    bullet = Bullet(player2.rect.center, Vector2(player2.fire_direction))
                    bullets.add(bullet)
                    all_sprites.add(bullet)

                # Player 1 Movement

                if event.key == pygame.K_d:
                    player1.vel.x = 5
                    player1.fire_direction = (8, 0)

                if event.key == pygame.K_a:
                    player1.vel.x = -5
                    player1.fire_direction = (-8, 0)

                if event.key == pygame.K_s:
                    player1.vel.y = 5
                    player1.fire_direction = (0, 8)

                if event.key == pygame.K_w:
                    player1.vel.y = -5
                    player1.fire_direction = (0, -8)
                
                # Player 2 Movement
                
                if event.key == pygame.K_RIGHT:
                    player2.vel.x = 5
                    player2.fire_direction = (8, 0)

                if event.key == pygame.K_LEFT:
                    player2.vel.x = -5
                    player2.fire_direction = (-8, 0)

                if event.key == pygame.K_DOWN:
                    player2.vel.y = 5
                    player2.fire_direction = (0, 8)

                if event.key == pygame.K_UP:
                    player2.vel.y = -5
                    player2.fire_direction = (0, -8)

                # Toggling off movement
            if event.type == pygame.KEYUP:

                if event.key == pygame.K_d:
                    player1.vel.x = 0

                if event.key == pygame.K_a:
                    player1.vel.x = 0

                if event.key == pygame.K_s:
                    player1.vel.y = 0

                if event.key == pygame.K_w:
                    player1.vel.y = 0

                if event.key == pygame.K_RIGHT:
                    player2.vel.x = 0

                if event.key == pygame.K_LEFT:
                    player2.vel.x = 0

                if event.key == pygame.K_DOWN:
                    player2.vel.y = 0

                if event.key == pygame.K_UP:
                    player2.vel.y = 0
                    
        all_sprites.update()
        screen.fill((0, 0, 0))
        all_sprites.draw(screen)

        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

if __name__ == '__main__':
    pygame.init()
    main()

                
                
