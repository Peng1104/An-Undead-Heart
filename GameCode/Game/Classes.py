#Arquivo que contem as class que vão ser usadas no Jogo

from GameCode.Construtores.Classes_Base import Novo_Objeto

class Jogador(Novo_Objeto):

	def __init__(self, Lista_de_Imagens, Multiplicador, Posição, Colorkey=(255, 0, 0, 255)):
		super().__init__(Lista_de_Imagens[0], Multiplicador, Posição, None, Colorkey)

		self.Colorkey = Colorkey
		self.Lista_de_Imagens = Lista_de_Imagens

		self.speedx = 0
		self.speedy = 0

	def speed(self, speedx, speedy):
		self.speedx = speedx
		self.speedy = speedy

		if self.speedy != 0:
			if self.speedy > 0:
				self.Atualizar_Imagem(self.Lista_de_Imagens[0], self.Colorkey)
			else:
				self.Atualizar_Imagem(self.Lista_de_Imagens[1], self.Colorkey)

		if self.speedx != 0:
			if self.speedx > 0:
				self.Atualizar_Imagem(self.Lista_de_Imagens[2], self.Colorkey)
			else:
				self.Atualizar_Imagem(self.Lista_de_Imagens[3], self.Colorkey)

	def atualização(self):
		self.HitBox.Atualizar_Localização(self.rect.x + self.speedx)
		self.HitBox.Atualizar_Localização(self.rect.y + self.speedy, False)

class NPC(Novo_Objeto):

	def __init__(self, Imagem, Multiplicador, Posição, ColorKey=(255, 0, 0)):
		super().__init__(Imagem, Multiplicador, Posição, None, ColorKey)
		
#'''
	def Falas_ao_chegar_próximo(Hitbox de quanto é próximo,Dicionario com as_falas desse personagem,Booleano = (randomico ou não)):

		if colide com a Hitbox:
			if Booleano:
				Dicionario com as_falas desse personagem
			else:
				Dicionario com as_falas desse personagem

class Porta(HitBox):

	def __init__(self, Posição, Tamanho=None, Raio=None):
		super().__init__(Posição, Tamanho, Raio)
		# Tamanho = (Largura , Altura)
		# Posição = (X , Y)

	def Mudança_de_Sala(Booleano, Sala que irá entrar):

		if Booleano:
			"Vai pra sala x"
'''