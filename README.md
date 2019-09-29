# sudoku-solver
Aplicativo para tentar resolver jogo Sudoku.

O aplicativo tem objetivo de tentar resolver o jogo de Sudoku sem a preocupação inicial de utilizar um algoritmo otimizado para isso. Minha intenção é mais testar algumas funcionalidades do Python, OO e alguma biblioteca gráfica (provavelmente Kivy).

22/08: Criação do projeto inicial e das classes Quadrante e GameBoard. 
    A classe Quadrante contém uma matriz 3x3 de listas com os possíveis números que podem ir naquela célula. Quando restar apenas um valor na lista, este é exibido pois é o único possível. 
    A classe GameBoard contém uma matriz 3x3 de células e é o desenho principal do jogo.
    
23/08: Menus de interação com usuário permitem criação de novos jogos mais facilmente. Também é possível consultar valores possíveis de uma célula quando o jogo não pode ser totalmente resolvido com o algoritmo atual.

25/08: Permite digitar um novo jogo sem os espaços entre os valores de cada linha. Correção importante no algoritmo. Melhor organização dos métodos da classe GameBoard.

29/09: Inserido interface gráfica em Kivy para o jogo.
