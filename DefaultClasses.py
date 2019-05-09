import os
import pygame

class Maps():

	def __init__(self):
		self.maps = self.loadFile("Configurações do Jogo/Imagens/Mapas", {})

	def loadFile(self, path, maps):
		for location, d, lista in os.walk(path):
			for file in lista:
				if file.find(".") > 0:
					if location[location.rfind("/")+1:] in maps:
						lista2 = maps[location[location.rfind("/")+1:]]

						lista2.append(pygame.image.load(location + "/" + file))

						maps[location[location.rfind("/")+1:]] = lista2
					else:
						maps[location[location.rfind("/")+1:]] = [pygame.image.load(location + "/" + file)]
				else:
					maps[location[location.rfind("/")+1:]] = self.loadFile(location + "/" + file, {})
		return maps

class DefaultPlayer(pygame.sprite.Sprite):

	def __init__(self):
		super().__init__()

		self.PlayerImage = None

		self.rect = self.image.get_rect()