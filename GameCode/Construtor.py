#Arquivo que contem as classes e funções de base para o Jogo

import pygame

#Função para adequar as Imagens do Tipo Objeto a Dimensão do Jogo (Botões)
def CriarObjeto(Imagem, Multiplicador):
	if type(Imagem) != pygame.Surface:
		raise TypeError("Imagem não é um pygame.Surface")
	elif type(Multiplicador) != float and type(Multiplicador) != int:
		raise TypeError("Multiplicador não é um Número")
	else:
		#Dimensiona a Imagem
		return pygame.transform.scale(Imagem, (int(Imagem.get_size()[0]*Multiplicador), int(Imagem.get_size()[1]*Multiplicador)))

#Classe Para criar um botão
class NewObject(pygame.sprite.Sprite):
	
	def __init__(self, Imagem, Multiplicador, Posição):
		if type(Imagem) != pygame.Surface:
			raise TypeError("Imagem não é um pygame.Surface")
		elif type(Multiplicador) != float and type(Multiplicador) != int:
			raise TypeError("Multiplicador não é um Número")
		elif type(Posição) != tuple:
			raise TypeError("Posição não é um Tuple")
		elif len(Posição) != 2:
			raise Exception("Posição presisa conter X e Y!")
		elif type(Posição[0]) != int or type(Posição[1]) != int:
			raise TypeError("Todos os elementos da Posição tem que ser Interios")
		else:
			super().__init__()

			#Cria a Imagem do Botão
			self.image = CriarObjeto(Imagem, Multiplicador)

			#Faz a Imagem Ficar Transparente
			self.image.set_colorkey((0, 0, 0))

			#Criar o rect do Botão
			self.rect = self.image.get_rect()

			#Define a posição X do Botão
			self.rect.x = int(Posição[0]*Multiplicador)

			#Define a posição Y do Botão
			self.rect.y = int(Posição[1]*Multiplicador)

#Função para criar ou alterar o Plano de Fundo do Jogo
def AtualizarPlanodeFundo(Tela, Imagem, Multiplicador, Objetos):
	if type(Tela) != pygame.Surface:
		raise TypeError("Tela não é um pygame.Surface")
	elif type(Imagem) != pygame.Surface:
		raise TypeError("Imagem não é um pygame.Surface")
	elif type(Multiplicador) != float and type(Multiplicador) != int:
		raise TypeError("Multiplicador não é um Número")
	elif Imagem.get_size()[0] != 1920 or Imagem.get_size()[1] != 1080:
		raise Exception("A Imagem de Plano de Fundo tem que ser 1920 por 1080")
	elif type(Objetos) != list:
		raise TypeError("Objetos não é uma Lista")
	else:
		#Dimensiona a Imagem de Plano de Fundo
		Imagem = pygame.transform.scale(Imagem, (int(Imagem.get_size()[0]*Multiplicador), int(Imagem.get_size()[1]*Multiplicador)))

		#Prenche a Tela de PRETO
		Tela.fill((0, 0, 0, 255))
		#Aplica o Plano de Fundo a Tela
		Tela.blit(Imagem, Imagem.get_rect())

		#Adiciona Todos os Objetos no pygame.Group
		Grupo = pygame.sprite.Group()

		for botão in Objetos:
			Grupo.add(botão)

		#Desenha os Objetos na Tela
		Grupo.draw(Tela)
		#Inverte o Display
		pygame.display.flip()

		return Tela