from kivy.app import App
from kivy.uix.gridlayout import GridLayout as Grid
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from logic import Game


class MyButton(Button):
    def __init__(self, game: Game, row: int, col: int, **kwargs):
        super().__init__(**kwargs)
        self.row = row
        self.text = ""
        self.col = col
        self.game = game
        self.bind(on_press=lambda x: self.press())

    def press(self):
        self.game.take_turn(self.game.current_player(), self.row, self.col)
        player = self.game.board[self.row][self.col]
        self.text = player.symbol
        self.game.turn += 1
        print(self.game.wincheck())

        if self.game.wincheck() is not None:
            self.game.display_winner()


class MyGrid(Grid):

    def __init__(self, game, **kwargs):
        self.game = game

        super(MyGrid, self).__init__(**kwargs)
        self.cols = 3
        self.btn00 = MyButton(self.game, 0, 0)
        self.btn01 = MyButton(self.game, 0, 1)
        self.btn02 = MyButton(self.game, 0, 2)
        self.btn10 = MyButton(self.game, 1, 0)
        self.btn11 = MyButton(self.game, 1, 1)
        self.btn12 = MyButton(self.game, 1, 2)
        self.btn20 = MyButton(self.game, 2, 0)
        self.btn21 = MyButton(self.game, 2, 1)
        self.btn22 = MyButton(self.game, 2, 2)

        self.add_widget(self.btn00)
        self.add_widget(self.btn01)
        self.add_widget(self.btn02)
        self.add_widget(self.btn10)
        self.add_widget(self.btn11)
        self.add_widget(self.btn12)
        self.add_widget(self.btn20)
        self.add_widget(self.btn21)
        self.add_widget(self.btn22)


class GameApp(App):

    class MyGame(Game):
        def __init__(self, parent):
            self.parent = parent
            super().__init__("Player 1", "Player 2")

        def get_col(self):
            pass

        def get_row(self):
            pass

        def play(self):
            pass

        def display_winner(self):
            if self.wincheck() is not None:
                self.parent.showWinner(str(self.wincheck()))

    def showWinner(self, text):
        popup = Popup(
            title="Winner",
            content=Label(text=text)
        )
        popup.open()

    def build(self):
        newGame = self.MyGame(self)
        return MyGrid(newGame)


if __name__ == "__main__":
    GameApp().run()
