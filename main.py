import time
import os
import random
from games.hangman import WordGuesser

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
os.system('cls' if os.name == 'nt' else 'clear')
def display_menu():
    print("===================================")
    print("===   WELCOME TO GAME CENTRAL   ===")
    print("===================================")
    print("[1] Hangman")
    print("[2] TicTacToe")
    print("[3] HigherLower")
    print("[4] Surprise Me!")
    print("[0] Exit")
    print("===================================")

def main():
    while True:
        display_menu()
        
        choice = input("Enter your choice (0-4): ").strip()
        
        if choice == "1":
            print("Starting Hangman...\n")
            hangman_game = WordGuesser()
            hangman_game.play()
        elif choice == "2":
            print("Starting TicTacToe...\n")
        elif choice == "3":
            print("Starting HigherLower...\n")
        elif choice == "4":
            print("Surprise!\n")
        elif choice == "0":
            print("Thank you for playing! Goodbye.")
            break
        else:
            print("Invalid choice. Please select a number between 0 and 4.\n")

if __name__ == '__main__':
    main()
