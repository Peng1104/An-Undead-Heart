# EP 2019-2: Insper Run
#
# Alunos: 
# - Lucas Hix, lucash@al.insper.edu.br
# - Fernando Giuseppe Avila Beltramo, fernandogab@al.insper.edu.br
# - Daniel Gurgel Terra, danielgt1@al.insper.edu.br

import pygame
import Default
import Telas
from ImageController import LoadImagens
from FileController import YamlFile
from Default import INICIANDO, NOVO_JOGO, CARREGAR_JOGO, OPÇÕES, SAIR

#Arquivo que contem as opções do jogo
config = YamlFile(Default.Dir_Opções + "/Config.yml")

#Variaveis do Jogo
FPS = config.getFloat("FPS", default_value=Default.FPS)
ALTURA = config.getInt("Altura", default_value=Default.ALTURA)
LARGURA = config.getInt("Largura", default_value=Default.LARGURA)
NOME_DO_JOGO = config.getString("Nome do Jogo", default_value=Default.NOME_DO_JOGO)

#Salvar o Arquivo
config.save()

#Imagens do Jogo
Imagens = LoadImagens(Default.Dir_Imagens).getImagens()

#Iniciando o Jogo
pygame.init()

#Aplica o FPS ao Jogo
pygame.time.Clock().tick(FPS)

#Aplicar nome do Jogo a Janela do Jogo
pygame.display.set_caption(NOME_DO_JOGO)

#Aplicar tamanho para a Janela do Jogo
tela = pygame.display.set_mode((LARGURA, ALTURA))

#
all_sprites = pygame.sprite.Group()

#Jogo em si
try:
    Estado = INICIANDO

    while Estado != SAIR:

    	#Fechando o Jogo atravez do X
    	for event in pygame.event.get():
    		if event.type == pygame.QUIT:
    	 		Estado = SAIR
    	 		break
    	
    	if Estado == SAIR:
    		break
    	elif Estado == INICIANDO:
        	Estado = Telas.Menu_Principal(tela, Imagens.get("Menu Principal"), (LARGURA, ALTURA))
finally:
	pygame.quit()