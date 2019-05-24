# EP 2019-2: Insper Run
#
# Alunos: 
# - Lucas Hix, lucash@al.insper.edu.br
# - Fernando Giuseppe Avila Beltramo, fernandogab@al.insper.edu.br
# - Daniel Gurgel Terra, danielgt1@al.insper.edu.br

from GameCode.Construtores.Funções_Base import *
from GameCode.Construtores.MenuMaker import Menu, SavedGamesMenu
from GameCode.Game.GameMaker import Start_Game

#Cria a Tela do Jogo e da o Multplicador das Imagens além de Iniciar o PyGAME
Multiplicador, Tela = Iniciar_Pygame()

#Estado Inicial do Jogo
Estado = JOGO

#Save do Jogo sendo Jogado
Save = -1

#Runable do Jogo
try:
	while True:

		#PARAR O LOOP
		if Estado == SAIR or Estado == SEM_MUDANÇA:
			break

		#Entra no Menu Principal
		elif Estado == MENU_PRINCIPAL:
			Estado = Menu(CONFIG.getString("Díretorios.Imagens.Menus.Principal", default_value="Menu Principal"), Estado).run(Tela, Multiplicador)

		#Entra no Menu das Opções
		elif Estado == MENU_DAS_OPÇÕES:
			Estado = Menu(CONFIG.getString("Díretorios.Imagens.Menus.Opções", default_value="Menu de Opções"), Estado).run(Tela, Multiplicador)

		#Entra no Menu de Como Jogar
		elif Estado == MENU_DE_COMO_JOGAR:
			Estado = Menu(CONFIG.getString("Díretorios.Imagens.Menus.Como Jogar", default_value="Menu de Como Jogar"), Estado).run(Tela, Multiplicador)

		#Entra no Menu de Vídeo
		elif Estado == MENU_DE_VIDEO:
			Estado = Menu(CONFIG.getString("Díretorios.Imagens.Menus.Vídeo", default_value="Menu de Vídeo"), Estado).run(Tela, Multiplicador)

		#Ativa a Tela cheia e volta para o Menu de Vídeo
		elif Estado == ATIVAR_TELA_CHEIA:
			#Atualiza a Tela e o Multiplicador
			Multiplicador, Tela = Atualizar_Tela(CONFIG.getInt("Nível de Resolução do Jogo"), True)

			#Retorna para o Menu de Vídeo
			Estado = MENU_DE_VIDEO

		#Desativa a Tela cheia e volta para o Menu de Vídeo
		elif Estado == DESATIVAR_TELA_CHEIA:
			#Atualiza a Tela e o Multiplicador
			Multiplicador, Tela = Atualizar_Tela(CONFIG.getInt("Nível de Resolução do Jogo"), False)

			#Retorna para o Menu de Vídeo
			Estado = MENU_DE_VIDEO

		#Troca para a Resolução de 1080p e volta para o Menu de Vídeo
		elif Estado == RESOLUÇÃO_DE_1080P:
			#Atualiza a Tela e o Multiplicador
			Multiplicador, Tela = Atualizar_Tela(6, CONFIG.getBoolean("Tela Cheia"))

			#Retorna para o Menu de Vídeo
			Estado = MENU_DE_VIDEO

		#Troca para a Resolução de 900p e volta para o Menu de Vídeo
		elif Estado == RESOLUÇÃO_DE_900P:
			#Atualiza a Tela e o Multiplicador
			Multiplicador, Tela = Atualizar_Tela(5, CONFIG.getBoolean("Tela Cheia"))

			#Retorna para o Menu de Vídeo
			Estado = MENU_DE_VIDEO

		#Troca para a Resolução de 720p e volta para o Menu de Vídeo
		elif Estado == RESOLUÇÃO_DE_720P:
			#Atualiza a Tela e o Multiplicador
			Multiplicador, Tela = Atualizar_Tela(4, CONFIG.getBoolean("Tela Cheia"))

			#Retorna para o Menu de Vídeo
			Estado = MENU_DE_VIDEO

		#Troca para a Resolução de 576p e volta para o Menu de Vídeo
		elif Estado == RESOLUÇÃO_DE_576P:
			#Atualiza a Tela e o Multiplicador
			Multiplicador, Tela = Atualizar_Tela(3, CONFIG.getBoolean("Tela Cheia"))

			#Retorna para o Menu de Vídeo
			Estado = MENU_DE_VIDEO

		#Troca para a Resolução de 540p e volta para o Menu de Vídeo
		elif Estado == RESOLUÇÃO_DE_540P:
			#Atualiza a Tela e o Multiplicador
			Multiplicador, Tela = Atualizar_Tela(2, CONFIG.getBoolean("Tela Cheia"))

			#Retorna para o Menu de Vídeo
			Estado = MENU_DE_VIDEO

		#Troca para a Resolução de 360p e volta para o Menu de Vídeo
		elif Estado == RESOLUÇÃO_DE_360P:
			#Atualiza a Tela e o Multiplicador
			Multiplicador, Tela = Atualizar_Tela(1, CONFIG.getBoolean("Tela Cheia"))

			#Retorna para o Menu de Vídeo
			Estado = MENU_DE_VIDEO

		#Entra no Menu para selecionar um Jogo Salvo
		elif Estado == MENU_PARA_CARREGAR_JOGO_SALVO:
			Estado, Save = SavedGamesMenu(CONFIG.getString("Díretorios.Imagens.Menus.Carregar Save", default_value="Menu para Carregar Jogo Salvo"), Estado).run(Tela, Multiplicador, CONFIG.getString("Díretorios.Jogos Salvos", default_value="Jogos Salvos"))

		#Entra no Menu para criar um Novo Jogo
		elif Estado == MENU_DE_NOVO_JOGO:
			Estado = Menu(CONFIG.getString("Díretorios.Imagens.Menus.Novo Jogo", default_value="Menu de Novo Jogo"), Estado).run(Tela, Multiplicador)

		#Vai para o Jogo
		elif Estado == JOGO:
			Estado = Start_Game(CONFIG.getString("Díretorios.Jogos Salvos", default_value="Jogos Salvos"), Save, Tela, Multiplicador)

		#Estado Desconhecido = Para o Jogo
		else:
			break

finally:
	#Fecha o Jogoz
	pygame.quit()

	#Salva o Config.yml
	CONFIG.save()