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
	jogador = Jogador(Imagens["FRENTE"], Multiplicador, (int(1920/2), int(1080/2)))
	Grupo = pygame.sprite.Group()
	Grupo.add(jogador)

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

		jogador.atualização()

		Atualizar_O_Plano_De_Fundo(Tela, Imagens["ACADEMIA"], Multiplicador, Grupo, JOGO)

	return SAIR