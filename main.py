import pygame

from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

largura = 640
altura = 480

x_cobra = int(largura/2)
y_cobra = int(altura/2)

velocidade = 10
x_controle = velocidade
y_controle = 0

x_maca = randint(40,600)
y_maca = randint(50,430)

barulho_colisao = pygame.mixer.Sound('paradinhas/8d82b5_New_Super_Mario_Bros_Coin_Sound_Effect.mp3')
barulho_colisao.set_volume(0.2)

pygame.mixer.music.set_volume(0.2)
musica_de_fundo = pygame.mixer.music.load('paradinhas/BoxCat Games - CPU Talk.mp3')
pygame.mixer.music.play(-1)

relogio = pygame.time.Clock()

fonte = pygame.font.SysFont('arial', 40, True, True)
pontos = 0

tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('jogo da cobrinha')

comprimento_inicial = 5
lista_cobra = []
def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        # XeY = [x,y]
        # XeY[0] = x
        # XeY[1] = y  
        pygame.draw.rect(tela, (0,255,0), (XeY[0], XeY[1], 20,20))
while True:
    relogio.tick(30)
    tela.fill((255,255,255))
    mensagem = f'Pontos:{pontos}'
    texto_formatado = fonte.render(mensagem,True, (0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
            if event.key == K_d:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    x_controle = 0
                    y_controle = -velocidade
            if event.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                    x_controle = 0
                    y_controle = velocidade
        
    x_cobra += x_controle
    y_cobra += y_controle
        
    cobra = pygame.draw.rect(tela, (0,255,0), (x_cobra,y_cobra,20,20))
    maca = pygame.draw.rect(tela, (255,0,0), (x_maca,y_maca,20,20))  

    if cobra.colliderect(maca):
        x_maca = randint(40,600)
        y_maca = randint(50,430) 
        pontos += 1
        barulho_colisao.play()
        comprimento_inicial += 1
    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
    lista_cobra.append(lista_cabeca)
    aumenta_cobra(lista_cobra)

    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]
    tela.blit(texto_formatado, (450,40))

    pygame.display.update()
