class Account:
    def __init__(self,name, balance,accNumber):
        self.name=name
        self.balance=balance
        self.accNumber=accNumber
    #**********************************************
    def Deposit(self,amount):
        print(amount, "$ added to your account.")
        self.balance=self.balance + amount
    #**********************************************
    def Withdraw(self,amount):
        print(amount,"$ withdraw from your account.")
        self.balance=self.balance - amount
    #**********************************************
    def __str__(self):
        return "Name= "+self.name+ " Balance="+ str(self.balance)+ " Account Number="+str(self.accNumber)
#**************************************************    
Acc1=Account("Azita",2000,123456)
print(Acc1.balance)
Acc1.Withdraw(500)
print(Acc1.balance)
Acc1.Deposit(50000)
print(Acc1.balance)
print(Acc1)
