from banco_de_palavras import BancoDePalavras

class Palavra:
    def __init__(self):
        # Utilização de encapsulamento para o atributo protegido _palavra
        banco_palavras = BancoDePalavras()
        self._palavra = banco_palavras.get_palavra_aleatoria()

    def get_palavra(self):
        # Método getter para acessar o atributo protegido _palavra
        return self._palavra

    def verificar_palavra(self, palavra_digitada):
        # Método que utiliza o conceito de encapsulamento para verificar a palavra
        return palavra_digitada == self._palavra
