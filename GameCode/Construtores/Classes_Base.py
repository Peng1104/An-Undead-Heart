#Arquivo que contem as Classes de Base do Jogo

import pygame
from os import path, listdir

class HitBox():

	def __init__(self, Posição, Tamanho=None, Raio=None):
		if type(Posição) != tuple and type(Posição) != list:
			raise TypeError("Posição não é uma Tuple")
		elif len(Posição) != 2:
			raise TypeError("Posição precisa conter X e Y")
		elif type(Posição[0]) != int or type(Posição[1]) != int:
			raise TypeError("X ou Y não é um Interio")
		elif type(Tamanho) != tuple and type(Tamanho) != list and Tamanho != None:
			raise TypeError("Tamanho não é uma Tuple")
		elif Tamanho != None and len(Tamanho) != 2:
			raise TypeError("O Tamanho precisa conter a Largura e Altura!")
		elif Tamanho != None and (type(Tamanho[0]) != int or type(Tamanho[1]) != int):
			raise TypeError("Largura ou Altura não é um Interio!")
		elif type(Raio) != int and type(Raio) != float and Raio != None:
			raise TypeError("Raio não é um Número!")
		else:
			#Posição da HitBox
			self.PosiçãoX = Posição[0]
			self.PosiçãoY = Posição[1]

			#Retangulo
			self.Retangulo = None

			if Tamanho != None:
				self.Retangulo = pygame.Rect(Posição[0], Posição[1], Tamanho[0], Tamanho[1])

			#Raio do Circulo
			self.Raio = Raio

	def Atualizar_Raio(self, Raio):
		if type(Raio) != int and type(Raio) != float and Raio != None:
			raise TypeError("Raio não é um Número!")
		else:
			self.Raio = Raio

	def Atualizar_Localização(self, Valor, EixoX=True):
		if type(Valor) != int:
			raise TypeError("Valor não é um Inteiro!")
		elif type(EixoX) != bool:
			raise TypeError("EixoX não é um Booleano!")
		elif EixoX:
			self.PosiçãoX = Valor

			#Atualiza a posição do Retangulo
			if self.Retangulo != None:
				self.Retangulo.x = Valor
		else:
			self.PosiçãoY = Valor

			#Atualiza a posição do Retangulo
			if self.Retangulo != None:
				self.Retangulo.y = Valor

	def Colisão_No_Retangulo(self, PosiçãoX, PosiçãoY):
		if self.Retangulo == None:
			raise Exception("HitBox não possui um Retangulo!")
		elif type(PosiçãoX) != int:
			raise TypeError("PosiçãoX não é um Inteiro!")
		elif type(PosiçãoY) != int:
			raise TypeError("PosiçãoY não é um Inteiro!")
		else:
			return self.Retangulo.collidepoint((PosiçãoX, PosiçãoY))

	def Colisão_No_Circulo(self, PosiçãoX, PosiçãoY):
		if self.Raio == None:
			raise Exception("HitBox não possui um Circulo!")
		elif type(PosiçãoX) != int:
			raise TypeError("PosiçãoX não é um Inteiro!")
		elif type(PosiçãoY) != int:
			raise TypeError("PosiçãoY não é um Inteiro!")
		elif self.Retangulo == None:
			return self.Raio**2 <= ((PosiçãoX - self.PosiçãoX)**2 + (PosiçãoY - self.PosiçãoY)**2)
		else:
			return self.Raio**2 <= ((PosiçãoX - self.Retangulo.centerx)**2 + (PosiçãoY - self.Retangulo.centery)**2)

#Classe Para criar um Nova Imagem Objeto
class Novo_Objeto(pygame.sprite.Sprite):
	
	def __init__(self, Imagem, Multiplicador=1, Posição=(int(1920/2), int(1080/2)), Raio=None, ColorKey=(0, 0, 0)):
		if type(Imagem) != pygame.Surface:
			raise TypeError("Imagem não é um pygame.Surface!")
		elif type(Multiplicador) != float and type(Multiplicador) != int:
			raise TypeError("Multiplicador não é um Número!")
		elif type(Posição) != tuple:
			raise TypeError("Posição não é um Tuple!")
		elif len(Posição) != 2:
			raise Exception("Posição presisa conter X e Y!")
		elif type(Posição[0]) != int or type(Posição[1]) != int:
			raise TypeError("Todos os elementos da Posição tem que ser Interios!")
		elif Raio != None and type(Raio) != float and type(Raio) != int:
			raise TypeError("Raio não é um Número!")
		elif type(ColorKey) != tuple:
			raise TypeError("ColorKey não é uma Tuple!")
		elif len(ColorKey) != 3 and len(ColorKey) != 4:
			raise Exception("ColorKey tem que ter 3 ou 4 Interios!")
		elif type(ColorKey[0]) != int or type(ColorKey[1]) != int or type(ColorKey[2]) != int or (len(ColorKey) == 4 and type(ColorKey[3]) != int):
			raise Exception("Um dos Valores de ColorKey não é um Inteiro!")
		else:
			super().__init__()

			#Variavel de Adequação do Objeto
			self.Multiplicador = Multiplicador

			#Variavel da Imagem do Objeto
			self.image = None

			#Cria a Imagem do Objeto
			self.Atualizar_Imagem(Imagem, ColorKey)

			#Cria a HitBox do Objeto
			self.HitBox = HitBox((int(Posição[0]*self.Multiplicador), int(Posição[1]*self.Multiplicador)), self.image.get_size(), Raio)

			#Cria a variavel rect do Objeto
			self.rect = None

			#Cria a mask do Objeto
			self.mask = pygame.mask.from_surface(self.image)

	#Função para adequar as Imagens do Objeto a Dimensão do Jogo
	def Atualizar_Imagem(self, Imagem, ColorKey=(0, 0, 0)):
		if type(Imagem) != pygame.Surface:
			raise TypeError("Imagem não é um pygame.Surface")
		else:
			#Dimensiona a Imagem
			preImagem = pygame.transform.scale(Imagem, (int(Imagem.get_size()[0]*self.Multiplicador), int(Imagem.get_size()[1]*self.Multiplicador)))

			if self.image != None and self.image.get_size() != preImagem.get_size():
				raise Exception("A Nova Imagem do Objeto não possui o mesmo Tamanho da Original!")

			#Faz a Imagem Ficar Transparente
			preImagem.set_colorkey(ColorKey)

			#Atualiza a Imagem do Objeto
			self.image = preImagem

	#Função para atualizar o Novo_Objeto
	def update(self):
		self.rect = self.HitBox.Retangulo

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