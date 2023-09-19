import random
import os


class BlackJack:

    def __init__(self):
        self.wealth = 1000

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def create_deck(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        deck = [{'Suit': suit, 'Value': value} for suit in suits for value in values]
        return deck

    def deal_cards(self, deck, num_cards):
        hand = []
        for _ in range(num_cards):
            hand.append(deck.pop())
        return hand

    def card_value(self, card):
        if card['Value'] in ['J', 'Q', 'K']:
            return 10
        elif card['Value'] == 'A':
            return 11
        else:
            return int(card['Value'])

    def hand_value(self, hand):
        value = sum(self.card_value(card) for card in hand)
        num_aces = sum(1 for card in hand if card['Value'] == 'A')

        while value > 21 and num_aces:
            value -= 10
            num_aces -= 1

        return value

    def play_game(self):
        self.clear_screen()
        deck = self.create_deck()
        random.shuffle(deck)

        
        bet = input(f"Your current wealth is {self.wealth}. How much would you like to bet: ")
        while not bet.isdigit() or int(bet) > self.wealth:
            if not bet.isdigit():
                bet = input(f"Your current wealth is {self.wealth}. Please enter a valid bet: ")
            else:
                bet = input(f"Your current wealth is {self.wealth}. You can't bet more than you have. Please enter a valid bet: ")
        bet = int(bet)

        self.wealth -= bet
        self.clear_screen()

        your_hand = self.deal_cards(deck, 2)
        dealer_hand = self.deal_cards(deck, 2)

        print(f"Dealer's revealed card: {dealer_hand[0]['Value']} of {dealer_hand[0]['Suit']}")

        hands = [your_hand]

        for hand_index, hand in enumerate(hands):
            print(f"\nPlaying hand {hand_index + 1}")
            while True:
                print(f"Your current hand: {[card['Value'] for card in hand]} with a total value of {self.hand_value(hand)}")
                action = input("Do you want to 'hit', 'stay', 'double', or 'split': ").lower()
                self.clear_screen()

                if action == 'hit':
                    new_card = self.deal_cards(deck, 1)[0]
                    hand.append(new_card)
                    print(f"You drew {new_card['Value']} of {new_card['Suit']}")
                    if self.hand_value(hand) > 21:
                        print("You bust!")
                        break

                elif action == 'stay':
                    break

                elif action == 'double':
                    if len(hand) == 2:
                        self.wealth -= bet
                        new_card = self.deal_cards(deck, 1)[0]
                        hand.append(new_card)
                        print(f"You drew {new_card['Value']} of {new_card['Suit']}")
                        if self.hand_value(hand) > 21:
                            print("You bust!")
                        break

                elif action == 'split' and len(hand) == 2 and hand[0]['Value'] == hand[1]['Value'] and len(hands) < 3:
                    card1 = hand.pop()
                    card2 = hand.pop()

                    hands.append([card1, self.deal_cards(deck, 1)[0]])
                    hands.append([card2, self.deal_cards(deck, 1)[0]])
                    continue

        while self.hand_value(dealer_hand) < 17:
            dealer_hand.append(self.deal_cards(deck, 1)[0])

        print(f"\nDealer's hand: {[card['Value'] for card in dealer_hand]} with a total value of {self.hand_value(dealer_hand)}")

        winnings = 0
        for hand_index, hand in enumerate(hands):
            print(f"\nResults for hand {hand_index + 1}")
            if self.hand_value(hand) > 21:
                print("You bust!")
                continue

            if self.hand_value(dealer_hand) > 21 or self.hand_value(hand) > self.hand_value(dealer_hand):
                print("You win this hand!")
                winnings += bet * 2
            elif self.hand_value(hand) == self.hand_value(dealer_hand):
                print("It's a tie for this hand!")
                winnings += bet
            else:
                print("Dealer wins this hand!")

        print(f"\nYou won {winnings - (bet * len(hands))} this round.")
        self.wealth += winnings
        print(f"Your total wealth is now: {self.wealth}")
        
        if self.wealth <= 0:
            print("You've run out of money!")
            if self.post_game_menu() == "play again":
                self.wealth = 1000
                return self.play_game()
            else:
                return

        return self.post_game_menu()

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
