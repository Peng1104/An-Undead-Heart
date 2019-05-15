#Arquivo que contem as condições originais do Jogo
from os import path

#Diretorios
Dir_Principal = path.join(path.dirname(__file__), "Configurações")

Dir_Imagens = path.join(Dir_Principal, "Imagens")
Dir_Opções = path.join(Dir_Principal, "Opções")

#Resoluções do Jogo
RESOLUÇÕES = {
	1 : (640, 360), 
	2 : (960, 540),
	3 : (1024, 576),
	4 : (1280, 720),
	5 : (1600, 900),
	6 : (1920, 1080)
}

#Transformadores para a escala dos objetos
DIVISORES = {
	1 : 3,
	2 : 2,
	3 : 1.6/3,
	4 : 2/3,
	5 : 2.5/3,
	6 : 1
}

#Cores do Jogo
BRANCO = (255, 255, 255, 255)
PRETO = (0, 0, 0, 255)
VERMELHO = (255, 0, 0, 255)
VERDE = (0, 255, 0, 255)
AZUL = (0, 0, 255, 255)
AMARELO = (255, 255, 0, 255)

#Estados do Jogo
SEM_MUDANÇA = -1
MENU_PRINCIPAL = 0
SAIR = 1
NOVO_JOGO = 2
CARREGAR_JOGO = 3
MENU_DAS_OPÇÕES = 4
MENU_DE_VIDEO = 5
MENU_DE_COMO_JOGAR = 6