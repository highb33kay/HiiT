class Hello:
    # class constructors
    def __init__(self, sender, receiver, wallet):
        self.sender = sender
        self.receiver = receiver
        self.wallet = wallet

    # class method
    def SendMessage(self):
        print(
            f"Hello {self.receiver}, {self.sender} has sent you 50 trillion Dollars")

    def Wallet(self, money):
        self.wallet.append(money)
        print(f"{self.receiver} has a total of {self.wallet}")

# defining an object
Highb33kay = Hello("Bill Gates", "Highb33kay", [50, 20, 30, 20])

Highb33kay.Wallet(50)
