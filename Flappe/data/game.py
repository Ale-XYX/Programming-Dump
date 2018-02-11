import pygame
import public
import sprites
import functions
import dictionaries


def title():
	loop = True
	ticks = 0

	all_sprites = pygame.sprite.Group()

	functions.generate_clouds(public.clouds, True)
	floor_bottom = sprites.Floor((0, 550), 0, public.floors)
	floor_top = sprites.Floor((0, 0), 1, public.floors)

	play_btn = sprites.Button((190, 300), 'Play', all_sprites)
	options_btn = sprites.Button((190, 400), 'Options', all_sprites)
	play_text = public.FONT_BIG.render(play_btn.type, True, (255, 255, 255))


	while loop:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				loop = False
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if play_btn.rect.collidepoint(event.pos):
					main()
					return 1


		# Game logic
		ticks += 1

		if ticks == 150:
			functions.generate_clouds(public.clouds, False)
			ticks = 0


		public.floors.update()
		public.clouds.update()

		# Game drawing
		public.screen.fill(public.BLUE)

		public.clouds.draw(public.screen)
		public.floors.draw(public.screen)
		public.screen.blit(dictionaries.MEDIA['title_texture'], (0, 105))
		all_sprites.draw(public.screen)
		public.screen.blit(play_text, (play_btn.pos.x + 20, play_btn.pos.y + 11))

		pygame.display.flip()
		public.clock.tick(public.FPS)	


def main():
	# Variables
	loop = True
	ticks = 0
	deathticks = 0

	# Sprites
	player = pygame.sprite.Group()

	functions.generate_pipes(public.pipes)

	flappe = sprites.Flappe((50, 250), public.floors, public.pipes, player)

	text = public.FONT_BIG.render(str(public.points), True, public.score_color)
	textpos = (220, 75)

	while loop:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				loop = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE and not flappe.is_dead:
					flappe.jump()

		# Game logic
		ticks += 1

		if ticks == 150:
			functions.generate_pipes(public.pipes)
			functions.generate_clouds(public.clouds, False)
			ticks = 0

		if public.score_color != (255, 255, 255):
			public.score_color = (public.score_color[0] + 5, public.score_color[1], public.score_color[2] + 5) 

		if flappe.is_dead:
			text = public.FONT_BIG.render('', True, public.score_color)
			deathticks += 1
			if deathticks == 100:
				gameover()
				return 1

		elif not flappe.is_dead:
			text = public.FONT_BIG.render(str(public.points), True, public.score_color)

		public.floors.update()
		player.update()
		public.pipes.update()
		public.clouds.update()

		# Game drawing
		public.screen.fill(public.BLUE)

		public.clouds.draw(public.screen)
		player.draw(public.screen)
		public.pipes.draw(public.screen)
		public.floors.draw(public.screen)
		public.screen.blit(text, textpos)

		pygame.display.flip()
		public.clock.tick(public.FPS)


def gameover():
	loop = True
	ticks = 0

	all_sprites = pygame.sprite.Group()


	while loop:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				loop = False
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if play_btn.rect.collidepoint(event.pos):
					main()
					return 1


		# Game logic
		ticks += 1

		if ticks == 150:
			functions.generate_clouds(public.clouds, False)
			ticks = 0

		public.floors.update()
		public.clouds.update()

		# Game drawing
		public.screen.fill(public.BLUE)

		public.clouds.draw(public.screen)
		public.pipes.draw(public.screen)
		public.floors.draw(public.screen)
		all_sprites.draw(public.screen)

		pygame.display.flip()
		public.clock.tick(public.FPS)


def options():
	pass