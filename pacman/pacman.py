import pygame
import corpo
import cenario
import constantes
import fantasma
import cores

pygame.init()

tela = pygame.display.set_mode((constantes.LARGURA, constantes.ALTURA), 0)
pacman = corpo.Corpo(constantes.SIZE)
fantasma_1 = fantasma.Fantasma(cores.VERMELHO, constantes.SIZE)
cenario = cenario.Cenario(constantes.SIZE, pacman, fantasma_1)


while True:
    # Calcula as regras
    pacman.calcular_regras()
    fantasma_1.calcular_regras()
    cenario.calcular_regras()

    # Pinta
    tela.fill(cores.PRETO)
    cenario.pintar(tela)
    pacman.pintar(tela)
    fantasma_1.pintar(tela)
    pygame.display.update()
    pygame.time.delay(constantes.DELAY)

    # Eventos
    eventos = pygame.event.get()
    pacman.processar_eventos(eventos)
    cenario.processar_eventos(eventos)
