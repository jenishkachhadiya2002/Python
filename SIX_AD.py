#  Polymorphism

class jenish:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def A(self):
        print("hello jenish")

class jjjjj:
    def __init__(self,t,o) :
        self.t=t
        self.o=o
    def A(self):
        print("hello world")

class kkkkk:
    def __init__(self,m,n):
        self.m=m
        self.n=n
    
    def A(self):
        print("hello demo")


jenish1=jenish("hello","jk")
jjjjj1=jjjjj("design","haiiiii")
kkkkk1=kkkkk("toyota","bmw")

for x in (jenish1,jjjjj1,kkkkk1):
    x.A()
