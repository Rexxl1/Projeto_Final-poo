import random

class BancoDePalavras:
    def __init__(self):
        # deixando a lista de palavras como protegida (convenção)
        self._palavras = [
            "amor", "amigo", "arvore", "abelha", "anel", "ave", "arte", "astronauta", "aviao", "agua",
            "bola", "bala", "bicho", "banco", "barco", "brasil", "batata", "banho", "bebida", "borboleta",
            "cachorro", "casa", "carro", "cavalo", "caneta", "camisa", "cama", "cidade", "cabelo", "circo",
            "dado", "dente", "dinheiro", "doce", "doutor", "dinossauro", "dança", "dedo", "diamante", "doente",
            "elefante", "escola", "esporte", "espada", "estrela", "escada", "escudo", "esqueleto", "ervilha", "espelho",
            "fogo", "fada", "foca", "futebol", "faca", "floresta", "festa", "flauta", "ferramenta", "filtro",
            "gato", "galinha", "galo", "golfinho", "girafa", "garrafa", "geleia", "gelo", "grama", "guitarra",
            "helicoptero", "hipopotamo", "hotel", "harpa", "horta", "hiena", "horizonte", "hormônio", "higiene", "hortelã",
            "igreja", "ilha", "indio", "inseto", "impressora", "internet", "iguana", "indústria", "ídolo", "ilha",
            "jardim", "jacaré", "janela", "jornal", "jarra", "joaninha", "jogo", "joia", "jabuticaba", "jaqueta",
            "ketchup", "kiwi", "karaokê", "kilo", "koala", "karatê", "kart", "kayak", "kiwi", "kryptonita",
            "leão", "lago", "livro", "lua", "lobo", "limão", "lápis", "lanterna", "lã", "lobo",
            "macaco", "mala", "mãe", "maçã", "mapa", "mar", "mão", "mesa", "muro", "martelo",
            "navio", "nuvem", "nariz", "nota", "noite", "navalha", "ninho", "natureza", "nadar", "natal",
            "olho", "osso", "ouro", "ovo", "ovelha", "oceano", "orquestra", "orvalho", "ovo", "ouro",
            "pato", "pote", "porta", "parque", "piano", "pincel", "palavra", "papel", "polvo", "pizza",
            "queijo", "quadro", "quarto", "quebra-cabeça", "quantidade", "quintal", "quimono", "quiche", "quadro", "química",
            "rato", "rosa", "rei", "rio", "roda", "raposa", "relógio", "régua", "ração", "roupa",
            "sapo", "sol", "sapato", "sorvete", "sal", "sino", "sombra", "sorriso", "sacola", "sabão",
            "tigre", "tatu", "teto", "trem", "tesoura", "teclado", "telefone", "tapete", "tubo", "tomate",
            "urso", "uva", "unha", "urna", "universo", "uniforme", "urubu", "urso", "urna", "unidade",
            "vaca", "vaso", "vassoura", "violão", "ventilador", "vidro", "viagem", "vulcão", "vulcão", "verbo",
            "waffle", "walkman", "wasabi", "webcam", "wifi", "whisky", "windsurf", "waffle", "walkie-talkie", "whale",
            "xarope", "xadrez", "xícara", "xale", "xerox", "xilofone", "xampu", "xarope", "xangô", "xenônio",
            "yakisoba", "yoga", "yakult", "yeti", "yoga", "yogurte", "yak", "yamaha", "yoga", "youtube",
            "zebra", "zoológico", "zangão", "zagueiro", "zebra", "zíper", "zodíaco", "zoeira", "zoologia", "zenite"
        ]

    def get_palavra_aleatoria(self):
        # Escolhe aleatoriamente uma palavra da lista protegida
        return random.choice(self._palavras)
