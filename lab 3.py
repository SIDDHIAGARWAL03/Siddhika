# 1
X=int(input())
Y=int(input())
H=int(input())
print("area of trapezoid is",0.5*(X+Y)*H)

# 2
W=int(input())
H=int(input())
print("BMI is",W/H**2)    

weight in pounds and height in inches
W = float(input("Enter your weight in pounds: "))
H = float(input("Enter your height in inches: "))

Convert to metric units (1 pound = 0.453592 kg, 1 inch = 0.0254 meters)
W = W * 0.453592
H = H * 0.0254
print("BMI IS",W / (H ** 2))

# 3
a=int(input())
b=int(input())
c=int(input())
if (a+b>c , a+c>b , b+c>a):
    print("these sides can form triangle")
else:
    print("these sides cannot form triangle")

# 4
number=int(input("---=")) 
d1=int(input())
d2=int(input())
d3=int(input())
s=d1+d2+d3
if(s%3==0):
    print("s is divisible by 3")
else:
    print("s is not divisible by 3")

# 5 (palindrome number is a number thst remains same when its digits are reversed)
n = int(input('enter a 5 digit no.: '))
a = n//10000
b = n%10000
c = b//1000
d = b%1000
e = d//100
f = d%100
g = f//10
h = f%10
i = h*10000+g*1000+e*100+c*10+a
if n<10000:
    print('not a 5 digit no.')
else:
    print(i)
    if n==i:
        print('the no.',n,' is a palindrome.')
    else:
        print('the no.',n,' is not a palindrome.')

# 6
x = int(input())
y = int(input())
print('The value of x is ',y)
print('The value of y is ',x)

# 7
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
z1 = complex(x1,y1)
z2 = complex(x2,y2)
print('complex no. are ',z1,',',z2)
s = z1 +z2
p = z1*z2
print('The sum of the complex no. is ',s)
print('The product of the complex no. is ',p)

# 11
n = int(input('enter a 3 digit no.: '))
h= n//100
p = n%100
t = p//10
o = p%10
x = h**3 + t**3 + o**3
if n==x:
    print(n,'is a Armstrong no.')
else:
    print(n,'is not a Armstong no.')

# 10
x = int(input('enter num:'))
y = int(input('enter num:'))
z = int(input('enter num;'))
if x>y and x>z:
    print(x)
elif y>z:
    print(y)
else :
    print(z)


    




