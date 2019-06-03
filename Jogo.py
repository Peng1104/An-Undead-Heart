from Configurações import *
from Classes import *

iniciar_pygame()

#Estado Inicial do Jogo
Estado = INICIAR_JOGO

#Save do Jogo sendo Jogado
Save = -1

RELÓGIO  = pygame.time.Clock()

COOLDOWN = 100

ultimo_tiro = pygame.time.get_ticks() - COOLDOWN

sprites = pygame.sprite.Group()

jogador = Jogador()
sprites.add(jogador)

aliens = pygame.sprite.Group()

for i in range(10):
	alien = Aliens(jogador)
	sprites.add(alien)
	aliens.add(alien)

pewpew = Pewpew(jogador)
sprites.add(pewpew)
	
bullets = pygame.sprite.Group()

try:

	pygame.mixer.music.play(loops=-1)

	score = 0

	vidas = 5
	timer = 0
	minutos  = 0

	colision_wall = False
	atirando = False
	running = True

	while running:
		
		RELÓGIO.tick(30)
		#atirando = False

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

		color_mask = MASCARA.get_at(jogador.rect.center)
		
		if color_mask == (BRANCO):
			colision_wall = True

		if atirando:
			tiro_atual = pygame.time.get_ticks()

			if tiro_atual - ultimo_tiro > COOLDOWN:
				bullet = Bullet(jogador)
				sprites.add(bullet)
				bullets.add(bullet)
				ultimo_tiro = tiro_atual

		collision_bullets = pygame.sprite.groupcollide(bullets, aliens, True, True)

		for colisao in collision_bullets:
			if alien.tipo == 0:
				score += 1
			if alien.tipo == 1:
				score += 2

		collision_alien = pygame.sprite.spritecollide(jogador, aliens, False)

		#if collision_alien:
		#	if 

		pewpew.posição(jogador.rect)
		jogador.wall(colision_wall)
		sprites.update()
		
		TELA.blit(FUNDO, FUNDO_RECT)
		sprites.draw(TELA)

		score_surface = FONTE.render("{:08d}".format(score), True, AMARELO)
		score_rect = score_surface.get_rect()
		score_rect.midtop = (LARGURA / 2,  10)
		TELA.blit(score_surface, score_rect)

		segundos = int(timer/30)
		if (timer/30) == 60:
			minutos += 1
			timer = 0

		timer_surface = FONTE.render("{0:02d}:{1:02d}".format(minutos,segundos), True, BRANCO)
		timer_rect = timer_surface.get_rect()
		timer_rect.left = 5
		timer_rect.top = 10
		TELA.blit(timer_surface, timer_rect)

		text_surface = SIMBOLO.render("E" * vidas, True, VERMELHO)
		text_rect = text_surface.get_rect()
		text_rect.bottomleft = (10, ALTURA - 10)
		TELA.blit(text_surface, text_rect)

		pygame.display.flip()

		colision_wall = False

		timer += 1

finally:
	pygame.quit()