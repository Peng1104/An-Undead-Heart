from Configurações import *

import math

class Jogador(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()

		self.image = JOGADOR

		self.rect = self.image.get_rect()
		
		self.rect.centerx = LARGURA / 2
		self.rect.centery = ALTURA  / 2
		
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

		self.speedx = speedx
		self.speedy = speedy

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

		if self.rect.right > LARGURA:
			self.rect.right = LARGURA
		if self.rect.left < 0:
			self.rect.left = 0
			
		if self.rect.bottom > ALTURA:
			self.rect.bottom = ALTURA
		if self.rect.top < 0:
			self.rect.top = 0

class Aliens (pygame.sprite.Sprite):

	def __init__(self, jogador):
		super().__init__()

		self.jogador = jogador

		self.image = ALIEN_1

		self.rect = self.image.get_rect()

		self.speedx =  0
		self.speedy =  0

		self.posicao()

	def TipoAlien(self):

		self.tipo = random.randint(0,1)
		#self.tipo = 0

		if self.tipo == 0:

			self.image = ALIEN_1

			self.speedx = self.jogador.rect.centerx - self.rect.centerx
			self.speedy = self.jogador.rect.centery - self.rect.centery

			self.norma = math.sqrt(self.speedx**2 + self.speedy**2)

			if self.norma > 0.0:
				self.speedx /= self.norma
				self.speedy /= self.norma

		if self.tipo == 1:

			self.image = ALIEN_2

			self.speedx = 800 - self.rect.x
			self.speedy = 450 - self.rect.y

			self.norma = math.sqrt(self.speedx**2 + self.speedy**2)

			if self.norma > 0.0:
				self.speedx /= self.norma
				self.speedy /= self.norma

	def posicao(self):
		self.valor = random.randint(0,3)

		if self.valor == 0:
			self.rect.centerx = random.randrange(-200, 1800)
			self.rect.centery = random.randrange(-200, -100)

			self.pos_x = self.rect.centerx
			self.pos_y = self.rect.centery

		if self.valor == 1:
			self.rect.centerx = random.randrange(-200, 1800)
			self.rect.centery = random.randrange(1000, 1100)

			self.pos_x = self.rect.centerx
			self.pos_y = self.rect.centery

		if self.valor == 2:
			self.rect.centerx = random.randrange(-200, -100)
			self.rect.centery = random.randrange(-200, 1100)

			self.pos_x = self.rect.centerx
			self.pos_y = self.rect.centery

		if self.valor == 3:
			self.rect.centerx = random.randrange(1700, 1800)
			self.rect.centery = random.randrange(-200, 1100)

			self.pos_x = self.rect.centerx
			self.pos_y = self.rect.centery

		self.TipoAlien()

	def update(self):
		
		self.pos_x += (self.speedx)*3
		self.pos_y += (self.speedy)*3

		self.rect.centerx = int(self.pos_x)
		self.rect.centery = int(self.pos_y)

		if (self.rect.bottom > ALTURA + 300) or (self.rect.left < -300) or (self.rect.right > LARGURA + 300) or (self.rect.top < -300) :
			self.posicao()

class Pewpew (pygame.sprite.Sprite):
	def __init__(self,jogador):
		super().__init__()

		self.image = PEWPEW

		self.imagem_original = PEWPEW

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

class Bullet (pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()

		self.image = BULLET

		self.rect = self.image.get_rect()

		self.rect.bottom = y
		self.rect.centerx = x
		self.speedy = -10

	def update(self):
		self.rect.y += self.speedy
		
		if self.rect.bottom < 0:
			self.kill()