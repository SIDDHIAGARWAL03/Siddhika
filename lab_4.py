# 1
n=int(input("enter the postive no.:"))
i=1
while n>0 and i<21:
   p=n*i
   print(n,"*",i,"=",p)
   i=i+1

# 2
X=int(input("enter the smaller no.:"))
Y=int(input("enter the larger no.:"))
N=int(input("enter the no.:"))
i=X+1
while  i<=Y:
  p=(i)%N
  if p==0:
    print(i)
  i=i+1
else:
  print("Enter the valid number" )
    
    # 3
n=int(input("enter the no.:"))
sum=0
while (n!=0):
  once=n%10
  n=n//10
  sum=sum+once
print("sum of digits is",sum)

# 4
N=int(input("Enter the positive no."))
count=0
count_1=0
p=1
while N!=-999 and p!=-999:
  p=int(input("enter the positive number:"))
  q=p%N
  if q==0:
    count=count+1
  else:
    count_1=count_1+1
print(count)
print(count_1)

# 5
n=int(input("enter the number:"))
i=1
fact=1
while i<=n and n>1:
  fact=fact*i
  i=i+1
print(fact)
if n==0:
  print(1)
elif n<0:
  print("enter the valid nnumber")

# 6
n=(input("enter the number:"))
r=len(n)
p=int(n)
# while (p>0):
for i in range(1,r+1):
  if n[i]==n[r-i-1]:
    print("number is pelindrome")
    break
  else:
    print("number is not pelindrome")
    break
left=0
right=r-1
while left<right:
  if n[left]==n[right]:
    print("palidrome")
    left=left+1
    right-=r-1
  else:
    print("not palidrome")

# 7
N=int(input("enter the number of terms:"))
a=1
b=1
print(a,b,end=" ")
i=0
while i<(N-2):
  c=a+b
  print(c,end=" ")
  a=b
  b=c
  i=i+1

# 8
n=int(input("enter the number:"))
i=2
if n==0 or n==1:
    print("number neither prime nor not prime")
while (i<n and n>=0):
    if n%i==0:
        print("not a prime no.")
        break
        i=i+1
    else:
        print("prime no")
        break
else:
    print("enter the valid number")

# 9
sent=input("enter the sentence:")
i=0
capital,lower,digit,char=0,0,0,0
while i<len(sent):
  if sent[i]>= 'A' and sent[i]<='Z':
    capital=capital+1
  elif ord(sent[i])>=48 and ord(sent[i])<=57:
    digit=digit+1
  elif ord(sent[i])>=97 and ord(sent[i])<=122:
    lower=lower+1
  i=i+1

print("capital letter",capital)
print("lower letters",lower)
print("digits",digit)
print("character letters",char)

# 10
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))
if a==0:
    print("Invalid input. Please enter valid numerical coefficients of a .")
d = b**2 - 4*a*c
if d > 0:
    x1 = (-b + math.sqrt(d)) / (2*a)
    x2 = (-b - math.sqrt(d)) / (2*a)
    print(f"Solutions: x1 = {x1:.2f}, x2 = {x2:.2f}")
elif d == 0:
    x1 = -b / (2*a)
    print(f"Solution: x1 = {x1:.2f}")
else:
    print("No real solutions. The solutions are complex.") 