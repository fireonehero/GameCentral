import time
import os
import random
from games.hangman import WordGuesser
from games.higherlower import NumberGuesser
from games.tictactoe import TicTacToe

print("""
  ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▄████▄  ▓█████  ███▄    █ ▄▄▄█████▓ ██▀███   ▄▄▄       ██▓    
 ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▀ ▀█  ▓█   ▀  ██ ▀█   █ ▓  ██▒ ▓▒▓██ ▒ ██▒▒████▄    ▓██▒    
▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒▓█    ▄ ▒███   ▓██  ▀█ ██▒▒ ▓██░ ▒░▓██ ░▄█ ▒▒██  ▀█▄  ▒██░    
░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒▓▓▄ ▄██▒▒▓█  ▄ ▓██▒  ▐▌██▒░ ▓██▓ ░ ▒██▀▀█▄  ░██▄▄▄▄██ ▒██░    
░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ▒ ▓███▀ ░░▒████▒▒██░   ▓██░  ▒██▒ ░ ░██▓ ▒██▒ ▓█   ▓██▒░██████▒
 ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ░▒ ▒  ░░░ ▒░ ░░ ▒░   ▒ ▒   ▒ ░░   ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ▒░▓  ░
  ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░  ▒    ░ ░  ░░ ░░   ░ ▒░    ░      ░▒ ░ ▒░  ▒   ▒▒ ░░ ░ ▒  ░
░ ░   ░   ░   ▒   ░      ░      ░      ░           ░      ░   ░ ░   ░        ░░   ░   ░   ▒     ░ ░   
      ░       ░  ░       ░      ░  ░   ░ ░         ░  ░         ░             ░           ░  ░    ░  ░
                                       ░                                                              

   ___       _   _____                       __ __           
  / _ )__ __(_) / __(_)______ ___  ___  ___ / // /__ _______ 
 / _  / // /   / _// / __/ -_) _ \/ _ \/ -_) _  / -_) __/ _ \\
/____/\_, (_) /_/ /_/_/  \__/\___/_//_/\__/_//_/\__/_/  \___/
     /___/                                                                                                               
""")
time.sleep(2)
def display_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("===================================")
    print("===   WELCOME TO GAME CENTRAL   ===")
    print("===================================")
    print("[1] Hangman")
    print("[2] TicTacToe")
    print("[3] HigherLower")
    print("[4] Surprise Me!")
    print("[0] Exit")
    print("===================================")

def play_hangman(hangman_game):
    print("Starting Hangman...\n")
    while True:
        decision = hangman_game.play_game() 
        if decision == "menu":
            break
        elif decision == "play again":
            continue

def play_tictactoe(tic_tac_toe_game):
    print("Starting TicTacToe...\n")
    while True:
        decision = tic_tac_toe_game.play_game()
        if decision == "menu":
            break
        elif decision == "play again":
            continue

def play_higherlower(higher_lower_game):
    print("Starting HigherLower...\n")
    while True:
        decision = higher_lower_game.play_game()
        if decision == "menu":
            break
        elif decision == "play again":
            continue

def main():
    hangman_game = WordGuesser()
    higher_lower_game = NumberGuesser()
    tic_tac_toe_game = TicTacToe()

    games = [(play_hangman, hangman_game), 
             (play_tictactoe, tic_tac_toe_game), 
             (play_higherlower, higher_lower_game)]

    while True:
        display_menu()
        choice = input("Enter your choice (0-4): ").strip()
        
        if choice == "1":
            play_hangman(hangman_game)
        elif choice == "2":
            play_tictactoe(tic_tac_toe_game)
        elif choice == "3":
            play_higherlower(higher_lower_game)
        elif choice == "4":
            random_game_func, random_game_instance = random.choice(games)
            random_game_func(random_game_instance)
        elif choice == "0":
            print("Thank you for playing! Goodbye.")
            break
        else:
            print("Invalid choice. Please select a number between 0 and 4.\n")

if __name__ == '__main__':
    main()