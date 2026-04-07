class Wallet:
    def __init__(self, _balance):
        self._balance = 100

    @property
    def balance(self):
        return self._balance

    def add_money(self, amount):
        if amount > 0:
            self._balance += amount


my_wallet = Wallet(100)
print(my_wallet.balance)
# print(my_wallet.balance = 999999) doesn't work because of the @property!!!