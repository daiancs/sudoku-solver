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

    def inserir_valor(self, quadrante, celula, valor):
        """Insere valores iniciais no jogo."""
        lin = celula // 3
        col = celula % 3
        self.__gameboard[quadrante // 3][quadrante % 3].set_value(lin, col, valor)

    def get_valores_possiveis_jogo(self, quadrante, celula):
        """Retorna lista de valores ainda possíves para aquela célula."""
        lin = celula // 3
        col = celula % 3
        return self[quadrante // 3][quadrante % 3].get_possiveis_valores(lin, col)

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
                            qtd_valores_possiveis = len(quadrante.get_possiveis_valores(lin, col))
                            if qtd_valores_possiveis > 1:
                                valores = []
                                valores.extend(self.get_valores_lin(numero_fila, lin))
                                valores.extend(self.get_valores_col(numero_coluna, col))
                                valores = set(valores)

                                quadrante.descontar_valores_no_quadrante(lin, col, valores)
                                if not descontou:
                                    descontou = qtd_valores_possiveis > len(quadrante.get_possiveis_valores(lin, col))

            if not descontou:
                print("Encontrou o máximo de valores no momento.")
