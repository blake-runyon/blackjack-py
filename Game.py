from Dealer import *
from Deck import *
from Player import *
from Settings import *


class Game:
    deck = None
    player = None
    dealer = None
    s = Settings()
    playing = True

    def __init__(self):
        s = Settings()
        if s.get_prompt() is True:
            name = input("Enter your name: ")
            self.player = Player(name)
        else:
            self.player = Player()

        self.dealer = Dealer()
        self.deck = Deck(s.get_num_decks())
        self.deck.shuffle()

        for i in range(2):
            self.player.m_hand.add_card(self.deck.deal_card())
            self.dealer.m_hand.add_card(self.deck.deal_card())

    def update(self):
        while self.playing is True:
            if self.player.m_hand.m_score > 21 or self.dealer.m_hand.m_score > 21:
                return self.check_win()

            print("Your Score: " + str(self.player.m_hand.m_score))
            for x in self.player.m_hand.m_hand:
                x.print_card()

            print()

            print("Dealer Score: " + str(self.dealer.m_hand.m_score - self.dealer.m_hand.m_hand[1].get_score()))
            self.dealer.m_hand.m_hand[0].print_card()

            choice = input("Hit or Stand [H / S] ")
            if choice == 'H':
                self.player.m_hand.add_card(self.deck.deal_card())
                return self.update()
            else:
                return self.check_win()

        print("Thanks for playing!")

    def win_message(self, player_win=0):
        if player_win == 0:
            print("Draw")

        if player_win is False:
            print("Dealer Wins!")
        else:
            print("Player Wins!")

        self.playing = False
        self.menu()

    def check_win(self):
        if self.player.m_hand.m_score > 21:
            return self.win_message(False)
        else:
            while self.dealer.m_hand.m_score < 17:
                self.dealer.m_hand.add_card(self.deck.deal_card())

        print("Your Score: " + str(self.player.m_hand.m_score))
        for x in self.player.m_hand.m_hand:
            x.print_card()

        print()

        print("Dealer Score: " + str(self.dealer.m_hand.m_score))
        for x in self.dealer.m_hand.m_hand:
            x.print_card()

        if self.player.m_hand.m_score < self.dealer.m_hand.m_score < 22:
            return self.win_message(False)
        elif self.dealer.m_hand.m_score < self.player.m_hand.m_score < 22:
            return self.win_message(True)
        elif self.player.m_hand.m_score == self.dealer.m_hand.m_score and self.player.m_hand.m_score <= 21 and self.dealer.m_hand.m_score <= 21:
            return self.win_message()
        elif self.dealer.m_hand.m_score > 21 and self.player.m_hand.m_score < 21:
            return self.win_message(True)
        else:
            print("error calculating winner.")

    def menu(self):
        menu_options = ["Play", "Profile", "Settings", "Exit"]
        i = 1
        for option in menu_options:
            print(str(i) + ". " + str(option))
            i += 1
        choice = input("What would you like to do? ")

        if choice == "1":
            self.playing = True
            self.update()
        elif choice == "2":
            print("Coming soon.")
        elif choice == "3":
            self.s.settings_menu()
        elif choice == "4":
            self.playing = False

    def new_game(self):
        if self.deck.cards.count() == 0:
            self.deck = Deck(self.s.get_num_decks())

        self.player.m_hand.m_hand.clear()
        self.player.m_hand.m_score = 0

        self.dealer.m_hand.m_hand.clear()
        self.dealer.m_hand.m_score = 0
