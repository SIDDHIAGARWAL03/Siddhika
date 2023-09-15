# 1
l=int(input())
 w=int(input())
print("area of given plot is",l*w)

#2
l=int(input())
 w=int(input())
print("the area of given plot is",l*w*0.3048*0.3048)

#3
x=int(input())
i=0
if(x>0,y>0):
     x%y==0
     print("y is divisible by x")

#4
a=int(input())
if(a%2==0):
    print("a is an even")
else:
    print("a is an odd")

#5
r=50
if(0<r<100):
    print("area of circle is",3.14*r**2)

#6
t=int(input())
print("in fahrenheit",t*1.8+32)
print("in kelvin",t+273.15)

#7
y=int(input("enter the year....----"))
if(y%4==0):
     print("it is an leap year")
else:
     print("it is not a leap year")

#8
r = 7.1 # bank calculates interest on RD accounts at 7.1% p.a.
p = float(input('enter the principle amount in rupees: '))
t = float(input('enter the duration of RD in years: '))
n= t*12
if p<500 or t<0.5:
    print('invalid input.')
else:
    a = p*(1+r/100)*n*t
print('amount is Rs ',a)
print('monthly return is ',a/12)

#9
x = int(input('enter the no. of sec :'))
if x in range(1,86400):
    h= x//3600
    m = x//60 - h*60


    s = x- h*3600- m*60
    print(x,'sec =',h,'hours',m,'min','and',s,'sec.')
else:
    print('enter sec in between 1 and 86400.')