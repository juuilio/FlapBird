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
while janela_aberta:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_SPACE]:
        y -= 30
    else:
        y += 10

    janela.blit(fundo, (0,0))
    janela.blit(passaro, (x,y))

    pygame.display.update()

pygame.quit()