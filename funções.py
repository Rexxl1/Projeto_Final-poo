# funções.py
import pygame
from constantes import Constantes

class funções:
    def __init__(self):
        self.constantes = Constantes()

    def desenhar_texto(self, screen, texto, fonte, cor, x, y):
        """Desenha texto na tela."""
        fonte_obj = pygame.font.Font(None, fonte)
        texto_renderizado = fonte_obj.render(texto, True, cor)
        rect = texto_renderizado.get_rect(center=(x, y))
        screen.blit(texto_renderizado, rect)

    def desenhar_botao(self, screen, texto, fonte, cor, x, y, acao=None):
        """Desenha botão na tela."""
        botao_rect = pygame.Rect(x - 100, y - 25, 200, 50)
        pygame.draw.rect(screen, self.constantes.get_cinza(), botao_rect)
        self.desenhar_texto(screen, texto, fonte, cor, x, y)
        if acao:
            self.verificar_clique(botao_rect, acao)

    def verificar_clique(self, rect, acao):
        """Verifica clique no botão."""
        mouse_pos = pygame.mouse.get_pos()
        if rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                acao()

    # Getters e Setters
    def get_constantes(self):
        return self.constantes

    def set_constantes(self, constantes):
        self.constantes = constantes
