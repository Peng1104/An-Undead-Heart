import pygame
from GameCode.Game.GameMaker import Game
from GameCode.Configurações import *
from GameCode.Construtores.MenuMaker import Menu, SavedGamesMenu

iniciar_pygame()

#Estado Inicial do Jogo
Estado = EM_JOGO

# Save do Jogo sendo Jogado
Save = -1

RELÓGIO  = pygame.time.Clock()

try:
	while Estado != SAIR:
		
		RELÓGIO.tick(30)

		# Entra no Menu Inicial
		if Estado == INICIAR_JOGO:
			Estado = Menu(DIR_MENU_INICIAL, Estado).run()

		# Entra no Menu das Opções
		elif Estado == MENU_DE_OPÇÕES:
			Estado = Menu(DIR_MENU_DE_OPÇÕES, Estado).run()

		# Mostra os controles do jogo
		elif Estado == CONTROLES:
			Estado = Menu(DIR_CONTROLES, Estado).run()

		# Entra no Menu das configurações de vídeo
		elif Estado == CONFIGURAÇÕES_DE_VÍDEO:
			Estado = Menu(DIR_CONFIGURAÇÕES_DE_VÍDEO, Estado).run()

	colision_wall = False
	atirando = False

	ESTADO = Configurações.MENU_INICIAL

	while ESTADO != Configurações.SAIR:
		
		RELÓGIO.tick(30)

		if ESTADO == Configurações.MENU_INICIAL:

			Configurações.TELA.fill((0, 0, 0, 255))

			#plano_de_fundo = pygame.transform.scale(Configurações.TELA_INICIAL, (int(Configurações.TELA_INICIAL.get_size()[0]*MULTIPLICADOR), int(Configurações.TELA_INICIAL.get_size()[1]*MULTIPLICADOR)))

			Configurações.TELA.blit(Configurações.TELA_INICIAL, Configurações.TELA_INICIAL.get_rect())

			Configurações.pygame.display.flip()

			for event in pygame.event.get():

				if event.type == pygame.QUIT:
					ESTADO = Configurações.SAIR 

				if event.type == pygame.KEYDOWN:

					if event.key == pygame.K_s:
						ESTADO = Configurações.SAIR

					if event.key == pygame.K_j:
						ESTADO = Configurações.EM_JOGO

		if ESTADO == Configurações.TELA_RESULTADOS:

			Configurações.TELA.fill((0, 0, 0, 255))

			Configurações.TELA.blit(Configurações.TELA_FINAL, Configurações.TELA_FINAL.get_rect())

			score_surface = Configurações.FONTE.render("{:08d}".format(Configurações.score), True, Configurações.AMARELO)
			score_rect = score_surface.get_rect()
			score_rect.midtop = (int(Configurações.TELA_FINAL.get_size()[0]*Configurações.MULTIPLICADOR) / 2,  int(Configurações.TELA_FINAL.get_size()[1]*Configurações.MULTIPLICADOR) / 2)
			Configurações.TELA.blit(score_surface, score_rect)

			Configurações.pygame.display.flip()

			for event in pygame.event.get():

				if event.type == pygame.QUIT:
					ESTADO = Configurações.SAIR 

				if event.type == pygame.KEYDOWN:

					if event.key == pygame.K_s:
						ESTADO = Configurações.SAIR

		if ESTADO == Configurações.EM_JOGO:

			Configurações.inimigos_vivos = len(aliens.sprites())

			if Configurações.inimigos_vivos == 0:

				x = random.randint(x, 100)

				for i in range(nivel*x):
					alien = Aliens(jogador)
					sprites.add(alien)
					aliens.add(alien)
					
				nivel = nivel + 1

			for event in pygame.event.get():

				if event.type == pygame.QUIT:
					ESTADO = Configurações.SAIR

				if event.type == pygame.KEYDOWN:

					# Parar o game
					if event.key == pygame.K_q:
						ESTADO = Configurações.SAIR

					if event.key == pygame.K_w:
						jogador.UP    = True
					if event.key == pygame.K_a:
						jogador.LEFT  = True
					if event.key == pygame.K_s:
						jogador.DOWN  = True
					if event.key == pygame.K_d:
						jogador.RIGHT = True

				if event.type == pygame.MOUSEBUTTONDOWN:
					if event.button == 1: #ESQUERDO 1, #DIREITO 3
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
					if event.button == 1: #ESQUERDO 1, #DIREITO 3
						atirando = False

			color_mask = Configurações.MASCARA.get_at(jogador.rect.center)
			
			if color_mask == Configurações.BRANCO:
				colision_wall = True

			if atirando:
				tiro_atual = pygame.time.get_ticks()

				if tiro_atual - ultimo_tiro > COOLDOWN:
					bullet = Bullet(jogador)
					sprites.add(bullet)
					bullets.add(bullet)
					ultimo_tiro = tiro_atual
					Configurações.TIRO.play()

			collision_bullets = pygame.sprite.groupcollide(bullets, aliens, True, True)

			for colisao in collision_bullets:
				if alien.tipo == 0:
					Configurações.score += 1
				if alien.tipo == 1:
					Configurações.score += 2

			collision_alien = pygame.sprite.spritecollide(jogador, aliens, False)

			for colisao in collision_alien:
				dano_atual = pygame.time.get_ticks()

				if dano_atual - ultimo_dano > COOLDOWN_DANO:
					Configurações.vidas -= 1
					ultimo_dano = dano_atual
					jogador.image.set_alpha(125)
			
			dano_atual = pygame.time.get_ticks()
			if (dano_atual - ultimo_dano > COOLDOWN_DANO):
					jogador.image.set_alpha(255)

			arma.posição(jogador.rect)
			jogador.wall(colision_wall)

			Configurações.atualizar_tela(Configurações.FUNDO, sprites, Estado)

			colision_wall = False

			Configurações.timer += 1
			Configurações.tempo_absoluto += 1

			if Configurações.vidas == 0:
				ESTADO = Configurações.TELA_RESULTADOS

finally:

	# Fecha o Jogo
	pygame.quit()