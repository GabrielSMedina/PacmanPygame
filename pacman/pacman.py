import pygame
import constantes
import corpo
import cores
import cenario

pygame.init()
size = 600//30
tela = pygame.display.set_mode((constantes.LARGURA, constantes.ALTURA), 0)
pacman = corpo.Pacman_corpo(size)
cenario = cenario.Cenario(constantes.ALTURA//30, pacman)

while True:

    #Calcula as regras
    pacman.calcular_regras()
    cenario.calcular_regras()

    #Pinta
    tela.fill(cores.PRETO)
    cenario.pintar(tela)
    pacman.pintar(tela)
    pygame.display.update()
    pygame.time.delay(100)


    #Eventos
    eventos = pygame.event.get()
    for e in eventos:
        if e.type == pygame.QUIT:
            exit()
    pacman.processar_eventos(eventos)