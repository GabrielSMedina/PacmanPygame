import pygame
import constantes
import cores
import elementos

pygame.init()


class Corpo(elementos.Elementos):
    def __init__(self, size):
        self.coluna = 1
        self.linha = 1
        self.centro_x = constantes.LARGURA / 2
        self.centro_y = constantes.ALTURA / 2
        self.tamanho = size
        self.raio = self.tamanho // 2
        self.vel_x = constantes.VELOCIDADE
        self.vel_y = constantes.VELOCIDADE
        self.coluna_intencao = self.coluna
        self.linha_intencao = self.linha

    def calcular_regras(self):
        self.coluna_intencao = self.coluna + self.vel_x
        self.linha_intencao = self.linha + self.vel_y
        self.centro_x = int(self.coluna * self.tamanho + self.raio)
        self.centro_y = int(self.linha * self.tamanho + self.raio)

    def pintar(self, tela):
        # Desenhar Pacman
        pygame.draw.circle(tela, cores.AMARELO, (self.centro_x, self.centro_y), self.raio, 0)

        # Desenha Boca
        canto_boca = (self.centro_x, self.centro_y)
        labio_superior = (self.centro_x + self.raio, self.centro_y - self.raio)
        labio_inferior = (self.centro_x + self.raio, self.centro_y)
        pontos = [canto_boca, labio_superior, labio_inferior]
        pygame.draw.polygon(tela, cores.PRETO, pontos, 0)

        # Desenha Olho
        olho_x = int(self.centro_x + self.raio / 3)
        olho_y = int(self.centro_y - self.raio * 0.70)
        olho_raio = int(self.raio / 10)
        pygame.draw.circle(tela, cores.PRETO, (olho_x, olho_y), olho_raio, 0)

    def processar_eventos(self, eventos):
        for e in eventos:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RIGHT:
                    self.vel_x = constantes.VELOCIDADE_PACMAN
                elif e.key == pygame.K_LEFT:
                    self.vel_x = -constantes.VELOCIDADE_PACMAN
                elif e.key == pygame.K_UP:
                    self.vel_y = -constantes.VELOCIDADE_PACMAN
                elif e.key == pygame.K_DOWN:
                    self.vel_y = +constantes.VELOCIDADE_PACMAN
            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_RIGHT:
                    self.vel_x = 0
                if e.key == pygame.K_LEFT:
                    self.vel_x = 0
                if e.key == pygame.K_UP:
                    self.vel_y = 0
                if e.key == pygame.K_DOWN:
                    self.vel_y = 0

    def aceitar_movimento(self):
        self.linha = self.linha_intencao
        self.coluna = self.coluna_intencao
