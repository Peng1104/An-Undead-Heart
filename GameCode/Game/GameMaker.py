#Arquivo responsavel por criar o Jogo

import pygame
from GameCode.Game.Classes import *
from GameCode.Construtores.Funções_Base import Atualizar_O_Plano_De_Fundo
from GameCode.Construtores.FileController import JSONFile
from GameCode.Configs import IMAGENS_DO_JOGO, SAIR, JOGO

Imagens = IMAGENS_DO_JOGO["Game"]

def Start_Game(SavedGamesDir, SavedGameNumber, Tela, Multiplicador):
	if SavedGameNumber != -1:
		return Game(JSONFile(SavedGamesDir + "/SavedGame-" + str(SavedGameNumber) + ".json"), Tela, Multiplicador)
	else:
		return Game(JSONFile(SavedGamesDir + "/last_game.json"), Tela, Multiplicador)

def Game(JSONFile, Tela, Multiplicador):

	Todos_os_sprites = pygame.sprite.Group()

	Lista_de_Imagens_do_Jogador = [Imagens["FRENTE"], Imagens["ATRAS"], Imagens["DIREITA"], Imagens["ESQUERDA"]]

	jogador = Jogador(Lista_de_Imagens_do_Jogador, Multiplicador, (int(1920/2), int(1080/2)))
	Todos_os_sprites.add(jogador)
	
	NPCs = pygame.sprite.Group()

	NPC1 = NPC(Imagens["NPC1"], Multiplicador, (640,500))
	NPCs.add(NPC1)
	Todos_os_sprites.add(NPC1)

	#Conversas = pygame.sprite.Group()

	#Fala = Falas(Imagens["HITBOX"], Multiplicador, (640,500))
	#Conversas.add(Fala)
	#Todos_os_sprites.add(Fala)

	while True:

		for evento in pygame.event.get():

			if evento.type == pygame.QUIT:
					return SAIR
			
			elif evento.type == pygame.KEYDOWN:

				if evento.key == pygame.K_UP:
					jogador.speed(0, -20)
				if evento.key == pygame.K_LEFT:
					jogador.speed(-20, 0)
				if evento.key == pygame.K_DOWN:
					jogador.speed(0, 20)
				if evento.key == pygame.K_RIGHT:
					jogador.speed(20, 0)

			elif evento.type == pygame.KEYUP:

				if evento.key == pygame.K_UP:
					jogador.speed(0, 0)
				if evento.key == pygame.K_LEFT:
					jogador.speed(0, 0)
				if evento.key == pygame.K_DOWN:
					jogador.speed(0, 0)
				if evento.key == pygame.K_RIGHT:
					jogador.speed(0, 0)

		Colisão_npc = pygame.sprite.spritecollide(jogador,NPCs,False)
		#Colisão_fala = pygame.sprite.spritecollide(jogador,Conversas,False)

		#jogador.Atualiza_Posição(Colisão_fala)
		jogador.Atualiza_Posição(Colisão_npc)

		Todos_os_sprites.update()

		Atualizar_O_Plano_De_Fundo(Tela, Imagens["ACADEMIA"], Multiplicador, Todos_os_sprites, JOGO)

	return SAIR