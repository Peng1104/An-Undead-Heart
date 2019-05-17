#Arquivo para criar as Telas dos Menus

from GameCode.Configs import IMAGENS_DO_JOGO, SEM_MUDANÇA, SAIR, Dir_Imagens, YamlFile, path
from GameCode.Construtor import *

class MenuButton(NewObject):

	def __init__(self, ImagemOriginal, Multiplicador, Posição, Imagem2, Ação):
		if type(Imagem2) != pygame.Surface:
			raise TypeError("Imagem2 não é um pygame.Surface")
		elif type(Ação) != int:
			raise TypeError("Ação tem que ser um Inteiro")
		elif ImagemOriginal.get_size() != Imagem2.get_size():
			raise Exception("O tamanho da Imagem2 não é Igual a ImagemOriginal")
		else:
			super().__init__(ImagemOriginal, Multiplicador, Posição)

			#Define a ação do Botão
			self.Ação = Ação
			#Define a imagem Orinal do Botão
			self.ImagemOriginal = ImagemOriginal
			#Dedfine a imagem de quando o Mouse está por cima do Botão
			self.Imagem2 = Imagem2

	#Função de execusão do botão
	def run(self, Multiplicador, Mouse_Press, Mouse_Pos):
		#Verficica se o mause está por cima do Botão
		if self.rect.collidepoint(Mouse_Pos):
			#Altera a Imagem
			self.image = CriarObjeto(self.Imagem2, Multiplicador)

			#Faz a Imagem Ficar Transparente
			self.image.set_colorkey((0, 0, 0))

			#Verficica se o houve um MOUSEBUTTONDOWN
			if Mouse_Press:
				return self.Ação
		else:
			#Altera a Imagem
			self.image = CriarObjeto(self.ImagemOriginal, Multiplicador)

			#Faz a Imagem Ficar Transparente
			self.image.set_colorkey((0, 0, 0))

		return SEM_MUDANÇA

class MenuMaker():

	def __init__(self, Diretório_do_Menu):
		if type(Diretório_do_Menu) != str:
			raise TypeError("Diretório_do_Menu tem que ser uma String")
		elif Diretório_do_Menu not in IMAGENS_DO_JOGO:
			raise Exception("Diretório_do_Menu não Carregado!")
		else:
			Imagens = IMAGENS_DO_JOGO[Diretório_do_Menu]

			if "Plano de fundo" not in Imagens:
				raise FileNotFoundError("Não foi possivel identificar o arquivo do plano de fundo")
			elif "Botões" not in Imagens:
				raise FileNotFoundError("Não foi possivel identificar o diretório dos Botões")
			else:
				self.Plano_de_Fundo = Imagens["Plano de fundo"]
				self.Imagens = Imagens["Botões"]
				self.path = path.join(path.join(Dir_Imagens, Diretório_do_Menu), "Botões")

	#Chama a execução do Menu
	def run(self, Tela, Multiplicador):
		while True:
			#Lista dos Botões
			Botões = []

			Mouse_Press = False

			for event in pygame.event.get():

				#Verifica se clicou no X
				if event.type == pygame.QUIT:
					return SAIR

				#Verifica se o mause foi precionado
				if event.type == pygame.MOUSEBUTTONDOWN:
					Mouse_Press = True

			for button in self.getObjects(Multiplicador):
				NOVO_ESTADO = button.run(Multiplicador, Mouse_Press, pygame.mouse.get_pos())

				#Adiciona Botão a lista
				Botões.append(button)

				if NOVO_ESTADO != SEM_MUDANÇA:
					return NOVO_ESTADO

			AtualizarPlanodeFundo(Tela, self.Plano_de_Fundo, Multiplicador, Botões)

	def getObjects(self, Multiplicador):
		Objetos = []

		#Arquivo que contem as informações dos Botões
		file = YamlFile(path.join(self.path, "INFO.yml"))

		#Cada Botão registrado no Arquivo
		for string in file.getStringList("Lista de Botões", default_value=[]):
			Posição = file.getIntList("Botão." + string + ".Posição", default_value=[0,0])
			ImagemOriginal = file.getString("Botão." + string + ".ImagemOriginal", default_value="")
			Imagem2 = file.getString("Botão." + string + ".Imagem2", default_value="")
			Ação = file.getInt("Botão." + string + ".Ação", default_value=0)

			if len(Posição) == 2 and Posição[0] >= 0 and Posição[1] >= 0 and ImagemOriginal in self.Imagens and Imagem2 in self.Imagens:
				Objetos.append(MenuButton(self.Imagens[ImagemOriginal], Multiplicador, (Posição[0], Posição[1]), self.Imagens[Imagem2], Ação))

		return Objetos