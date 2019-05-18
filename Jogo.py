# EP 2019-2: Insper Run
#
# Alunos: 
# - Lucas Hix, lucash@al.insper.edu.br
# - Fernando Giuseppe Avila Beltramo, fernandogab@al.insper.edu.br
# - Daniel Gurgel Terra, danielgt1@al.insper.edu.br

from GameCode.Construtores.Funções_Base import *
from GameCode.MenuMaker import Menu

#EM FASE DE TESTES
from GameCode.tela_jogo import tela_jogo

#Cria a Tela do Jogo e da o Multplicador das Imagens além de Iniciar o PyGAME
MULTIPLICADOR, TELA = Iniciar_Pygame()

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
			Estado = Menu("Menu Principal", Estado).run(TELA, MULTIPLICADOR)

		#Entra no Menu das Opções
		elif Estado == MENU_DAS_OPÇÕES:
			Estado = Menu("Menu de Opções", Estado).run(TELA, MULTIPLICADOR)

		#Entra no Menu de Como Jogar
		elif Estado == MENU_DE_COMO_JOGAR:
			Estado = Menu("Menu de Como Jogar", Estado).run(TELA, MULTIPLICADOR)

		#Entra no Menu de Vídeo
		elif Estado == MENU_DE_VIDEO:
			Estado = Menu("Menu de Vídeo", Estado).run(TELA, MULTIPLICADOR)

		#Ativa a Tela cheia e volta para o Menu de Vídeo
		elif Estado == ATIVAR_TELA_CHEIA:
			#Atualiza a Tela e o Multiplicador
			MULTIPLICADOR, TELA = Atualizar_Tela(CONFIG.getInt("Nível de Resolução do Jogo"), True)

			#Retorna para o Menu de Vídeo
			Estado = MENU_DE_VIDEO

		#Desativa a Tela cheia e volta para o Menu de Vídeo
		elif Estado == DESATIVAR_TELA_CHEIA:
			#Atualiza a Tela e o Multiplicador
			MULTIPLICADOR, TELA = Atualizar_Tela(CONFIG.getInt("Nível de Resolução do Jogo"), False)

			#Retorna para o Menu de Vídeo
			Estado = MENU_DE_VIDEO

		#Troca para a Resolução de 1080p e volta para o Menu de Vídeo
		elif Estado == RESOLUÇÃO_DE_1080P:
			#Atualiza a Tela e o Multiplicador
			MULTIPLICADOR, TELA = Atualizar_Tela(6, CONFIG.getBoolean("Tela Cheia"))

			#Retorna para o Menu de Vídeo
			Estado = MENU_DE_VIDEO

		#Troca para a Resolução de 900p e volta para o Menu de Vídeo
		elif Estado == RESOLUÇÃO_DE_900P:
			#Atualiza a Tela e o Multiplicador
			MULTIPLICADOR, TELA = Atualizar_Tela(5, CONFIG.getBoolean("Tela Cheia"))

			#Retorna para o Menu de Vídeo
			Estado = MENU_DE_VIDEO

		#Troca para a Resolução de 720p e volta para o Menu de Vídeo
		elif Estado == RESOLUÇÃO_DE_720P:
			#Atualiza a Tela e o Multiplicador
			MULTIPLICADOR, TELA = Atualizar_Tela(4, CONFIG.getBoolean("Tela Cheia"))

			#Retorna para o Menu de Vídeo
			Estado = MENU_DE_VIDEO

		#Troca para a Resolução de 576p e volta para o Menu de Vídeo
		elif Estado == RESOLUÇÃO_DE_576P:
			#Atualiza a Tela e o Multiplicador
			MULTIPLICADOR, TELA = Atualizar_Tela(3, CONFIG.getBoolean("Tela Cheia"))

			#Retorna para o Menu de Vídeo
			Estado = MENU_DE_VIDEO

		#Troca para a Resolução de 540p e volta para o Menu de Vídeo
		elif Estado == RESOLUÇÃO_DE_540P:
			#Atualiza a Tela e o Multiplicador
			MULTIPLICADOR, TELA = Atualizar_Tela(2, CONFIG.getBoolean("Tela Cheia"))

			#Retorna para o Menu de Vídeo
			Estado = MENU_DE_VIDEO

		#Troca para a Resolução de 360p e volta para o Menu de Vídeo
		elif Estado == RESOLUÇÃO_DE_360P:
			#Atualiza a Tela e o Multiplicador
			MULTIPLICADOR, TELA = Atualizar_Tela(1, CONFIG.getBoolean("Tela Cheia"))

			#Retorna para o Menu de Vídeo
			Estado = MENU_DE_VIDEO

		#Entra no Menu para selecionar um Jogo Salvo
		elif Estado == MENU_PARA_CARREGAR_JOGO_SALVO:
			Estado = Menu("Menu para Carregar Jogo Salvo", Estado).run(TELA, MULTIPLICADOR)

		#Entra no Menu para criar um Novo Jogo
		elif Estado == MENU_DE_NOVO_JOGO:
			Estado = Menu("Menu de Novo Jogo", Estado).run(TELA, MULTIPLICADOR)

		#Vai para o Jogo
		elif Estado == JOGO:
			Estado = tela_jogo(TELA)

		#Estado Desconhecido = Para o Jogo
		else:
			break

finally:
	#Fecha o Jogo
	pygame.quit()