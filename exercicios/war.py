from random import shuffle

class Carta():
    naipes = ("Espadas", "Copas", "Ouros", "Paus")
    
    # Primeiros são None para índice == valor
    valores = (None, None, "Dois", "Três", "Quatro", "Cinco", "Seis",
            "Sete", "Oito", "Nove", "Dez", "Valete", "Dama", "Rei", "Ás")
    
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe

    def __lt__(self, c2):
        if self.valor < c2.valor:
            return True
        if self.valor == c2.valor:
            if self.naipe < c2.naipe:
                return True
            else:
                return False
        
        return False
    
    def __gt__(self, c2):
        if self.valor > c2.valor:
            return True
        if self.valor == c2.valor:
            if self.naipe > c2.naipe:
                return True
            else:
                return False

        return False

    def __repr__(self):
        r = self.valores[self.valor] + " de " + self.naipes[self.naipe]
        return r

class Baralho:
    def __init__(self):
        self.cartas = []

        for i in range(2, 15):
            for j in range(4):
                self.cartas.append(Carta(i, j))

        shuffle(self.cartas)

    def rm_carta(self):
        if len(self.cartas) == 0:
            return

        return self.cartas.pop()

class Jogador:

    def __init__(self, nome):
        self.nome = nome
        self.carta = None
        self.vitorias = 0

class Jogo:

    def __init__(self):
        nome1 = input("Nome Jogador 1: ")
        nome2 = input("Nome Jogador 2: ")
        self.j1 = Jogador(nome1)
        self.j2 = Jogador(nome2)
        self.baralho = Baralho()

    def ganhar_rodada(self, ganhador):
        print("{} ganhou essa rodada!".format(ganhador))

    def imprimir_compra(self, j1n, j1c, j2n, j2c):
        print("{} comprou {}, {} comprou {}".format(j1n, j1c, j2n, j2c))

    def ganhar(self):
        if self.j1.vitorias > self.j2.vitorias:
            return j1.nome
        if self.j1.vitorias < self.j2.vitorias:
            return j2.nome
        else:
            return "Foi um empate!"

    def jogar(self):
        cartas = self.baralho.cartas
        print("=== WAR ===")
       
        while len(cartas) >= 2:
           resposta = input("Aperte q para sair." + \
                   " Qualquer tecla para continuar\n")
           if resposta == 'q':
               break

           j1c = self.baralho.rm_carta()
           j2c = self.baralho.rm_carta()
           self.imprimir_compra(self.j1.nome, j1c, self.j2.nome, j2c)
           
           if j1c > j2c:
               self.j1.vitorias += 1
               self.ganhar_rodada(self.j1.nome)
           else:
               self.j2.vitorias += 1
               self.ganhar_rodada(self.j2.nome)         

        print("A guerra acabou. VENCEDOR: {}".format(self.ganhar()))

jogo = Jogo()
jogo.jogar()
