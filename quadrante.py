class Quadrante:
    def __init__(self):
        self.__valores_descobertos = set()
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
        self.__valores_descobertos.add(valor)

    def get_possiveis_valores(self, lin, col):
        """Retorna os possiveis valores de uma célula"""
        return self.__matriz[lin][col]

    def descontar_valores_no_quadrante(self, lin, col, valores_descontar):
        """Descontar valores já conhecidos no próprio quadrante e descontar conjunto passado por parâmetro.
        Retorna True se descontou algo."""
        valores_para_descontar = set(self.__matriz[lin][col]) & valores_descontar
        valores_para_descontar.update(set(self.__matriz[lin][col]) & self.__valores_descobertos)
        if len(valores_para_descontar) > 0:
            self.__matriz[lin][col] = list(set(self.__matriz[lin][col]) - valores_para_descontar)

            if len(self.__matriz[lin][col]) == 1:  # Encontrou o último valor possível
                self.set_value(lin, col, self.__matriz[lin][col][0])


if __name__ == "__main__":
    quad1 = Quadrante()

    quad1.set_value(0, 0, 5)
    quad1.set_value(0, 1, 3)
    quad1.set_value(1, 0, 6)
    quad1.set_value(2, 1, 9)
    quad1.set_value(2, 2, 8)
    quad1.descontar_valores_no_quadrante(0, 2, {7})
    quad1.descontar_valores_no_quadrante(1, 1, {3, 5})
    print(quad1)
    print(f"Valores possiveis lin 0, col 2: {quad1.get_possiveis_valores(0, 2)}")
    print(f"Valores possiveis lin 1, col 1: {quad1.get_possiveis_valores(1, 1)}")
    print(f"Valores possiveis lin 1, col 2: {quad1.get_possiveis_valores(1, 2)}")
