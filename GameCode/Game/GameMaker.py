#Arquivo responsavel por criar o Jogo

import pygame
from os import path
from GameCode.Game.Classes import *
import GameCode.Configurações as Configurações

#=======================================================================================================================#

JOGADOR    = Configurações.IMAGENS[Configurações.DIR_GAME[Configurações.DIR_GAME.rfind("/")+1:]]["Imagens"]["JOGADOR"]
JOGADOR    = pygame.transform.scale( JOGADOR, (50,50) )
JOGADOR.set_colorkey(Configurações.VERMELHO)

ALIEN_1    = Configurações.IMAGENS[Configurações.DIR_GAME[Configurações.DIR_GAME.rfind("/")+1:]]["Imagens"]["ALIEN1"]
ALIEN_1    = pygame.transform.scale( ALIEN_1, (50,50) )
ALIEN_1.set_colorkey(Configurações.PRETO)

ALIEN_2    = Configurações.IMAGENS[Configurações.DIR_GAME[Configurações.DIR_GAME.rfind("/")+1:]]["Imagens"]["ALIEN2"]
ALIEN_2    = pygame.transform.scale( ALIEN_2, (50,50) )
ALIEN_2.set_colorkey(Configurações.PRETO)

ARMA       = Configurações.IMAGENS[Configurações.DIR_GAME[Configurações.DIR_GAME.rfind("/")+1:]]["Imagens"]["ARMA"]
ARMA       = pygame.transform.scale( ARMA, (50,50) )
ARMA.set_colorkey((255, 255, 255, 0))

BULLET     = Configurações.IMAGENS[Configurações.DIR_GAME[Configurações.DIR_GAME.rfind("/")+1:]]["Imagens"]["BULLET"]
BULLET.set_colorkey((255, 255, 255, 0))

FUNDO      = Configurações.IMAGENS[Configurações.DIR_GAME[Configurações.DIR_GAME.rfind("/")+1:]]["Imagens"]["FUNDO"]

#=======================================================================================================================#

FONTE      = pygame.font.Font(path.join(Configurações.DIR_GAME, "Fontes/FONTE.ttf"), 28)

SIMBOLO    = pygame.font.Font(path.join(Configurações.DIR_GAME, "Fontes/SYMBOL_1.otf"), 32)

#=======================================================================================================================#

pygame.mixer.music.load(path.join(Configurações.DIR_GAME + "/Sons", 'Musica_de_Fundo.ogg'))
pygame.mixer.music.set_volume(0.4)

TIRO = Configurações.SONS[Configurações.DIR_GAME[Configurações.DIR_GAME.rfind("/")+1:]]["Sons"]["Tiro"]
TIRO.set_volume(0.05)

#=======================================================================================================================#

def Game():

	COOLDOWN = 100
	COOLDOWN_DANO = 1500

	ultimo_tiro = pygame.time.get_ticks() - COOLDOWN
	ultimo_dano = pygame.time.get_ticks() - COOLDOWN_DANO

	sprites = pygame.sprite.Group()

	jogador = Jogador(JOGADOR, Configurações.getTamanho_Tela())

	sprites.add(jogador)

	aliens = pygame.sprite.Group()

	# Vareavel de Sorte
	x = random.randint(0, 10)

	for i in range(x):
		alien = Aliens(jogador, ALIEN_1, ALIEN_2, Configurações.getTamanho_Tela())
		sprites.add(alien)
		aliens.add(alien)

	arma = Arma(jogador, ARMA)
	sprites.add(arma)
		
	bullets = pygame.sprite.Group()

	nivel = 1

	pygame.mixer.music.play(loops=-1)

	colision_wall = False
	atirando = False

	while True:

		Configurações.inimigos_vivos = len(aliens.sprites())

		if Configurações.inimigos_vivos == 0:

			x = random.randint(x, 100)

			for i in range(nivel*x):
				alien = Aliens(jogador, ALIEN_1, ALIEN_2, Configurações.getTamanho_Tela())
				sprites.add(alien)
				aliens.add(alien)
				
			nivel = nivel + 1

		for event in pygame.event.get():

			if event.type == pygame.QUIT:
					return Configurações.SAIR
			
			if event.type == pygame.KEYDOWN:

				if event.key == pygame.K_q:
					return Configurações.SAIR
					
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
				bullet = Bullet(jogador, BULLET, Configurações.getTamanho_Tela())
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

		Configurações.atualizar_tela(FUNDO, sprites, Configurações.EM_JOGO)

		colision_wall = False

		Configurações.timer += 1
		Configurações.tempo_absoluto += 1

		if Configurações.vidas == 0:
			return Configurações.SAIR

	return Configurações.SAIR