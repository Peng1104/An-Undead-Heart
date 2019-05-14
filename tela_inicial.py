import pygame
from os import path

from Configs import img_dir, VERMELHO, VERDE, AMARELO, AZUL, PRETO, FPS, NEW_GAME, LOAD_GAME, OPTIONS, QUIT

def tela_inicial(screen):
    clock = pygame.time.Clock()

    background = pygame.image.load(path.join(img_dir, 'Titulo1.png')).convert()
    background_rect = background.get_rect()
    botoes = pygame.image.load(path.join(img_dir, 'Tela_inicial_botoes.png')).convert()

    running = True
    while running:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            
            mouse_x, mouse_y = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONDOWN: # Verificar se pygame.MOUSEBUTTONUP é mais intuitivo para o jogador
                color = botoes.get_at((mouse_x,mouse_y))
                if color == AZUL:
                    state = NEW_GAME
                    return state
                    running = False
                if color == AMARELO:
                    state = LOAD_GAME
                    running = False
                if color == VERMELHO:
                    state = OPTIONS
                    running = False
                if color == VERDE:
                    state = QUIT
                    running = False
                    
        screen.fill(PRETO)
        screen.blit(background, background_rect)

        pygame.display.flip()

    return state