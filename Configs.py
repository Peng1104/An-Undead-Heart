from os import path
from FileController import YamlFile
import Default

main_dir = path.join(path.dirname(__file__), "Configuracoes")

img_dir = path.join(main_dir, 'Imagens')
snd_dir = path.join(main_dir, 'snd')
fnt_dir = path.join(main_dir, 'font')
opt_dir = path.join(main_dir, 'Opcoes')

NOME_DO_JOGO = "PlaceHolder"

config = YamlFile(opt_dir + "/Config.yml")

FPS = config.getFloat("FPS", default_value=Default.FPS)
ALTURA = config.getInt("Altura", default_value=Default.Altura)
LARGURA = config.getInt("Largura", default_value=Default.Largura)

config.save()

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AMARELO = (255, 255, 0)

INIT = 0
NEW_GAME = 1
LOAD_GAME = 2
OPTIONS = 3
QUIT = 4
