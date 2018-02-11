import pygame

class Config:
	SWIDTH = 500
	SHEIGHT = 500
	GRAVITY = 0.5
	BLACK = (0, 0, 0)
	WHITE = (255, 255, 255)
	GREEN = (0, 255, 0)
	RED = (255, 0, 0)
	BLUE = (0, 0, 255)

class Floor(pygame.sprite.Sprite):
	def __init__(self, pos, w, h, *groups):
		super().__init__(*groups)

		self.image = pygame.Surface((w,h))
		self.rect = self.image.get_rect(topleft=pos)
		self.pos = pygame.math.Vector2(pos)
		self.image.fill(Config.GREEN)

	def update(self):
		pass


class RectPlayer(pygame.sprite.Sprite):
    def __init__(self, pos, blocks, *groups):
        super().__init__(*groups)
        self.image = pygame.Surface((50, 50))
        self.image.fill(Config.BLUE)
        self.rect = self.image.get_rect(topleft=pos)
        self.vel = pygame.math.Vector2(0, 0)
        self.pos = pygame.math.Vector2(pos)
        self.blocks = blocks
        self.on_ground = False

    def update(self):
        # Move along x-axis.
        self.pos.x += self.vel.x
        self.rect.x = self.pos.x

        collisions = pygame.sprite.spritecollide(self, self.blocks, False)
        for block in collisions:  # Horizontal collision occurred.
            if self.vel.x > 0:  # Moving right.
                self.rect.right = block.rect.left  # Reset the rect pos.
            elif self.vel.x < 0:  # Moving left.
                self.rect.left = block.rect.right  # Reset the rect pos.
            self.pos.x = self.rect.x  # Update the actual x-position.

        # Move along y-axis.
        self.pos.y += self.vel.y
        self.rect.y = self.pos.y

        collisions = pygame.sprite.spritecollide(self, self.blocks, False)
        for block in collisions:  # Vertical collision occurred.
            if self.vel.y > 0:  # Moving down.
                self.rect.bottom = block.rect.top  # Reset the rect pos.
                self.vel.y = 0  # Stop falling.
                self.on_ground = True
            elif self.vel.y < 0:  # Moving up.
                self.rect.top = block.rect.bottom  # Reset the rect pos.
                self.vel.y = 0  # Stop jumping.
            self.pos.y = self.rect.y  # Update the actual y-position.

        # Stop the player at screen bottom.
        if self.rect.bottom >= Config.SHEIGHT:
            self.vel.y = 0
            self.rect.bottom = Config.SHEIGHT
            self.pos.y = self.rect.y
            self.on_ground = True
        else:
            self.vel.y += Config.GRAVITY  # Gravity

    def jump(self):
        self.rect.y += 1
        hits = pygame.sprite.spritecollide(self, self.blocks, False)
        self.rect.y -= 1
        if hits:
            self.vel.y = -13

global screen
screen = pygame.display.set_mode((Config.SWIDTH, Config.SHEIGHT))

def main():
	global screen

	loop = True
	clock = pygame.time.Clock()

	all_sprites = pygame.sprite.Group()
	floor_group = pygame.sprite.Group()

	floor = Floor((0, 470), 500, 30, all_sprites, floor_group)
	player = RectPlayer((50, 400), floor_group, all_sprites)

	while loop:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				loop = False

			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					player.vel.x = -3
				elif event.key == pygame.K_RIGHT:
					player.vel.x = 3
				elif event.key == pygame.K_UP:
					player.jump()

			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					player.vel.x = 0
				elif event.key == pygame.K_RIGHT:
					player.vel.x = 0

		screen.fill(Config.BLACK)
		all_sprites.update()
		all_sprites.draw(screen)

		pygame.display.flip()
		clock.tick(60)

if __name__ == '__main__':
	pygame.init()
	main()
	pygame.quit() 