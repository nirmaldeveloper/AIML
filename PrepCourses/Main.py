'''
Created on Apr. 29, 2020

@author: nirmal
'''
from Customer import Customer
from SavingsAcount import SavingsAccount

def main():
    customerid = input("Please Enter your Customer ID: ")#432
    customername = input("Please Enter your Name: ")#"Nirmal"
    customeraddress = input("Please Enter you address: ") #"Hyderabad"
    customerdetails = input("Please Enter your details: ") #"ComplexObject"
    accountID = input("Please Enter your Account ID: ") #781
    
    customer = Customer(customerid, customername, customeraddress, customerdetails)
    savingsaccount = SavingsAccount(accountID, customer)
    savingsaccount.getSavingAccountInfo()
    
    
    while(True):
        transactionType = int(input("Please Enter 1 for getting Account Balance, 2 for Deposit, 3 for withdrawal, Any other key and Enter for logging out : \n"))
    
        if(transactionType == 1):
            savingsaccount.getBalance()
        elif(transactionType == 2):
            amountToDeposit = int(input("Enter the amount to deposit: "))
            savingsaccount.deposit(amountToDeposit)
            savingsaccount.getBalance()
        elif(transactionType == 3):
            amountToWithdraw = int(input("Enter withdrawal Amount:"))
            savingsaccount.withdraw(amountToWithdraw)
        else:
            print("Logging out!!")
            break



if __name__ == '__main__':
    main()