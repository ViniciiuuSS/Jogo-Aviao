import pygame
from random import randint
import os

def resource_path(relative_path):
    """ Pega o caminho correto, para .py e .exe """
    try:
        base_path = sys._MEIPASS  # Quando estiver rodando como .exe
    except Exception:
        base_path = os.path.abspath(".")  # Quando estiver rodando como .py
    return os.path.join(base_path, relative_path)


# Inicializar o Pygame
pygame.init()

# Obter a resolução do monitor do usuário
info = pygame.display.Info()
SCREEN_WIDTH = info.current_w
SCREEN_HEIGHT = info.current_h

# Definir a janela em tela cheia
janela = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Score - Avião")

# Resolução base original do jogo
ORIGINAL_WIDTH = 1200
ORIGINAL_HEIGHT = 800

# Calcular proporções de escala
scale_x = SCREEN_WIDTH / ORIGINAL_WIDTH
scale_y = SCREEN_HEIGHT / ORIGINAL_HEIGHT

# Caminhos das imagens
diretorio_atual = os.path.dirname(__file__)
caminho_background = os.path.join(diretorio_atual, 'Imagens', 'BackGroud.jpg')
caminho_background = resource_path(os.path.join('Imagens', 'BackGroud.jpg'))
caminho_hub_background = resource_path(os.path.join('Imagens', 'HUB_BackGround.png'))
caminho_morreu_tela = resource_path(os.path.join('Imagens', 'Morreu.png'))
caminho_tiro = resource_path(os.path.join('Imagens', 'Tiro.png'))
caminho_tiro_up = resource_path(os.path.join('Imagens', 'TiroUp.png'))
caminho_tiro_upgrade = resource_path(os.path.join('Imagens', 'CompraTiro.png'))
caminho_personagem = resource_path(os.path.join('Imagens', 'Personagem.png'))
caminho_inimigo = resource_path(os.path.join('Imagens', 'Inimigo.png'))
caminho_inimigo1 = resource_path(os.path.join('Imagens', 'Inimigo1.png'))
caminho_inimigo2 = resource_path(os.path.join('Imagens', 'inimigo2.png'))

# Carregar e escalar as imagens
BackGround = pygame.image.load(caminho_background)
BackGround = pygame.transform.scale(BackGround, (SCREEN_WIDTH, SCREEN_HEIGHT))  # Cobrir toda a tela

Hub_BackGround = pygame.image.load(caminho_hub_background)
Hub_BackGround = pygame.transform.scale(Hub_BackGround, (int(Hub_BackGround.get_width() * scale_x), int(Hub_BackGround.get_height() * scale_y)))

Morreu_tela = pygame.image.load(caminho_morreu_tela)
Morreu_tela = pygame.transform.scale(Morreu_tela, (SCREEN_WIDTH, SCREEN_HEIGHT))

Tiro = pygame.image.load(caminho_tiro)
Tiro = pygame.transform.scale(Tiro, (int(Tiro.get_width() * scale_x), int(Tiro.get_height() * scale_y)))

TiroUp = pygame.image.load(caminho_tiro_up)
TiroUp = pygame.transform.scale(TiroUp, (int(TiroUp.get_width() * scale_x), int(TiroUp.get_height() * scale_y)))

Tiro_Upgrade = pygame.image.load(caminho_tiro_upgrade)
Tiro_Upgrade = pygame.transform.scale(Tiro_Upgrade, (int(Tiro_Upgrade.get_width() * scale_x), int(Tiro_Upgrade.get_height() * scale_y)))

Personagem = pygame.image.load(caminho_personagem)
Personagem = pygame.transform.scale(Personagem, (int(Personagem.get_width() * scale_x), int(Personagem.get_height() * scale_y)))

Inimigo = pygame.image.load(caminho_inimigo)
Inimigo = pygame.transform.scale(Inimigo, (int(Inimigo.get_width() * scale_x), int(Inimigo.get_height() * scale_y)))

Inimigo1 = pygame.image.load(caminho_inimigo1)
Inimigo1 = pygame.transform.scale(Inimigo1, (int(Inimigo1.get_width() * scale_x), int(Inimigo1.get_height() * scale_y)))

Inimigo2 = pygame.image.load(caminho_inimigo2)
Inimigo2 = pygame.transform.scale(Inimigo2, (int(Inimigo2.get_width() * scale_x), int(Inimigo2.get_height() * scale_y)))

# Variáveis globais ajustadas
Jg_x = int(400 * scale_x)
Jg_y = int(400 * scale_y)
ini_x = int(1300 * scale_x)
ini_y = int(400 * scale_y)
ini1_x = int(1500 * scale_x)
ini1_y = int(550 * scale_y)
ini2_x = int(1300 * scale_x)
ini2_y = randint(int(200 * scale_y), int(380 * scale_y))
vida = 0
total_vida = 0
Money = 0
Preço_Tiro = 5
inimigos_mortos = 0
velocidade_personagem = int(15 * scale_x)
velocidade_inimigo = int(15 * scale_x)
velocidade_tiro = int(10 * scale_x)
morreu = False

# Lista para armazenar os tiros (x, y)
tiros = []

# Fontes ajustadas
font_size = int(30 * scale_y)
font = pygame.font.SysFont('arial black', font_size)

font1_size = int(25 * scale_y)
font1 = pygame.font.SysFont('arial black', font1_size)

font2_size = int(20 * scale_y)
font2 = pygame.font.SysFont('arial black', font2_size)

# Posições dos textos ajustadas
pos_texto = pygame.Rect(0, 0, 0, 0)
pos_texto.center = (int(1080 * scale_x), int(15 * scale_y))

pos_valor = pygame.Rect(0, 0, 0, 0)
pos_valor.center = (int(180 * scale_x), int(658 * scale_y))

pos_valor_level = pygame.Rect(0, 0, 0, 0)
pos_valor_level.center = (int(120 * scale_x), int(706 * scale_y))

pos_valor_levelprox = pygame.Rect(0, 0, 0, 0)
pos_valor_levelprox.center = (int(225 * scale_x), int(706 * scale_y))

pos_vida = pygame.Rect(0, 0, 0, 0)
pos_vida.center = (int(50 * scale_x), int(15 * scale_y))

pos_score = pygame.Rect(0, 0, 0, 0)
pos_score.center = (int(500 * scale_x), int(10 * scale_y))

pos_recado = pygame.Rect(0, 0, 0, 0)
pos_recado.center = (int(700 * scale_x), int(650 * scale_y))

pos_recado1 = pygame.Rect(0, 0, 0, 0)
pos_recado1.center = (int(700 * scale_x), int(680 * scale_y))

# Funções
def reiniciar_jogo():
    global Money, Preço_Tiro, velocidade_tiro, velocidade_personagem, velocidade_inimigo, Jg_y, Jg_x, ini_y, ini_x, ini1_y, ini1_x, morreu, ini2_x, ini2_y, vida, total_vida, inimigos_mortos, tiros
    Money = 0
    Preço_Tiro = 5
    velocidade_tiro = int(10 * scale_x)
    velocidade_personagem = int(15 * scale_x)
    velocidade_inimigo = int(5 * scale_x)
    Jg_x = int(400 * scale_x)
    Jg_y = int(400 * scale_y)
    ini_x = int(1300 * scale_x)
    ini_y = int(400 * scale_y)
    ini1_x = int(1500 * scale_x)
    ini1_y = int(550 * scale_y)
    ini2_x = int(1300 * scale_x)
    ini2_y = int(400 * scale_y)
    vida = 0
    total_vida = 0
    inimigos_mortos = 0
    tiros = []
    morreu = False

def inimigos():
    janela.blit(Inimigo, (ini_x, ini_y))

def inimigos1():
    janela.blit(Inimigo1, (ini1_x, ini1_y))

# Loop principal
janela_Aberta = True
while janela_Aberta:
    pygame.time.delay(15)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_Aberta = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Botão esquerdo do mouse
            tiros.append([Jg_x, Jg_y])  # Adiciona um novo tiro na posição do personagem

    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_w]:
        if Jg_y < int(-60 * scale_y):
            Jg_y = int(550 * scale_y)
        Jg_y -= velocidade_personagem
    if comandos[pygame.K_s]:
        if Jg_y > int(550 * scale_y):
            Jg_y = int(-60 * scale_y)
        Jg_y += velocidade_personagem
    if comandos[pygame.K_a] and Jg_x >= 0:
        Jg_x -= velocidade_personagem
    if comandos[pygame.K_d] and Jg_x <= int(1100 * scale_x):
        Jg_x += velocidade_personagem

    # Movimentar inimigos
    ini_x -= velocidade_inimigo
    ini1_x -= velocidade_inimigo

    if ini_x < int(-150 * scale_x):
        ini_x = randint(int(1300 * scale_x), int(1500 * scale_x))
        ini_y = randint(int(70 * scale_y), int(200 * scale_y))
    if ini1_x < int(-150 * scale_x):
        ini1_x = randint(int(1600 * scale_x), int(1800 * scale_x))
        ini1_y = randint(int(400 * scale_y), int(550 * scale_y))

    # Movimentar tiros
    for tiro in tiros[:]:
        tiro[0] += velocidade_tiro
        if tiro[0] > SCREEN_WIDTH:
            tiros.remove(tiro)

    # Atualizar HUD
    score_font = font.render("Naves Abatidas: " + str(inimigos_mortos), True, (255, 255, 255))
    vida_font = font.render("Vida: " + str(total_vida), True, (255, 0, 0))
    texto = font.render("$: " + str(Money), True, (0, 255, 0))
    valor = font1.render("$: " + str(Preço_Tiro), True, (0, 0, 0))
    valor_level = font2.render(str(velocidade_tiro), True, (0, 0, 0))
    valor_levelprox = font2.render(str(velocidade_tiro + 1), True, (0, 0, 0))
    recado_font = font.render("CLIQUE PARA DISPARAR", True, (0, 0, 0))

    # Compra de upgrade
    if comandos[pygame.K_SPACE]:
        if Money >= Preço_Tiro:
            Money -= Preço_Tiro
            velocidade_tiro += int(1 * scale_x)
            Preço_Tiro += randint(2, 3)
            if velocidade_tiro >= int(40 * scale_x):
                velocidade_personagem += int(5 * scale_x)
        else:
            print("dinheiro insuficiente")

    # Desenhar na tela
    janela.blit(BackGround, (0, 0))
    janela.blit(Hub_BackGround, (int(50 * scale_x), int(600 * scale_y)))
    janela.blit(texto, pos_texto)
    janela.blit(valor, pos_valor)
    janela.blit(vida_font, pos_vida)
    janela.blit(recado_font, pos_recado)
    janela.blit(score_font, pos_score)
    janela.blit(valor_level, pos_valor_level)
    janela.blit(valor_levelprox, pos_valor_levelprox)
    Personagem_Tela = janela.blit(Personagem, (Jg_x, Jg_y))
    inimigos()
    inimigos1()
    janela.blit(Tiro_Upgrade, (int(-50 * scale_x), int(450 * scale_y)))

    # Desenhar os tiros
    for tiro in tiros:
        janela.blit(Tiro, (tiro[0], tiro[1]))

    # Verificar colisões com inimigos
    offset_x = int(30 * scale_x)
    offset_y = int(20 * scale_y)
    tiro_offset_x = int(20 * scale_x)
    tiro_offset_y1 = int(50 * scale_y)
    tiro_offset_y2 = int(10 * scale_y)

    for tiro in tiros[:]:
        if (tiro[0] + tiro_offset_x > ini_x and tiro[1] + tiro_offset_y1 > ini_y and tiro[1] - tiro_offset_y2 < ini_y):
            inimigos_mortos += 1
            Money += randint(1, 6)
            ini_x = randint(int(1300 * scale_x), int(1500 * scale_x))
            ini_y = randint(int(70 * scale_y), int(380 * scale_y))
            tiros.remove(tiro)
        elif (tiro[0] + tiro_offset_x > ini1_x and tiro[1] + tiro_offset_y1 > ini1_y and tiro[1] - tiro_offset_y2 < ini1_y):
            inimigos_mortos += 1
            Money += randint(1, 6)
            ini1_x = randint(int(1600 * scale_x), int(1800 * scale_x))
            ini1_y = randint(int(400 * scale_y), int(550 * scale_y))
            tiros.remove(tiro)
            if inimigos_mortos in [10, 20, 30, 40]:
                velocidade_inimigo += int(4 * scale_x) + (inimigos_mortos // 10) * int(2 * scale_x)

    # Verificar colisão do personagem com inimigos
    if (Jg_x + offset_x > ini_x and Jg_x - offset_x < ini_x and Jg_y + offset_y > ini_y and Jg_y - offset_y < ini_y) or \
       (Jg_x + offset_x > ini1_x and Jg_x - offset_x < ini1_x and Jg_y + offset_y > ini1_y and Jg_y - offset_y < ini1_y):
        vida += 1
        if vida >= 8:
            morreu = True
            while morreu:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                        reiniciar_jogo()
                janela.blit(Morreu_tela, (0, 0))
                pygame.display.update()

    # Atualizar vida
    if vida < 3:
        total_vida = 3
    elif vida < 6:
        total_vida = 2
    elif vida < 8:
        total_vida = 1
    else:
        total_vida = 0

    pygame.display.update()

pygame.quit()