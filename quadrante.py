class Quadrante:
    def __init__(self):
        self.__valores_descobertos = []
        self.__matriz = [[list(range(1, 10)) for i in range(3)] for i in range(3)]

    def __str__(self):
        saida = ""
        for lin in self.__matriz:
            for col in lin:
                if len(col) == 1:
                    saida += str(col) + " "
                else:
                    saida += "[ ] "
            saida += "\n"
        return saida

    def __getitem__(self, item):
        return self.__matriz[item]

    def set_value(self, lin, col, valor):
        self.__matriz[lin][col] = [valor]
        self.__valores_descobertos.append(valor)
        self.__valores_descobertos.sort()

    def get_possiveis_valores(self, lin, col):
        """Retorna os possiveis valores de uma célula"""
        return self.__matriz[lin][col]

    def get_linha(self, lin):
        return self.__matriz[lin]

    def descobrir_valores_quadrante(self):
        lado = range(len(self.__matriz))
        for lin in lado:
            for col in lado:
                if len(self.get_possiveis_valores(lin, col)) > 1:
                    self.__matriz[lin][col] = list(set(self.__matriz[lin][col]) - set(self.__valores_descobertos))


if __name__ == "__main__":
    quad1 = Quadrante()

    quad1.set_value(0, 0, 5)
    quad1.set_value(0, 1, 3)
    quad1.set_value(1, 0, 6)
    quad1.set_value(2, 1, 9)
    quad1.set_value(2, 2, 8)
    print(quad1._Quadrante__valores_descobertos)
    quad1.descobrir_valores_quadrante()
    print(quad1)
    print(f"Valores possiveis lin 0, col 2: {quad1.get_possiveis_valores(0, 1)}")
    print(f"Valores possiveis lin 1, col 1: {quad1.get_possiveis_valores(1, 1)}")
    print(f"Valores possiveis lin 1, col 2: {quad1.get_possiveis_valores(1, 2)}")

