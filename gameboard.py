"""Classe que armazena toda matriz do jogo. Ou seja, a matriz 3x3 de Quadrantes de valor"""
from quadrante import Quadrante


class GameBoard:
    def __init__(self):
        self.__gameboard = [[Quadrante() for i in range(3)] for i in range(3)]
        # self.__gameboard[]

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

    def inserir_valor(self, quad, lin, col, valor):
        self.__gameboard[quad // 3][quad % 3].set_value(lin, col, valor)


if __name__ == "__main__":
    jogo = GameBoard()

    jogo.inserir_valor(0, 0, 0, 5)
    jogo.inserir_valor(0, 0, 1, 3)
    jogo.inserir_valor(0, 1, 0, 6)
    jogo.inserir_valor(0, 2, 1, 9)
    jogo.inserir_valor(0, 2, 2, 8)

    jogo.inserir_valor(1, 0, 1, 7)
    jogo.inserir_valor(1, 1, 0, 1)
    jogo.inserir_valor(1, 1, 1, 9)
    jogo.inserir_valor(1, 1, 2, 5)

    jogo.inserir_valor(2, 2, 1, 6)

    jogo.inserir_valor(3, 0, 0, 8)
    jogo.inserir_valor(3, 1, 0, 4)
    jogo.inserir_valor(3, 2, 0, 7)

    jogo.inserir_valor(4, 0, 1, 6)
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
