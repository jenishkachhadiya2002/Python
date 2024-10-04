#  .....ARRAY.....


# from array import *
# value=('u','jenish','hello','demo','world')
# print(value)
# print(type(value))

# from array import *
# number=['i',1,2,3,4,5]
# print(number)
# print(type(number))

# .....BILT.....IN...../.....IN.....BILT.....FUNCTION.....


# print("hello")
# print(len("my name is jenish"))
# x=(int(21))
# print(x)


# .....USER.....DEFIN.....FUNCTION..... 


# def J (j=21,k=82):
#     print(j,k)
# J()

# def jenish(jenu={1:2,"to":34,2.35:12},data={1,23,45,6,7,21.8}):
    # print(jenu,data)
    # print(type(jenu))
    # print(data)
# jenish()


#  .....IF.....ELIF.....ELSE....


# def jojo (k=[1,2,34,5,67,8],j=("jenish","jenu")):
#     if 34 in k:
#         print("Right")
#     else:
#         print("Wrong")
#     if "jenish" not in j:
#         print("True")
#     elif "hello" not in j:
#         print("False")
#     else:
#         print("Error")
# jojo()


#  .....IMPORT.....RANDOM..... 


# import random
# def jenu ():
#     for j in range (1,21,2):
#         print(j)
#         print(type(j))
#     k=random.randrange(1,21)
#     print(k) 
# jenu()

# import random
# x=random.randrange(1,21)
# print(x)


# .....WHILE.....LOOP.....CONTINUE.....BREAK.....


# def jenish():
#    j=1
#    while j<-21:
#       j+=15
#       if j==10:
#          continue
#       print(j)
#    n=1
#    while n<=20:
#          print(n)
#          if n==15:
#             break
#          n+=2
#    s=1
#    while s<21:
#       print(s)
#       s+=1
#    else:
#       print("COMPLETE")
# jenish()


# .....TASK.....


# x= [1,2,3,[4,5,[6,7],8,9],10,11,12]
# print(x[3][2][0])


#....PRINT.....IN.....ONE.....LINE.....


# def jenish():
#               x = 2
#               while x<=10:
#                 print(f'{x}',end='')
#                 x=x+2
# jenish()


# for num in range(1,21):
#     if num % 2 == 0:
#         print(num,"is even",end=',')
#     else:
#         print(num,"is odd",end=',')

# result = [f"{num} is even"   for num in range(1,21) if num % 2 != 0]
# print(result)

# result = [f"{num} is even" for num in range(1,11) if num % 2 == 0]
# print(result)

# num=int(input("enter your number = "))
# print("Even" if num % 2 == 0 else "Odd")
