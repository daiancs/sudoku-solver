import gameboard


def menu_inicial():
    print("1. Entrar com novo jogo")
    print("0. Sair")
    return int(input("Opção: "))


def menu_jogo():
    print("1. Resolver o jogo")
    print("2. Valores possíveis de uma célula")
    print("0. Voltar para menu inicial")
    return int(input("Opção: "))


def get_numero_quadrante(lin, col):
    """Retorna o número do quadrante para os valores absolutos de linha e coluna"""
    return ((lin // 3) * 3) + (col // 3)


def novo_jogo():
    jogo = gameboard.GameBoard()
    linhas = range(9)
    for linha in linhas:
        linha_de_valores = [int(val) for val in input(f"Valores [0..9] da linha {linha}: ").split()]

        for col, valor in enumerate(linha_de_valores):
            if valor != 0:
                quad = get_numero_quadrante(linha, col)
                jogo.inserir_valor(quad, linha % 3, col % 3, valor)
    return jogo


def get_valores_possiveis(lin, col):
    quadrante = get_numero_quadrante(lin, col)
    return jogo[quadrante // 3][quadrante % 3].get_possiveis_valores(lin % 3, col % 3)


while True:
    opcao = menu_inicial()
    if opcao == 0:  # SAIR
        break
    elif opcao == 1:  # Digitar novo jogo
        jogo = novo_jogo()
        print(jogo)

        while True:
            opcao_jogo = menu_jogo()
            if opcao_jogo == 0:
                break
            elif opcao_jogo == 1:
                jogo.descobrir_valores()
                print(jogo)
            elif opcao_jogo == 2:
                lin = int(input("Linha: "))
                col = int(input("Coluna: "))
                valores = sorted(get_valores_possiveis(lin, col))
                print(f"Valores possíveis: {valores}")