# bitwise operator

# &,|,^
# x=2
# y=8

# print(bin(x))
# print(bin(y))
# print(bin(x&y))
# print(bin(x|y))
# print(bin(x^y))

# x  y  x&y  x|y  x^y 
# 0  0   0    0    0   
# 0  1   0    1    1
# 1  0   0    1    1
# 1  1   1    1    0

#  membership operator

# x="Hello"
# print("H" in x)

# y=[10,20,30,40]
# print(50 not in y )

#  python creator and year 

#  guido van rossum , 1991

#  python latest version 
#   3.12.5


# python total data types and name 
# 8
# int
# float
# str
# list
# tuple
# dict
# sets
# list 
# bool

# after run chnagabel 

# x=[1,2,3]
# print(x)
# print(type(x))

# x.clear()
# print(x)
# x.copy()
# print(x)
# x.pop()
# print(x)
# x.insert()
# print(x)
# x.remove()
# print(x)
# x.reverse()
# print(x)

#  tuple
# not changabel after  randomly print

# x={1,2,3,"hello",21.08,}
# print(x)
# print(type(x))

#  dict

# x={1:[1,2,3,4],2:"hello",3:21.08}
# print(x)
# print(type(x))

#  sets 

# x={1,2,3,4,5,6,7,8,9,10,"hello",21.8,"demo"}
# print(x)
# print(type(x))


# Calculator in Python

# def add(x, y):
#     return x + y

# def subtract(x, y):
#     return x - y

# def multiply(x, y):
#     return x * y

# def divide(x, y):
#     if y == 0:
#         return "Error: Division by zero!"
#     return x / y

# print("Welcome to the calculator!")

# while True:
    # print("\nOperations:")
    # print("1. Addition")
    # print("2. Subtraction")
    # print("3. Multiplication")
    # print("4. Division")
    # print("5. Quit")

    # choice = input("Enter your choice (1/2/3/4/5): ")

    # if choice == "5":
    #     break

    # num1 = float(input("Enter the first number: "))
    # num2 = float(input("Enter the second number: "))

    # if choice == "1":
    #     result = add(num1, num2)
    # elif choice == "2":
    #     result = subtract(num1, num2)
    # elif choice == "3":
    #     result = multiply(num1, num2)
    # elif choice == "4":
    #     result = divide(num1, num2)

    # print(f"\nThe result is: {result}")
