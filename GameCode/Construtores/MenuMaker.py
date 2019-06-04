# Arquivo para criar as os menus

import re
from os import listdir, path
from GameCode.Construtores.FileController import JSONFile, YamlFile
from GameCode.Configurações import *

class MenuButton(Novo_Sprite):

	def __init__(self, lista_de_imagens, posição, click):
		if type(click) != str:
			raise TypeError("click não é uma String")
		else:
			super().__init__(lista_de_imagens, posição, (0, 0, 0))

			# Estado que o jogo vai ter quando o botão for clicado
			self.click = click

	# Função para executar o botão
	def run(self, mouse_press, mouse_pos):

		# Verificica se o mause está por cima do botão
		if self.rect.collidepoint(mouse_pos):

			# Verifica se contem uma imagem de aviso de botão selecionado
			if len(self.lista_de_imagens) -1 > 0:

				# Coloca a imagem de botão selecionado
				self.mudar_imagem(1)

			# Verificica se o houve um MOUSEBUTTONDOWN
			if Mouse_Press:
				return self.click
		else:

			# Altera a imagem para a imagem padrão
			self.mudar_imagem(0)

		return SEM_MUDANÇA

class Menu():

	def __init__(self, diretório_do_menu, estado):
		if type(diretório_do_menu) != str:
			raise TypeError("diretório_do_menu não é uma String")
		elif diretório_do_menu not in IMAGENS:
			raise Exception(diretório_do_menu + " não existe ou não foi possível carregar ele!")
		elif type(estado) != str:
			raise TypeError("estado não é uma String")
		else:
			imagens_do_menu = IMAGENS[diretório_do_menu]

			if "Plano de fundo" not in imagens_do_menu:
				raise FileNotFoundError("Não foi possível identificar a imagem de plano de fundo")
			elif "Botões" not in imagens_do_menu:
				raise FileNotFoundError("Não foi possível identificar o diretório dos Botões")
			else:
				self.plano_de_fundo = imagens_do_menu["Plano de fundo"]
				self.imagens_do_menu = imagens_do_menu["Botões"]
				self.path = diretório_do_menu + "/Botões"
				self.estado = estado

	# Chama a execução do Menu
	def run(self):
		while True:
			todos_os_sprites = pygame.sprite.Group()

			mouse_press = False

			for event in pygame.event.get():

				# Verifica se clicou no X
				if event.type == pygame.QUIT:
					return SAIR

				# Verifica se o mouse foi precionado
				if event.type == pygame.MOUSEBUTTONDOWN:
					mouse_press = True

			for button in self.getObjects():
				NOVO_ESTADO = button.run(mouse_press, pygame.mouse.get_pos())

				todos_os_sprites.add(button)

				if NOVO_ESTADO != SEM_MUDANÇA:
					return NOVO_ESTADO

			atualizar_tela(self.Plano_de_Fundo, todos_os_sprites, self.estado)

	# Cria os botões
	def getObjects(self):
		objetos = []

		# Arquivo que contem as informações de cada botão
		file = YamlFile(self.path + "/INFO.yml")

		# Para cada botão registrado no arquivo
		for string in file.getStringList("Lista de Botões", default_value=[]):

			# Posição do botão
			posição = file.getIntList("Botão." + string + ".Posição", default_value=[0,0])

			# Lista de imagens do botão
			lista_dos_nomes_das_imagens = file.getStringList("Botão." + string + ".Lista de Imagens", default_value=[])

			# Ação que deve ser executada no click deste botão
			ação = file.getString("Botão." + string + ".Ação", default_value="")

			# Verifição se é possível criar um botão - posição
			if len(posição) == 2 and posição[0] >= 0 and posição[0] <= 1920 and posição[1] >= 0 and posição[1] <= 1080:

				#Lista de imagens
				lista_de_imagens = []

				for name in lista_dos_nomes_das_imagens:

					# Verifica se o name existe dentro de self.imagens_do_menu
					if name in self.imagens_do_menu:
						lista_de_imagens.append(self.imagens_do_menu[name])

				# Verifição se é possível criar um botão - minimo de 1 imagem

				if len(lista_de_imagens) > 0:
					objetos.append(MenuButton(lista_de_imagens, (Posição[0], Posição[1]), ação))

		return objetos

class SavedGamesMenu(Menu):

	def __init__(self, diretório_do_menu, estado):
		super().__init__(diretório_do_menu, estado)

		# Variavel de botão retornar ao menu
		self.existe_voltar = False

	# Chama a execução do Menu IMPORTANTE - Retorna NOVO_ESTADO e o SAVE
	def run(self):
		while True:
			todos_os_sprites = pygame.sprite.Group()

			mouse_press = False

			for event in pygame.event.get():

				# Verifica se clicou no X
				if event.type == pygame.QUIT:
					return SAIR

				#Verifica se o mause foi precionado
				if event.type == pygame.MOUSEBUTTONDOWN:
					mouse_press = True

			# Numero do jogo salvo
			SAVE = 1

			if self.existe_voltar:
				SAVE = -1

			for button in self.getObjects():
				NOVO_ESTADO = button.run(mouse_press, pygame.mouse.get_pos())

				todos_os_sprites.add(button)

				if NOVO_ESTADO != SEM_MUDANÇA:
					return NOVO_ESTADO, SAVE

				if SAVE == -1:
					SAVE = SAVE + 2
				else:
					SAVE = SAVE + 1

			atualizar_tela(self.plano_de_fundo, todos_os_sprites, self.estado)

	# Cria os botões
	def getObjects(self):
		objetos = []

		# Arquivo que contem as informações dos botões
		file = YamlFile(self.path + "/INFO.yml")

		# Lista das localizações dos botões (em Tuple)
		localizações = []

		# Lista todos a localização dos botões
		for string in file.getStringList("Posições dos Botões", default_value=[]):

			# Verifica se a string é valida
			if re.search("^\[\d{1,4}, \d{1,4}\]$", string):

				# Processa a criaçao da tuple
				a = string.split(", ")

				localização = (int(a[0][1:]), int(a[1][:-1]))

				# Verifica se a localização é valida
				if localização[0] >= 0 and localização[0] <= 1920 and localização[1] >= 0 and localização[1] <= 1080:
					localizações.append(localização)

		# Sem botões registrados
		if len(localizações) == 0:
			raise Exception("ERRO! Não foi possivel criar o SavedGamesMenu - Sem Botões registrados")

		imagem_voltar_normal = file.getString("Imagem Botão Voltar", default_value="")
		imagem_voltar_especial = file.getString("Brilho Botão Voltar", default_value="")

		# Verifica se deve ser criado o botão de voltar ao MENU_INICIAL
		if imagem_voltar_normal in self.imagens_do_menu and imagem_voltar_especial in self.imagens_do_menu:
			objetos.append(MenuButton([self.imagens_do_menu[imagem_voltar_normal], self.imagens_do_menu[imagem_voltar_especial]], localizações[0], MENU_INICIAL))

			# Apaga a localização do botão de voltar
			del localizações[0]

			# Confirma a existencia do botão voltar
			self.existe_voltar = True

			# Somente Botão de Voltar
			if len(localizações) == 0:
				return objetos

		imagem_sem_save_normal = file.getString("Imagem Sem Save", default_value="")
		imagem_sem_save_especial = file.getString("Brilho Sem Save", default_value="")

		# Verifica a existência das imagens padrões does botões:
		if imagem_sem_save_normal in self.imagens_do_menu and imagem_sem_save_especial in self.imagens_do_menu:

			# Lista contendo todos os números dos arquivo savedgame
			lista_de_jogos_salvos = []

			# Lista todos os itens no díretorio dos jogos salvos
			for f in listdir(DIR_SAVED_GAMES):

				# Checagem se o arquivo é um SavedGame
				if f.startswith("SavedGame-") and f.endswith(".json") and re.search("^\d+$", f[10:-5]):
					lista_de_jogos_salvos.append(int(f[10:-5]))

			# Cria os botôes de Slots para um SaveGame
			for i in range(len(Localizações)):

				# Verifica se existe um Save na localização i
				if (i+1) in lista_de_jogos_salvos:

					# Abre o save
					JFile = JSONFile(DIR_SAVED_GAMES + "/SavedGame-" + str(i+1) + ".json")

					# Procura a imagem do nível do Save
					imagem_nivel_normal = JFile.getString("Nivel", default_value="0")
					imagem_nivel_especial = imagem_nivel_normal + "-BRILHO"

					if imagem_nivel_normal in self.imagens_do_menu and imagem_nivel_especial in self.imagens_do_menu:
						objetos.append(MenuButton([self.imagens_do_menu[imagem_nivel_normal], self.imagens_do_menu[imagem_nivel_especial]], Localizações[i], INICIAR_JOGO))
					else:
						objetos.append(MenuButton([self.imagens_do_menu[imagem_sem_save_normal], self.imagens_do_menu[imagem_sem_save_especial]], Localizações[i], MENU_DOS_JOGOS_SALVOS))
				else:
					objetos.append(MenuButton([self.imagens_do_menu[imagem_sem_save_normal], self.imagens_do_menu[imagem_sem_save_especial]], Localizações[i], MENU_DOS_JOGOS_SALVOS))
		else:
			raise Exception("ERRO! Não foi possivel criar o SavedGamesMenu - Imagens não identificadas")

		return objetos