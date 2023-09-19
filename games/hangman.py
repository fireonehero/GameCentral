import random
import os

class WordGuesser:

    def __init__(self):
        self.win = False
        self.guesses_left = 5
        self.reset()
        self.guessed_letters = []
        self.word_list = [
    "floccinaucinihilipilification",
    "antidisestablishmentarianism",
    "pneumonoultramicroscopicsilicovolcanoconiosis",
    "supercalifragilisticexpialidocious",
    "hippopotomonstrosesquippedaliophobia",
    "honorificabilitudinitatibus",
    "uncopyrightable",
    "subdermatoglyphic",
    "hydropneumatics",
    "misconjugatedly",
    "thunderstrike",
    "psychophysicotherapeutics",
    "squirrelled",
    "unimaginatively",
    "uncompromisingly",
    "unquestionably",
    "dichlorodifluoromethane",
    "counterdemonstration",
    "uncategorizable",
    "ambidextrously",
    "vexatiousnesses",
    "zephyr", 
    "zigzagging", 
    "zodiac", 
    "zilch", 
    "axiom", 
    "haiku",
    "heart like truck",
    "jumping through hoops",
    "bite the bullet",
    "break a leg",
    "read between the lines",
    "kick the bucket",
    "let the cat out of the bag",
    "spill the beans",
    "throw in the towel",
    "close, but no cigar",
    "cry over spilled milk",
    "an arm and a leg",
    "burning the midnight oil",
    "speak of the devil",
    "the early bird catches the worm",
    "you can't judge a book by its cover",
    "every cloud has a silver lining",
    "hit the nail on the head",
    "an apple a day keeps the doctor away",
    "dont count your chickens before they hatch",
    "a picture is worth a thousand words"]


    def generate_display(self, word):
        display = ""
        for char in word:
            if char == " ":
                display += "- "
            elif char in self.guessed_letters:
                display += char + " "
            else:
                display += "_ "
        return display

    def reset(self):
        self.win = False
        self.guesses_left = 5
        self.guessed_letters = []
        

    def play(self):
        chosen_word = random.choice(self.word_list)
        while self.guesses_left > 0:
            print("Word: ", self.generate_display(chosen_word))
            print("Guesses left:", self.guesses_left)
            print("Guessed Letters: ", ", ".join(self.guessed_letters))
            letter = input("Enter your guess: ").strip().lower()
            
            if letter in self.guessed_letters:
                print("You've already guessed that letter!")
                continue
                
            self.guessed_letters.append(letter)
            
            if letter in chosen_word:
                print(f"Good job! {letter} is in the word.")
            else:
                print(f"Sorry, {letter} is not in the word.")
                self.guesses_left -= 1
            
            if all(char in self.guessed_letters or char == " " for char in chosen_word):
                self.win = True
                break
                
        os.system('cls' if os.name == 'nt' else 'clear')
        
        if self.win:
            print(f"Congratulations! You've guessed the word: {chosen_word}.")
        else:
            print(f"You've run out of guesses! The word was: {chosen_word}.")

    

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

    def play_game(self):
        self.reset()
        os.system('cls' if os.name == 'nt' else 'clear')
        self.play()
        decision = self.post_game_menu()
        return decision

if __name__ == "__main__":
    game = WordGuesser()
    game.play_game()
