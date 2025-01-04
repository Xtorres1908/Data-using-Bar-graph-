#Here, we are gonna use matplotlib to visualize our bar and time to make it user efficent
#Don't forget to install matplotlib as it is not preinstalled
import matplotlib.pyplot as pl
import time

#This the function we will be using for students results 
def students():
    x=[]
    y=[]
    num = int(input("Enter the number of students: "))
    for i in range(num):
        stu=input("Enter Student name: ")
        mark=int(input("Enter his marks: "))
        x.append(stu)
        y.append(mark)
        time.sleep(1)
    c=[]
    for i in range(len(y)):
        if y[i]>75:
            c.append('green')
        elif y[i]<75 and y[i]>50:
            c.append('yellow')
        else:
            c.append('red')
    label=[]
    for j in range(len(c)):
        if c=='green':
            label.append('Excellent')
        elif c=='yellow':
            label.append('Good')
        else:
            label.append('Needs practice')
        
    pl.xlabel('Students',fontsize=15)
    pl.ylabel('Marks',fontsize=15)
    pl.title("Results(out of 100)",fontsize=30,fontweight="bold",color="r")
    bar = pl.bar(x,y,width=0.3,color=c)
    pl.bar_label(bar,labels=y,label_type='center')
    pl.show()

#This one is for monthly sales
def salesmonth():
    x=[]
    y=[]
    num = int(input("Enter the number of months: "))
    for i in range(num):
        mon=input("Enter the month: ")
        sales=int(input("Enter the sales : "))
        x.append(mon)
        y.append(sales)
        time.sleep(1)
    colors = ['red','blue','green','yellow','black','cyan','pink']
    pl.xlabel('Months',fontsize=15)
    pl.ylabel('Sales',fontsize=15)
    pl.title("Sales Comparison",fontsize=30,fontweight="bold",color="r")
    bar = pl.bar(x,y,width=0.5,color=colors)
    pl.bar_label(bar,labels=y,label_type="center")
    pl.show()

#This one is for yearly sales
def salesyear():
    x=[]
    y=[]
    num = int(input("Enter the number of years: "))
    for i in range(num):
        mon=input("Enter the year: ")
        sales=int(input("Enter the sales : "))
        x.append(mon)
        y.append(sales)
        time.sleep(1)
    colors = ['red','blue','green','yellow','black','cyan','pink']
    pl.xlabel('Years',fontsize=15)
    pl.ylabel('Sales',fontsize=15)
    pl.title("Sales Comparison",fontsize=30,fontweight="bold",color="r")
    bar = pl.bar(x,y,width=0.3,color=colors)
    pl.bar_label(bar,labels=y,label_type="center")
    pl.show()


#Here we will execute the code
print("Hi! I'm here to help you visualise your data in bar fromat")
print("I can help you with the following: ")
print("1.Students results")
print("2.Monthly sales")
print("3.Yearly sales")
choice = int(input("Enter the number of your choice: "))
if choice==1:
    students()
elif choice==2:
    salesmonth()
else:
    salesyear()
print("Thank you!!")