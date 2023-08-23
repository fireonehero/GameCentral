import random

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
        word = random.choice(self.word_list)
        print(self.generate_display(word))
        
        while not self.win and self.guesses_left > 0:
            guess = input("Guess a letter: ")
            
            while len(guess) != 1 or not guess.isalpha():
                print("Error: Please input only one letter.")
                guess = input("Guess a letter: ")

            if guess not in self.guessed_letters:
                if guess not in word:
                    self.guesses_left -= 1
                self.guessed_letters.append(guess.lower())

            print(self.generate_display(word))
            print(f"Guesses Left: {self.guesses_left} | " + "Guessed Letters:", ', '.join(self.guessed_letters))

            if "_" not in self.generate_display(word):
                self.win = True
                print("You Won!")
                
        if not self.win:
            print("You lost! The word was:", word)

if __name__ == "__main__":
    game = WordGuesser()
    while True:
        game.play()
        print("=====================================")
        print("===   WHAT WOULD YOU LIKE TO DO   ===")
        print("=====================================")
        print("[1] Play Again")
        print("[2] Return to Game Central Menu")
        print("[0] Exit")
        print("===================================")
        choice = input("Enter your choice (0-2): ").strip()

        if choice == "1":
            game.reset()
        elif choice == "2":
            # You can add the logic to return to the main menu here.
            pass
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please select between 0 and 2.")
