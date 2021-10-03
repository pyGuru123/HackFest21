import tkinter as tk
import tkinter.messagebox as tkMessageBox
from functools import partial  # We need partial for passing arguments with onclick event in tkinter.
import math
import SaveGames
import pickle


def check_list(_list):
    # We are gonna use this function to check if all the elements of the single
    # element are the same. We're using the set function because that removes all
    # the duplicate items. Hence, if the length of the list is 1, it means  that
    # all the elements in the list were same.

    # We are going to use this function to see if anyone won :P
    return len(set(_list)) == 1


class App:
    def __init__(self, N=3, first_computer=False):

        # N being the grid size.
        self.ai = "O"
        self.human = "X"
        self.Buttons = []
        self.N = N
        self.app = tk.Tk()
        self.app.title("TicTacToe Made By EmperorAj")
        self.app.geometry("600x300")

        with open("board_evals.pkl", "rb") as f:
            self.GAME_EVALS = pickle.load(f)

        tk.Label(self.app, text="Tic-tac-toe Game",
                 font=('Helvetica', '15')).grid(row=0, column=0)
        tk.Label(self.app, text="Player: X", font=(
            'Helvetica', '10')).grid(row=1)
        tk.Label(self.app, text="Computer: O",
                 font=('Helvetica', '10')).grid(row=2)

        self.computers_turn = first_computer

        self.create_widgets()

        if self.computers_turn:
            self.make_next_move()

        self.app.mainloop()

    def create_widgets(self):
        for i in range(self.N ** 2):
            # Looping N*N times, making all the buttons for the board.
            temp_button = tk.Button(self.app, text=" ", bg="green", fg="Black", width=6, height=2, font=(
                "Helvetica", "20"), command=partial(self.on_click, i))
            self.Buttons.append(temp_button)
            self.Buttons[i].grid(row=1 + i // self.N, column=1 + i % self.N)

    def on_click(self, button_index):
        if self.Buttons[button_index]['text'] == " ":
            # If it's player's turn, then mark X else make computer move.
            if not self.computers_turn:
                self.Buttons[button_index]['text'] = self.human
                self.computers_turn = not self.computers_turn
            self.check_for_win()
            self.make_next_move()

    def find_best_move(self):

        best_score = -math.inf
        best_move = None
        possible_moves = self.find_empty_places(self.get_board())

        for move in possible_moves:
            temp_board = [self.Buttons[i]['text'] for i in range(self.N ** 2)]
            temp_board[move] = self.ai
            board_to_number = SaveGames.convert_board_to_number(temp_board)
            if board_to_number in self.GAME_EVALS.keys():
                score = self.GAME_EVALS[board_to_number]
            else:
                score = self.minimax(temp_board, False, 0)
                self.GAME_EVALS[board_to_number] = score
            print(temp_board, score)
            if score > best_score:
                best_score = score
                best_move = move

        with open("board_evals.pkl", "wb") as f:
            pickle.dump(self.GAME_EVALS, f)

        return best_move

    def minimax(self, board, maximizing, depth):
        score = None
        if self.is_winner(board, self.human):
            score = -1
        elif self.is_winner(board, self.ai):
            score = 1
        elif len(self.find_empty_places(board)) == 0:
            score = 0

        if score is not None:
            self.GAME_EVALS[SaveGames.convert_board_to_number(board)] = score
            print(board, score)
            return score

        if maximizing:
            best_val = -math.inf
            for move in self.find_empty_places(board):
                board[move] = self.ai
                value = self.minimax(board, False, depth + 1)
                board[move] = " "
                best_val = max(best_val, value)
            return best_val

        else:
            best_val = math.inf
            for move in self.find_empty_places(board):
                board[move] = self.human
                value = self.minimax(board, True, depth + 1)
                board[move] = " "
                best_val = min(best_val, value)
            return best_val

    def make_next_move(self):
        position = self.find_best_move()
        self.Buttons[position]['text'] = self.ai
        self.computers_turn = not self.computers_turn
        self.check_for_win()

    def find_empty_places(self, board):
        indices = []
        for i in range(self.N ** 2):
            if board[i] == " ":
                indices.append(i)
        return indices

    def get_board(self):
        return [self.Buttons[i]['text'] for i in range(self.N ** 2)]

    def win_indices(self):
        # this will return all the possible indices that can be possible
        # in a given N*N board.

        for row in range(self.N):
            yield [row * self.N + col for col in range(self.N)]

        for col in range(self.N):
            yield [row * self.N + col for row in range(self.N)]

        yield [i * self.N + i for i in range(self.N)]
        yield [i * self.N + self.N - 1 - i for i in range(self.N)]

    def is_winner(self, board, player):
        for indices in self.win_indices():
            if check_list([board[index] for index in indices]) and board[indices[0]] == player:
                return True
        return False

    def check_for_win(self):
        if self.is_winner(self.get_board(), self.human):
            self.win(self.human)
        elif self.is_winner(self.get_board(), self.ai):
            self.win(self.ai)
        else:
            if len(self.find_empty_places(self.get_board())) == 0:
                tkMessageBox.showinfo("Game Complete", "This is a tie.")
                self.exit_application()

    def win(self, player):
        if player == self.ai:
            ans = "Game Complete, Computer won."
        else:
            ans = "Game Complete, Human won."
        tkMessageBox.showinfo("Game Complete", ans)
        self.exit_application()

    def exit_application(self):
        msg_box = tk.messagebox.askquestion('New Game', 'Do you want to start a new game? ',
                                           icon='warning')
        if msg_box == 'yes':
            self.app.destroy()
            main()
        else:
            self.app.destroy()


def main():
    app = tk.Tk()
    app.geometry("0x0")
    msg_box = tk.messagebox.askquestion('First Move', 'Do you want play the first move?')
    if msg_box == 'yes':
        first_computer = False
    else:
        first_computer = True
    app.destroy()
    App(N=3, first_computer=first_computer)


if __name__ == "__main__":
    main()
