# Encapsulation
# Restricts direct access to certain attributes/methods.
# Provides controlled access via methods (getters and setters).
# Achieved using private attributes (prefix _ or __ to variable names).

# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance  # Private attribute
    
#     def get_balance(self):  # Getter
#         return self.__balance
    
#     def set_balance(self, amount):  # Setter
#         self.__balance = amount

# Sample program to understand Encapsulation
class Account:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute
    
    def deposit(self, amount):
        self.__balance += amount
    
    def get_balance(self):
        return self.__balance

account = Account(1000)
account.deposit(500)
print(account.get_balance())  
