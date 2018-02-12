# Import modules
import pygame
import public

# Floor sprite (Enemy)
class Floor(pygame.sprite.Sprite):
	def __init__(self, pos, *groups):
		super().__init__(*groups)

		self.image = pygame.Surface((480, 50))
		self.rect = self.image.get_rect(topleft=pos)
		self.pos = pygame.math.Vector2(pos)

		self.image.fill(public.GREEN)

class Pipe(pygame.sprite.Sprite):
	def __init__(self, pos, *groups):
		super().__init__(*groups)

		self.image = pygame.Surface((50, 500))
		self.rect = self.image.get_rect(topleft=pos)
		self.pos = pygame.math.Vector2(pos)

		self.image.fill(public.RED)

	def update(self):
		if self.pos.x < -60:
			self.kill()

		self.pos.x -= public.pipe_velocity
		self.rect.center = self.pos


class Checkpoint(pygame.sprite.Sprite):
	def __init__(self, pos, *groups):
		super().__init__(*groups)

		self.image = pygame.Surface((50, 100))
		self.rect = self.image.get_rect(topleft=pos)
		self.pos = pygame.math.Vector2(pos)

		self.image.fill(public.WHITE)

	def update(self):
		if self.pos.x < -60:
			self.kill()

		self.pos.x -= public.pipe_velocity
		self.rect.center = self.pos


class Flappe(pygame.sprite.Sprite):
	def __init__(self, pos, *groups):
		super().__init__(*groups)

		self.image = pygame.Surface((35, 35))
		self.rect = self.image.get_rect(center=pos)
		self.pos = pygame.math.Vector2(pos)
		self.vel = pygame.math.Vector2((0, 0))

		self.image.fill(public.BLUE)

	def flap(self):
		self.vel.y = -4

	def update(self):
		self.vel.y += public.gravity

		self.pos += self.vel
		self.rect.center = self.pos