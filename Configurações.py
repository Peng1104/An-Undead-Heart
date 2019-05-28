import pygame
import random
import time
from os import path
import math
#==================#

LARGURA  = 1600
ALTURA   = 900

#==================#

BRANCO   = (255, 255, 255)
PRETO    = (0, 0, 0)
VERMELHO = (255, 0, 0)
VERDE    = (0, 255, 0)
AZUL     = (0, 0, 255)
AMARELO  = (255, 255, 0)

#==================#

IMAGENS  = path.join(path.dirname(__file__), "Imagens")
#SONS    = path.join(path.dirname(__file__), "Sons"   )

#==================#

TELA     = pygame.display.set_mode((LARGURA, ALTURA))
RELÓGIO  = pygame.time.Clock().tick(60)
NOME     = "LAST SURPRISE"
pygame.display.set_caption(NOME)

#==================#

JOGADOR    = pygame.image.load(path.join(IMAGENS, "JOGADOR.png")).convert()
JOGADOR    = pygame.transform.scale( JOGADOR, (50,50) )
JOGADOR.set_colorkey(VERMELHO)

ALIEN_1    = pygame.image.load(path.join(IMAGENS, "ALIEN1.png")).convert()
ALIEN_1    = pygame.transform.scale( ALIEN_1, (50,50) )
ALIEN_1.set_colorkey(PRETO)

ALIEN_2    = pygame.image.load(path.join(IMAGENS, "ALIEN2.png")).convert()
ALIEN_2    = pygame.transform.scale( ALIEN_2, (50,50) )
ALIEN_2.set_colorkey(PRETO)

MASCARA    =   pygame.image.load(path.join(IMAGENS, "MASCARA.png")).convert()
FUNDO      =   pygame.image.load(path.join(IMAGENS, "FUNDO.png")).convert()
FUNDO_RECT =   FUNDO.get_rect()