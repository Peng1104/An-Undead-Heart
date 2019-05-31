from Configurações import *
from Classes import *
pygame.init()

sprites = pygame.sprite.Group()

jogador = Jogador()
sprites.add(jogador)

aliens = pygame.sprite.Group()
for i in range(10):
	alien = Aliens(jogador)
	sprites.add(alien)
	aliens.add(alien)

pewpews = pygame.sprite.Group()
pewpew = Pewpew(jogador)
sprites.add(pewpew)
pewpews.add(pewpew)
	
bullets = pygame.sprite.Group()

try:

	colision_wall = False
	atirando = False
	running = True
	while running:
		atirando = False

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

			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1: #ESQUERDO 3, #DIREITO 1
					atirando = True

			if event.type == pygame.KEYUP:

				if event.key == pygame.K_w:
					jogador.UP    = False
				if event.key == pygame.K_a:
					jogador.LEFT  = False
				if event.key == pygame.K_s:
					jogador.DOWN  = False
				if event.key == pygame.K_d:
					jogador.RIGHT = False

			if event.type == pygame.MOUSEBUTTONUP:
				if event.button == 1: #ESQUERDO 3, #DIREITO 1
					atirando = False

		color_mask = MASCARA.get_at(jogador.rect.center)
		
		if color_mask == (BRANCO):
			colision_wall = True

		if atirando:
			bullet = Bullet(jogador)
			sprites.add(bullet)
			bullets.add(bullet)

		pewpew.posição(jogador.rect)
		jogador.wall(colision_wall)
		sprites.update()

		colision_bullets = pygame.sprite.groupcollide(bullets, aliens, True, True)
		colision_alien   = pygame.sprite.spritecollide(jogador, aliens, False)

		#if colision_alien:
		#	jogador.kill()
		#	pewpew.kill()
		#jogador.hitbox(npc.rect, colision_npcs)
		
		TELA.blit(FUNDO, FUNDO_RECT)
		sprites.draw(TELA)

		pygame.display.flip()

		colision_wall = False

finally:
	pygame.quit()
