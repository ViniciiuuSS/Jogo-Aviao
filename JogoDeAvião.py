import pygame
from random import randint
import pygame as pygame
from pygame import KEYDOWN, QUIT, K_r
from pynput.mouse import Button, Listener

pygame.init()

janela = pygame.display.set_mode((1200,800))
pygame.display.set_caption("Score - Avião")
BackGround = pygame.image.load(r'D:\MateriasAnotadasnoBlocodeNotas\MateriaPython\PythonPycharm\JogoDeAvião\GUI_HUB\BackGroud.jpg')
Hub_BackGround = pygame.image.load(r'D:\MateriasAnotadasnoBlocodeNotas\MateriaPython\PythonPycharm\JogoDeAvião\GUI_HUB\HUB_BackGround.png')
Morreu_tela = pygame.image.load(r"D:\MateriasAnotadasnoBlocodeNotas\MateriaPython\PythonPycharm\JogoDeAvião\GUI_HUB\Morreu.png")
Tiro = pygame.image.load(r"D:\MateriasAnotadasnoBlocodeNotas\MateriaPython\PythonPycharm\JogoDeAvião\GUI_HUB\Tiro.png")
TiroUp = pygame.image.load(r"D:\MateriasAnotadasnoBlocodeNotas\MateriaPython\PythonPycharm\JogoDeAvião\GUI_HUB\TiroUp.png")
Tiro_Upgrade = pygame.image.load(r"D:\MateriasAnotadasnoBlocodeNotas\MateriaPython\PythonPycharm\JogoDeAvião\GUI_HUB\CompraTiro.png")
Personagem = pygame.image.load(r'D:\MateriasAnotadasnoBlocodeNotas\MateriaPython\PythonPycharm\JogoDeAvião\GUI_HUB\Personagem.png')
Inimigo =  pygame.image.load(r"D:\MateriasAnotadasnoBlocodeNotas\MateriaPython\PythonPycharm\JogoDeAvião\GUI_HUB\Inimigo.png")
Inimigo1 = pygame.image.load(r"D:\MateriasAnotadasnoBlocodeNotas\MateriaPython\PythonPycharm\JogoDeAvião\GUI_HUB\Inimigo1.png")
Inimigo2 = pygame.image.load(r"D:\MateriasAnotadasnoBlocodeNotas\MateriaPython\PythonPycharm\JogoDeAvião\GUI_HUB\inimigo2.png")
#-----------------------------------------------VARIAVEIS GLOBAIS-------------------------------------------------------
Jg_x = 400
Jg_y = 400
ini_x = 1300
ini_y = 400
ini1_x = 1500
ini1_y = 550
ini2_x = 1300
ini2_y = randint(200,380)
tiro_x = Jg_x
tiro_y = Jg_y
vida = 0
total_vida = 0
pos_x = randint(300, 600)
pos_y = randint(100,200)
Money = 0
Preço_Tiro = 5
inimigos_mortos = 0
velocidade_personagem = 15
velocidade_inimigo = 15
velocidade_tiro = 10

morreu = False
#-----------------------------------------------------FONTES------------------------------------------------------------
font = pygame.font.SysFont('arial black', 30)
texto = font.render("$: ",True,(0,255,0))
pos_texto = texto.get_rect()
pos_texto.center = (1080,15)

font1 = pygame.font.SysFont('arial black', 25)
valor = font.render("$: ",True,(0,0,0))
pos_valor = valor.get_rect()
pos_valor.center = (180,658)

font2 = pygame.font.SysFont('arial black', 20)
valor_level = font.render("",True,(0,0,0))
pos_valor_level = valor_level.get_rect()
pos_valor_level.center = (120,706)

font2 = pygame.font.SysFont('arial black', 20)
valor_levelprox = font.render("",True,(0,0,0))
pos_valor_levelprox = valor_levelprox.get_rect()
pos_valor_levelprox.center = (225,706)

font = pygame.font.SysFont('arial black', 30)
vida_font = font.render("Vida: ", True,(255,0,0))
pos_vida = vida_font.get_rect()
pos_vida.center = (50,15)

font = pygame.font.SysFont('arial black', 30)
score_font = font.render("Inimigos Mortos: ", True,(255,0,0))
pos_score = score_font.get_rect()
pos_score.center = (500,10)

font3 = pygame.font.SysFont('arial black', 5)
recado_font = font.render("MANTENHA O BOTÃO DO MOUSE PRESSIONADO",True,(0,0,0))
pos_recado = recado_font.get_rect()
pos_recado.center = (700,650)

font = pygame.font.SysFont('arial black', 30)
recado1_font = font.render("PARA QUE O DISPARO CONTINUEI.",True,(0,0,0))
pos_recado1 = recado1_font.get_rect()
pos_recado1.center = (700,680)
#-------------------------------------------------FUNÇÕES---------------------------------------------------------------
def reiniciar_jogo():
    global Money, Preço_Tiro, velocidade_tiro, velocidade_personagem, velocidade_inimigo, Jg_y, Jg_x, ini_y, ini_x, ini1_y,ini1_x,morreu,ini2_x,ini2_y,vida,total_vida, inimigos_mortos
    Money = 0
    Preço_Tiro = 5
    velocidade_tiro = 10
    velocidade_personagem = 15
    velocidade_inimigo = 5
    Jg_x = 400
    Jg_y = 400
    ini_x = 1300
    ini_y = 400
    ini1_x = 1500
    ini1_y = 550
    ini2_x = 1300
    ini2_y = 400
    vida = 0
    total_vida = 0
    inimigos_mortos = 0
    morreu = False

def inimigos():
    Inimigo_Tela = janela.blit(Inimigo, (ini_x, ini_y))
def inimigos1():
    Inimigo1_Tela = janela.blit(Inimigo1, (ini1_x, ini1_y))

#-------------------------------------------------EVENTOS GLOBAIS-------------------------------------------------------
janela_Aberta = True
while janela_Aberta:
    pygame.time.delay(15)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_Aberta = False

    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_w]:
        if Jg_y < -60:
            Jg_y = 550
        Jg_y += - velocidade_personagem
    if comandos[pygame.K_s]:
        if Jg_y > 550:
            Jg_y = -60
        Jg_y += + velocidade_personagem
    if comandos[pygame.K_a] and Jg_x >= 0:
        Jg_x += - velocidade_personagem
    if comandos[pygame.K_d] and Jg_x <= 1100:
        Jg_x += + velocidade_personagem

    recado_font = font.render("MANTENHA O BOTÃO DO MOUSE PRESSIONADO", True, (0, 0, 0))
    score_font = font.render("Naves Abatidas: "+str(inimigos_mortos), True, (255, 255, 255))
    vida_font = font.render("Vida: "+str(total_vida), True, (255, 0, 0))
    texto = font.render("$: " + str(Money), True, (0, 255, 0))
    valor = font.render("$: " + str(Preço_Tiro), True, (0, 0, 0))
    valor_level = font.render("" + str(velocidade_tiro), True, (0, 0, 0))
    valor_levelprox = font.render("" + str(velocidade_tiro + 1), True, (0, 0, 0))
    mx, my = pygame.mouse.get_pos()
    print(mx,my)
# -----------------------------------------------------------------------------------------------------------------------
    ini_x -= velocidade_inimigo
    ini1_x -= velocidade_inimigo
    botao = pygame.key.get_pressed()
    if botao[pygame.K_SPACE]:
            if Money >= Preço_Tiro:
                Money -= Preço_Tiro
                velocidade_tiro += 1
                Preço_Tiro += randint(2, 3)
                if velocidade_tiro == 40:
                    velocidade_personagem += 5
            else:
                print("dinheiro insuficiente")


    if ini_x < -150:
        ini_x = randint(1300, 1500)
        ini_y = randint(70, 200)
    if ini1_x < -150:
        ini1_x = randint(1600, 1800)
        ini1_y = randint(400, 550)
    janela.blit(BackGround, (0, 0))
    janela.blit(Hub_BackGround, (50, 600))
    janela.blit(texto, pos_texto)
    janela.blit(valor, pos_valor)
    janela.blit(vida_font, pos_vida)
    janela.blit(recado_font,pos_recado)
    janela.blit(recado1_font,pos_recado1)
    janela.blit(score_font, pos_score)
    janela.blit(valor_level,pos_valor_level)
    janela.blit(valor_levelprox, pos_valor_levelprox)
    Personagem_Tela = janela.blit(Personagem, (Jg_x, Jg_y))
    inimigos()
    inimigos1()
    Tiro_Upgrade1 = janela.blit(Tiro_Upgrade, (-50,450))
    if ((Jg_x + 30 > ini_x and Jg_x - 30 < ini_x and Jg_y + 20 > ini_y and Jg_y - 20 < ini_y)):
        vida += 1
        if vida == 8:
            morreu = True
            while morreu:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        exit()
                    if event.type == KEYDOWN:
                        if event.key == K_r:
                            reiniciar_jogo()

                janela.blit(Morreu_tela, (0,0))
                pygame.display.update()

    if ((Jg_x + 30 > ini1_x and Jg_x - 30 < ini1_x and Jg_y + 20 > ini1_y and Jg_y - 20 < ini1_y)):
        vida += 1
        if vida == 8:
            morreu = True
            while morreu:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        exit()
                    if event.type == KEYDOWN:
                        if event.key == K_r:
                            reiniciar_jogo()

                janela.blit(Morreu_tela, (0, 0))
                pygame.display.update()
    mouse = pygame.mouse.get_pressed()[0]
    if mouse:
        B = janela.blit(Tiro, (tiro_x , tiro_y))
        tiro_x += velocidade_tiro

        if ((tiro_x + 20 > ini_x and tiro_y + 50 > ini_y and tiro_y - 10 < ini_y)):
            inimigos_mortos += 1
            Money += randint(1, 6)
            texto = font.render("$: " + str(Money), True, (0, 255, 0))
            ini_x = randint(1300, 1500)
            ini_y = randint(70, 380)
        if ((tiro_x + 20 > ini1_x and tiro_y + 50 > ini1_y and tiro_y - 10 < ini1_y)):
            inimigos_mortos += 1
            Money += randint(1, 6)
            texto = font.render("$: " + str(Money), True, (0, 255, 0))
            ini1_x = randint(1600, 1800)
            ini1_y = randint(400, 550)
            if inimigos_mortos == 10:
                velocidade_inimigo += 4
            if inimigos_mortos == 20:
                velocidade_inimigo += 6
            if inimigos_mortos == 30:
                velocidade_inimigo += 8
            if inimigos_mortos == 40:
                velocidade_inimigo += 12
    elif tiro_x > 1210:
        tiro_x = Jg_x
        tiro_y = Jg_y
    else:
        tiro_x = Jg_x
        tiro_y = Jg_y

    if vida < 3:
        total_vida = 3
    elif vida < 6:
        total_vida = 2
    elif vida < 2:
        total_vida = 1
    else:
        total_vida = 0
    recado_font = font.render("MANTENHA O BOTÃO DO MOUSE PRESSIONADO", True, (0, 0, 0))
    score_font = font.render("Naves Abatidas:"+str(inimigos_mortos), True, (255, 255, 255))
    vida_font = font.render("Vida: "+str(total_vida), True, (255, 0, 0))
    texto = font.render("$: " + str(Money), True, (0, 255, 0))
    valor1 = font.render("$: " + str(Preço_Tiro),True,(0,0,0))
    #-----------------------------------------------------------------------------------------------------------------------


    pygame.display.update()


pygame.quit()
