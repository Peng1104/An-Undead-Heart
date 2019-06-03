import pygame
import random
import time
from os import path
import math

pygame.init()
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

TELA     = pygame.display.set_mode((LARGURA, ALTURA))
NOME     = "LAST SURPRISE"
pygame.display.set_caption(NOME)

#==================#

IMAGENS  = path.join(path.dirname(__file__), "Imagens")

JOGADOR    = pygame.image.load(path.join(IMAGENS, "JOGADOR.png")).convert()
JOGADOR    = pygame.transform.scale( JOGADOR, (50,50) )
JOGADOR.set_colorkey(VERMELHO)

ALIEN_1    = pygame.image.load(path.join(IMAGENS, "ALIEN1.png")).convert()
ALIEN_1    = pygame.transform.scale( ALIEN_1, (50,50) )
ALIEN_1.set_colorkey(PRETO)

ALIEN_2    = pygame.image.load(path.join(IMAGENS, "ALIEN2.png")).convert()
ALIEN_2    = pygame.transform.scale( ALIEN_2, (50,50) )
ALIEN_2.set_colorkey(PRETO)

PEWPEW     = pygame.image.load(path.join(IMAGENS, "PEWPEW.png")).convert()
PEWPEW     = pygame.transform.scale( PEWPEW, (50,50) )
PEWPEW.set_colorkey(BRANCO)

BULLET     = pygame.image.load(path.join(IMAGENS, "BULLET.png")).convert()
BULLET.set_colorkey(BRANCO)

MASCARA    =   pygame.image.load(path.join(IMAGENS, "MASCARA.png")).convert()
FUNDO      =   pygame.image.load(path.join(IMAGENS, "FUNDO.png")).convert()
FUNDO_RECT =   FUNDO.get_rect()

#=================#

SCORE = pygame.font.Font(path.join(IMAGENS, "PressStart2P.ttf"), 28)

#=================#

#SONS    = path.join(path.dirname(__file__), "Sons"   )
#pygame.mixer.music.load(path.join(snd_dir, 'musica.ogg'))
#pygame.mixer.music.set_volume(0.4)
#boom_sound = pygame.mixer.Sound(path.join(snd_dir, 'musica.ogg'))

#==================#