import os
import pygame
from pathlib import Path

class LoadImagens():

	def __init__(self, FilePath):
		if type(FilePath) == str:
			if Path(FilePath).is_file():
				raise NotADirectoryError("FilePath não é um Dirétorio!!")
			else:
				self.maps = self.loadFile(FilePath, {})
		else:
			raise TypeError("ERRO! FilePath deve ser uma String")

	def __loadFile__(self, FilePath, maps):
		for location, d, lista in os.walk(FilePath):
			for file in lista:
				if file.find(".") > 0:
					if file.endswith(".png") or file.endswith(".jpg") or file.endswith(".gif") or file.endswith(".bmp") or file.endswith(".pcx") or file.endswith(".tga") or file.endswith(".tif") or file.endswith(".lbm") orfile.endswith(".pbm") or orfile.endswith(".pgm") or orfile.endswith(".ppm") or orfile.endswith(".xpm"):  
						if file[:-4] in maps:
							continue
						else:
							imagem = pygame.image.load(location + "/" + file)
							Largura = imagem.get_size()[0]
							Altura = imagem.get_size()[1]
							Centro = (Largura/2, Altura/2)

							maps[file[:-4]] = [imagem, Largura, Altura, Centro]
					else:
						continue
				else:
					maps[file] = self.loadFile(location + "/" + file, {})
		return maps

		def getImages(self):
			return self.maps