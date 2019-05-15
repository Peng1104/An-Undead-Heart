import os
import pygame
from pathlib import Path

class LoadImagens():

	def __init__(self, FilePath):
		if type(FilePath) == str:
			if Path(FilePath).is_file():
				raise NotADirectoryError("FilePath não é um Dirétorio!!")
			else:
				self.maps = self.__loadFile__(FilePath, {})
		else:
			raise TypeError("ERRO! FilePath deve ser uma String")

	def __loadFile__(self, FilePath, maps):
		for file in os.listdir(FilePath):
			if file.find(".") > 0:
				if file.endswith(".png") or file.endswith(".jpg") or file.endswith(".gif") or file.endswith(".bmp") or file.endswith(".pcx") or file.endswith(".tga") or file.endswith(".tif") or file.endswith(".lbm") or file.endswith(".pbm") or file.endswith(".pgm") or file.endswith(".ppm") or file.endswith(".xpm"):  
					if not file[:-4] in maps:
						maps[file[:-4]] = pygame.image.load(FilePath + "/" + file)
			else:
				maps[file] = self.__loadFile__(FilePath + "/" + file, {})
		return maps

	def getImagens(self):
		return self.maps