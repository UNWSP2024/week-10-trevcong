#AUTHOR: Trevor Conger UNWSP
#DATE: 11/8/24
#TITLE: OOP BankAccount

#SAMPLE CODE FROM VIDEOS

class BankAccount:
    def __init__(self, bal):
        self.__balance = bal

    def deporit(self, amount):
        self.__balance += amount
    
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else: 
            print('Error: Insuffient funds')
        
    def get_balance(self):
        return self.__balance
        
