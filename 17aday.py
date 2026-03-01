class BankAccount:
    def __init__(self,acc_no,acc_bal):
        self.__acc_noum=acc_no
        self.__acc_bal=acc_bal
    def check_bal(self):
        return self.__acc_bal
    
    def deposit(self,amount):
        if amount > 0:
            self.__acc_bal += amount
            print(f"deposit {amount} new balance{self.__acc_bal}")

        else:
            print("deposit amount must be positive")

    def withdra(self,amount):
        if 0 < amount <= self.__acc_bal:
            self.__acc_bal -= amount
            print(f"whithdraw{amount} new balance{self.__acc_bal}")
        else:
            print("invalid found ")

dp=BankAccount("shivaraj",666)
dp.deposit(5000)
print(dp.check_bal())

