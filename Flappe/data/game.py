# Import modules
import pygame
import public
import sprites
import functions

# Main Game Scene
# Where most flappe functions take place
def main():
	# Define Variables and Sprites
	loop = True
	tick = 0

	all_sprites = pygame.sprite.Group()
	player = pygame.sprite.Group()
	pipes, checkpoints = functions.generate_pipes()

	floor_h = sprites.Floor((0, 0), all_sprites)
	floor_l = sprites.Floor((0, 550), all_sprites)
	player = sprites.Flappe((50, 250), all_sprites, player)

	# Game loop
	while loop:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				loop = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					player.flap()

		# Game logic
		tick += 1
		if tick == 200:
			pipes, checkpoints = functions.generate_pipes()
			tick = 0

		all_sprites.update()
		pipes.update()
		checkpoints.update()

		# Game drawing
		public.screen.fill(public.BLACK)

		pipes.draw(public.screen)
		checkpoints.draw(public.screen)
		all_sprites.draw(public.screen)

		pygame.display.flip()
		public.clock.tick(public.FPS)
