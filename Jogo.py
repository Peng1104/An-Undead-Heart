from Configurações import *
from Classes import *
pygame.init()

sprites = pygame.sprite.Group()

jogador = Jogador()
sprites.add(jogador)

aliens = pygame.sprite.Group()
for i in range(100):
	alien = Aliens(jogador)
	sprites.add(alien)
	aliens.add(alien)

	
try:

	colision_wall = False
	running = True
	while running:

		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				running = False

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_w:
					jogador.UP    = True
				if event.key == pygame.K_a:
					jogador.LEFT  = True
				if event.key == pygame.K_s:
					jogador.DOWN  = True
				if event.key == pygame.K_d:
					jogador.RIGHT = True

			elif event.type == pygame.KEYUP:

				if event.key == pygame.K_w:
					jogador.UP    = False
				if event.key == pygame.K_a:
					jogador.LEFT  = False
				if event.key == pygame.K_s:
					jogador.DOWN  = False
				if event.key == pygame.K_d:
					jogador.RIGHT = False

		color_mask = MASCARA.get_at(jogador.rect.center)
		
		if color_mask == (BRANCO):
			colision_wall = True

		jogador.speed()
		jogador.wall(colision_wall)
		sprites.update()

		#colision_npcs = pygame.sprite.spritecollide(jogador, npcs, False)
		#jogador.hitbox(npc.rect, colision_npcs)
		
		TELA.blit(FUNDO, FUNDO_RECT)
		sprites.draw(TELA)

		pygame.display.flip()

		colision_wall = False

finally:
	pygame.quit()
