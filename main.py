from kivy.config import Config
# Esse bloco está antes do import do App do Kivy pois define configurações da aplicação
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', 500)
Config.set('graphics', 'heigth', 600)

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from gameboard import GameBoard


class SelectNumberPopup(Popup):
    """Popup para selecionar o valor no grid do jogo"""
    def __init__(self, parent_button, **kwargs):
        super().__init__(**kwargs)
        self.parent_button = parent_button

        quad = int(self.parent_button.id[4])
        celula = int(self.parent_button.id[5])
        valores_possiveis = jogo.get_valores_possiveis_jogo(quad, celula)

        popup_layout = BoxLayout(orientation="vertical")

        grd_numeros_layout = GridLayout(cols=3)
        for valor in range(1, 10):
            if valor in valores_possiveis:
                grd_numeros_layout.add_widget(
                    Button(
                        text=f"{valor}",
                        font_size=25,
                        color=[.8, .8, .8, 1],
                        halign="center",
                        bold=True,
                        background_color=[.1, .1, .1, 1],
                        on_release=self.seleciona_valor,
                    )
                )
            else:
                grd_numeros_layout.add_widget(
                    Button(
                        background_color=[.1, .1, .1, 1],
                    )
                )
        popup_layout.add_widget(grd_numeros_layout)
        popup_layout.add_widget(ButtonsPopup(self, parent_button))
        self.add_widget(popup_layout)

    def seleciona_valor(self, button):
        self.parent_button.text = button.text
        self.dismiss()


class ButtonsPopup(BoxLayout):
    def __init__(self, root_popup, button, **kwargs):
        super().__init__(**kwargs)
        self.button = button
        self.root_popup = root_popup

    def limpar(self):
        self.button.text = ""
        self.root_popup.dismiss()

    def cancelar(self):
        self.root_popup.dismiss()


class GameGrid(GridLayout):
    pass


class QuadranteGrid(GridLayout):
    pass


class MainGrid(AnchorLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        global game_grd
        game_grd = GameGrid()

        for quad in range(9):
            quad_grd = QuadranteGrid()
            for cel in range(9):
                nome_btn = f"btn_{quad}{cel}"
                quad_grd.add_widget(
                    Button(
                        id=nome_btn,
                        text="",
                        font_size=25,
                        color=[.8, .8, .8, 1],
                        halign="center",
                        bold=True,
                        background_color=[.1, .1, .1, 1],
                        on_release=self.callback
                    )
                )
            game_grd.add_widget(quad_grd)
        self.add_widget(game_grd)

    @staticmethod
    def callback(button):
        popup = SelectNumberPopup(button)
        popup.open()


class ButtonsGrid(GridLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)

    @staticmethod
    def inicializar_jogo():
        #  Percorre os botões que possuem valor associado
        for btn_valor in game_grd.walk():
            if isinstance(btn_valor, Button) and \
                    btn_valor.id is not None and \
                    btn_valor.id[:4] == "btn_" and \
                    btn_valor.text:
                quad = int(btn_valor.id[4])
                celula = int(btn_valor.id[5])
                valor = int(btn_valor.text)
                jogo.inserir_valor(quad, celula, valor)

    def resolver(self):
        self.inicializar_jogo()
        jogo.descobrir_valores()
        for btn_valor in game_grd.walk():
            if isinstance(btn_valor, Button) and \
                    btn_valor.id is not None and \
                    btn_valor.id[:4] == "btn_" and \
                    not btn_valor.text:
                quad = int(btn_valor.id[-2])
                celula = int(btn_valor.id[-1])
                valores = jogo.get_valores_possiveis_jogo(quad, celula)
                if len(valores) == 1:
                    btn_valor.text = str(valores[0])

    @staticmethod
    def validar():
        print(jogo)

    @staticmethod
    def zerar():
        global jogo
        jogo = GameBoard()
        for btn_valor in game_grd.walk():
            if isinstance(btn_valor, Button) and \
                    btn_valor.id is not None and \
                    btn_valor.id[:4] == "btn_":
                btn_valor.text = ""

    @staticmethod
    def sair():
        exit()


class RootWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        # Grade principal do Sudoku
        self.add_widget(MainGrid())

        # Barra de botões na parte inferior
        self.add_widget(ButtonsGrid())

        # Inicia um novo jogo
        ButtonsGrid.zerar()


class SudokuSolverApp(App):
    def build(self):
        self.title = "Sudoku Solver"
        return RootWidget()


if __name__ == '__main__':
    SudokuSolverApp().run()
