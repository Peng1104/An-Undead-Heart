#Arquivo das variáveis do Jogo

from os import path
from GameCode.Construtores.FileController import YamlFile
from GameCode.Construtores.Classes_Base import CarregarImagens

#Diretório Principal (Diretorio Pai)
DIR_PRINCIPAL = path.join("Configurações")

#Diretório das Imagens
DIR_IMAGENS = path.join(DIR_PRINCIPAL, "Imagens")

#Diretório das Configurações do jogo
DIR_OPÇÕES = path.join(DIR_PRINCIPAL, "Opções")

#Transformadores para a escala dos objetos
MULTIPLICADORES = {
	1 : 1/3,
	2 : 1/2,
	3 : 1.6/3,
	4 : 2/3,
	5 : 2.5/3,
	6 : 1
}

#Arquivo que contem as opções do jogo
CONFIG = YamlFile(DIR_OPÇÕES + "/Config.yml")

#Imagens do Jogo
IMAGENS_DO_JOGO = CarregarImagens(DIR_IMAGENS).getImagens()

#Cores base
BRANCO = (255, 255, 255, 255)
PRETO = (0, 0, 0, 255)
VERMELHO = (255, 0, 0, 255)
VERDE = (0, 255, 0, 255)
AZUL = (0, 0, 255, 255)
AMARELO = (255, 255, 0, 255)
ROSA = (255, 0, 255, 255)
CIANO = (0, 255, 255, 255)
LARANJA = (255, 125, 0 ,255)
ROXO = (125, 0, 255, 255)

#Estados do Jogo
SEM_MUDANÇA = -1
MENU_PRINCIPAL = 0
SAIR = 1
MENU_DAS_OPÇÕES = 2
MENU_DE_COMO_JOGAR = 3
MENU_DE_VIDEO = 4
ATIVAR_TELA_CHEIA = 5
DESATIVAR_TELA_CHEIA = 6
RESOLUÇÃO_DE_1080P = 7
RESOLUÇÃO_DE_900P = 8
RESOLUÇÃO_DE_720P = 9
RESOLUÇÃO_DE_576P = 10
RESOLUÇÃO_DE_540P = 11
RESOLUÇÃO_DE_360P = 12
MENU_PARA_CARREGAR_JOGO_SALVO = 13
MENU_DE_NOVO_JOGO = 14
JOGO = 15