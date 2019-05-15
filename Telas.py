#Arquivo que controla as telas do Jogo
import pygame
from Configs import *
from abc import ABC, abstractmethod

#Função para adequar as Imagens do Tipo Objeto a Dimensão do Jogo
def CriarObjeto(Imagem, Multiplicador):
	if type(Imagem) != pygame.Surface:
		raise TypeError("Imagem não é um Surface")
	elif type(Multiplicador) != float and type(Multiplicador) != int:
		raise TypeError("Multiplicador não é um Número")
	else:
		#Dimensiona a Imagem
		return pygame.transform.scale(Imagem, (int(Imagem.get_size()[0]*Multiplicador), int(Imagem.get_size()[1]*Multiplicador)))

#Função para criar ou alterar o Plano de Fundo do Jogo
def AtualizarPlanodeFundo(Tela, Imagem, Multiplicador):
	if type(Tela) != pygame.Surface:
		raise TypeError("Tela não é um Surface")
	elif type(Imagem) != pygame.Surface:
		raise TypeError("Imagem não é um Surface")
	elif type(Multiplicador) != float and type(Multiplicador) != int:
		raise TypeError("Multiplicador não é um Número")
	elif Imagem.get_size()[0] != 1920 or Imagem.get_size()[1] != 1080:
		raise Exception("A Imagem de Plano de Fundo tem que ser 1920 por 1080")
	else:
		#Dimensiona a Imagem
		Imagem = pygame.transform.scale(Imagem, (int(Imagem.get_size()[0]*Multiplicador), int(Imagem.get_size()[1]*Multiplicador)))

		#Configura a Tela
		Tela.fill((0, 0, 0, 255)) #PRETO
		Tela.blit(Imagem, Imagem.get_rect())
		pygame.display.flip()

		return Tela

class MenuMaker(ABC):

	def __init__(self, Imagens):
		if "Plano de fundo" not in Imagens:
			raise FileNotFoundError("Não foi possivel identificar o arquivo do plano de fundo")
		elif "Localização dos botões" not in Imagens:
			raise FileNotFoundError("Não foi possivel identificar o arquivo da localização dos botões")
		elif Imagens["Plano de fundo"].get_size() != Imagens["Localização dos botões"].get_size():
			raise Exception("O Tamanho da imagem da localização dos botões não é igual a imagem de plano de fundo")
		else:
			super().__init__()
			self.Plano_de_Fundo = Imagens["Plano de fundo"]
			self.Localização_dos_Botões = Imagens["Localização dos botões"]

	#Executa a tela
	def run(self, Tela, Multiplicador):
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

			AtualizarPlanodeFundo(Tela, self.Plano_de_Fundo, Multiplicador)

	@abstractmethod
	def __action__(self, Cor_selecionada):
		pass

class Menu_Principal(MenuMaker):

	def __init__(self, Imagens):
		super().__init__(Imagens)

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

	def __init__(self, Imagens):
		super().__init__(Imagens)

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

	def __init__(self, Imagens):
		super().__init__(Imagens)

	def __action__(self, Cor_selecionada):
		if Cor_selecionada == AMARELO:
			return MENU_DAS_OPÇÕES
		else:
			return SEM_MUDANÇA

#TODO PENSAR MELHOR COMO FAZER
class Menu_De_Video(MenuMaker):

	def __int__(self, Imagens):
		super().__init__(Imagens)

	def __action__(self, Cor_selecionada):
		if Cor_selecionada == AZUL:
			return MENU_DE_VIDEO
		elif Cor_selecionada == VERMELHO:
			return MENU_DE_COMO_JOGAR
		elif Cor_selecionada == VERDE:
			return MENU_DAS_OPÇÕES
		else:
			return SEM_MUDANÇA