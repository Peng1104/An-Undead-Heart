import pygame
from os import path
from GameCode.Construtores.Classes_Base import Novo_Objeto
from GameCode.Configs import PRETO, VERMELHO, SAIR, IMAGENS_DO_JOGO

#----------------------------------------------------------------------------------------------

# Carrega as imagens do diretório: "Game"
Imagens = IMAGENS_DO_JOGO["Game"]

#==================================================================================================================================================

# Classe Jogador
class Jogador(Novo_Objeto):
    
    # Construtor da classe.
    def __init__(self):
        
        super().__init__(Imagens["FRENTE"])
        
        # Velocidade do personagem
        self.speedx = 0
        self.speedy = 0

    # Atualiza a posição do jogador
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy


#===========================================================================================================================================================

def tela_jogo(Tela, Multiplicador):

    plano_de_fundo = Imagens["ACADEMIA"]
    plano_de_fundo_rect = plano_de_fundo.get_rect()

    jogador = Jogador()
    
    todos_os_sprites = pygame.sprite.Group()
    todos_os_sprites.add(jogador)

##----------------------------------------------------------------------------------------------
    
    PLAYING = 0
    DONE = 1
    
    Estado = PLAYING
    while Estado != DONE:
        
        for EVENTO in pygame.event.get():

            # Ao pressionar tecla
            if EVENTO.type == pygame.KEYDOWN:

                # Qual tecla, o que ocorre...

                if EVENTO.key == pygame.K_LEFT:
                    jogador.speedx = 5

                if EVENTO.key == pygame.K_RIGHT:
                    jogador.speedx = -5

                if EVENTO.key == pygame.K_UP:
                    jogador.speedy = 5

                if EVENTO.key == pygame.K_DOWN:
                    jogador.speedy = -5

                if EVENTO.key == pygame.K_q:
                    state = DONE

            # Ao soltar tecla
            if EVENTO.type == pygame.KEYUP:

                # Qual tecla, o que ocorre...
                if EVENTO.key == pygame.K_LEFT:
                    jogador.speedx = 0

                if EVENTO.key == pygame.K_RIGHT:
                    jogador.speedx = 0

                if EVENTO.key == pygame.K_UP:
                    jogador.speedy = 0

                if EVENTO.key == pygame.K_DOWN:
                    jogador.speedy = 0

#--------------------------------------------------------------------------------------------------
        
        todos_os_sprites.update()
        # A cada loop, redesenha o fundo e os sprites
        Tela.fill( PRETO )

        Tela.blit( plano_de_fundo, plano_de_fundo_rect )

        todos_os_sprites.draw( Tela )
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return SAIR