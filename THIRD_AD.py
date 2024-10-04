# lambda Function :

# 'Normal function :'

# def hello(X):
#     return X*3
# print(hello(5))

# python lambda function :


# j=lambda k:(k*3,k+4,k%2)
# print(j(3))

# Multipel Variable in Lambda:


# jenu = lambda a,b,c,d:(a+b,a-c,b*d,c-b)
# print(jenu(1,2,3,4))


# Retrun using lambda Function :


# def jenish (j,k):
#     return lambda l:(l+j,l-k)
# jk=jenish(10,20)
# print(jk(50))


# Multiple value return using lambda function :

# def mydata(Djengo,panda,syntex):
#     return lambda y,h,c: (Djengo+y, panda*h, syntex-c)
# hii = mydata(1.2,1.3,1.4)
# TG = mydata(1,2,3)
# print(TG(1.2,1.3,1.4))
# print(hii(20,30,40))


# def frog(inthepound): 
#     well = [1,2,3,4,5,6,7,8,9,1.0,1.2,"compleate"]
#     for well in range(inthepound,len(well)):
#         print(float(well))
# frog(2)

# Genral question practice :

# x = "My name is hello"
# y = "My name is hello"
# for y in x:
#     print(x[-10:2:-1])
   
# print(x[-10:2:-1],y[-1:9:-1])

# def myfunction(x):
#     y = "my name is hello"
#     print(y[-10:2:-1])
# myfunction("my name is hello") 

# x = "my name is hello"
# y = "my name is hello"

# if x in y:
#     print(x[-10:2:-1])
# elif y not in x:
#     print("error") 
# else:
#     print("Error")

# x = "my name is hello"
# y = x[8:10]
# print(y[::-1])

# user = int(input("Enter your first value :"))
# value = int(input("Enter your second value :"))
# x = user*value
# print(x)

# for i in range(1,11):
#     print(i,end=" ")

# for j in range (0,11,2):
#     print(j)

#  fibonacci series

# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34

# a, b = 0, 1
# n = int(input("enter the numbr:"))
# for i in range(n):
#     print(a)
#     a, b = b, a + b
 
# a, b = 0, 1
# n = int(input("enter the value = "))
# for i in range(n):
#     print(" " * (n - i - 1) * 2, end=' ')
#     for j in range(i - 1):
#         print(a, end='   ')
#         a, b = b, a + b
#     a, b = 0, 1
#     print()

# only pyramid pattern 

# n = 5
# for x in range(n, 0, -1):
#     for y in range(n-x):
#         print(" ", end=" ")
#     for z in range(1, 2*x):
#         print("*", end=" ")
#     print()
 
# n=5
# for x in range (1,n+1):
#     for y in range(n-x):
#         print(" ",end=" ")
#     for z in range(1,2*x):
#         print("*",end=" ")
#     print()

# x = int(input("enter your number :"))

# def Hello(x,y):
#     self = x
#     self = y
#     print(x,y)
# Hello(1,22)
