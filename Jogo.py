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
config = YamlFile("Configurações do Jogo/Opções/Config.yml")

FPS = config.getFloat("FPS", default_value=Default.FPS)
Altura = config.getInt("Altura", default_value=Default.Altura)
Largura = config.getInt("Largura", default_value=Default.Largura)

config.save()

pygame.init()

pygame.display.set_caption(Default.Nome_Do_Jogo)

clock = clock = pygame.time.Clock()
screen = pygame.display.set_mode((Largura, Altura))

background = pygame.image.load("Configurações do Jogo/Imagens/Menus/Titulo1.png")
background = pygame.transform.scale(background, (Largura, Altura))
background_rect = background.get_rect()

all_sprites = pygame.sprite.Group()

try:
	rodando = True
	while rodando:
		clock.tick(FPS)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				rodando = False
				break

		screen.blit(background, background_rect)
		all_sprites.draw(screen)

		pygame.display.flip()
finally:
	pygame.quit()