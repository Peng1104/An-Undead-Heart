import pygame
from os import path

from GameCode.Configs import PRETO, VERMELHO, SAIR, DIR_IMAGENS

# >> importações temporarias <<
LARGURA = 1920
ALTURA = 1080
FPS = 60
Dir_Game = path.join(DIR_IMAGENS, "Game")

# Classe Jogador
class Player(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self, player_img, camera):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Dá camera ao personagem
        self.camera = camera
        
        # Carregando a imagem do personagem
        self.image = player_img
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(player_img, (200, 200))
        
        # Deixando transparente.
        self.image.set_colorkey(VERMELHO)
        
        self.px = LARGURA /2
        self.py = ALTURA /2
        
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
    
    # Atualiza a posição do Player
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
    background = pygame.image.load(path.join(Dir_Game, 'Escola 01.png')).convert()
    background_rect = background.get_rect()
    
    camera = Camera(0, 0)
    
    player = Player(pygame.image.load(path.join(Dir_Game, "FRENTE.png")).convert(), camera)
    
    
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
                    player.speedx = 5
                if event.key == pygame.K_RIGHT:
                    player.speedx = -5
                if event.key == pygame.K_UP:
                    player.speedy = 5
                if event.key == pygame.K_DOWN:
                    player.speedy = -5
                if event.key == pygame.K_q:
                    state = DONE
            
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

    return SAIR