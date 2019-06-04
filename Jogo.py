import Configurações
import random
from Classes import *

Configurações.iniciar_pygame()

#Estado Inicial do Jogo
Estado = Configurações.INICIAR_JOGO

#Save do Jogo sendo Jogado
Save = -1

RELÓGIO  = pygame.time.Clock()

COOLDOWN = 100

ultimo_tiro = pygame.time.get_ticks() - COOLDOWN

sprites = pygame.sprite.Group()

jogador = Jogador()
sprites.add(jogador)

aliens = pygame.sprite.Group()

# Vareavel de Sorte
x = random.randint(0, 100)

for i in range(x):
	alien = Aliens(jogador)
	sprites.add(alien)
	aliens.add(alien)

arma = Arma(jogador)
sprites.add(arma)
	
bullets = pygame.sprite.Group()

nivel = 1

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

		inimigos_vivos = len(aliens.sprites())

		if inimigos_vivos == 0:

			x = random.randint(x, 100)

			for i in range(nivel*x):
				alien = Aliens(jogador)
				sprites.add(alien)
				aliens.add(alien)
				
			nivel = nivel + 1

		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				running = False

			if event.type == pygame.KEYDOWN:

				# Parar o game
				if event.key == pygame.K_q:
					running = False
					break

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
				score += 1
			if alien.tipo == 1:
				score += 2

		collision_alien = pygame.sprite.spritecollide(jogador, aliens, False)

		#if collision_alien:
		#	if 

		arma.posição(jogador.rect)
		jogador.wall(colision_wall)

		score_surface = Configurações.FONTE.render("{:08d}".format(score), True, Configurações.AMARELO)
		score_rect = score_surface.get_rect()
		score_rect.midtop = (Configurações.getTamanho_Tela()[0] / 2,  10)
		Configurações.TELA.blit(score_surface, score_rect)

		segundos = int(timer/30)
		if (timer/30) == 60:
			minutos += 1
			timer = 0

		timer_surface = Configurações.FONTE.render("{0:02d}:{1:02d}".format(minutos,segundos), True, Configurações.BRANCO)
		timer_rect = timer_surface.get_rect()
		timer_rect.left = 5
		timer_rect.top = 10
		Configurações.TELA.blit(timer_surface, timer_rect)

		text_surface = Configurações.SIMBOLO.render("E" * vidas, True, Configurações.VERMELHO)
		text_rect = text_surface.get_rect()
		text_rect.bottomleft = (10, Configurações.getTamanho_Tela()[1] - 10)
		Configurações.TELA.blit(text_surface, text_rect)

		Configurações.atualizar_tela(Configurações.FUNDO, sprites, Estado)

		colision_wall = False

		timer += 1

finally:
	pygame.quit()