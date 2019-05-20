#Arquivo que contem as Classes de Base do Jogo

import pygame
from os import path, listdir

#Classe Para criar um Nova Imagem Objeto
class Novo_Objeto(pygame.sprite.Sprite):
	
	def __init__(self, Imagem, Multiplicador, Posição):
		if type(Imagem) != pygame.Surface:
			raise TypeError("Imagem não é um pygame.Surface")
		elif type(Multiplicador) != float and type(Multiplicador) != int:
			raise TypeError("Multiplicador não é um Número")
		elif type(Posição) != tuple:
			raise TypeError("Posição não é um Tuple")
		elif len(Posição) != 2:
			raise Exception("Posição presisa conter X e Y!")
		elif type(Posição[0]) != int or type(Posição[1]) != int:
			raise TypeError("Todos os elementos da Posição tem que ser Interios")
		else:
			super().__init__()

			#Cria a Imagem do Objeto
			self.Criar_Objeto(Imagem, Multiplicador)

			#Criar o rect do Objeto
			self.rect = self.image.get_rect()

			#Define a posição X do Rect
			self.rect.x = int(Posição[0]*Multiplicador)

			#Define a posição Y do Rect
			self.rect.y = int(Posição[1]*Multiplicador)

	#Função para adequar as Imagens do Objeto a Dimensão do Jogo
	def Criar_Objeto(self, Imagem, Multiplicador):
		if type(Imagem) != pygame.Surface:
			raise TypeError("Imagem não é um pygame.Surface")
		elif type(Multiplicador) != float and type(Multiplicador) != int:
			raise TypeError("Multiplicador não é um Número")
		else:
			#Dimensiona a Imagem
			self.image = pygame.transform.scale(Imagem, (int(Imagem.get_size()[0]*Multiplicador), int(Imagem.get_size()[1]*Multiplicador)))

			#Faz a Imagem Ficar Transparente
			self.image.set_colorkey((0, 0, 0))

#Classe para Carregar todas as Imagens para o Jogo
class CarregarImagens():

	def __init__(self, FilePath):
		if type(FilePath) == str:
			if path.isdir(FilePath):
				self.DictDeImagens = self.__loadFile__(FilePath)
			else:
				raise NotADirectoryError(FilePath + " não existe ou não é um Dirétorio!!")
		else:
			raise TypeError("ERRO! FilePath deve ser uma String")

	def __loadFile__(self, FilePath):
		#Dicionário que vai conter todas as Imagens
		maps = {}

		#Lista todos os Arquivos no FilePath
		for file in listdir(FilePath):
			#Verifica se não é um diretório
			if file.find(".") > 0 and len(file) > 4:
				#Verifica se uma Imagem com o mesmo nome já foi salva 
				if not file[:-4] in maps:
					#Arruma a extenção do arquivo caso não esteja em minusculo
					file = file[:-4] + file[-4:].lower()

					#Verifica se o arquivo é do tipo Imagem
					if file.endswith(".png") or file.endswith(".jpg") or file.endswith(".gif") or file.endswith(".bmp") or file.endswith(".pcx") or file.endswith(".tga") or file.endswith(".tif") or file.endswith(".lbm") or file.endswith(".pbm") or file.endswith(".pgm") or file.endswith(".ppm") or file.endswith(".xpm"):  
						#Salva a Imagem com seu nome no Dicionário
						maps[file[:-4]] = pygame.image.load(FilePath + "/" + file)
			else:
				#Cria um Dicionário Interno
				maps[file] = self.__loadFile__(FilePath + "/" + file)

		return maps

	#Retorna um Dicionario contendo todas as Imagens no FilePath
	def getImagens(self):
		return self.DictDeImagens