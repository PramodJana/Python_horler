class Account:
    def __init__(self,id=0,balance=100.0,annualInterestRate=0.0):
        self.__id=id
        self.__balance=balance
        self.__annualInterestRate=annualInterestRate
    def getId(self):
        return self.__id
    def getBalance(self):
        return self.__balance
    def getAnnualInterest(self):
        return self.__annualInterestRate
    def setId(self,newid):
        self.__id=newid
    def setBalance(self,newbalance):
        self.__balance=newbalance
    def setAnnualInterestRate(self,newannualInterestRate):
        self.__annualInterestRate=newannualInterestRate
    def getMonthlyInterestRate(self,getAnnualInterest):
        return(getAnnualInterest(self)/12)
    def getMonthlyInterest(self,getBalance,getMonthly):
        return(getBalance(self)*getMonthlyInterestRate(self))

    def withdraw(self,amount):
        if(amount<=self.__balance):
            self.__balance=self.__balance-amount
    def deposit(self,amount):
        self.__balance=self.__balance+amount
    def __str__(self):
        return "Account ID : "+str(self.__id)+" Account Balance : "+str(self.__balance)+" Annual Interest Rate : "+str(self.__annualInterestRate)






acoountA =Account
accountA = Account(0,100,0)
accountA.id = 1122
accountA.balance = 20000
accountA.annualInterestRate = 4.5
accountA.withdraw(2500)
accountA.deposit(3000)
print(accountA.Id + accountA.balance + accountA.monthlyInterestRate + accountA.monthlyInterest)
