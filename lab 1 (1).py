# 1
a = int(input())
b = int(input())
print('Sum of the numbers = ',a+b)
print('Difference of numbers =',a-b) 
print('Product of the numbers =',a*b)
print('quoitent of the numbers = ',a/b) 

# 2
a = int(input())
b = int(input())
c = int(input())
d = int(input())
avg = (a+b+c+d)/4
print('Average of the numbers =',avg)

# 3
P = int(input('Enter the Principle Amount in Rupees: '))
R = int(input('Enter the Rate of Interest: '))
T = int(input('Enter Time Period in Years :'))
SI = (P*R*T)/100
print('Simple Interest for the given details is ',SI)

# 4
d = int(input('Enter the distance in km: '))
t = int(input('Enter the time taken in minutes: '))
s = d*60/t
print('Speed is ',s,'km/h.')

# 5
reply = str(input('Do you know the base and height of the Triangle ? yes or no? '))
if reply == 'yes':
    b = float(input('Enter the base of the triangle in metre: '))
    h = float(input('Enter the height of the triangle in metre: '))
    a = 0.5*b*h
    print('Area of the triangle is ',a,'sq m.')
elif reply == 'no':
    x = float(input('Enter 1st side of triangle in m: '))
    y = float(input('enter 2nd side in m: '))
    z = float(input('enter 3rd side in m: '))
    s = (x+y+z)/2
    A = (s*(s-x)*(s-y)*(s-z))**0.5
    print('Area of the triangle is ',A,'sq m.')
else:
    print('please reply yes or no')
    
# 6
a = int(input('enter the cofficient of x^2 :'))
b = int(input('enter the cofficient of x :'))
c = int(input('enter the constant :'))
d = b**2 - 4*a*c
if d < 0:
    print('The roots are not real.')
elif d >= 0:
    r1 = (-b + d**0.5)/(2*a)
    r2 = (-b - d**0.5)/(2*a)
    print('The roots are ',r1,' ',r2,)