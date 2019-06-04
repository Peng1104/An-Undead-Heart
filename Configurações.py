import pygame
import random
import time
from os import path, listdir, makedirs
from GameCode.Construtores.FileController import YamlFile
import math


pygame.init()

#==================================================================================================================================#

# Classe para Carregar todas as Imagens para o Jogo
class CarregarImagens():

	def __init__(self, file_path):
		if type(file_path) == str:
			if path.isdir(file_path):
				self.dictdeimagens = self.__loadFile__(file_path)
			else:
				raise NotADirectoryError(file_path + " não existe ou não é um Dirétorio")
		else:
			raise TypeError("ERRO! file_path não é uma String")

	def __loadFile__(self, file_path):
		# Dicionário que vai conter todas as Imagens
		maps = {}

		# Lista todos os arquivos e diretórios dentro do file_path
		for file in listdir(file_path):

			# Verifica se não é um diretório
			if file.find(".") > 0 and len(file) > 4:

				# Verifica se uma Imagem com o mesmo nome já foi salva 
				if not file[:-4] in maps:

					# Arruma a extenção do arquivo caso não esteja em minusculo
					file = file[:-4] + file[-4:].lower()

					# Verifica se o arquivo é de uma imagem
					if file.endswith(".png") or file.endswith(".jpg") or file.endswith(".gif") or file.endswith(".bmp") or file.endswith(".pcx") or file.endswith(".tga") or file.endswith(".tif") or file.endswith(".lbm") or file.endswith(".pbm") or file.endswith(".pgm") or file.endswith(".ppm") or file.endswith(".xpm"):  
						
						#Salva a imagem com seu nome no dicionário
						maps[file[:-4]] = pygame.image.load(file_path + "/" + file)
			else:

				#Cria um dicionário interno
				maps[file] = self.__loadFile__(file_path + "/" + file)

		return maps

	# Retorna um dicionario contendo todas as imagens no file_path em forma de surfaces, os diretórios criaram dicionários internos
	def getImagens(self):
		return self.dictdeimagens

#==================================================================================================================================#

# Classe para Carregar todas os Sons para o Jogo
class CarregarSons():

	def __init__(self, file_path):
		if type(file_path) == str:
			if path.isdir(file_path):
				self.dictdesons = self.__loadFile__(file_path)
			else:
				raise NotADirectoryError(file_path + " não existe ou não é um Dirétorio")
		else:
			raise TypeError("ERRO! file_path não é uma String")

	def __loadFile__(self, file_path):
		# Dicionário que vai conter todas os sons
		maps = {}

		# Lista todos os arquivos e diretórios dentro do file_path
		for file in listdir(file_path):

			# Verifica se não é um diretório
			if file.find(".") > 0 and len(file) > 4:

				# Verifica se um som com o mesmo nome já foi salva 
				if not file[:-4] in maps:

					# Arruma a extenção do arquivo caso não esteja em minusculo
					file = file[:-4] + file[-4:].lower()

					# Verifica se o arquivo é de um som
					if file.endswith(".ogg"):  
						
						#Salva o som com seu nome no dicionário
						maps[file[:-4]] = pygame.mixer.Sound(file_path + "/" + file)
			else:

				#Cria um dicionário interno
				maps[file] = self.__loadFile__(file_path + "/" + file)

		return maps

	# Retorna um dicionario contendo todas os Sons no file_path em forma de surfaces, os diretórios criaram dicionários internos
	def getSons(self):
		return self.dictdesons

#==================================================================================================================================#

# Diretórios

# Diretório do Config.yml
DIR_CONFIG = path.join("Configurações", "Opções")

#==================================================================================================================================#

# Variáveis uteis para o jogo

#Transformadores para a escala dos objetos
MULTIPLICADORES = {
	1 : 1/3,
	2 : 1/2,
	3 : 1.6/3,
	4 : 2/3,
	5 : 2.5/3,
	6 : 1
}

CONFIG = YamlFile(DIR_CONFIG + "/Config.yml")

#==================================================================================================================================#

# Diretório principal
DIR_PRINCIPAL 			   = CONFIG.getString("Diretórios.Pai", default_value="Configurações")

# Diretório do menu inicial 
DIR_MENU_INICIAL 		   = DIR_PRINCIPAL + "/" + CONFIG.getString("Diretórios.Menu das Opções", default_value="Menus/Opções")

# Diretório do menu de opções
DIR_MENU_DE_OPÇÕES		   = DIR_PRINCIPAL + "/" + CONFIG.getString("Diretórios.Controles", default_value="Menus/Controles")

# Diretório do menu de como jogador
DIR_CONTROLES 			   = DIR_PRINCIPAL + "/" + CONFIG.getString("Diretórios.Controles", default_value="Menus/Controles")

# Diretório das configurações de vídeo
DIR_CONFIGURAÇÕES_DE_VÍDEO = DIR_PRINCIPAL + "/" + CONFIG.getString("Diretórios.Configurações de Vídeo", default_value="Menus/Vídeo")

# Diretório da localização dos jogos salvos
DIR_SAVED_GAMES 		   = CONFIG.getString("Diretórios.Jogos Salvos", default_value="Jogos Salvos")

# Diretório do menu dos jogos salvos
DIR_MENU_DOS_JOGO_SALVO    = DIR_PRINCIPAL + "/" + CONFIG.getString("Diretórios.Menu dos Jogos Salvos", default_value="Menus/Jogos Salvos")

# Diretório do menu de iniciar um novo jogo
DIR_INICIAR_NOVO_JOGO      = DIR_PRINCIPAL + "/" + CONFIG.getString("Diretórios.Iniciar Novo Jogo", default_value="Menus/Inicar Novo Jogo")

# Diretório das opções do jogo
DIR_GAME                   = DIR_PRINCIPAL + "/" + CONFIG.getString("Diretórios.Jogo", default_value="Assets")

#==================================================================================================================================#

# Variáveis do jogo

TELA            = None
MULTIPLICADOR   = 1
IMAGENS         = CarregarImagens(DIR_PRINCIPAL).getImagens()
SONS            = CarregarSons(DIR_PRINCIPAL).getSons()
score           = 0
minutos         = 0
timer           = 0
vidas           = 5
inimigos_vivos  = 0
tempo_absoluto  = 0

#==================================================================================================================================#

# CORES

BRANCO   = (255, 255, 255, 255)
PRETO    = (0,     0,   0, 255)
VERMELHO = (255,   0,   0, 255)
VERDE    = (0,   255,   0, 255)
AZUL     = (0,     0, 255, 255)
AMARELO  = (255, 255,   0, 255)
ROSA     = (255,   0, 255, 255)
CIANO    = (0,   255, 255, 255)
LARANJA  = (255, 125,   0, 255)
ROXO     = (125,   0, 255, 255)

#==================================================================================================================================#

# Tela do jogo

LARGURA_PADRÃO = 1920
ALTURA_PADRÃO  = 1080

def getTamanho_Tela():
	return (int(LARGURA_PADRÃO*MULTIPLICADOR), int(ALTURA_PADRÃO*MULTIPLICADOR))

#==================================================================================================================================#

# ESTADOS

# Estados do Jogo
SEM_MUDANÇA = "SEM MUDANÇA"
MENU_INICIAL = "MENU INICIAL"
SAIR = "SAIR DO JOGO"
MENU_DE_OPÇÕES = "MENU DE OPÇÕES"
CONTROLES = "CONTROLES"
CONFIGURAÇÕES_DE_VÍDEO = "CONFIGURAÇÕES DE VÍDEO"
ATIVAR_TELA_CHEIA = "MODIFICAR O JOGO PARA TELA CHEIA"
DESATIVAR_TELA_CHEIA = "MODIFICAR O JOGO PARA TELA NORMAL"
RESOLUÇÃO_DE_1080P = "MODIFICAR O JOGO PARA A ESCALA PADRÃO" # Multiplicador para 1
RESOLUÇÃO_DE_900P = "MODIFICAR O JOGO PARA A ESCALA 900P" #    Multiplicador para 2.5/3
RESOLUÇÃO_DE_720P = "MODIFICAR O JOGO PARA A ESCALA 720P" #    Multiplicador para 2/3
RESOLUÇÃO_DE_576P = "MODIFICAR O JOGO PARA A ESCALA 576P" #    Multiplicador para 1.6/3
RESOLUÇÃO_DE_540P = "MODIFICAR O JOGO PARA A ESCALA 540P" #    Multiplicador para 1/2
RESOLUÇÃO_DE_360P = "MODIFICAR O JOGO PARA A ESCALA 360P" #    Multiplicador para 1/3
MENU_DOS_JOGOS_SALVOS = "MENU DOS JOGOS SALVOS"
INICIAR_NOVO_JOGO = "INICAR NOVO JOGO"
INICIAR_JOGO = "INICAR JOGO"
EM_JOGO = "EM JOGO"
TELA_RESULTADOS = "TELA RESULTADOS"

#==================================================================================================================================#

JOGADOR      = IMAGENS[DIR_GAME[DIR_GAME.rfind("/")+1:]]["Imagens"]["JOGADOR"]
JOGADOR      = pygame.transform.scale( JOGADOR, (50,50) )
JOGADOR.set_colorkey(VERMELHO)

ALIEN_1      = IMAGENS[DIR_GAME[DIR_GAME.rfind("/")+1:]]["Imagens"]["ALIEN1"]
ALIEN_1      = pygame.transform.scale( ALIEN_1, (50,50) )
ALIEN_1.set_colorkey(PRETO)

ALIEN_2      = IMAGENS[DIR_GAME[DIR_GAME.rfind("/")+1:]]["Imagens"]["ALIEN2"]
ALIEN_2      = pygame.transform.scale( ALIEN_2, (50,50) )
ALIEN_2.set_colorkey(PRETO)

ARMA         = IMAGENS[DIR_GAME[DIR_GAME.rfind("/")+1:]]["Imagens"]["ARMA"]
ARMA         = pygame.transform.scale( ARMA, (50,50) )
ARMA.set_colorkey((255, 255, 255, 0))

BULLET       = IMAGENS[DIR_GAME[DIR_GAME.rfind("/")+1:]]["Imagens"]["BULLET"]
BULLET.set_colorkey((255, 255, 255, 0))

MASCARA      =   IMAGENS[DIR_GAME[DIR_GAME.rfind("/")+1:]]["Imagens"]["MASCARA"]
FUNDO        =   IMAGENS[DIR_GAME[DIR_GAME.rfind("/")+1:]]["Imagens"]["FUNDO"]

TELA_INICIAL = IMAGENS[DIR_GAME[DIR_GAME.rfind("/")+1:]]["Imagens"]["TELA_INICIAL"]

TELA_FINAL = IMAGENS[DIR_GAME[DIR_GAME.rfind("/")+1:]]["Imagens"]["TELA_FINAL"]

#=================#

FONTE        = pygame.font.Font(path.join(DIR_GAME, "Fontes/FONTE.ttf"), 28)

SIMBOLO      = pygame.font.Font(path.join(DIR_GAME, "Fontes/SYMBOL_1.otf"), 32)

#=================#

pygame.mixer.music.load(path.join(DIR_GAME + "/Sons", 'Musica_de_Fundo.ogg'))
pygame.mixer.music.set_volume(0.4)

TIRO = SONS[DIR_GAME[DIR_GAME.rfind("/")+1:]]["Sons"]["Tiro"]
TIRO.set_volume(0.05)

#==================================================================================================================================#

# Função para criar ou redimencionar a tela do jogo
def redimencionar_tela(nível_de_resolução, tela_cheia):

	global CONFIG

	# Atualiza as opções no arquivo Config.yml

	CONFIG.set("Nível de Resolução do Jogo", nível_de_resolução)
	CONFIG.set("Tela Cheia", tela_cheia)
	CONFIG.save()

	global MULTIPLICADORES
	global MULTIPLICADOR
	global TELA

	# Atualiza o Multiplicador
	MULTIPLICADOR = MULTIPLICADORES[nível_de_resolução]

	global MASCARA

	MASCARA = pygame.transform.scale(MASCARA, (int(MASCARA.get_size()[0] * MULTIPLICADOR), int(MASCARA.get_size()[1] * MULTIPLICADOR)))

	if tela_cheia:
		TELA = pygame.display.set_mode(getTamanho_Tela(), flags=pygame.FULLSCREEN)
	else:
		TELA = pygame.display.set_mode(getTamanho_Tela())

#==================================================================================================================================#

# Função para carregar as váriaveis deste arquivo

def iniciar_pygame():
	# Checagens

	global CONFIG
	global DIR_SAVED_GAMES

	if not path.isdir(DIR_SAVED_GAMES):
		makedirs(DIR_SAVED_GAMES)

	if CONFIG.getFloat("FPS", default_value=60) < 1.0:
		CONFIG.set("FPS", 60)

	if CONFIG.getInt("Nível de Resolução do Jogo", default_value=4) > 6 or CONFIG.getInt("Nível de Resolução do Jogo") < 1:
		CONFIG.set("Nível de Resolução do Jogo", 4)

	# Inicia o jogo
	pygame.init()

	pygame.display.set_caption(CONFIG.getString("Nome do Jogo", default_value="LAST SURPRISE"))

	redimencionar_tela(CONFIG.getInt("Nível de Resolução do Jogo"), CONFIG.getBoolean("Tela Cheia", default_value=False))

#==================================================================================================================================#

# Função para criar ou alterar o plano de fundo da tela
def atualizar_tela(plano_de_fundo, todos_os_sprites, estado_do_jogo):
	if type(plano_de_fundo) != pygame.Surface:
		raise TypeError("plano_de_fundo não é um pygame.Surface")
	elif type(todos_os_sprites) != pygame.sprite.Group:
		raise TypeError("todos_os_sprites não é um pygame.sprite.Group")
	elif type(estado_do_jogo) != str:
		raise TypeError("Estado não é uma STRING")
	elif estado_do_jogo != EM_JOGO and (plano_de_fundo.get_size()[0] != 1920 or plano_de_fundo.get_size()[1] != 1080):
		raise Exception("A Imagem de Plano de Fundo tem que ser 1920 por 1080")
	else:

		global MULTIPLICADOR
		global TELA
		global timer
		global minutos
		global vidas
		global inimigos_vivos

		if estado_do_jogo != EM_JOGO:
			#Dimensiona a Plano_De_Fundo de Plano de Fundo para menus
			plano_de_fundo = pygame.transform.scale(plano_de_fundo, (int(plano_de_fundo.get_size()[0]*MULTIPLICADOR), int(plano_de_fundo.get_size()[1]*MULTIPLICADOR)))

		#Prenche a Tela de PRETO
		TELA.fill((0, 0, 0, 255))

		#Aplica o Plano de Fundo a Tela
		TELA.blit(plano_de_fundo, plano_de_fundo.get_rect())

		score_surface = FONTE.render("{:08d}".format(score), True, AMARELO)
		score_rect = score_surface.get_rect()
		score_rect.midtop = (int(plano_de_fundo.get_size()[0]*MULTIPLICADOR) / 2,  10)
		TELA.blit(score_surface, score_rect)

		segundos = int(timer/30)
		if (timer/30) == 60:
			minutos += 1
			timer = 0

		timer_surface = FONTE.render("{0:02d}:{1:02d}".format(minutos,segundos), True, BRANCO)
		timer_rect = timer_surface.get_rect()
		timer_rect.topleft = (10, 10)
		TELA.blit(timer_surface, timer_rect)

		text_surface = SIMBOLO.render("E" * vidas, True, VERMELHO)
		text_rect = text_surface.get_rect()
		text_rect.bottomleft = (10, (int(plano_de_fundo.get_size()[1]*MULTIPLICADOR) - 10))
		TELA.blit(text_surface, text_rect)

		#Atualiza todos os membros do Grupo
		todos_os_sprites.update()

		#Desenha os Spites na Tela
		todos_os_sprites.draw(TELA)

		#Inverte o Display
		pygame.display.flip()

		return TELA

#==================================================================================================================================#

# Classe para criar um Sprites com imagens ultilizando o MULTIPLICADOR
class Novo_Sprite(pygame.sprite.Sprite):
	
	def __init__(self, lista_de_imagens, posição, colorkey):
		if type(lista_de_imagens) != tuple and type(lista_de_imagens) != list:
			raise TypeError("lista_de_imagens não é uma lista")
		elif len(lista_de_imagens) == 0:
			raise Exception("lista_de_imagens tem que conter uma imagem pelo menos")
		elif all(isinstace(x, pygame.Surface) for x in lista_de_imagens):
			raise TypeError("Algum elemento da lista_de_imagens não é um pygame.Surface")
		elif type(Posição) != tuple and type(Posição) != list:
			raise TypeError("Posição não é um Tuple!")
		elif len(Posição) != 2:
			raise Exception("Posição presisa conter X e Y!")
		elif type(Posição[0]) != int or type(Posição[1]) != int:
			raise TypeError("Todos os elementos da Posição tem que ser Interios!")
		elif type(ColorKey) != tuple:
			raise TypeError("ColorKey não é uma Tuple!")
		elif len(ColorKey) != 3 and len(ColorKey) != 4:
			raise Exception("ColorKey tem que ter 3 ou 4 Interios!")
		elif type(ColorKey[0]) != int or type(ColorKey[1]) != int or type(ColorKey[2]) != int or (len(ColorKey) == 4 and type(ColorKey[3]) != int):
			raise Exception("Um dos Valores de ColorKey não é um Inteiro!")
		else:
			super().__init__()

			# Imagem do sprite
			self.image = None

			# Lista das imagens do Objeto
			self.lista_de_imagens = lista_de_imagens

			# ColorKey das imagens
			self.colorkey = colorkey

			# Cria a imagem do sprite
			self.Atualizar_Imagem(lista_de_imagens[0])

			#Cria o rect do sprite
			self.rect = self.image.get_rect()

	# Função para adequar as imagens do Objeto a dimensão do Jogo
	def mudar_imagem(self, posição):
		if type(posição) != int:
			raise TypeError("Imagem não é um Inteiro")
		elif posição > len(posição) - 1:
			raise Exception("lista_de_imagens não possui a posição " + str(posição))
		else:
			imagem = self.lista_de_imagens[posição]

			# Dimensiona a ímagem
			preImagem = pygame.transform.scale(imagem, (int(imagem.get_size()[0]*MULTIPLICADOR), int(imagem.get_size()[1]*MULTIPLICADOR)))

			if self.image != None and self.image.get_size() != preImagem.get_size():
				raise Exception("A nova imagem do Novo_Sprite não possui o mesmo tamanho da original")

			# Faz a imagem ficar transparente
			preImagem.set_colorkey(self.colorkey)

			# Atualiza a imagem do objeto
			self.image = preImagem