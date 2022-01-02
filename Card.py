class Card:
    m_suit = ""
    m_rank = ""
    m_score = -1
    m_suits = ["Diamonds", "Clubs", "Hearts", "Spades"]
    m_ranks = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "King", "Queen"]

    def __init__(self, suit, rank) -> None:
        self.m_suit = self.m_suits[suit]
        self.m_rank = self.m_ranks[rank]
        if rank == 0:
            self.m_score = 1
        elif rank >= 9:
            self.m_score = 10
        else:
            self.m_score = rank + 1

    def get_rank(self):
        return self.m_rank

    def get_suit(self):
        return self.m_suit

    def get_score(self):
        return self.m_score

    def print_card(self):
        print(self.get_rank() + " of " + self.get_suit())
