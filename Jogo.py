# EP 2019-2: Insper Run
#
# Alunos: 
# - Lucas Hix, lucash@al.insper.edu.br
# - Fernando Giuseppe Avila Beltramo, fernandogab@al.insper.edu.br
# - Daniel Gurgel Terra, danielgt1@al.insper.edu.br

import pygame
from GameCode.Configs import *
from GameCode.MenuMaker import MenuMaker

#EM FASE DE TESTES
from GameCode.tela_jogo import tela_jogo

def MakeScreen(Nível_de_Resolução, Tela_Cheia):
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

#Cria a Tela do Jogo e da o Multplicador das Imagens
MULTIPLICADOR, TELA = MakeScreen(CONFIG.getInt("Nível de Resolução do Jogo"), CONFIG.getBoolean("Tela Cheia", default_value=False))

#Estado Inicial do Jogo
Estado = MENU_PRINCIPAL

#Runable do Jogo
try:
	while True:

		#Fechando o Jogo atravez do X
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				Estado = SAIR
				break

		#PARAR O LOOP
		if Estado == SAIR or Estado == SEM_MUDANÇA:
			break

		#Entra no Menu Principal
		elif Estado == MENU_PRINCIPAL:
			Estado = MenuMaker("Menu Principal").run(Tela, MULTIPLICADOR)

		#Entra no Menu das Opções
		elif Estado == MENU_DAS_OPÇÕES:
			Estado = MenuMaker("Menu de Opções").run(Tela, MULTIPLICADOR)

		#Entra no Menu de Como Jogar
		elif Estado == MENU_DE_COMO_JOGAR:
			Estado = MenuMaker("Menu de Como Jogar").run(Tela, MULTIPLICADOR)

		#Entra no Menu de Vídeo
		elif Estado == MENU_DE_VIDEO:
			Estado = MenuMaker("Menu de Vídeo").run(Tela, MULTIPLICADOR)

		#Ativa a Tela cheia e volta para o Menu de Vídeo
		elif Estado == ATIVAR_TELA_CHEIA:
			#Atualiza a Tela e o Multiplicador
			MULTIPLICADOR, TELA = MakeScreen(CONFIG.getInt("Nível de Resolução do Jogo"), True)

			#Retorna para o Menu de Vídeo
			Estado = MENU_DE_VIDEO

		#Desativa a Tela cheia e volta para o Menu de Vídeo
		elif Estado == DESATIVAR_TELA_CHEIA:
			#Atualiza a Tela e o Multiplicador
			MULTIPLICADOR, TELA = MakeScreen(CONFIG.getInt("Nível de Resolução do Jogo"), False)

			#Retorna para o Menu de Vídeo
			Estado = MENU_DE_VIDEO

		#Troca para a Resolução de 1080p e volta para o Menu de Vídeo
		elif Estado == RESOLUÇÃO_DE_1080P:
			#Atualiza a Tela e o Multiplicador
			MULTIPLICADOR, TELA = MakeScreen(6, CONFIG.getBoolean("Tela Cheia"))

			#Retorna para o Menu de Vídeo
			Estado = MENU_DE_VIDEO

		#Troca para a Resolução de 900p e volta para o Menu de Vídeo
		elif Estado == RESOLUÇÃO_DE_900P:
			#Atualiza a Tela e o Multiplicador
			MULTIPLICADOR, TELA = MakeScreen(5, CONFIG.getBoolean("Tela Cheia"))

			#Retorna para o Menu de Vídeo
			Estado = MENU_DE_VIDEO

		#Troca para a Resolução de 720p e volta para o Menu de Vídeo
		elif Estado == RESOLUÇÃO_DE_720P:
			#Atualiza a Tela e o Multiplicador
			MULTIPLICADOR, TELA = MakeScreen(4, CONFIG.getBoolean("Tela Cheia"))

			#Retorna para o Menu de Vídeo
			Estado = MENU_DE_VIDEO

		#Troca para a Resolução de 576p e volta para o Menu de Vídeo
		elif Estado == RESOLUÇÃO_DE_576P:
			#Atualiza a Tela e o Multiplicador
			MULTIPLICADOR, TELA = MakeScreen(3, CONFIG.getBoolean("Tela Cheia"))

			#Retorna para o Menu de Vídeo
			Estado = MENU_DE_VIDEO

		#Troca para a Resolução de 540p e volta para o Menu de Vídeo
		elif Estado == RESOLUÇÃO_DE_540P:
			#Atualiza a Tela e o Multiplicador
			MULTIPLICADOR, TELA = MakeScreen(2, CONFIG.getBoolean("Tela Cheia"))

			#Retorna para o Menu de Vídeo
			Estado = MENU_DE_VIDEO

		#Troca para a Resolução de 360p e volta para o Menu de Vídeo
		elif Estado == RESOLUÇÃO_DE_360P:
			#Atualiza a Tela e o Multiplicador
			MULTIPLICADOR, TELA = MakeScreen(1, CONFIG.getBoolean("Tela Cheia"))

			#Retorna para o Menu de Vídeo
			Estado = MENU_DE_VIDEO

		#Entra no Menu para selecionar um Jogo Salvo
		elif Estado == MENU_PARA_CARREGAR_JOGO_SALVO:
			Estado = MenuMaker("Menu para Carregar Jogo Salvo").run(Tela, MULTIPLICADOR)

		#Entra no Menu para criar um Novo Jogo
		elif Estado == MENU_DE_NOVO_JOGO:
			Estado = MenuMaker("Menu de Novo Jogo").run(Tela, MULTIPLICADOR)

		#Vai para o Jogo
		elif Estado == JOGO:
			Estado = tela_jogo(Tela)

		#Estado Desconhecido = Para o Jogo
		else:
			break

finally:
	#Fecha o Jogo
	pygame.quit()