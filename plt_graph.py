import matplotlib.pyplot as plt
import math as m

def f1():
    x = range(-10, 11)
    y = [i for i in x] 
    plt.plot(x,y)
    plt.show()
    
def f2():
		x=range(-10,11)
		y=[i**2 for i in x]
		plt.plot(x,y)
		plt.show()

def f3():
    x=range(-10,11)
    y=[2**i for i in x]
    plt.plot(x,y)
    plt.show()


def f4():
    x=range(-10,11)
    y=[m.sin(i) for i in x]
    plt.plot(x,y)
    plt.show()
    
def f5():
    x=range(-10,11)
    y=[m.cos(i) for i in x]
    plt.plot(x,y)
    plt.show()
    
def f6():
    x=range(-10,11)
    y=[m.exp(i) for i in x]
    plt.plot(x,y)
    plt.show()


ch=0
while (ch!=10):
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    print("Choose Function to Plot : ")
    print("\n1.y=x\n2.y=x^2\n3.y=2^x\n4.y=sin\n5.y=cosx\n6.y=e^x\n10.Exit\n")
    ch=int(input("Enter Choice : "))
    if ch==1:
        f1()
    elif ch==2:
        f2()
    elif ch==3:
        f3()
    elif ch==4:
        f4()
    elif ch==5:
        f5()
    elif ch==6:
        f6()
    elif ch==10:
        print("Exiting...")
        break
    else:
        print("Invalid Choice")
        break
