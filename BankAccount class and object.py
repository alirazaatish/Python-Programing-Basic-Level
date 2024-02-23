class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.balance=balance

    def deposite(self,amount):
        if amount>0:
            self.balance+=amount
            return f"Deposite ${amount},New amount ${self.balance}"
        else:
            return f"Invalide deposite amount"
        
    def withdraw(self,amount):
        self.amount=amount
        if 0<amount<=self.balance:
            self.balance-=amount
            return f"Withdraw ${amount}.New balance ${self.balance}"
        else:
            return f"Insufficient funds"
    
    def get_balance(self):
        return f"Account balance for {self.account_holder}: ${self.balance}"

account1=BankAccount("Ali Raza",(1000))
account2=BankAccount("Aimen",(500))

print(account1.deposite(200))
print(account2.deposite(50))

print(account1.withdraw(500))
print(account2.withdraw(250))

print(account1.get_balance())
print(account2.get_balance())