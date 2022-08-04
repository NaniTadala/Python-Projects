class Account:
    
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
    
    def __str__(self):
        return f"Account Owner: {self.owner}\nAmount Available: Rs.{self.balance}"
    
    def deposit(self,dep_amount):
        self.balance += dep_amount
        print(f"Deposited Rs.{dep_amount}\nAvailable Balance: Rs.{self.balance}")

    def withdraw(self,wd_amount):
        if self.balance >= wd_amount:
            self.balance -= wd_amount
            print(f"Withdrawed Rs.{wd_amount}\nAvailable Balance: Rs.{self.balance}")
        else:
            print("Funds Unavailable")

accnt1 = Account('Nani',1000)

while True:
    mode = int(input("Select Mode\n1.Deposit\n2.Withdraw\n"))

    if (mode == 1):
        dp = int(input("Enter amount to deposit: Rs."))
        accnt1.deposit(dp)
    elif (mode == 2):
        wth = int(input("Enter amount to withdraw: Rs."))
        accnt1.withdraw(wth)
    else:
        print("Only select from 1 and 2")
        continue
    
    repeat = input("Click 'Yes' to continue or 'No' to exit\n")
    if repeat.lower() == "yes":
        continue
    elif repeat.lower() == "no":
        break