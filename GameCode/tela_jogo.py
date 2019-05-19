import pygame
from os import path
from GameCode.Construtores.Classes_Base import Novo_Objeto
from GameCode.Configs import PRETO, VERMELHO, SAIR, IMAGENS_DO_JOGO

# Carrega as imagens do diretório: "Game"
Imagens = IMAGENS_DO_JOGO["Game"]

# Classe Jogador
class Player(Novo_Objeto):
    
    # Construtor da classe.
    def __init__(self, Lista_imagens_player, Multiplicador, camera):
        
        centro_da_tela = ( int(1920/2), int(1080/2) )
        super().__init__(Lista_imagens_player[0], Multiplicador, centro_da_tela)
        
        # Dá camera ao personagem
        self.camera = camera

        # Imagem da câmera
        self.px = 1920/2
        self.py = 1080/2
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Centraliza embaixo da tela.
        self.rect.centerx = self.px - self.camera.px
        self.rect.centery = self.py - self.camera.py
        
        # Velocidade do personagem
        self.speedx = 0
        self.speedy = 0
        
        # Melhora a colisão estabelecendo um raio de um circulo
        self.radius = 25
    
    def update_Imagem(self, Lista_imagens_player, Multiplicador, BAIXO, CIMA, ESQUERDA, DIREITA):
        if BAIXO:
            self.Criar_Objeto(Lista_imagens_player[0], Multiplicador)
        elif CIMA:
            self.Criar_Objeto(Lista_imagens_player[1], Multiplicador)
        elif ESQUERDA:
            self.Criar_Objeto(Lista_imagens_player[2], Multiplicador)
        elif DIREITA:
            self.Criar_Objeto(Lista_imagens_player[3], Multiplicador)

    # Atualiza a posição do Player
    def update_Posição(self):
        self.px += self.speedx
        self.py += self.speedy

        self.camera.px += self.speedx
        self.camera.py += self.speedy
        
        # Centraliza embaixo da tela.
        self.rect.centerx = self.px - self.camera.px
        self.rect.centery = self.py - self.camera.py
        
        # Mantem dentro da tela
        if self.rect.right > LARGURA:
            self.rect.right = LARGURA
        if self.rect.left < 0:
            self.rect.left = 0
                    
class Camera:
    def __init__(self, px, py):
        self.px = px
        self.py = py

def tela_jogo(Tela, Multiplicador):

    Fundo = Imagens["Escola 01"]
    P_Frente = Imagens["FRENTE"]
    P_Atras = Imagens["ATRAS"]
    P_Esquerda = Imagens["ESQ"]
    P_Direita = Imagens["DIR"]

    Lista_imagens_player = [P_Frente, P_Atras, P_Esquerda, P_Direita]

    background = Fundo
    background_rect = background.get_rect()
    
    camera = Camera(0, 0)

    player = Player(Lista_imagens_player, Multiplicador, camera)
    
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    
    PLAYING = 0
    DONE = 1
    
    state = PLAYING
    while state != DONE:
        
        BAIXO, CIMA, ESQUERDA, DIREITA = False, False, False, False
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    player.speedx = 5
                    ESQUERDA = True

                if event.key == pygame.K_RIGHT:
                    player.speedx = -5
                    DIREITA = True

                if event.key == pygame.K_UP:
                    player.speedy = 5
                    CIMA = True

                if event.key == pygame.K_DOWN:
                    player.speedy = -5
                    BAIXO = True

                if event.key == pygame.K_q:
                    state = DONE

            player.update_Imagem(Lista_imagens_player, Multiplicador, BAIXO, CIMA, ESQUERDA, DIREITA)
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.speedx = 0
                    ESQUERDA = False

                if event.key == pygame.K_RIGHT:
                    player.speedx = 0
                    DIREITA = False

                if event.key == pygame.K_UP:
                    player.speedy = 0
                    CIMA = False

                if event.key == pygame.K_DOWN:
                    player.speedy = 0
                    BAIXO = False

            player.update_Imagem(Lista_imagens_player, Multiplicador, BAIXO, CIMA, ESQUERDA, DIREITA)
        
        all_sprites.update()
        # A cada loop, redesenha o fundo e os sprites
        Tela.fill(PRETO)
        background_rect.x = camera.px
        background_rect.y = camera.py
        Tela.blit(background, background_rect)
        all_sprites.draw(Tela)
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return SAIR