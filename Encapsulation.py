# class BadBankAccount:
#     def __init__(self,balance):
#         self.balance =  balance

# account =BadBankAccount(0.0)
# account.balance = -1 # bad assignment
# print(account.balance)


class BankAccount:
    def __init__(self):
        self.__balance = 0.0
    
    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance (self, new_balance):
        if new_balance<=0:
            raise ValueError("Please enter value greater than 0")
        else:
            self.__balance+=new_balance

account = BankAccount()
account.balance = 2500

print(account.balance)


        
