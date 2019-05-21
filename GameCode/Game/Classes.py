#Arquivo que contem as class que vão ser usadas no Jogo

from GameCode.Construtores.Classes_Base import Novo_Objeto

class Jogador(Novo_Objeto):

	def __init__(self, Imagem, Multiplicador, Posição):
		super().__init__(Imagem, Multiplicador, Posição)

		self.speedx = 0
		self.speedy = 0

	def speed(self, speedx, speedy):
		self.speedx = speedx
		self.speedy = speedy

		if self.speedx != 0:
			if self.speedx > 0:
				self.Atualizar_Imagem(Imagens["DIREITA"])
			else:
				self.Atualizar_Imagem(Imagens["ESQUERDA"])

		if self.speedx != 0:
			if self.speedy > 0:
				self.Atualizar_Imagem(Imagens["FRENTE"])
			else:
				self.Atualizar_Imagem(Imagens["ATRAS"])

	def atualização(self):
		self.rect.x += self.speedx
		self.rect.y += self.speedy
