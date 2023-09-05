class BankAccount():
    """
        The class for BankAccount
    """
    interest_rate = 0.3

    def __init__(self, name, number, balance):
        """
           Init function/constructor
        """
        self.name = name
        self.number = number
        self.balance = balance

    def withdraw(self, amount):
        """
           withdraw function
        """
        self.balance = self.balance - amount

    def deposit(self, amount):
        """
           deposit function
        """
        self.balance = self.balance + amount

    def add_interest(self):
        """
           add_interest function
        """
        #just a comment
        self.balance += self.balance * self.interest_rate
