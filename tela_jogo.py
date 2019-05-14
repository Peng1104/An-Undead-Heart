import pygame
import random
from os import path

from Configs import INIT, QUIT, NEW_GAME, LARGURA, ALTURA, FPS, PRETO, img_dir

#classe

# Classe Jogador
class Player(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self, player_img, camera):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        self.camera = camera
        
        # Carregando a imagem de fundo.
        self.image = player_img
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(player_img, (50, 38))
        
        # Deixando transparente.
        self.image.set_colorkey(PRETO)
        
        self.px = LARGURA / 2
        self.py = ALTURA / 2
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Centraliza embaixo da tela.
        self.rect.centerx = self.px - self.camera.px
        self.rect.centery = self.py - self.camera.py
        
        # Velocidade da nave
        self.speedx = 0
        self.speedy = 0
        
        # Melhora a colisão estabelecendo um raio de um circulo
        self.radius = 25
    
    # Metodo que atualiza a posição da navinha
    def update(self):
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

def tela_jogo(screen):
    background = pygame.image.load(path.join(img_dir, 'Escola 01.jpg')).convert()
    background_rect = background.get_rect()
    
    camera = Camera(0, 0)
    
    player = Player(pygame.image.load(path.join(img_dir, "pawn.png")).convert(), camera)
    
    
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
                    player.speedx = 8
                if event.key == pygame.K_RIGHT:
                    player.speedx = -8
                if event.key == pygame.K_UP:
                    player.speedy = 8
                if event.key == pygame.K_DOWN:
                    player.speedy = -8
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
        background_rect.x = camera.px
        background_rect.y = camera.py
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return QUIT