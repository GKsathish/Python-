#import random
#random_integer = random.randint(1, 10)
#print(random_integer)

#  MAP FUNCTION

"""def square(n):
   return n * n
numbers = [1, 2, 3, 4]
result = map(square, numbers)
numbers_square = list(result)
print(numbers_square)

"""
# Filter Function 

"""def is_positive_number(num):
   return num >= 0
  
list_a = [1, -2, 3, -4]
positive_nums = filter(is_positive_number, list_a)
print(list(positive_nums))"""


# Reduce Functions
"""from functools import reduce

def sum_of_num(a, b):
   return a*b

list_a = [1, 2, 3, 4]
sum_of_list = reduce(sum_of_num, list_a)
print(sum_of_list)"""


#exeception 


class BankAccount:
    def __init__(self, account_number):
        self.account_number = str(account_number)
        self.balance = 0

    def get_balance(self):
        return self.balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise ValueError("Insufficient Funds")

    def deposit(self, amount):
        self.balance += amount


def transfer_amount(acc_1, acc_2, amount):  
    try:
        acc_1.withdraw(amount)
        acc_2.deposit(amount)
        return True
    except ValueError as e:
        print(str(e))  
        print(type(e))  
        print(e.args)  
        return False

user_1 = BankAccount("001")
user_2 = BankAccount("002")
user_1.deposit(25)
user_2.deposit(100)

print("User 1 Balance: {}/-".format(user_1.get_balance()))
print("User 2 Balance: {}/-".format(user_2.get_balance()))
print(transfer_amount(user_1, user_2, 50))
print("Transferring 50/- from User 1 to User 2")
print("User 1 Balance: {}/-".format(user_1.get_balance()))
print("User 2 Balance: {}/-".format(user_2.get_balance()))

from datetime import time

time_object = time(11, 34, 56)
print(time_object)
print(time_object.hour)
print(time_object.minute)
print(time_object.second)


from datetime import datetime

date_time_obj = datetime(2018, 11, 28, 10, 15, 26)
print(date_time_obj.year)
print(date_time_obj.month)
print(date_time_obj.hour)
print(date_time_obj.minute)


import datetime

datetime_object = datetime.datetime.now()
print(datetime_object)



from datetime import datetime

date_string = "28 November, 2018"
print(date_string)

date_object = datetime.strptime(date_string, "%d %B, %Y")
print(date_object)


from datetime import timedelta

delta = timedelta(days=365, hours=4)
print(delta)


from datetime import timedelta, datetime
delta = timedelta(days=365)
current_datetime = datetime.now()
print(current_datetime)
next_year_datetime = current_datetime + delta
print(next_year_datetime)


import datetime

dt1 = datetime.datetime(2021, 2, 5)
dt2 = datetime.datetime(2022, 1, 1)
duration = dt2 - dt1
print(duration)
print(type(duration))