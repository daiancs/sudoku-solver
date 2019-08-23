"""Classe que armazena toda matriz do jogo. Ou seja, a matriz 3x3 de Quadrantes de valor"""
from quadrante import Quadrante


class GameBoard:
    def __init__(self):
        self.__gameboard = [[Quadrante() for i in range(3)] for i in range(3)]

    def __str__(self):
        saida = ""
        lado = range(3)
        for fila in lado:  # Primeira fileira de quadrante, segunda fileira, terceira fileira
            for lin in lado:  # Primeira linha da primeira fila, segunda linha da primeira fila, etc.
                for quad in lado:
                    for celula in self.__gameboard[fila][quad][lin]:
                        if len(celula) == 1:
                            saida += str(celula) + " "
                        else:
                            saida += "[ ] "
                    saida += "  "
                saida += "\n"
            saida += "\n"
        return saida

    def __getitem__(self, item):
        return self.__gameboard[item]

    def inserir_valor(self, quad, lin, col, valor):
        """Insere valores iniciais no jogo."""
        self.__gameboard[quad // 3][quad % 3].set_value(lin, col, valor)

    def get_valores_lin(self, fila, lin):
        """Retorna os valores já descobertos de uma determinada linha.
        fila se refere a fileira de quadrante correspondente"""
        valores = []
        for pos_quad in self.__gameboard[fila]:
            for celula in pos_quad[lin]:
                if len(celula) == 1:
                    valores.append(celula[0])
        return valores

    def get_valores_col(self, posicao_quad, col):
        """Retorna os valores já descobertos de uma determinada coluna.
        posicao_quad se refere a coluna do quadrante correspondente (posição dele na fileira)"""
        valores = []
        lado = range(3)
        for fila in lado:
            for linha in lado:
                celula = self.__gameboard[fila][posicao_quad].get_possiveis_valores(linha, col)
                if len(celula) == 1:
                    valores.append(celula[0])
        return valores

    def descobrir_valores(self):
        descontou = True
        lado = range(3)

        while descontou:
            descontou = False

            # Descobre valores já utilizados no próprio quadrante
            for numero_fila, fileira in enumerate(self.__gameboard):
                for numero_coluna, quadrante in enumerate(fileira):
                    for lin in lado:
                        for col in lado:
                            if len(quadrante.get_possiveis_valores(lin, col)) > 1:
                                valores = []
                                valores.extend(self.get_valores_lin(numero_fila, lin))
                                valores.extend(self.get_valores_col(numero_coluna, col))
                                valores = set(valores)

                                descontou = quadrante.descontar_valores_no_quadrante(lin, col, valores)

            if not descontou:
                print("Encontrou o máximo de valores possível no momento.")


if __name__ == "__main__":
    jogo = GameBoard()

    jogo.inserir_valor(0, 0, 0, 5)  # 0 == 0, 0
    jogo.inserir_valor(0, 0, 1, 3)
    jogo.inserir_valor(0, 1, 0, 6)
    jogo.inserir_valor(0, 2, 1, 9)
    jogo.inserir_valor(0, 2, 2, 8)

    jogo.inserir_valor(1, 0, 1, 7)  # 1 == 0, 1
    jogo.inserir_valor(1, 1, 0, 1)
    jogo.inserir_valor(1, 1, 1, 9)
    jogo.inserir_valor(1, 1, 2, 5)

    jogo.inserir_valor(2, 2, 1, 6)  # 2 == 0, 2

    jogo.inserir_valor(3, 0, 0, 8)  # 3 == 1, 0
    jogo.inserir_valor(3, 1, 0, 4)
    jogo.inserir_valor(3, 2, 0, 7)

    jogo.inserir_valor(4, 0, 1, 6)  # 4 == 1, 1
    jogo.inserir_valor(4, 1, 0, 8)
    jogo.inserir_valor(4, 1, 2, 3)
    jogo.inserir_valor(4, 2, 1, 2)

    jogo.inserir_valor(5, 0, 2, 3)
    jogo.inserir_valor(5, 1, 2, 1)
    jogo.inserir_valor(5, 2, 2, 6)

    jogo.inserir_valor(6, 0, 1, 6)

    jogo.inserir_valor(7, 1, 0, 4)
    jogo.inserir_valor(7, 1, 1, 1)
    jogo.inserir_valor(7, 1, 2, 9)
    jogo.inserir_valor(7, 2, 1, 8)

    jogo.inserir_valor(8, 0, 0, 2)
    jogo.inserir_valor(8, 0, 1, 8)
    jogo.inserir_valor(8, 1, 2, 5)
    jogo.inserir_valor(8, 2, 1, 7)
    jogo.inserir_valor(8, 2, 2, 9)

    print(jogo)
    jogo.descobrir_valores()
    print(jogo)
