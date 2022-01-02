class Wallet:
    m_money = None

    def __init__(self, starting_bal=100):
        self.m_money = starting_bal

    def decrement_money(self, amount):
        self.m_money = self.m_money - amount

    def increment_money(self, amount):
        self.m_money = self.m_money + amount

    def get_curr_bal(self):
        return self.m_money
