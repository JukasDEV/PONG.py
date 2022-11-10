import pygame

from jogo.cores import CORES

class Paleta:
    def __init__(self, posicao, acao_subir, acao_descer, height):
        self.posicao = posicao
        self.subir = acao_subir
        self.descer = acao_descer
        self.height = height

    def desenha(self, tela):
        pygame.draw.rect(
            tela,
            CORES.branco,
            # [pos_x, pos_y, larg, alt da paleta]
            self.posicao + [15, self.height]
        )

    def movimenta(self, teclas):
        if teclas[self.subir] and self.posicao[1] > 0:
            self.posicao[1] -= 5

        if teclas[self.descer] and self.posicao[1] < 400 - self.height: #tamanho tela - altura
            self.posicao[1] += 5
