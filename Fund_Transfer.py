# from abc import ABC,abstractmethod

# class FundTransfer(ABC):
#     def __inti__(self,account_number,balance):
#         self.__account_number = account_number
#         self.__balance = balance
     
#     @property   
#     def account_number(self):
#         return self.__account_number
    
#     @account_number.setter
#     def account_number(self,account_number):
#         if len(str(account_number))==10:
#          self.account_number = account_number
    
#     @property  
#     def balance(self):
#         return self.__balance
    
#     @balance.setter
#     def balance(self,balance):
#         if balance > 0:
#             self.__balance=balance
        
#     def validate(self,amount):
#         if len(str(self.account_number)) == 10 and amount < self.balance and amount > 0:
#             return True
#         return False
        
#     @abstractmethod
#     def transfer(self,amount):
#         pass
    
# class NEFT_Transfer(FundTransfer):
#     def __init__(self, account_number, balance):
#         super().__init__(account_number,balance)
        
# def transfer(self,amount):
#     sc = amount*0.05  #service charge = sc --> 5percent
#     if (amount + sc) < self.balance:
#         self.balance = self.balance - (amount +sc)
#         return True
    
#     return False

# class IMPS_Transfer(FundTransfer):
#     def __init__(self,account_number,balance):
#         super().__init__(account_number,balance)
        
# def transfer(self,amount):
#     sc = amount*0.02  #service charge = sc --> 2percent
#     if (amount + sc) < self.balance:
#         self.balance = self.balance - (amount +sc)
#         return True
    
#     return False


# class RTGS_Transfer(FundTransfer):
#     def __init__(self,account_number,balance):
#         super().__init__(account_number,balance)
        
# def transfer(self,amount):
#    #no service charge
#     if (amount ) < self.balance and amount >= 10000:
#         self.balance = self.balance - (amount)
#         return True
    
#     return False

from abc import ABC, abstractmethod

class FundTransfer(ABC):
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    @property
    def account_number(self):
        return self.__account_number

    @account_number.setter
    def account_number(self, account_number):
        if len(str(account_number)) == 10:
            self.__account_number = account_number

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):
        if balance > 0:
            self.__balance = balance

    def validate(self, amount):
        return (
            len(str(self.account_number)) == 10
            and amount > 0
            and amount < self.balance
        )

    @abstractmethod
    def transfer(self, amount):
        pass


class NEFT_Transfer(FundTransfer):
    def transfer(self, amount):
        sc = amount * 0.05
        if amount + sc < self.balance:
            self.balance -= (amount + sc)
            return True
        return False


class IMPS_Transfer(FundTransfer):
    def transfer(self, amount):
        sc = amount * 0.02
        if amount + sc < self.balance:
            self.balance -= (amount + sc)
            return True
        return False


class RTGS_Transfer(FundTransfer):
    def transfer(self, amount):
        if amount >= 10000 and amount < self.balance:
            self.balance -= amount
            return True
        return False


def main():
  account_number =  int(input("Enter your accountNumber:\n"))
  account_balance =  int(input("Enter your accountBalance:\n"))
  
  print('Enter your choice\n')
  
  print(' 1 - NEFT\n 2 - IMPS \n 3 - RTGS \n')
  
  choice = int(input('Your choice:\n'))
  
  if choice == 1:
      ref = NEFT_Transfer(account_number , account_balance)
  elif choice == 2:
      ref = IMPS_Transfer(account_number , account_balance)
  elif choice == 3:
      ref = RTGS_Transfer(account_number , account_balance)
  else:
      print("Invalid choice")
  
  amt = int(input('Enter the amount to be transffered: '))
  
  if ref.validate(amt):
      if ref.transfer(amt):
          print('Transfer account Successfully')
          print(f'Remaining balance is {ref.balance}')
      else:
          print('Transfer could not made')
  else:
      print("Hi Check your your account number is equal-to 10 digits / your amount less than your balance amount ")
      

if __name__ == '__main__':
    main()
    
    
  
  
   