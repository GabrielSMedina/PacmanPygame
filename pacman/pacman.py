import pygame
import constantes
import corpo
import cores
import cenario

pygame.init()

tela = pygame.display.set_mode((constantes.LARGURA, constantes.ALTURA), 0)
pacman = corpo.Pacman_corpo()
mapa = cenario.Mapa(constantes.ALTURA//30, pacman)

def aceitar_movimento():

while True:

    #Calcula as regras
    pacman.calcular_regras()

    #Pinta
    tela.fill(cores.PRETO)
    mapa.pintar(tela)
    pacman.pintar(tela)
    pygame.display.update()
    pygame.time.delay(100)


    #Eventos
    eventos = pygame.event.get()
    for e in eventos:
        if e.type == pygame.QUIT:
            exit()
    pacman.processar_eventos(eventos)