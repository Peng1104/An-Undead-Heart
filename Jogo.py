# EP 2019-2: Insper Run
#
# Alunos: 
# - Lucas Hix, lucash@al.insper.edu.br
# - Fernando Giuseppe Avila Beltramo, fernandogab@al.insper.edu.br
# - Daniel Gurgel Terra, danielgt1@al.insper.edu.br

import pygame
import Telas
from Default import *
from ImageController import LoadImagens
from FileController import YamlFile

#Arquivo que contem as opções do jogo
config = YamlFile(Dir_Opções + "/Config.yml")

#Variaveis do Jogo
GAME_FPS = config.getFloat("FPS", default_value=FPS)
GAME_ALTURA = config.getInt("Altura", default_value=ALTURA)
GAME_LARGURA = config.getInt("Largura", default_value=LARGURA)
GAME_NOME_DO_JOGO = config.getString("Nome do Jogo", default_value=NOME_DO_JOGO)

#Salvar o Arquivo
config.save()

#Imagens do Jogo
Imagens = LoadImagens(Dir_Imagens).getImagens()

#Iniciando o Jogo
pygame.init()

#Aplica o FPS ao Jogo
pygame.time.Clock().tick(GAME_FPS)

#Aplicar nome do Jogo a Janela do Jogo
pygame.display.set_caption(GAME_NOME_DO_JOGO)

#Aplicar tamanho para a Janela do Jogo
Tela = pygame.display.set_mode((GAME_LARGURA, GAME_ALTURA))

#
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
            Estado = Telas.Menu_Principal(Imagens.get("Menu Principal"), (GAME_LARGURA, GAME_ALTURA)).run(Tela)
        elif Estado == MENU_DAS_OPÇÕES:
            Estado = Telas.Menu_De_Opções(Imagens.get("Menu de Opções"), (GAME_LARGURA, GAME_ALTURA)).run(Tela)
        elif Estado == MENU_DE_COMO_JOGAR:
            Estado = Telas.Menu_De_Como_Jogar(Imagens.get("Menu de Como Jogar"), (GAME_LARGURA, GAME_ALTURA)).run(Tela)
        elif Estado == MENU_DE_VIDEO:
            Estado = Telas.Menu_De_Video(Imagens.get("Menu de Vídeo"), (GAME_LARGURA, GAME_ALTURA)).run(Tela)
finally:
	pygame.quit()