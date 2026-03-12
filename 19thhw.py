def banking_system():
    balens=0

    while (True):
        print("welcome to bank management system")
        print("1.Check Balance \n 2.Deposit Money \n 3.Withdraw Money \n 4.Exit")

        choise=int(input("enter your choice"))

        if choise==1:
            print(f"your balence is {balens}")
        elif choise==2:
            amount=int(input("enter youur deposit amount"))
            if amount>0:
                balens+=amount
                print(f"Success fullyy deposit {balens}")
            else:
                print("faild amount deposit")

        elif choise==3:
            amount=int(input("enter your deposit balece"))
            if amount>=0:
                balens-=amount
                print(f"success fully withdra{balens}")
            else:
                print("failed in whith draw")

        elif choise==4:
            print("exiting banking system")
            break
        else:
            print("invalid choice")



if __name__ == "__main__":
    banking_system()