#Programmer: Solomon Rantlhago
#Purpose: ATM TRANSACTION
from decimal import *
user_balance = 3000

def GetChoice():
    try:
        print("ATM TRANSACTION\n==================")
        print("1. Check Balance\n2. Withdraw Cash\n3. Deposit Cash\n4. Quit")
        Choice = int(input("Enter your Choice: "))

    except:
        print("Invalid Input. Try Again")
        Choice=GetChoice()


    return Choice

def Transaction(prompt):
    Amount = Decimal(input(prompt))
    return Amount

def DisplayBalance():
    print("Balance: R", user_balance)

Choice = GetChoice()
while(Choice!=4):
    if(Choice==1):
        DisplayBalance()
        input("PRESS ANY KEY TO CONTINUE.....")
        Choice = GetChoice()
    elif(Choice==2):
       Amount =Transaction("ENTER THE AMOUNT TO WITHDRAW: ")
       if(Amount>user_balance):
           print("You don't have enough Funds  ")
           input("PRESS ANY KEY TO CONTINUE....")
           Choice = GetChoice()
       else:
           print("PLEASE COLLECT YOUR CASH\n")
           user_balance = user_balance-Amount
           DisplayBalance()
           input("PRESS ANY KEY TO CONTINUE....")
           Choice = GetChoice()

    elif(Choice==3):
        Amount = Transaction("ENTER THE AMOUNT TO DEPOSIT: ")
        print("PLEASE INSERT CASH\n")
        user_balance = user_balance+Amount
        DisplayBalance()
        input("PRESS ANY KEY TO CONTINUE....")
        Choice = GetChoice()
    else:
       print("Invalid Choice Try Again")
       Choice= GetChoice()

if(Choice==4):
    print("THANK YOU FOR YOUR BUSINESS")
    input("PRESS ANY KEY TO EXIT.....")

