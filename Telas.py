#Arquivo que controla as telas do Jogo
import pygame
from Default import *
from abc import ABC, abstractmethod

class MenuMaker(ABC):

	def __init__(self, Imagens, Tamanho):
		if "Imagem" not in Imagens or "Localização Dos Botões" not in Imagens or Imagens["Imagem"][1] != Imagens["Localização Dos Botões"][1]:
			print("Erro-Imagem:", not("Imagem" not in Imagens))
			print("Erro-Localização-Dos-Botões:", not("Localização Dos Botões" not in Imagens))
			print("Erro de Tamanho:", not(Imagens["Imagem"][1] != Imagens["Localizaçã Dos Botões"][1]))
			raise Error()
		else:
			super().__init__()
			self.Plano_de_Fundo = pygame.transform.scale(Imagens["Imagem"][0], Tamanho)
			self.Rect_do_Plano_de_Fundo = self.Plano_de_Fundo.get_rect()
			self.Localização_dos_Botões = pygame.transform.scale(Imagens["Localização Dos Botões"][0], Tamanho)

	#Executa a tela
	def run(self, Tela):
		while True:
			for event in pygame.event.get():

				#Verifica se clicou no X
				if event.type == pygame.QUIT:
					return SAIR

				#PegaPosição do Mouse
				mouse_x, mouse_y = pygame.mouse.get_pos()

				#Verficia se o jogador clicou
				if event.type == pygame.MOUSEBUTTONDOWN:

					#Pega a cor selecionada
					__action__ = self.__action__(self.Localização_dos_Botões.get_at((mouse_x, mouse_y)))

					#Mundaça de Estado do Jogo
					if __action__ != -1:
						return __action__

			#Atualiza a Tela do Jogo
			Tela.fill(PRETO)
			Tela.blit(self.Plano_de_Fundo, self.Rect_do_Plano_de_Fundo)
			pygame.display.flip()

	@abstractmethod
	def __action__(self, Cor_selecionada):
		pass

class Menu_Principal(MenuMaker):

	def __init__(self, Imagens, Tamanho):
		super().__init__(Imagens, Tamanho)

	def __action__(self, Cor_selecionada):
		if Cor_selecionada == AZUL:
			return NOVO_JOGO
		elif Cor_selecionada == AMARELO:
			return CARREGAR_JOGO
		elif Cor_selecionada == VERMELHO:
			return MENU_DAS_OPÇÕES
		elif Cor_selecionada == VERDE:
			return SAIR
		else:
			return SEM_MUDANÇA

class Menu_De_Opções(MenuMaker):

	def __init__(self, Imagens, Tamanho):
		super().__init__(Imagens, Tamanho)

	def __action__(self, Cor_selecionada):
		if Cor_selecionada == AZUL:
			return MENU_DE_VIDEO
		elif Cor_selecionada == VERMELHO:
			return MENU_DE_COMO_JOGAR
		elif Cor_selecionada == VERDE:
			return MENU_PRINCIPAL
		else:
			return SEM_MUDANÇA

class Menu_De_Como_Jogar(MenuMaker):

	def __init__(self, Imagens, Tamanho):
		super().__init__(Imagens, Tamanho)

	def __action__(self, Cor_selecionada):
		if Cor_selecionada == VERDE:
			return MENU_PRINCIPAL
		else:
			return SEM_MUDANÇA

#TODO PENSAR MELHOR COMO FAZER
class Menu_De_Video(MenuMaker):

	def __int__(self, Imagens, Tamanho):
		super().__init__(Imagens, Tamanho)

	def __action__(self, Cor_selecionada):
		if Cor_selecionada == AZUL:
			return MENU_DE_VIDEO
		elif Cor_selecionada == VERMELHO:
			return MENU_DE_COMO_JOGAR
		elif Cor_selecionada == VERDE:
			return Menu_De_Opções
		else:
			return SEM_MUDANÇA