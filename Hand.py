class Hand:
    m_hand = []
    m_score = -1

    def __init__(self):
        self.m_hand = []
        self.m_score = 0

    def add_card(self, card):
        self.m_hand.append(card)
        self.m_score += card.m_score

    def print_hand(self):
        for x in self.m_hand:
            print(x.get_rank() + " of " + x.get_suit())
