# -*- coding: utf-8 -*-
"""
Created on Tue May  7 00:48:00 2019

@author: Yang
"""

import pygame
import random
from os import path

from config import img_dir, BLACK, FPS, GAME, QUIT

def tela_inicial(screen):
    clock = pygame.time.Clock()

    background = pygame.image.load(path.join(img_dir, 'Titulo1.png')).convert()
    background_rect = background.get_rect()

    running = True
    while running:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            
            mouse_x, mouse_y = pygame.mouse.get_pos()
            
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN: # Verificar se pygame.MOUSEBUTTONUP é mais intuitivo para o jogador
                if (mouse_x > 291) and (mouse_x < 501):
                    if (mouse_y > 203) and (mouse_y < 282):
                        state = NEW_GAME
                        running = False
                    if (mouse_y > 284) and (mouse_y < 362):
                        state = LOAD_GAME
                        running = False
                    if (mouse_y > 364) and (mouse_y < 442):
                        state = OPCOES
                        running = False
                    if (mouse_y > 444) and (mouse_y < 522):
                        state = QUIT
                        running = False
                    
        screen.fill(BLACK)
        screen.blit(background, background_rect)

        pygame.display.flip()

    return state