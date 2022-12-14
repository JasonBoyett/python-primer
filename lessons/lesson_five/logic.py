from abc import ABC

# Abstract base class. This is a way of making an abstract class in python
from abc import abstractmethod

# this is an anotation that lets you make abstract methods when making
# abstract classes


class Player:
    def __init__(self, name: str, symbol: str):
        self.name = name
        self.symbol = symbol

    def __str__(self):
        return self.name


class Game(ABC):
    # game is abstract since it inharits from ABC or abstract base class

    def __init__(self, p1_name: str, p2_name: str):
        self.turn = 1
        self.player1 = Player(p1_name, "X")
        self.player2 = Player(p2_name, "O")
        self.cat = Player("cat", "cat")
        self.board = [
            # the board starts filled with None types and will be filled
            # with player objects
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]

    def current_player(self):
        # this method returns the player who is currently selecting a space
        if self.turn % 2 != 0:
            return self.player1
        else:
            return self.player2

    def __str__(self):
        result = "  0 1 2\n"
        for i in range(0, len(self.board[0])):
            result += str(i) + "|"
            for j in range(0, len(self.board[0])):
                if self.board[i][j] is None:
                    result += " |"
                else:
                    result += self.board[i][j].symbol + "|"
            result += "\n"
        return result

    def __int__(self):
        # purely for the sake of an example this is rather useless in practice
        return self.turn

    def wincheck(self):
        filled = 0
        for i in range(0, 3):
            for j in range(0, 3):
                if self.board[i][j] is not None:
                    filled += 1
        if filled == 9:
            return self.cat
        for i in range(0, 3):
            if (
                self.board[i][0] == self.board[i][1]
                and self.board[i][0] == self.board[i][2]
            ):
                if self.board[i][0] is None:
                    pass
                else:
                    return self.board[i][0]
            if (
                self.board[0][i] == self.board[1][i]
                and self.board[0][i] == self.board[2][i]
            ):
                if self.board[0][i] is None:
                    pass
                else:
                    return self.board[0][i]
        if self.board[1][1] is not None:
            center = self.board[1][1]
            if self.board[0][0] == center and center == self.board[2][2]:
                return center
            if self.board[0][2] == center and self.board[2][0] == center:
                return center
        return None

    def take_turn(self, player: Player, row: int, col: int):

        if self.board[row][col] is None:
            self.board[row][col] = player
        else:
            self.take_turn(player, self.get_row(), self.get_col())

    def get_winner(self):
        if self.wincheck() is not None:
            return self.wincheck().name

    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def get_row(self):
        pass

    @abstractmethod
    def get_col(self):
        pass

    @abstractmethod
    def display_winner(self):
        pass


if __name__ == "__main__":

    class My_Game(Game):
        def __init__(self):
            super().__init__("Jason", "Not Jason")

        def get_row(self):
            try:
                entry = int(input("ROW: "))
                if entry == 69:
                    print("Nice")
                    quit()
                if entry < 0 or entry > 2:
                    print(entry, " is not a valid entry")
                    print("you must enter an integer between 0 and 2")
                    return self.get_row()
                else:
                    return entry
            except ValueError:
                print("please enter an integer between 0 and 2")
                return self.get_row()
            except Exception:
                print("something went wrong")
                return self.get_row()

        def get_col(self):
            try:
                entry = int(input("COL: "))
                if entry == 69:
                    print("Nice")
                    quit()
                if entry < 0 or entry > 2:
                    print(entry, " is not a valid entry")
                    print("you must enter an integer between 0 and 2")
                    return self.get_col()
                else:
                    return entry
            except ValueError:
                print("please enter an integer between 0 and 2")
                return self.get_col()
            except Exception:
                print("something went wrong")
                return self.get_col()

        def display_winner(self):
            winner = self.wincheck()
            print(winner, "WON!")

        def play(self):
            print(self)
            while self.wincheck() is None:
                if self.wincheck() == self.cat:
                    print("The cat won")
                    break
                if self.turn % 2 != 0:
                    self.take_turn(
                        self.player1,
                        self.get_row(),
                        self.get_col()
                    )
                    self.turn += 1
                else:
                    self.take_turn(
                        self.player2,
                        self.get_row(),
                        self.get_col()
                    )
                    self.turn += 1
                print(self)

                self.display_winner()

    new_game = My_Game()
    new_game.play()
