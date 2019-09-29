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
        """Insere valor na célula correspondente do quadrante"""
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
