'''
Created on Apr. 29, 2020

@author: nirmal
'''
from Bank import Bank

class Account(Bank):
    
    
    branchname = "Jubilee Hills Corporate Office"
    branchlocation = "Jubilee Hills"
    
    
    def __init__(self, accountID, customer, balance, SMinBalance):
        self.AccountID = accountID
        self.Cust = customer 
        self.balance = balance
        self.SMinBalance = SMinBalance
        super(Account, self).__init__(self.branchname, self.branchlocation)
 
    
    
    def getAccountInfo(self):
        print("Customer Name:" + self.Cust.custname) 
    
    def deposit(self, depositAmount = 2000, state = 'true'):
        pass
    
    def withdraw(self, withdrawalAmount = 500):
        if( withdrawalAmount < self.balance - self.SMinBalance):
            self.balance -= withdrawalAmount
            print("Amount" + str(withdrawalAmount) + "withdrawn from account, new balance is :" + str(self.balance))
        else:
            print("Amount to withdraw exceeds minimum balance")
            
    
    def getBalance(self):
        print("Current balance is: " + str(self.balance))
    