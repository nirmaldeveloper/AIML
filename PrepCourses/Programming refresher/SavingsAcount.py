'''
Created on Apr. 29, 2020

@author: nirmal
'''
from Account import Account


class SavingsAccount(Account):
    
    balance = 40
    SMinBalance = 10 
    
    def __init__(self, accountID, customer):
        
        super(SavingsAccount, self).__init__(accountID, customer, self.balance, self.SMinBalance)
    
    
    def getSavingAccountInfo(self):
        print("Welcome, Customer Name:" + self.Cust.custname) 
    
    def deposit(self, depositAmount, allowed = 'true'):
        if(allowed):
            self.balance += depositAmount
    
    def withdraw(self, withdrawalAmount):
        if( withdrawalAmount > self.balance - self.SMinBalance):
            print("Not sufficient balance")
        else:
            self.balance -= withdrawalAmount
            print("Balance successfully withdrawn for Amount:" + str(withdrawalAmount) + ". New balance is: " + str(self.balance))
    
    def getBalance(self):
        print("Current Savings Account Balance is:" + str(self.balance))
