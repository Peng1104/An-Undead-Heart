# Arquivo que contem as class que vão ser usadas no Jogo

import pygame
import math
import random

class Jogador(pygame.sprite.Sprite):

	def __init__(self, imagem, tamanho_tela):
		super().__init__()

		self.image = imagem

		self.rect = self.image.get_rect()
		self.radius = 25
		
		self.rect.centerx = tamanho_tela[0] / 2
		self.rect.centery = tamanho_tela[1] / 2
		
		self.speedx = 0
		self.speedy = 0

		self.next_positionx = self.rect.x
		self.next_positiony = self.rect.y

		self.last_positionx = self.rect.x
		self.last_positiony = self.rect.y

		self.UP    = False
		self.LEFT  = False
		self.DOWN  = False
		self.RIGHT = False

		self.has_hit = False

	def speed(self):

		if self.UP:
			speedy = -4
			if self.LEFT:
				speedx = -2*(2**0.5)
				speedy = -2*(2**0.5)
			elif self.RIGHT:
				speedx = +2*(2**0.5)
				speedy = -2*(2**0.5)
			else:
				speedx = 0

		elif self.DOWN:
			speedy = 4
			if self.LEFT:
				speedx = -2*(2**0.5)
				speedy = +2*(2**0.5)
			elif self.RIGHT:
				speedx = +2*(2**0.5)
				speedy = +2*(2**0.5)
			else:
				speedx = 0

		elif self.LEFT:
			speedx = -4
			speedy =  0

		elif self.RIGHT:
			speedx = 4
			speedy = 0

		else:
			speedx = 0
			speedy = 0

		self.speedx = speedx * 8
		self.speedy = speedy * 8

	def hitbox(self, rect_objet, has_collided):

		if has_collided:

			if self.rect.left < rect_objet.right and self.rect.left > rect_objet.left:
				self.rect.left = rect_objet.right
				self.next_positionx -= self.speedx

			elif self.rect.right > rect_objet.left and self.rect.right < rect_objet.right:
				self.rect.right = rect_objet.left
				self.next_positionx -= self.speedx

			elif self.rect.top < rect_objet.bottom and self.rect.bottom > rect_objet.bottom:
				self.rect.top = rect_objet.bottom
				self.next_positiony -= self.speedy

			elif self.rect.bottom > rect_objet.top and self.rect.top < rect_objet.top:
				self.rect.bottom = rect_objet.top
				self.next_positiony -= self.speedy

	def wall(self, has_collided):

		if has_collided:

			self.next_positionx = self.last_positionx
			self.next_positiony = self.last_positiony

		else:

			self.next_positionx += self.speedx
			self.next_positiony += self.speedy

			self.last_positionx = self.rect.x
			self.last_positiony = self.rect.y

	def update(self):

		self.speed()

		self.rect.x = self.next_positionx
		self.rect.y = self.next_positiony

class Aliens(pygame.sprite.Sprite):

	def __init__(self, jogador, ALIEN_1, ALIEN_2, tamanho_tela):
		super().__init__()

		self.jogador = jogador

		self.image = ALIEN_1

		self.ALIEN_1 = ALIEN_1
		self.ALIEN_2 = ALIEN_2
		self.tamanho_tela = tamanho_tela

		self.rect = self.image.get_rect()

		self.speedx =  0
		self.speedy =  0

		self.nascimento = pygame.time.get_ticks()

		self.partida = self.nascimento + random.randint(0, 10000)

		self.posicao()

	def TipoAlien(self):

		self.tipo = random.randint(0,1)

		if self.tipo == 0:

			self.image = self.ALIEN_1

			self.speedx = self.jogador.rect.centerx - self.rect.centerx
			self.speedy = self.jogador.rect.centery - self.rect.centery

			self.norma = math.sqrt(self.speedx**2 + self.speedy**2)

			if self.norma > 0.0:
				self.speedx /= self.norma
				self.speedy /= self.norma

		if self.tipo == 1:

			self.image = self.ALIEN_2

			self.speedx = (self.tamanho_tela[0] / 2) - self.rect.x
			self.speedy = (self.tamanho_tela[1] / 2) - self.rect.y

			self.norma = math.sqrt(self.speedx**2 + self.speedy**2)

			if self.norma > 0.0:
				self.speedx /= self.norma
				self.speedy /= self.norma

	def posicao(self):
		self.valor = random.randint(0,3)

		if self.valor == 0:
			self.rect.centerx = random.randrange(-200, (self.tamanho_tela[0] + 200))
			self.rect.centery = random.randrange(-200, -100)

			self.pos_x = self.rect.centerx
			self.pos_y = self.rect.centery

		if self.valor == 1:
			self.rect.centerx = random.randrange(-200, (self.tamanho_tela[0] + 200))
			self.rect.centery = random.randrange((self.tamanho_tela[1] + 100), (self.tamanho_tela[1] + 200))

			self.pos_x = self.rect.centerx
			self.pos_y = self.rect.centery

		if self.valor == 2:
			self.rect.centerx = random.randrange(-200, -100)
			self.rect.centery = random.randrange(-200, (self.tamanho_tela[1] + 200))

			self.pos_x = self.rect.centerx
			self.pos_y = self.rect.centery

		if self.valor == 3:
			self.rect.centerx = random.randrange((self.tamanho_tela[0] + 100), (self.tamanho_tela[0] + 200))
			self.rect.centery = random.randrange(-200, (self.tamanho_tela[1] + 200))

			self.pos_x = self.rect.centerx
			self.pos_y = self.rect.centery

		self.TipoAlien()

	def update(self):

		if self.partida < pygame.time.get_ticks():
		
			self.pos_x += (self.speedx) * 22
			self.pos_y += (self.speedy) * 22

			self.rect.centerx = int(self.pos_x)
			self.rect.centery = int(self.pos_y)

			if (self.rect.bottom > self.tamanho_tela[1] + 300) or (self.rect.left < -300) or (self.rect.right > self.tamanho_tela[0] + 300) or (self.rect.top < -300) :
				self.posicao()

class Arma(pygame.sprite.Sprite):

	def __init__(self, jogador, ARMA):
		super().__init__()

		self.image = ARMA

		self.imagem_original = ARMA

		self.rect = self.image.get_rect()

		self.rect.centerx = jogador.rect.centerx
		self.rect.centery = jogador.rect.centery

	def posição(self,rect_jogador):

		self.rect.centerx = rect_jogador.centerx
		self.rect.centery = rect_jogador.centery

	def rotacionar(self):

		mouse_x, mouse_y = pygame.mouse.get_pos()

		vetor_x, vetor_y = mouse_x - self.rect.centerx, mouse_y - self.rect.centery

		angulo = (180 / math.pi) * ( -math.atan2(vetor_y, vetor_x) )

		self.image = pygame.transform.rotate(self.imagem_original, angulo)

		self.rect = self.image.get_rect(center=self.rect.center)

	def update(self):

		self.rotacionar()

class Bullet(pygame.sprite.Sprite):

	def __init__(self, jogador, BULLET, tamanho_tela):
		super().__init__()

		self.image = BULLET
		self.imagem_original = BULLET

		self.tamanho_tela = tamanho_tela

		self.rect = self.image.get_rect()

		self.pos_x = jogador.rect.centerx
		self.pos_y = jogador.rect.centery

		self.mouse_x, self.mouse_y = pygame.mouse.get_pos()

		self.speedx = self.pos_x - self.mouse_x
		self.speedy = self.pos_y - self.mouse_y

		self.norma = math.sqrt(self.speedx**2 + self.speedy**2)

		if self.norma > 0.0:
			self.speedx /= self.norma
			self.speedy /= self.norma

		self.rotacionar()

	def rotacionar(self):

		mouse_x, mouse_y = pygame.mouse.get_pos()

		vetor_x, vetor_y = mouse_x - self.pos_x, mouse_y - self.pos_y

		angulo = (180 / math.pi) * ( -math.atan2(vetor_y, vetor_x) )

		self.image = pygame.transform.rotate(self.imagem_original, angulo)

		self.rect = self.image.get_rect(center=self.rect.center)

	def update(self):

		self.pos_x -= self.speedx * 30
		self.pos_y -= self.speedy * 30

		self.rect.centerx = int(self.pos_x)
		self.rect.centery = int(self.pos_y)

		if (self.rect.bottom < 0) or (self.rect.top > self.tamanho_tela[1]) or (self.rect.left > self.tamanho_tela[0]) or (self.rect.right < 0) :
			self.kill()