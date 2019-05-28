from Configurações import *

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

	def __init__(self):
		super().__init__()

		self.image = ALIEN

		self.rect = self.image.get_rect()

		self.rect.centerx = 0
		self.rect.centery = 0

	def update(self):
		self.speedx =  800 - self.rect.centerx
		self.speedy =  450 - self.rect.centery
		

		self.rect.centerx += (self.speedx)/200
		self.rect.centery += (self.speedy)/200
