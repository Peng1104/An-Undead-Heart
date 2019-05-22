#Arquivo que contem as Funções de Base do Jogo

import pygame
from GameCode.Configs import *

#Função para criar ou alterar a Tela do Jogo
def Atualizar_Tela(Nível_de_Resolução, Tela_Cheia):
	#Atualiza a regra no Config
	CONFIG.set("Tela Cheia", Tela_Cheia)
	CONFIG.set("Nível de Resolução do Jogo", Nível_de_Resolução)
	CONFIG.save()

	#Atualiza o Multiplicador
	Multiplicador = MULTIPLICADORES[Nível_de_Resolução]

	if Tela_Cheia:
		return Multiplicador, pygame.display.set_mode((int(1920*Multiplicador), int(1080*Multiplicador)), flags=pygame.FULLSCREEN)
	else:
		return Multiplicador, pygame.display.set_mode((int(1920*Multiplicador), int(1080*Multiplicador)))

#Função para Iniciar o pygame
def Iniciar_Pygame():
	#Inicia o Jogo
	pygame.init()

	#Vareavel do Clock (FPS)
	if CONFIG.getFloat("FPS", default_value=60) < 1.0:
		CONFIG.set("FPS", 60)

	#Ativa o Clock do Jogo
	pygame.time.Clock().tick(CONFIG.getFloat("FPS", default_value=60))

	#Aplicar nome do Jogo a Janela do Jogo
	pygame.display.set_caption(CONFIG.getString("Nome do Jogo", default_value="An Undead Heart"))

	#Vareavel de Resolução do Jogo
	if CONFIG.getInt("Nível de Resolução do Jogo", default_value=4) > 6 or CONFIG.getInt("Nível de Resolução do Jogo") < 1:
		CONFIG.set("Nível de Resolução do Jogo", 4)

	return Atualizar_Tela(CONFIG.getInt("Nível de Resolução do Jogo"), CONFIG.getBoolean("Tela Cheia", default_value=False))

#Função para criar ou alterar o Plano de Fundo do Jogo
def Atualizar_O_Plano_De_Fundo(Tela, Plano_De_Fundo, Multiplicador, Group, Estado):
	if type(Tela) != pygame.Surface:
		raise TypeError("Tela não é um pygame.Surface")
	elif type(Plano_De_Fundo) != pygame.Surface:
		raise TypeError("Plano_De_Fundo não é um pygame.Surface")
	elif type(Estado) != int:
		raise TypeError("Estado não é um Inteiro")
	elif Estado != JOGO and (Plano_De_Fundo.get_size()[0] != 1920 or Plano_De_Fundo.get_size()[1] != 1080):
		raise Exception("A Imagem de Plano de Fundo tem que ser 1920 por 1080")
	elif type(Multiplicador) != float and type(Multiplicador) != int:
		raise TypeError("Multiplicador não é um Número")
	elif type(Group) != pygame.sprite.Group:
		raise TypeError("Group não é um pygame.sprite.Group")
	else:
		#Dimensiona a Plano_De_Fundo de Plano de Fundo
		Plano_De_Fundo = pygame.transform.scale(Plano_De_Fundo, (int(Plano_De_Fundo.get_size()[0]*Multiplicador), int(Plano_De_Fundo.get_size()[1]*Multiplicador)))

		#Prenche a Tela de PRETO
		Tela.fill((0, 0, 0, 255))
		#Aplica o Plano de Fundo a Tela
		Tela.blit(Plano_De_Fundo, Plano_De_Fundo.get_rect())

		#Desenha os Spites na Tela
		Group.draw(Tela)
		#Inverte o Display
		pygame.display.flip()

		return Tela