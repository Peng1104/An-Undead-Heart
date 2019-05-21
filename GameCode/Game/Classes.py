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

	def atualização(self):
		self.rect.x += self.speedx
		self.rect.y += self.speedy