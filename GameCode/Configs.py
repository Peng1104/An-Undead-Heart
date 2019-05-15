from os import path, pardir

#Arquivo das configurações do Jogo

#Diretório Principal (Diretorio Pai)
Dir_Principal = path.join("Configurações")

#Diretório das Imagens
Dir_Imagens = path.join(Dir_Principal, "Imagens")

#Diretório do Arquivo Config.yml
Dir_Opções = path.join(Dir_Principal, "Opções")

#Resoluções do Jogo todas 16:9
RESOLUÇÕES = {
	1 : (640, 360),
	2 : (960, 540),
	3 : (1024, 576),
	4 : (1280, 720),
	5 : (1600, 900),
	6 : (1920, 1080)
}

#Transformadores para a escala dos objetos
MULTIPLICADORES = {
	1 : 3,
	2 : 2,
	3 : 1.6/3,
	4 : 2/3,
	5 : 2.5/3,
	6 : 1
}

#Cores base
BRANCO = (255, 255, 255, 255)
PRETO = (0, 0, 0, 255)
VERMELHO = (255, 0, 0, 255)
VERDE = (0, 255, 0, 255)
AZUL = (0, 0, 255, 255)
AMARELO = (255, 255, 0, 255)
ROSA = (255, 0, 255, 255)
CIANO = (0, 255, 255, 255)

#Estados do Jogo
SEM_MUDANÇA = -1
MENU_PRINCIPAL = 0
SAIR = 1
MENU_DAS_OPÇÕES = 2
MENU_DE_COMO_JOGAR = 3
MENU_DE_VIDEO = 4
NOVO_JOGO = 5
CARREGAR_JOGO = 6