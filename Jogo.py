# EP 2019-2: Insper Run
#
# Alunos: 
# - Lucas Hix, lucash@al.insper.edu.br
# - Fernando Giuseppe Avila Beltramo, fernandogab@al.insper.edu.br
# - Daniel Gurgel Terra, danielgt1@al.insper.edu.br

import pygame
from GameCode.Configs import *
from GameCode.MenuMaker import MenuMaker

#EM FASE DE TESTES
from GameCode.tela_jogo import tela_jogo

def MakeTela(Multiplicador, Tela_Cheia):
    if Tela_Cheia:
        return pygame.display.set_mode((int(1920*MULTIPLICADOR), int(1080*MULTIPLICADOR)), flags=pygame.FULLSCREEN)
    else:
        return pygame.display.set_mode((int(1920*MULTIPLICADOR), int(1080*MULTIPLICADOR)))

#Inicia o Jogo
pygame.init()

#Vareavel do Clock (FPS)
if CONFIG.getFloat("FPS", default_value=60) < 1.0:
	CONFIG.set("FPS", 60)

#Ativa o Clock do Jogo
pygame.time.Clock().tick(CONFIG.getFloat("FPS", default_value=60))

#Aplicar nome do Jogo a Janela do Jogo
pygame.display.set_caption(CONFIG.getString("Nome do Jogo", default_value="An Undead Heart"))

#Vareavel de Resolução do Jogo
if CONFIG.getInt("Nível de Resolução do Jogo", default_value=4) > 6 or CONFIG.getInt("Nível de Resolução do Jogo") < 1:
	CONFIG.set("Nível de Resolução do Jogo", 4)

#Define o tamanho das Imagens
MULTIPLICADOR = MULTIPLICADORES[CONFIG.getInt("Nível de Resolução do Jogo")]

#Cria a Tela do Jogo ultilizando a função MakeTela
Tela = MakeTela(MULTIPLICADOR, CONFIG.getBoolean("Tela Cheia", default_value=False))

#Estado Inicial do Jogo
Estado = MENU_PRINCIPAL

#Runable do Jogo
try:
    while True:

        #Fechando o Jogo atravez do X
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Estado = SAIR
                break

        #PARAR O LOOP
        if Estado == SAIR or Estado == SEM_MUDANÇA:
            break

        #Entra no Menu Principal
        elif Estado == MENU_PRINCIPAL:
            Estado = MenuMaker("Menu Principal").run(Tela, MULTIPLICADOR)

        #Entra no Menu das Opções
        elif Estado == MENU_DAS_OPÇÕES:
            Estado = MenuMaker("Menu de Opções").run(Tela, MULTIPLICADOR)

        #Entra no Menu de Como Jogar
        elif Estado == MENU_DE_COMO_JOGAR:
            Estado = MenuMaker("Menu de Como Jogar").run(Tela, MULTIPLICADOR)

        #Entra no Menu de Vídeo
        elif Estado == MENU_DE_VIDEO:
            Estado = MenuMaker("Menu de Vídeo").run(Tela, MULTIPLICADOR)

        #Ativa a Tela cheia e volta para o Menu de Vídeo
        elif Estado == ATIVAR_TELA_CHEIA:
            #Atualiza a regra no Config
            CONFIG.set("Tela Cheia", True)
            CONFIG.save()

            #Atualiza a Tela
            Tela = MakeTela(MULTIPLICADOR, CONFIG.getBoolean("Tela Cheia"))

            #Retorna para o Menu de Vídeo
            Estado = MENU_DE_VIDEO

        #Desativa a Tela cheia e volta para o Menu de Vídeo
        elif Estado == DESATIVAR_TELA_CHEIA:
            #Atualiza a regra no Config
            CONFIG.set("Tela Cheia", False)
            CONFIG.save()

            #Atualiza a Tela
            Tela = MakeTela(MULTIPLICADOR, CONFIG.getBoolean("Tela Cheia"))

            #Retorna para o Menu de Vídeo
            Estado = MENU_DE_VIDEO

        #Troca para a Resolução de 1080p e volta para o Menu de Vídeo
        elif Estado == RESOLUÇÃO_DE_1080P:
            #Atualiza a regra no Config
            CONFIG.set("Nível de Resolução do Jogo", 6)
            CONFIG.save()

            #Atualiza o Multiplicador
            MULTIPLICADOR = MULTIPLICADORES[CONFIG.getInt("Nível de Resolução do Jogo")]

            #Atualiza a Tela
            Tela = MakeTela(MULTIPLICADOR, CONFIG.getBoolean("Tela Cheia"))

            #Retorna para o Menu de Vídeo
            Estado = MENU_DE_VIDEO

        #Troca para a Resolução de 900p e volta para o Menu de Vídeo
        elif Estado == RESOLUÇÃO_DE_900P:
            #Atualiza a regra no Config
            CONFIG.set("Nível de Resolução do Jogo", 5)
            CONFIG.save()

            #Atualiza o Multiplicador
            MULTIPLICADOR = MULTIPLICADORES[CONFIG.getInt("Nível de Resolução do Jogo")]

            #Atualiza a Tela
            Tela = MakeTela(MULTIPLICADOR, CONFIG.getBoolean("Tela Cheia"))

            #Retorna para o Menu de Vídeo
            Estado = MENU_DE_VIDEO

        #Troca para a Resolução de 720p e volta para o Menu de Vídeo
        elif Estado == RESOLUÇÃO_DE_720P:
            #Atualiza a regra no Config
            CONFIG.set("Nível de Resolução do Jogo", 4)
            CONFIG.save()

            #Atualiza o Multiplicador
            MULTIPLICADOR = MULTIPLICADORES[CONFIG.getInt("Nível de Resolução do Jogo")]

            #Atualiza a Tela
            Tela = MakeTela(MULTIPLICADOR, CONFIG.getBoolean("Tela Cheia"))

            #Retorna para o Menu de Vídeo
            Estado = MENU_DE_VIDEO

        #Troca para a Resolução de 576p e volta para o Menu de Vídeo
        elif Estado == RESOLUÇÃO_DE_576P:
            #Atualiza a regra no Config
            CONFIG.set("Nível de Resolução do Jogo", 3)
            CONFIG.save()

            #Atualiza o Multiplicador
            MULTIPLICADOR = MULTIPLICADORES[CONFIG.getInt("Nível de Resolução do Jogo")]

            #Atualiza a Tela
            Tela = MakeTela(MULTIPLICADOR, CONFIG.getBoolean("Tela Cheia"))

            #Retorna para o Menu de Vídeo
            Estado = MENU_DE_VIDEO

        #Troca para a Resolução de 540p e volta para o Menu de Vídeo
        elif Estado == RESOLUÇÃO_DE_540P:
            #Atualiza a regra no Config
            CONFIG.set("Nível de Resolução do Jogo", 2)
            CONFIG.save()

            #Atualiza o Multiplicador
            MULTIPLICADOR = MULTIPLICADORES[CONFIG.getInt("Nível de Resolução do Jogo")]

            #Atualiza a Tela
            Tela = MakeTela(MULTIPLICADOR, CONFIG.getBoolean("Tela Cheia"))

            #Retorna para o Menu de Vídeo
            Estado = MENU_DE_VIDEO

        #Troca para a Resolução de 360p e volta para o Menu de Vídeo
        elif Estado == RESOLUÇÃO_DE_360P:
            #Atualiza a regra no Config
            CONFIG.set("Nível de Resolução do Jogo", 1)
            CONFIG.save()

            #Atualiza o Multiplicador
            MULTIPLICADOR = MULTIPLICADORES[CONFIG.getInt("Nível de Resolução do Jogo")]

            #Atualiza a Tela
            Tela = MakeTela(MULTIPLICADOR, CONFIG.getBoolean("Tela Cheia"))

            #Retorna para o Menu de Vídeo
            Estado = MENU_DE_VIDEO

        #Entra no Menu para selecionar um Jogo Salvo
        elif Estado == MENU_PARA_CARREGAR_JOGO_SALVO:
            Estado = MenuMaker("Menu para Carregar Jogo Salvo").run(Tela, MULTIPLICADOR)

        #Entra no Menu para criar um Novo Jogo
        elif Estado == MENU_DE_NOVO_JOGO:
            Estado = MenuMaker("Menu de Novo Jogo").run(Tela, MULTIPLICADOR)

        #Vai para o Jogo
        elif Estado == JOGO:
            Estado = tela_jogo(Tela)
finally:
	#Fecha o Jogo
	pygame.quit()

	#Salvar o Arquivo de Configuração
	CONFIG.save()