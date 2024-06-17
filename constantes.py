class Constantes:
    def __init__(self):
        self._LARGURA = 1500
        self._ALTURA = 800
        self._TEMPO_LIMITE = 30
        self._BRANCO = (255, 255, 255)
        self._PRETO = (0, 0, 0)
        self._VERMELHO = (255, 0, 0)
        self._CINZA = (128, 128, 128)  # Adicionando a cor cinza

    # Getters
    def get_largura(self):
        return self._LARGURA

    def get_altura(self):
        return self._ALTURA

    def get_tempo_limite(self):
        return self._TEMPO_LIMITE

    def get_branco(self):
        return self._BRANCO

    def get_preto(self):
        return self._PRETO

    def get_vermelho(self):
        return self._VERMELHO

    def get_cinza(self):
        return self._CINZA  # Método getter para obter a cor cinza

    # Setters (caso necessário, mas não foram alterados neste exemplo)
    # Métodos setters omitidos para manter o foco na adição da cor cinza
