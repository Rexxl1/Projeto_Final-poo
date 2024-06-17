import pygame
import time
import random
from constantes import *
from funções import *
from buscar_palavras import *
import pandas as pd

# Instanciando as constantes e funções necessárias
constantes = Constantes()
funcoes = funções()

class JogoDigitaPalavra:
    def __init__(self):
        pygame.init()  # Inicializa o Pygame
        self.palavra_atual = Palavra()  # Utiliza a classe Palavra para gerar palavras aleatórias
        self.score = 0  # Encapsulamento: Atributo encapsulado para armazenar o score do jogador
        self.tempo_inicial = time.time()
        self.tempo_limite = constantes.get_tempo_limite()
        self.tempo_atual = self.tempo_limite
        self.ranking = {}  # Encapsulamento: Atributo encapsulado para armazenar o ranking dos jogadores
        self.jogando = False  # Encapsulamento: Atributo encapsulado para controlar o estado do jogo
        self.nome_jogador = ""  # Encapsulamento: Atributo encapsulado para armazenar o nome do jogador
        self.screen = pygame.display.set_mode((constantes.get_largura(), constantes.get_altura()))  # Encapsulamento: Atributo encapsulado para a tela do jogo
        pygame.display.set_caption('Jogo Digita Palavra')  # Abstração: Define o título da janela do jogo
        self.random_x, self.random_y = self.gerar_coordenadas_aleatorias()  # Encapsulamento: Utiliza método encapsulado para gerar coordenadas aleatórias iniciais
        self.carregar_ranking()
        
    def gerar_coordenadas_aleatorias(self):
        """Método para gerar coordenadas aleatórias na tela."""
        while True:
            x = random.randint(100, constantes.get_largura() - 100)
            y = random.randint(100, constantes.get_altura() - 100)
            if not (450 <= x <= 1050 and 250 <= y <= 450):
                return x, y

    def menu(self):
        """Método que exibe o menu principal do jogo."""
        while True:
            self.screen.fill(constantes.get_branco())
            funcoes.desenhar_texto(self.screen, "Menu Principal", 60, constantes.get_preto(), constantes.get_largura() / 2, 100)
            funcoes.desenhar_botao(self.screen, "Jogar", 40, constantes.get_preto(), constantes.get_largura() / 2, 250, self.pedir_nome_jogador)
            funcoes.desenhar_botao(self.screen, "Ranking", 40, constantes.get_preto(), constantes.get_largura() / 2, 350, self.mostrar_ranking)
            funcoes.desenhar_botao(self.screen, "Sair", 40, constantes.get_preto(), constantes.get_largura() / 2, 450, self.sair)
            funcoes.desenhar_botao(self.screen, "Zerar Ranking", 40, constantes.get_preto(), constantes.get_largura() / 2, 550, self.zerar_ranking)
            pygame.display.flip()
            self.verificar_eventos()

    def verificar_eventos(self):
        """Método para verificar eventos do jogo."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.sair()  # Encapsulamento: Chama método encapsulado para sair do jogo
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.verificar_clique_botoes()  # Polimorfismo: Chama método genérico para verificar cliques
    ## 
    def verificar_clique_botoes(self):
        """Método para verificar cliques nos botões do menu."""
        mouse_pos = pygame.mouse.get_pos()
        if 550 <= mouse_pos[0] <= 950 and 200 <= mouse_pos[1] <= 300:
            self.pedir_nome_jogador()  # Polimorfismo: Chama método específico para pedir nome do jogador
        elif 550 <= mouse_pos[0] <= 950 and 300 <= mouse_pos[1] <= 400:
            self.mostrar_ranking()  # Polimorfismo: Chama método específico para mostrar ranking
        elif 550 <= mouse_pos[0] <= 950 and 400 <= mouse_pos[1] <= 500:
            self.sair()  # Polimorfismo: Chama método específico para sair do jogo
        elif 550 <= mouse_pos[0] <= 950 and 500 <= mouse_pos[1] <= 600:
            self.zerar_ranking

    def pedir_nome_jogador(self):
        """Método para solicitar que o jogador digite seu nome."""
        nome = ""
        while True:
            self.screen.fill(constantes.get_branco())
            funcoes.desenhar_texto(self.screen, "Digite seu nome:", 30, constantes.get_preto(), constantes.get_largura() / 2, 200)
            pygame.draw.rect(self.screen, constantes.get_preto(), (450, 300, 600, 100), 2)
            funcoes.desenhar_texto(self.screen, nome, 30, constantes.get_preto(), constantes.get_largura() / 2, 350)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.sair()  # Encapsulamento: Chama método encapsulado para sair do jogo
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and nome:
                        self.nome_jogador = nome
                        self.jogar()  # Polimorfismo: Chama método específico para iniciar o jogo
                        return
                    elif event.key == pygame.K_BACKSPACE:
                        nome = nome[:-1]
                    else:
                        nome += event.unicode

    def jogar(self):
        """Método principal para jogar o jogo."""
        palavra_digitada = ''
        self.score = 0
        self.tempo_atual = self.tempo_limite
        self.tempo_inicial = time.time()
        self.palavra_atual = Palavra()
        self.jogando = True
        self.random_x, self.random_y = self.gerar_coordenadas_aleatorias()

        while self.jogando:
            tempo_decorrido = time.time() - self.tempo_inicial

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.sair()  # Encapsulamento: Chama método encapsulado para sair do jogo
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        palavra_digitada = palavra_digitada[:-1]
                    elif event.key == pygame.K_RETURN:
                        self.verificar_palavra_digitada(palavra_digitada)
                        palavra_digitada = ''
                    else:
                        palavra_digitada += event.unicode

            self.screen.fill(constantes.get_branco())
            funcoes.desenhar_texto(self.screen, self.palavra_atual.get_palavra(), 60, constantes.get_preto(), self.random_x, self.random_y)
            pygame.draw.rect(self.screen, constantes.get_preto(), (450, 300, 600, 100), 2)
            funcoes.desenhar_texto(self.screen, palavra_digitada, 30, constantes.get_preto(), 750, 350)
            funcoes.desenhar_texto(self.screen, f"Tempo: {int(self.tempo_atual - tempo_decorrido)}s", 20, constantes.get_vermelho(), constantes.get_largura() / 2, 50)

            if tempo_decorrido >= self.tempo_atual:
                self.jogando = False
                self.atualizar_ranking()  # Abstração: Chama método encapsulado para atualizar o ranking
                self.menu()  # Polimorfismo: Chama método genérico para voltar ao menu

            pygame.display.flip()

    def verificar_palavra_digitada(self, palavra_digitada):
        """Método para verificar se a palavra digitada está correta."""
        if self.palavra_atual.verificar_palavra(palavra_digitada):  # Encapsulamento: Chama método encapsulado para verificar a palavra digitada
            self.score += 1
            self.tempo_inicial = time.time()
            self.tempo_atual = max(3, self.tempo_atual - 1)
            self.random_x, self.random_y = self.gerar_coordenadas_aleatorias()
        else:
            self.jogando = False
            self.atualizar_ranking()  # Abstração: Chama método encapsulado para atualizar o ranking
            self.menu()  # Polimorfismo: Chama método genérico para voltar ao menu
        
        self.palavra_atual = Palavra()  # Encapsulamento: Cria uma nova instância da classe Palavra

    def atualizar_ranking(self):
        """Método para atualizar o ranking com o nome e score do jogador."""
        self.ranking[self.nome_jogador] = self.score  # Encapsulamento: Atualiza o ranking com o nome e score do jogador
        self.salvar_ranking()
    
    def salvar_ranking(self):
        try:
            sorted_ranking = sorted(self.ranking.items(), key=lambda item: item[1], reverse=True)
            if not sorted_ranking:
                raise ValueError("Ranking vazio")
            
            # Criando DataFrame com o ranking ordenado
            df_ranking = pd.DataFrame(sorted_ranking, columns=["Nome", "Pontuação"])

            # Salvando o DataFrame em uma planilha Excel
            df_ranking.to_excel('ranking.xlsx', index=False, engine='openpyxl')
            print("Ranking salvo com sucesso em ranking.xlsx!")

        except ValueError as e:
            print(f"Erro ao salvar ranking: {e}")

    def carregar_ranking(self):
        try:
            df_ranking = pd.read_excel('ranking.xlsx', engine='openpyxl')
            if df_ranking.empty:
                raise ValueError("Ranking vazio")
            
            self.ranking = dict(zip(df_ranking['Nome'], df_ranking['Pontuação']))
            
            print("Ranking carregado com sucesso:")
            print(df_ranking)

        except FileNotFoundError:
            print("Arquivo ranking.xlsx não encontrado.")
        except ValueError as e:
            print(f"Erro ao carregar ranking: {e}")
 
    
    def mostrar_ranking(self):
        """Método para exibir o ranking na tela com tratamento de erro."""
        exibindo_ranking = True

        while exibindo_ranking:
            self.screen.fill(constantes.get_branco())
            funcoes.desenhar_texto(self.screen, "Ranking", 60, constantes.get_preto(), constantes.get_largura() / 2, 50)

            try:
                sorted_ranking = sorted(self.ranking.items(), key=lambda item: item[1], reverse=True)
                if not sorted_ranking:
                    raise ValueError("Ranking vazio")
                
                for posicao, (nome, score) in enumerate(sorted_ranking):
                    funcoes.desenhar_texto(self.screen, f"{posicao + 1}. {nome}: {score}", 40, constantes.get_preto(), constantes.get_largura() / 2, 150 + posicao * 50)

            except ValueError as e:
                funcoes.desenhar_texto(self.screen, "Ranking vazio", 40, constantes.get_preto(), constantes.get_largura() / 2, 150)
                print(f"Erro ao exibir ranking: {e}")

            # Desenha o botão "Voltar"
            pygame.draw.rect(self.screen, constantes.get_preto(), (550, 600, 400, 50))
            funcoes.desenhar_texto(self.screen, "Voltar", 40, constantes.get_branco(), 750, 610)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.sair()  # Encapsulamento: Chama método encapsulado para sair do jogo
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        exibindo_ranking = False
                        self.menu()  # Polimorfismo: Retorna ao menu principal
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if 550 <= event.pos[0] <= 950 and 600 <= event.pos[1] <= 650:
                        exibindo_ranking = False
                        self.menu()  # Polimorfismo: Retorna ao menu principal
    #atribuir valor vazio ao ranking para zerar ele
    #tem que colocar um botão para zeralo e verificar posicao do clique
    def zerar_ranking(self):
        self.ranking = {}
        self.salvar_ranking = {}
    
    def sair(self):
        """Método para sair do jogo."""
        pygame.quit()
        quit()

if __name__ == "__main__":
    jogo = JogoDigitaPalavra()
    jogo.menu()
