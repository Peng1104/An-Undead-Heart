#Arquivo que contem as condições originais do Jogo

from os import path

#Nome do jogo
NOME_DO_JOGO = "PlaceHolder"

#Diretorios
Dir_Principal = path.join(path.dirname(__file__), "Configurações")

Dir_Imagens = path.join(Dir_Principal, "Imagens")
Dir_Opções = path.join(Dir_Principal, "Opções")

#Clock do Jogo
FPS = 60

#Alura da Página do Jogo
ALTURA = 900

#Largura da Página do Jogo
LARGURA = 1600

#Cores do Jogo
BRANCO = (255, 255, 255, 255)
PRETO = (0, 0, 0, 255)
VERMELHO = (255, 0, 0, 255)
VERDE = (0, 255, 0, 255)
AZUL = (0, 0, 255, 255)
AMARELO = (255, 255, 0, 255)

#Estados do Jogo
INICIANDO = 0
NOVO_JOGO = 1
CARREGAR_JOGO = 2
OPÇÕES = 3
SAIR = 4