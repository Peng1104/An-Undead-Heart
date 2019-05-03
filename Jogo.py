# EP 2019-2: Insper Run
#
# Alunos: 
# - Lucas Hix, lucash@al.insper.edu.br
# - Fernando Giuseppe Avila Beltramo, fernandogab@al.insper.edu.br
# - Daniel Gurgel Terra, danielgt1@al.insper.edu.br

import Default
import pygame
from FileController import YamlFile

#Arquivo as configurações opcionais do jogo
config = YamlFile("Opções/Config.yml")

try:
	running = True
	#Jogo em si
	while running:
		print("Hello World")
		break