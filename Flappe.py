import pygame
import time
import random
import sys

pygame.init()

class Public:
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAVITY = 0.1
    BIG_FONT = pygame.font.SysFont(None, 40, False, False)

    screen = pygame.display.set_mode((500, 500))
    clock = pygame.time.Clock()
    univel = 3
    LAYOUTS = [
    ['N','N','Y','Y','Y','Y','Y','Y','Y'],
    ['Y','N','N','Y','Y','Y','Y','Y','Y'],
    ['Y','Y','N','N','Y','Y','Y','Y','Y'],
    ['Y','Y','Y','N','N','Y','Y','Y','Y'],
    ['Y','Y','Y','Y','N','N','Y','Y','Y'],
    ['Y','Y','Y','Y','Y','N','N','Y','Y'],
    ['Y','Y','Y','Y','Y','Y','N','N','Y'],
    ]
    counter = 0

class Floor(pygame.sprite.Sprite):
    def __init__(self, pos, size, type, *groups):
        super().__init__(*groups)
        self.image = pygame.Surface(size)
        self.rect = self.image.get_rect(topleft=pos)
        self.pos = pygame.math.Vector2(pos)
        self.type = type
        self.image.fill(Public.GREEN)
    
class Flappe(pygame.sprite.Sprite):
    def __init__(self, pos, floors, pipes, *groups):
        super().__init__(*groups)
        self.image = pygame.Surface((35, 35))
        self.rect = self.image.get_rect(topleft=pos)
        self.pos = pygame.math.Vector2(pos)
        self.vel = pygame.math.Vector2((0, 0))
        self.floors = floors
        self.is_dead = False
        self.toggle = False
        self.pipes = pipes

        self.image.fill(Public.BLUE)

    def flap(self):
        self.vel.y = -5

    def update(self):
        collided = pygame.sprite.spritecollide(self, self.floors, False)
        collided2 = pygame.sprite.spritecollide(self, self.pipes, False)
        for sprite in collided:
            if not self.is_dead:
                if sprite.type == 'low':
                    self.vel.y = -3
                    Public.GRAVITY = 0.3
                    Public.univel = 0
                    self.is_dead = True
                    self.toggle = True

                elif sprite.type == 'high':
                    self.pos.y = sprite.rect.bottom + 24
                    self.vel.y = 0
                    Public.GRAVITY = 0.3
                    Public.univel = 0
                    self.is_dead = True
                    self.toggle = True

        for sprite in collided2:
            if not self.is_dead:
                Public.univel = 0
                self.vel.y = -3
                Public.GRAVITY = 0.3
                self.is_dead = True
                self.toggle = True

        self.vel.y += Public.GRAVITY

        if self.pos.y > 550:
            self.kill()
            time.sleep(0.5)
            pygame.quit()
            sys.exit()

        self.pos += self.vel
        self.rect.center = self.pos

class Pipe(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        self.image = pygame.Surface((50, 50))
        self.rect = self.image.get_rect(topleft=pos)
        self.pos = pygame.math.Vector2(pos)
        self.image.fill(Public.RED)
        self.toggle = False

    def update(self):
        if not self.toggle:
            self.pos.x -= Public.univel
            self.rect.topleft = self.pos

            if self.pos.x > 550:
                self.kill()

class Checkpoint(pygame.sprite.Sprite):
    def __init__(self, pos, player):
        super().__init__() 
        self.image = pygame.Surface([1, 500], pygame.SRCALPHA, 32).convert_alpha()
        self.rect = self.image.get_rect(center=pos)
        self.player = player
        self.pos = pygame.math.Vector2(pos)

    def update(self):
        collided = pygame.sprite.spritecollide(self, self.player, False)

        self.pos.x -= Public.univel
        self.rect.center = self.pos

        if self.pos.x > 570:
            self.kill()
            return -1

        for sprite in collided:
            Public.counter += 1
            self.kill()
            return -1


def main():
    loop = True
    counter = 0

    all_sprites = pygame.sprite.Group()
    floors = pygame.sprite.Group()
    pipes = pygame.sprite.Group()
    players = pygame.sprite.Group()

    floorlow = Floor((0, 473), (500, 30), 'low', all_sprites, floors)
    floorhigh = Floor((0, 0), (500, 23), 'high', all_sprites, floors)

    player = Flappe((100, 250), floors, pipes, all_sprites, players)

    layout = Public.LAYOUTS[random.randint(0, len(Public.LAYOUTS) - 1)]
    spawntable = [23, 73, 123, 173, 223, 273, 323, 373, 423]
    for i,c in enumerate(layout):
        if c == 'Y':
            pipe = Pipe((530, spawntable[i]))
            pipes.add(pipe)
            all_sprites.add(pipe)
        elif c == 'X':
            pass
    checkpoint = Checkpoint((555, 250), players)
    all_sprites.add(checkpoint)
    text = Public.BIG_FONT.render(str(Public.counter), True, Public.WHITE)

    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and not player.toggle:
                    player.flap()

        counter += 1
        if counter == 200 and not Public.univel == 0:
            layout = Public.LAYOUTS[random.randint(0, len(Public.LAYOUTS) - 1)]
            spawntable = [23, 73, 123, 173, 223, 273, 323, 373, 423]
            for i,c in enumerate(layout):
                if c == 'Y':
                    pipe = Pipe((530, spawntable[i]))
                    pipes.add(pipe)
                    all_sprites.add(pipe)
                elif c == 'X':
                    pass
            checkpoint = Checkpoint((555, 250), players)
            all_sprites.add(checkpoint)
            counter = 0

        text = Public.BIG_FONT.render(str(Public.counter), True, Public.WHITE)
        all_sprites.update() 

        Public.screen.fill(Public.BLACK)
        all_sprites.draw(Public.screen)
        Public.screen.blit(text, (200, 50))

        pygame.display.flip()
        Public.clock.tick(60)

if __name__ == '__main__':
    main()
    pygame.quit()
    
