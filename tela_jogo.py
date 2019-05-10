import pygame
import random
from os import path

from Configs import INIT, QUIT, NEW_GAME, LARGURA, ALTURA, FPS, PRETO, img_dir

# Classe Jogador que representa a nave
class Player(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self, player_img):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        self.image = player_img
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(player_img, (50, 38))
        
        # Deixando transparente.
        self.image.set_colorkey(PRETO)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Centraliza embaixo da tela.
        self.rect.centerx = LARGURA / 2
        self.rect.bottom = ALTURA / 2
        
        # Velocidade da nave
        self.speedx = 0
        self.speedy = 0
        
        # Melhora a colisão estabelecendo um raio de um circulo
        self.radius = 25
    
    # Metodo que atualiza a posição da navinha
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        # Mantem dentro da tela
        if self.rect.right > LARGURA:
            self.rect.right = LARGURA
        if self.rect.left < 0:
            self.rect.left = 0
                    
            
def tela_jogo(screen):
    background = pygame.image.load(path.join(img_dir, 'Escola 01.jpg')).convert()
    background_rect = background.get_rect()
    player = Player(pygame.image.load(path.join(img_dir, "pawn.png")).convert())
    
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    
    clock = pygame.time.Clock()
    
    PLAYING = 0
    DONE = 1
    
    state = PLAYING
    while state != DONE:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.speedx = -8
                if event.key == pygame.K_RIGHT:
                    player.speedx = 8
                if event.key == pygame.K_UP:
                    player.speedy = -8
                if event.key == pygame.K_DOWN:
                    player.speedy = 8
                if event.key == pygame.K_q:
                    state = QUIT
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.speedx = 0
                if event.key == pygame.K_RIGHT:
                    player.speedx = 0
                if event.key == pygame.K_UP:
                    player.speedy = 0
                if event.key == pygame.K_DOWN:
                    player.speedy = 0
        
        all_sprites.update()
        # A cada loop, redesenha o fundo e os sprites
        screen.fill(PRETO)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return QUIT