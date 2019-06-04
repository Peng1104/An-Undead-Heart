import pygame
from GameCode.Game.GameMaker import Game
from GameCode.Configurações import *
from GameCode.Construtores.MenuMaker import Menu, SavedGamesMenu

iniciar_pygame()

#Estado Inicial do Jogo
Estado = EM_JOGO

# Save do Jogo sendo Jogado
Save = -1

RELÓGIO  = pygame.time.Clock()

try:
	while Estado != SAIR:
		
		RELÓGIO.tick(30)

		# Entra no Menu Inicial
		if Estado == INICIAR_JOGO:
			Estado = Menu(DIR_MENU_INICIAL, Estado).run()

		# Entra no Menu das Opções
		elif Estado == MENU_DE_OPÇÕES:
			Estado = Menu(DIR_MENU_DE_OPÇÕES, Estado).run()

		# Mostra os controles do jogo
		elif Estado == CONTROLES:
			Estado = Menu(DIR_CONTROLES, Estado).run()

		# Entra no Menu das configurações de vídeo
		elif Estado == CONFIGURAÇÕES_DE_VÍDEO:
			Estado = Menu(DIR_CONFIGURAÇÕES_DE_VÍDEO, Estado).run()

		# Ativa a Tela cheia e volta para o Menu das configurações de vídeo
		elif Estado == ATIVAR_TELA_CHEIA:

			# Redimenciona a tela do jogo
			redimencionar_tela(CONFIG.getInt("Nível de Resolução do Jogo"), True)

			# Retorna para o Menu das configurações de vídeo
			Estado = CONFIGURAÇÕES_DE_VÍDEO

		#Desativa a Tela cheia e volta para o Menu das configurações de vídeo
		elif Estado == DESATIVAR_TELA_CHEIA:

			# Redimenciona a tela do jogo
			redimencionar_tela(CONFIG.getInt("Nível de Resolução do Jogo"), False)

			# Retorna para o Menu das configurações de vídeo
			Estado = CONFIGURAÇÕES_DE_VÍDEO

		#Troca para a Resolução de 1080p e volta para o Menu das configurações de vídeo
		elif Estado == RESOLUÇÃO_DE_1080P:

			# Redimenciona a tela do jogo
			redimencionar_tela(6, CONFIG.getBoolean("Tela Cheia"))

			# Retorna para o Menu das configurações de vídeo
			Estado = CONFIGURAÇÕES_DE_VÍDEO

		#Troca para a Resolução de 900p e volta para o Menu das configurações de vídeo
		elif Estado == RESOLUÇÃO_DE_900P:

			# Redimenciona a tela do jogo
			redimencionar_tela(5, CONFIG.getBoolean("Tela Cheia"))

			# Retorna para o Menu das configurações de vídeo
			Estado = CONFIGURAÇÕES_DE_VÍDEO

		#Troca para a Resolução de 720p e volta para o Menu das configurações de vídeo
		elif Estado == RESOLUÇÃO_DE_720P:

			# Redimenciona a tela do jogo
			redimencionar_tela(4, CONFIG.getBoolean("Tela Cheia"))

			# Retorna para o Menu das configurações de vídeo
			Estado = CONFIGURAÇÕES_DE_VÍDEO

		#Troca para a Resolução de 576p e volta para o Menu das configurações de vídeo
		elif Estado == RESOLUÇÃO_DE_576P:

			# Redimenciona a tela do jogo
			redimencionar_tela(3, CONFIG.getBoolean("Tela Cheia"))

			# Retorna para o Menu das configurações de vídeo
			Estado = CONFIGURAÇÕES_DE_VÍDEO

		#Troca para a Resolução de 540p e volta para o Menu das configurações de vídeo
		elif Estado == RESOLUÇÃO_DE_540P:

			# Redimenciona a tela do jogo
			redimencionar_tela(2, CONFIG.getBoolean("Tela Cheia"))

			# Retorna para o Menu das configurações de vídeo
			Estado = CONFIGURAÇÕES_DE_VÍDEO

		#Troca para a Resolução de 360p e volta para o Menu das configurações de vídeo
		elif Estado == RESOLUÇÃO_DE_360P:

			# Redimenciona a tela do jogo
			redimencionar_tela(1, CONFIG.getBoolean("Tela Cheia"))

			# Retorna para o Menu das configurações de vídeo
			Estado = CONFIGURAÇÕES_DE_VÍDEO

		# Entra no Menu para selecionar um jogo salvo
		elif Estado == MENU_DOS_JOGOS_SALVOS:
			Estado, Save = SavedGamesMenu(DIR_MENU_DOS_JOGO_SALVO, Estado).run()

		# Entra no Menu para criar um novo jogo
		elif Estado == INICIAR_NOVO_JOGO:
			Estado = Menu(DIR_INICIAR_NOVO_JOGO, Estado).run()

		# Vai para o jogo
		elif Estado == EM_JOGO:
			Estado = Game()

		# Estado Desconhecido (Ou estado para para o jogo) = Para o Jogo
		else:
			break

finally:

	# Fecha o Jogo
	pygame.quit()