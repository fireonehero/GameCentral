import os
import random

class RockPaperScissors:
    def __init__(self):
        self.win_flag = False
        self.moves = ['Rock', 'Paper', 'Scissors']

    def win(self):
        print("You Won!")
        self.win_flag = True

    def lose(self):
        print("You lost!")
        self.win_flag = False

    def tie(self):
        print("It's a tie!")

    def play_game(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("[1] Rock, [2] Paper, [3] Scissors")
        player = int(input("What would you like to do: "))

        if player not in [1, 2, 3]:
            print("Invalid choice. Try again.")
            return

        computer = random.randint(1, 3)
        print(f"Computer chose: {self.moves[computer-1]}")

        if player == computer:
            self.tie()
        elif (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1):
            self.lose()
        else:
            self.win()
        
        decision = self.post_game_menu()
        return decision

    def post_game_menu(self):
        while True:
            print("=====================================")
            print("===   WHAT WOULD YOU LIKE TO DO   ===")
            print("=====================================")
            print("[1] Play Again")
            print("[2] Return to Game Central Menu")
            print("[0] Exit")
            print("===================================")
            choice = input("Enter your choice (0-2): ").strip()

            if choice == "1":
                return "play again"
            elif choice == "2":
                return "menu"
            elif choice == "0":
                exit()
            else:
                print("Invalid choice. Please select between 0 and 2.")
 

if __name__ == "__main__":
    game = RockPaperScissors()
    game.play_game()
