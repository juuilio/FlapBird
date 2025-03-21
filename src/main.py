#A FAZER:
#   alterar a velocidade dos canos
#   alterar a altura dos canos
#   acrecentar pontuação
#   adicionar som
#   adicionar tela de game over
#   adicionar tela de inicio
#   hit box
from random import randint
import pygame
pygame.init()
x = 50
y = 320
velocidade = 10
fundo = pygame.image.load("src/assets/images/background.png")
fundo = pygame.transform.scale(fundo, (360,640))
passaro = pygame.image.load("src/assets/images/bird.png")
passaro = pygame.transform.scale(passaro, (50,50))
janela = pygame.display.set_mode((360,640))
pygame.display.set_caption("Flappy Bird")

janela_aberta = True
canoInferior = pygame.image.load("src/assets/images/canoInferior.png")
canoInferior = pygame.transform.scale(canoInferior, (80, 500))
canoInferior_x = 360
canoInferior_y = 300


canoSuperior = pygame.image.load("src/assets/images/canoSuperior.png")
canoSuperior = pygame.transform.scale(canoSuperior, (80, 500))
canoSuperior_x = 360
canoSuperior_y = -300

while janela_aberta:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()

    if comandos[pygame.K_SPACE] and y > 0:
        y -= 30
    elif y < 590:
        y += 10

    canoInferior_x -= 10
    canoSuperior_x -= 10

    if canoInferior_x < -80:
        canoInferior_x = 360
    if canoSuperior_x < -80:
        canoSuperior_x = 360

    janela.blit(fundo, (0,0))
    janela.blit(passaro, (x,y))
    janela.blit(canoInferior, (canoInferior_x, canoInferior_y))
    janela.blit(canoSuperior, (canoInferior_x, canoSuperior_y))

    pygame.display.update()

pygame.quit()