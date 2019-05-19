#Arquivo responsavel por criar o Jogo

import pygame
from GameCode.Construtores.FileController import JSONFile
from GameCode.Configs import IMAGENS_DO_JOGO

Imagens = IMAGENS_DO_JOGO["Game"]

def Start_Game(FilePath, SavedGameNumber, Tela):
	if SavedGameNumber > 0 and SavedGameNumber < 6:
		return Game(JSONFile(FilePath + "/Game_" + str(SavedGameNumber) + ".json"), Tela)
	else:
		return Game(JSONFile(FilePath + "/last_game.json"), Tela)

def Game(JSONFile, Tela):
	print(JSONFile.FilePath)
	return -1