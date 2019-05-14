#Arquivo que controla as telas do Jogo
import pygame
import Default

def Menu_Principal(tela, Imagens, tamanho):
	plano_de_fundo = Imagens["Imagem"][0]
	plano_de_fundo = pygame.transform.scale(plano_de_fundo, tamanho)
	rect_do_plano_de_fundo = Imagens["Imagem"][1]
	localização_dos_botões = Imagens["Localização Botões"][0]

	while True:
		for event in pygame.event.get():

			#Verefica se clicou no X
			if event.type == pygame.QUIT:
				return Default.SAIR

			#PegaPosição do Mouse
			mouse_x, mouse_y = pygame.mouse.get_pos()

			#Verficia se o jogador clicou
			if event.type == pygame.MOUSEBUTTONDOWN:
				#Pega a cor selecionada
				Cor_selecionada = localização_dos_botões.get_at((mouse_x,mouse_y))

				if Cor_selecionada == Default.AZUL:
					return Default.NOVO_JOGO
				elif Cor_selecionada == Default.AMARELO:
					return Default.CARREGAR_JOGO
				elif Cor_selecionada == Default.VERMELHO:
					return Default.OPÇÕES
				elif Cor_selecionada == Default.VERDE:
					return Default.SAIR

			tela.fill(Default.PRETO)
			tela.blit(plano_de_fundo, rect_do_plano_de_fundo)
			pygame.display.flip()