import os

class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def reset_board(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'


    def display_board(self):
        print("-" * 13)
        for i, row in enumerate(self.board):
            print("|", " | ".join(row), "|")
            if i < 2:
                print("-" * 13)
        print("-" * 13)

    def is_valid_move(self, row, col):
        return 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == ' '

    def is_winner(self, player):
        for i in range(3):
            if all([cell == player for cell in self.board[i]]) or all([self.board[j][i] == player for j in range(3)]):
                return True
        return self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player or \
               self.board[0][2] == player and self.board[1][1] == player and self.board[2][0] == player

    def is_full(self):
        return all(cell != ' ' for row in self.board for cell in row)

    def game_over(self):
        return self.is_winner('X') or self.is_winner('O') or self.is_full()

    def switch_player(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'

    def minimax(self, depth, isMaximizing):
        if self.is_winner('X'):
            return -10 + depth
        if self.is_winner('O'):
            return 10 - depth
        if self.is_full():
            return 0

        if isMaximizing:
            maxEval = float('-inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == ' ':
                        self.board[i][j] = 'O'
                        eval = self.minimax(depth + 1, False)
                        self.board[i][j] = ' '
                        maxEval = max(maxEval, eval)
            return maxEval

        else:
            minEval = float('inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == ' ':
                        self.board[i][j] = 'X'
                        eval = self.minimax(depth + 1, True)
                        self.board[i][j] = ' '
                        minEval = min(minEval, eval)
            return minEval

    def find_best_move(self):
        best_move = (-1, -1)
        best_value = float('-inf')
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    self.board[i][j] = 'O'
                    move_value = self.minimax(0, False)
                    self.board[i][j] = ' '
                    if move_value > best_value:
                        best_value = move_value
                        best_move = (i, j)
        return best_move


    def choose_mode(self):
        print("Choose a mode:")
        print("[1] Player vs Player")
        print("[2] Player vs Computer")
        choice = input("Enter 1 or 2: ").strip()
        if choice == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            return 'PvP'
        elif choice == "2":
            os.system('cls' if os.name == 'nt' else 'clear')
            return 'PvC'

    def player_vs_player(self):
        while not self.game_over():
            self.display_board()
            valid_input = False
            while not valid_input:
                try:
                    row, col = map(int, input("Enter row and column (1-3, separated by a space): ").split())
                    if self.is_valid_move(row-1, col-1):
                        self.board[row-1][col-1] = self.current_player
                        valid_input = True
                    else:
                        print("That square is already taken or out of range! Choose another.")
                except ValueError:
                    print("Invalid input. Please enter two numbers separated by a space (e.g., '2 3').")
            if self.is_winner(self.current_player):
                self.display_board()
                print(f"Player {self.current_player} wins!")
                return self.post_game_menu()
            elif self.is_full():
                self.display_board()
                print("It's a draw!")
                return self.post_game_menu()
            self.switch_player()

    def player_vs_computer(self):
        current_player = 'X'
        self.display_board()

        while not self.game_over():

            if current_player == 'X':
                row, col = map(int, input("Enter row and column (1-3, separated by a space): ").split())
                row -= 1
                col -= 1
                while not self.is_valid_move(row, col):
                    print("Invalid move. Try again.")
                    row, col = map(int, input("Enter row and column (1-3, separated by a space): ").split())
                    row -= 1
                    col -= 1
                self.board[row][col] = current_player
            else:
                row, col = self.find_best_move()
                self.board[row][col] = current_player
                self.display_board()

            if self.is_winner(current_player):
                print(f"{current_player} wins!")
                return self.post_game_menu()
            elif self.is_full():
                print("It's a tie!")
                return self.post_game_menu()

            current_player = 'X' if current_player == 'O' else 'O'

    def post_game_menu(self):
        print("====================================")
        print("===   WHAT WOULD YOU LIKE TO DO   ===")
        print("====================================")
        print("[1] Play Again")
        print("[2] Return to Game Central Menu")
        print("[0] Exit")
        print("====================================")
        while True:
            choice = input("Enter your choice (0-2): ").strip()
            if choice == "1":
                return "play again"
            elif choice == "2":
                return "menu"
            elif choice == "0":
                return "exit"
            else:
                print("Invalid choice. Please select a number between 0 and 2.")

    def play_game(self):
        self.reset_board()
        mode = self.choose_mode()
        if mode == 'PvP':
            return self.player_vs_player()
        elif mode == 'PvC':
            return self.player_vs_computer()
            
if __name__ == "__main__":
    game = TicTacToe()
    while True:
        action = game.play_game()
        if action == "exit":
            break
