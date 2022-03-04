class BankAccount:
    def __init__(self,accNo, name, type, balance):
        self.accNo = accNo
        self.name = name
        self.type = type
        self.balance = balance
    def deposit(self,amount):
        self.balance = self.balance + amount
        print("Rs ",amount, " debited from ", self.type , " account ", self.accNo)
        print("Balance : ",self.balance)
    def withdraw(self,amount):
        if self.balance > amount:
            self.balance = self.balance - amount
            print("Rs ",amount, " credited from ", self.type , " account ", self.accNo)
            print("Balance : ",self.balance)
        else:
            print("Insufficent balance!")

c1 = BankAccount(14145, "denny", "savings", 5000)
while True:
    c = int(input("1. Deposit\n2. Withdraw\n"))
    if c==1:
        amount = int(input("Enter amount to deposit: "))
        c1.deposit(amount)
    elif c==2:
        amount = int(input("Enter amount to withdraw: "))
        c1.withdraw(amount)
    else:
        break
