#Arquivo que contem as class que vão ser usadas no Jogo

from GameCode.Construtores.Classes_Base import Novo_Objeto

class Jogador(Novo_Objeto):

	def __init__(self, Lista_de_Imagens, Multiplicador, Posição, Colorkey=(255, 0, 0, 255)):
		super().__init__(Lista_de_Imagens[0], Multiplicador, Posição, None, Colorkey)

		self.Colorkey = Colorkey
		self.Lista_de_Imagens = Lista_de_Imagens

		self.speedx = 0
		self.speedy = 0

		self.posiçãox = 0
		self.posiçãoy = 0

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

	def Atualiza_Posição(self, Colisão):
		if Colisão:
			if self.speedy < 0:
				self.posiçãoy = self.HitBox.Retangulo.y + 40
				self.posiçãox = self.HitBox.Retangulo.x

			elif self.speedy > 0:
				self.posiçãoy = self.HitBox.Retangulo.y - 40
				self.posiçãox = self.HitBox.Retangulo.x

			elif self.speedx < 0:
				self.posiçãoy = self.HitBox.Retangulo.y
				self.posiçãox = self.HitBox.Retangulo.x + 40

			elif self.speedx > 0:
				self.posiçãoy = self.HitBox.Retangulo.y
				self.posiçãox = self.HitBox.Retangulo.x - 40
		else:
			self.posiçãox = self.HitBox.Retangulo.x + self.speedx
			self.posiçãoy = self.HitBox.Retangulo.y + self.speedy

	def update(self):
		self.HitBox.Atualizar_Localização(self.posiçãox)
		self.HitBox.Atualizar_Localização(self.posiçãoy,False)

class NPC(Novo_Objeto):

	def __init__(self, Imagem, Multiplicador, Posição, ColorKey=(255, 0, 0)):
		super().__init__(Imagem, Multiplicador, Posição, None, ColorKey)

#class Falas(Novo_Objeto):

#	def __init__(self, Imagem, Multiplicador, Posição, Raio = 30,ColorKey=(255, 0, 0)):
#		super().__init__(Imagem, Multiplicador, Posição, Raio, ColorKey)
