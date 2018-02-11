import pygame
import public
import dictionaries


class Flappe(pygame.sprite.Sprite):
	def __init__(self, pos, floors, pipes, *groups):
		super().__init__(*groups)

		self.image = dictionaries.MEDIA['flappe_texture']
		self.rect = self.image.get_rect(center=pos)
		self.pos = pygame.math.Vector2(pos)
		self.vel = pygame.math.Vector2((0, 0))
		self.is_dead = False
		self.rotation = 0
		self.floors = floors
		self.pipes = pipes

	def jump(self):
		self.vel.y = -4
		dictionaries.MEDIA['flap'].play()

	def update(self):
		self.vel.y += public.GRAVITY
		if self.vel.y > 0:
			if self.rotation > -40:
				self.rotation -= public.GRAVITY * 10
		if self.vel.y < 0:
			if self.rotation < 40:
				self.rotation += public.GRAVITY * 20

		self.image = pygame.transform.rotate(dictionaries.MEDIA['flappe_texture'], self.rotation)

		collided = pygame.sprite.spritecollide(self, self.floors, False)
		for floor in collided:
			if not self.is_dead:
				if self.pos.y > 250:
					self.is_dead = True
					self.vel.y += -2
					public.PIPE_VEL = 0
					public.GRAVITY = 0.2
					dictionaries.MEDIA['fall'].play()

				elif self.pos.y < 250:
					self.is_dead = True
					public.PIPE_VEL = 0
					public.GRAVITY = 0.2
					dictionaries.MEDIA['fall'].play()

		collided2 = pygame.sprite.spritecollide(self, self.pipes, False)
		for pipe in collided2:
			if pipe.type == 'pipe':
				if not self.is_dead:
					if self.pos.y > 250:
						self.is_dead = True
						self.vel.y += -2
						public.PIPE_VEL = 0
						public.GRAVITY = 0.2
						dictionaries.MEDIA['fall'].play()

					elif self.pos.y < 250:
						self.is_dead = True
						public.PIPE_VEL = 0
						public.GRAVITY = 0.2
						dictionaries.MEDIA['fall'].play()

			elif pipe.type == 'checkpoint':
				pipe.kill()
				public.points += 1
				dictionaries.MEDIA['pass_pipe'].play()
				public.score_color = (100, 255, 100)


		if self.pos.y < -60:
			self.kill()

		self.pos += self.vel
		self.rect.center = self.pos

class Floor(pygame.sprite.Sprite):
	def __init__(self, pos, type, *groups):
		super().__init__(*groups)

		if type == 0:
			self.image = dictionaries.MEDIA['floor_texture']
		elif type == 1:
			self.image = pygame.transform.flip(dictionaries.MEDIA['floor_texture'], False, True)

		self.rect = self.image.get_rect(topleft=pos)
		self.pos = pygame.math.Vector2(pos)


class Pipe(pygame.sprite.Sprite):
	def __init__(self, pos, type, *groups):
		super().__init__(*groups)

		if type == 0:
			self.image = dictionaries.MEDIA['pipe_texture']
			self.rect = self.image.get_rect(topleft=pos)
		elif type == 1:
			self.image = pygame.transform.flip(dictionaries.MEDIA['pipe_texture'], False, True)
			self.rect = self.image.get_rect(topleft=pos)

		self.pos = pygame.math.Vector2(pos)
		self.type = 'pipe'

	def update(self):
		self.pos.x -= public.PIPE_VEL
		self.rect.center = self.pos
		
		if self.pos.x < -60:
			self.kill()


class Checkpoint(pygame.sprite.Sprite):
	def __init__(self, pos, *groups):
		super().__init__(*groups)	

		self.image = pygame.Surface((50, 100), pygame.SRCALPHA, 32).convert_alpha()
		self.rect = self.image.get_rect(center=pos)
		self.pos = pygame.math.Vector2(pos)
		self.type = 'checkpoint'

	def update(self):
		self.pos.x -= public.PIPE_VEL
		self.rect.center = self.pos
		
		if self.pos.x < -60:
			self.kill()

class Cloud(pygame.sprite.Sprite):
	def __init__(self, pos, type, *groups):
		super().__init__(*groups)
		if type == 0:
			self.image = dictionaries.MEDIA['cloud_tiny']
		elif type == 1:
			self.image = dictionaries.MEDIA['cloud_small']
		elif type == 2:
			self.image = dictionaries.MEDIA['cloud_normal']
		elif type == 3:
			self.image = dictionaries.MEDIA['cloud_large']

		self.rect = self.image.get_rect(center=pos)
		self.pos = pygame.math.Vector2(pos)
		self.type = type
		self.ticks = 0

	def update(self):
		self.ticks += 1
		if self.type == 0:
			if self.ticks == 10:
				self.pos.x -= 1
				self.rect.center = self.pos
				self.ticks = 0
				
				if self.pos.x < -60:
					self.kill()
		elif self.type == 1:
			if self.ticks == 7:
				self.pos.x -= 1
				self.rect.center = self.pos
				self.ticks = 0
				
				if self.pos.x < -60:
					self.kill()
		elif self.type == 2:
			if self.ticks == 3:
				self.pos.x -= 1
				self.rect.center = self.pos
				self.ticks = 0
				
				if self.pos.x < -60:
					self.kill()	

		elif self.type == 3:
			if self.ticks == 1:
				self.pos.x -= 1
				self.rect.center = self.pos
				self.ticks = 0
				
				if self.pos.x < -60:
					self.kill()	


class Button(pygame.sprite.Sprite):
	def __init__(self, pos, type, *groups):
		super().__init__(*groups)

		self.image = dictionaries.MEDIA['button_texture']
		self.rect = self.image.get_rect(topleft=pos)
		self.pos = pygame.math.Vector2(pos)
		self.type = type
