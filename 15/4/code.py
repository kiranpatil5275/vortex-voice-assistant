# from abc import ABC, abstractmethod

# class Payment(ABC):
#     def __init__(self, amount):
#         self.amount = amount

#     @abstractmethod
#     def pay(self):
#         pass


# class CreditCardPayment(Payment):
#     def pay(self):
#         print(f"Payment of ${self.amount} done using Credit Card.")


# class UPIPayment(Payment):
#     def pay(self):
#         print(f"Payment of ${self.amount} done using UPI.")


# credit = CreditCardPayment(500)
# upi = UPIPayment(300)

# credit.pay()
# upi.pay()


# class Emailnotification:
#     def send(self,message):
#         print(f"Email sent : {message}")

# class SMSnotification:
#     def send(self,message):
#         print(f"SMS sent :{message}")

# class Appnotification:
#     def send(self,message):
#         print(f"App notification :{message}")

# #FUNCTION THAT USES DUCK TYPING
# def notify(user_channel,message):
#     user_channel.send(message)     #no type checking

# #-----testing the duck typing system-----

# email = Emailnotification()
# sms = SMSnotification()
# App = Appnotification()

# notify(email,"your order has been shipped!")
# notify(sms,"your OTP is 5566.")
# notify(App,"you have a new message!")



# class account:
#     def __init__(self,balance,name):  
#             self.name="name"
#             self.balance="balance"
    
#     def __str__(self):
#             return f"{self.name}:{self.balance}"
    
#     def __add__(self,other):
#             return self.balance+other.balance
    
#     def __gt__(self,other):
#             return self.balance>other.balance
    
# user1 = account("kiran",3000)
# user2 = account("varun",1000)

# total = user1+user2


# if user1>user2:
#         print("kiran will pay")
    
# else:
#        print("varun will pay")

#        print(total)


# class payment:
#         def pay(self):
#                 print("processing general payment...")

# class cardpayment(payment):
#         def pay(self):
#                 print("processing card payment...")

# class UPIpayment(payment):
#         def pay(self):
#                 print("processing UPI payment...")

# #Testing
# p = payment()
# p.pay()

# c = cardpayment()
# c.pay()

# u = UPIpayment()
# u.pay()



# PYTHON LAB

# import numpy as np
# import pandas as pd
# names = ["list1","list2","list3","list4"]
# array = np.array([150, 250, 350, 450, 550])
# series =pd.Series(array)
# print(series,names)
# a=np.ones([3,3]) 
# b=(["a","b","c"])
# x=(["e","f","g"])
# c= pd.DataFrame(a,b,columns =x)
# print(c)

# df = pd.read_csv("customers-100.csv")

# print(df.head())






