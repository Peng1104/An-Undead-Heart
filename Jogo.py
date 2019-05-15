# EP 2019-2: Insper Run
#
# Alunos: 
# - Lucas Hix, lucash@al.insper.edu.br
# - Fernando Giuseppe Avila Beltramo, fernandogab@al.insper.edu.br
# - Daniel Gurgel Terra, danielgt1@al.insper.edu.br

import pygame
import Telas
from Configs import *
from ImageController import LoadImagens
from FileController import YamlFile

#Arquivo que contem as opções do jogo
config = YamlFile(Dir_Opções + "/Config.yml")

#Imagens do Jogo
Imagens = LoadImagens(Dir_Imagens).getImagens()

#Inicia o Jogo
pygame.init()

#Vareavel do Clock (FPS)
if config.getFloat("FPS", default_value=60) < 1.0:
	config.set("FPS", 60)

#Ativa o Clock do Jogo
pygame.time.Clock().tick(config.getFloat("FPS", default_value=60))

#Aplicar nome do Jogo a Janela do Jogo
pygame.display.set_caption(config.getString("Nome do Jogo", default_value="An Undead Heart"))

#Vareavel de Resolução do Jogo
if config.getInt("Nível de Resolução do Jogo", default_value=4) > 6 or config.getInt("Nível de Resolução do Jogo") < 1:
	config.set("Nível de Resolução do Jogo", 4)

#Cria a Tela ultilizando a Resolução do Jogo
if config.getBoolean("Tela Cheia", default_value=False):
	Tela = pygame.display.set_mode(RESOLUÇÕES[config.getInt("Nível de Resolução do Jogo")], flags=pygame.FULLSCREEN)
else:
	Tela = pygame.display.set_mode(RESOLUÇÕES[config.getInt("Nível de Resolução do Jogo")])

#Define o tamanho das Imagens
MULTIPLICADOR = MULTIPLICADORES[config.getInt("Nível de Resolução do Jogo")]

#Todas As Imagens Transformadas
all_sprites = pygame.sprite.Group()

#Jogo em si
try:
    Estado = MENU_PRINCIPAL

    while Estado != SAIR:

        #Fechando o Jogo atravez do X
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Estado = SAIR
                break

        if Estado == SAIR:
            break
        elif Estado == MENU_PRINCIPAL:
            Estado = Telas.Menu_Principal(Imagens.get("Menu Principal")).run(Tela, MULTIPLICADOR)
        elif Estado == MENU_DAS_OPÇÕES:
            Estado = Telas.Menu_De_Opções(Imagens.get("Menu de Opções")).run(Tela, MULTIPLICADOR)
        elif Estado == MENU_DE_COMO_JOGAR:
            Estado = Telas.Menu_De_Como_Jogar(Imagens.get("Menu de Como Jogar")).run(Tela, MULTIPLICADOR)
        elif Estado == MENU_DE_VIDEO:
            Estado = Telas.Menu_De_Video(Imagens.get("Menu de Vídeo")).run(Tela, MULTIPLICADOR)
finally:
	pygame.quit()
	#Salvar o Arquivo
	config.save()