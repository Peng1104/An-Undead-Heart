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

	def update(self):
		self.HitBox.Atualizar_Localização(self.HitBox.PosiçãoX + self.speedx)
		self.HitBox.Atualizar_Localização(self.HitBox.PosiçãoY + self.speedy, False)

		if self.HitBox.PosiçãoX < 0:
			self.HitBox.PosiçãoX = 0

		if self.HitBox.PosiçãoX > int(1920*self.Multiplicador - self.HitBox.Retangulo.width):
			self.HitBox.PosiçãoX = int(1920*self.Multiplicador - self.HitBox.Retangulo.width)

		if self.HitBox.PosiçãoY < 0:
			self.HitBox.PosiçãoY = 0

		if self.HitBox.PosiçãoY > int(1080*self.Multiplicador - self.HitBox.Retangulo.height):
			self.HitBox.PosiçãoY = int(1080*self.Multiplicador - self.HitBox.Retangulo.height)

		super().update()

class NPC(Novo_Objeto):

	def __init__(self, Imagem, Multiplicador, Posição, ColorKey=(255, 0, 0)):
		super().__init__(Imagem, Multiplicador, Posição, None, ColorKey)
