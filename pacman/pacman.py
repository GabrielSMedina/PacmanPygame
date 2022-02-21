import pygame
import constantes
import corpo
import cores
import cenario

pygame.init()

tela = pygame.display.set_mode((constantes.LARGURA, constantes.ALTURA), 0)
pacman = corpo.Corpo(constantes.SIZE)
cenario = cenario.Cenario(constantes.ALTURA // 30, pacman)

while True:
    # Calcula as regras
    pacman.calcular_regras()
    cenario.calcular_regras()

    # Pinta
    tela.fill(cores.PRETO)
    cenario.pintar(tela)
    pacman.pintar(tela)
    pygame.display.update()
    pygame.time.delay(constantes.DELAY)

    # Eventos
    eventos = pygame.event.get()
    pacman.processar_eventos(eventos)
    cenario.processar_eventos(eventos)
