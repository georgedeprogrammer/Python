Balance = 10000
list=["CheckBalance", "Withdraw", "Deposit", "Exit"]
print(list)
Option = input("Enter from the list: ")
if Option == "CheckBalance":
    print(Balance)

elif Option == "Withdraw":
    Amount = int(input("Enter Amount to withdraw: "))
    if Amount >Balance:
        print("Not enough money to withdraw")
    else:
        Balance = (Balance-Amount)
        print(Balance)

elif Option == "Deposit":
    DepositAmount = int(input("Enter amount to be deposited: "))
    if DepositAmount < 0 :
        print("Can't deposit!")
    else:
        Balance = (Balance+DepositAmount)
        print(Balance)
else:
    Option == "Exit"
    print("Terminated")
