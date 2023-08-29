import random
from math import sqrt
import os

class NumberGuesser:
    def __init__(self):
        self.win = False
        self.reset()

    def get_number_input(self, prompt):
        while True:
            try:
                num = int(input(prompt))
                return num
            except ValueError:
                print("Please enter a valid number!")

    def play(self):
        print("Welcome to the Number Guesser!")
        low_number = self.get_number_input("Please enter the lowest number it can be: ")
        high_number = self.get_number_input("Please enter the highest number it can be: ")

        while low_number == high_number:
            print("The two numbers cannot be the same!")
            low_number = self.get_number_input("Please enter the lowest number it can be: ")
            high_number = self.get_number_input("Please enter the highest number it can be: ")

        secret_number = random.randint(low_number, high_number)
        MAX_GUESSES = int((high_number - low_number)**(1/3) + .5)

        for i in range(MAX_GUESSES):
            print(f"You have {MAX_GUESSES - i} guesses left.")
            guess = self.get_number_input("Guess the secret number: ")

            if guess == secret_number:
                print("Congratulations! You've guessed the number!")
                self.win = True
                break
            elif guess < secret_number:
                print("Higher!")
            else:
                print("Lower!")

        if not self.win:
            print(f"Sorry, you ran out of guesses! The number was {secret_number}")

    def reset(self):
        self.win = False
        self.guesses_left = 5

    def play_game(self):
        self.reset()
        os.system('cls' if os.name == 'nt' else 'clear')
        self.play()
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
    game = NumberGuesser()
    game.play_game()
