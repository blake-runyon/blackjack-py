from Hand import *
from Wallet import *

class Player:
    m_name = ""
    m_hand = None
    m_wallet = ""

    def __init__(self, name="player", starting_bal=100) -> None:
        self.m_name = name
        self.m_hand = Hand()
        self.m_wallet = Wallet(starting_bal)

    def get_name(self):
        return self.m_name
