#Arquivo para criar as Telas dos Menus

import pygame
import re
from os import path, listdir
from GameCode.Construtores.Classes_Base import Novo_Objeto
from GameCode.Construtores.Funções_Base import Atualizar_O_Plano_De_Fundo
from GameCode.Construtores.FileController import YamlFile, JSONFile
from GameCode.Configs import IMAGENS_DO_JOGO, SEM_MUDANÇA, SAIR, DIR_IMAGENS, MENU_PRINCIPAL, JOGO, MENU_DE_NOVO_JOGO

class MenuButton(Novo_Objeto):

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
	def run(self, Mouse_Press, Mouse_Pos):
		#Verficica se o mause está por cima do Botão
		if self.HitBox.Colisão_No_Retangulo(Mouse_Pos[0], Mouse_Pos[1]):
			#Altera a Imagem
			self.Atualizar_Imagem(self.Imagem2)

			#Verficica se o houve um MOUSEBUTTONDOWN
			if Mouse_Press:
				return self.Ação
		else:
			#Altera a Imagem
			self.Atualizar_Imagem(self.ImagemOriginal)

		return SEM_MUDANÇA

class Menu():

	def __init__(self, Diretório_do_Menu, Estado):
		if type(Diretório_do_Menu) != str:
			raise TypeError("Diretório_do_Menu tem que ser uma String")
		elif type(Estado) != int:
			raise TypeError("Estado precisa ser um Inteiro")
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
				self.path = path.join(path.join(DIR_IMAGENS, Diretório_do_Menu), "Botões")
				self.Estado = Estado

	#Chama a execução do Menu
	def run(self, Tela, Multiplicador):
		while True:
			Botões = pygame.sprite.Group()

			Mouse_Press = False

			for event in pygame.event.get():

				#Verifica se clicou no X
				if event.type == pygame.QUIT:
					return SAIR

				#Verifica se o mause foi precionado
				if event.type == pygame.MOUSEBUTTONDOWN:
					Mouse_Press = True

			for button in self.getObjects(Multiplicador):
				NOVO_ESTADO = button.run(Mouse_Press, pygame.mouse.get_pos())

				Botões.add(button)

				if NOVO_ESTADO != SEM_MUDANÇA:
					return NOVO_ESTADO

			Atualizar_O_Plano_De_Fundo(Tela, self.Plano_de_Fundo, Multiplicador, Botões, self.Estado)

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

class SavedGamesMenu(Menu):

	def __init__(self, Diretório_do_Menu, Estado):
		super().__init__(Diretório_do_Menu, Estado)

	#Chama a execução do Menu IMPORTANTE - Retorna NOVO_ESTADO E O SAVE
	def run(self, Tela, Multiplicador, Dir_Jogos_Salvos):
		while True:
			Botões = pygame.sprite.Group()

			Mouse_Press = False

			for event in pygame.event.get():

				#Verifica se clicou no X
				if event.type == pygame.QUIT:
					return SAIR

				#Verifica se o mause foi precionado
				if event.type == pygame.MOUSEBUTTONDOWN:
					Mouse_Press = True

			#Lista de Botôes
			Objetos = self.getObjects(Multiplicador, Dir_Jogos_Salvos)

			#Numero do Jogo Salvo
			SAVE = -1

			if len(Objetos) != 7:
				SAVE = 1

			for button in Objetos:
				NOVO_ESTADO = button.run(Mouse_Press, pygame.mouse.get_pos())

				Botões.add(button)

				if NOVO_ESTADO != SEM_MUDANÇA:
					return NOVO_ESTADO, SAVE

				if SAVE == -1:
					SAVE = SAVE + 2
				else:
					SAVE = SAVE + 1

			Atualizar_O_Plano_De_Fundo(Tela, self.Plano_de_Fundo, Multiplicador, Botões, self.Estado)

	#Cria os Botôes
	def getObjects(self, Multiplicador, Dir_Jogos_Salvos):
		Objetos = []

		#Arquivo que contem as informações dos Botões
		file = YamlFile(path.join(self.path, "INFO.yml"))

		#Lista das Localizações dos Botões (em Tuple)
		Localizações = []

		for string in file.getStringList("Posições dos Botões", default_value=[]):
			if re.search("^\[\d{1,4}, \d{1,4}\]$", string):
				Numbers = string.split(", ")
				Localizações.append((int(Numbers[0][1:]), int(Numbers[1][:-1])))

		#Sem botões registrados
		if len(Localizações) == 0:
			raise Exception("ERRO! Não foi possivel criar o SavedGamesMenu - Sem Botões registrados")

		Imagem_Voltar_Normal = file.getString("Imagem Botão Voltar", default_value="")
		Imagem_Voltar_Brilhando = file.getString("Brilho Botão Voltar", default_value="")

		#Verifica se deve ser criado o botão de voltar ao Menu Principal
		if Imagem_Voltar_Normal in self.Imagens and Imagem_Voltar_Brilhando in self.Imagens:
			Objetos.append(MenuButton(self.Imagens[Imagem_Voltar_Normal], Multiplicador, Localizações[0], self.Imagens[Imagem_Voltar_Brilhando], MENU_PRINCIPAL))

			#Apaga a Lozalização do Botão de Voltar
			del Localizações[0]

			#Somente Botão de Voltar
			if len(Localizações) == 0:
				return Objetos

		Imagem_Sem_Save_Normal = file.getString("Imagem Sem Save", default_value="")
		Imagem_Sem_Save_Brilhando = file.getString("Brilho Sem Save", default_value="")

		#Verifica a Existencia das Imagens de Saves
		if Imagem_Sem_Save_Normal in self.Imagens and Imagem_Sem_Save_Brilhando in self.Imagens:
			#Lista contendo todos os numeros de Jogos Salvos
			Lista_de_Jogos_Salvos = []

			#Verifica a existência do Diretório dos Saves
			if path.isdir(Dir_Jogos_Salvos):
				#Lista todos os itens no Díretorio
				for f in listdir(Dir_Jogos_Salvos):
					if f.startswith("SavedGame-") and f.endswith(".json") and re.search("^\d+$", f[10:-5]):
						Lista_de_Jogos_Salvos.append(int(f[10:-5]))

			#Cria os botôes de Slots de Save Game
			for i in range(len(Localizações)):
				#Verifica se existe um Save na localização i
				if (i+1) in Lista_de_Jogos_Salvos:
					#Abre o save
					JFile = JSONFile(Dir_Jogos_Salvos + "/SavedGame-" + str(i+1) + ".json")

					#Procura a Imagem da Classe do Save
					Imagem_Classe_Normal = JFile.getString("Classe", default_value="")
					Imagem_Classe_Brilho = Imagem_Classe_Normal + "-BRILHO"

					if Imagem_Classe_Normal in self.Imagens and Imagem_Classe_Brilho in self.Imagens:
						Objetos.append(MenuButton(self.Imagens[Imagem_Classe_Normal], Multiplicador, Localizações[i], self.Imagens[Imagem_Classe_Brilho], JOGO))
					else:
						Objetos.append(MenuButton(self.Imagens[Imagem_Sem_Save_Normal], Multiplicador, Localizações[i], self.Imagens[Imagem_Sem_Save_Brilhando], MENU_DE_NOVO_JOGO))
				else:
					Objetos.append(MenuButton(self.Imagens[Imagem_Sem_Save_Normal], Multiplicador, Localizações[i], self.Imagens[Imagem_Sem_Save_Brilhando], MENU_DE_NOVO_JOGO))
		else:
			raise Exception("ERRO! Não foi possivel criar o SavedGamesMenu - Imagens não identificadas")

		return Objetos