# EP 2019-2: Insper Run
#
# Alunos: 
# - Lucas Hix, lucash@al.insper.edu.br
# - Fernando Giuseppe Avila Beltramo, fernandogab@al.insper.edu.br
# - Daniel Gurgel Terra, danielgt1@al.insper.edu.br

import Default
import pygame
from FileController import YamlFile
from tela_inicial import tela_inicial
from tela_jogo import tela_jogo
from Configs import INIT, QUIT, NEW_GAME, LARGURA, ALTURA, FPS

#Arquivo as configurações opcionais do jogo

pygame.init()

pygame.display.set_caption(Default.NOME_DO_JOGO)

clock = clock = pygame.time.Clock()
screen = pygame.display.set_mode((LARGURA, ALTURA))


all_sprites = pygame.sprite.Group()

try:
    state = INIT
    while state != QUIT:
        if state == INIT:
            state = tela_inicial(screen)
        elif state == NEW_GAME:
            state = tela_jogo(screen)
        else:
            state = QUIT
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
                break

finally:
	pygame.quit()