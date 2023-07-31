class AIWallet:
    def __init__(self):
        self.balance = 0

    def add_balance(self, amount):
        self.balance += amount

    def get_balance(self):
        return self.balance