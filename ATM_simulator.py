import time

Bank_Balance = int(input("enter your balance:"))
value = 0
print("WELLCOME TO TECHNO BANK")
print("DONT REMOVE YOUR CARD TILL PROCESS GET COMPLETED")
print("""
Press 1 for bank balance
Press 2 for amount Withdrawl
Press 3 for amount deposit
Press 4 to change your registred mobile number
""")
value = int(input("PLEASE FILL YOUR CHOICE:  "))
if value == 1:
    print(f'YOUR BANK BALANCE IS {Bank_Balance}')
    print("THANK YOU VISIT AGAIN")
elif value == 3:
    reply = input("DO YOU WANT TO DEPOSIT CASH Y/N: ").upper()
    if reply == "Y":
        ACCOUNT_NUMBER = int(input("PLEASE ENTER THE BENIFERCIERY ACCOUNT NUMBER: "))
        ACCOUNT_HOLDER_NUMBER = int(input("PLEASE ENTER THE BENIFERCIERY ACCOUNT MOBILE NUMBER: "))
        AMOUNT = int(input("PLEASE ENTER THE AMOUNT (less than 49000):  "))
        if AMOUNT < 49000:
            time.sleep(2)
            print("PLEASE DEPOSIT THE CASH")
            time.sleep(5)
            print("PLEASE WAIT WHILE AMOUNT IS GET PROCEEDING")
            time.sleep(6)
            print("THANK YOU YOUR AMOUNT HAS BEEN DEPOSITED")
        else:
            print("INVALID AMOUNT")
            print("Thank you visit again")
elif value == 2:
    print("WELLCOME TO TECHNO BANK")
    WITHDRAWL = int(input("PLEASE ENTER THE AMOUNT:  "))
    time.sleep(3)
    if WITHDRAWL > 25000:
        print("AMOUNT SHOULD BE LESS THAN 25000")
        print("THANK YOU VISIT AGAIN")
    elif WITHDRAWL < Bank_Balance:
        print("PLEASE COLLECT YOUR CARD YOUR AMOUNT HAS BEEN PROCEED")
        time.sleep(4)
        New_Balance = Bank_Balance - WITHDRAWL
        reply = input("DO YOU WANT TO SEE YOUR BALANCE ON SCREEN: Y/N ").upper()
        if reply == "Y":
            time.sleep(3)
            print(f'YOUR BANK BALANCE IS {New_Balance}')
        elif reply == "N":
            print(f'THANK YOU VISIT AGAIN')
    else:
        print("SORRY UNABLE TO PROCESS INSUFFICIENT AMOUNT")
elif value == 4:
    reply = input("DO YOU WANT TO CAHNGE THE REGISTRED MOBILE NUMBER Y/N:  ").upper()
    if reply == "Y":
        NEW_MOBILE = int(input("PLEASE ENTER YOUR MOBILE NUMBER:  "))
        time.sleep(3)
        print("THANK YOU YOUR REGISTERED MOBILE NUMBER IS CHANGED")
        print(f'YOUR NEW REGISTRIED MOBILE NUMBER IS {NEW_MOBILE}')
        print("THANK YOU VISIT AGAIN")
else:
    print("INVALID OPTION")
