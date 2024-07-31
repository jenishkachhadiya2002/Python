#  Email validation 

# x=(input("enter email = "))
# print(x)
# y="@gmail.com"
# if x==y:
#     print("RIGHT")
# elif x>y:
#     print ("RIGHT")
# elif x<y:
#     print ("RIGHT")

#  else:
#      print("wrong")

import re

# def is_valid_email(email):
#     # Regular expression for validating an email
#     pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
#     if re.match(pattern, email):
#         return True
#     else:
#         return False

# Example usage
email = (input("enter email= "))
if is_valid_email(email):
    print(f"{email} is a valid email address.")
else:
    print(f"{email} is not a valid email address.")
