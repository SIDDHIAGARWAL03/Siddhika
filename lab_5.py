# 1
N=int(input("enter the number:"))
p=1
while p<(N+1):
  i=1
  while i<=20:
    q=p*i
    print(p,"*",i,"=",q)
    i=i+1
  p+=1

#   2
N=int(input("enter the number:"))
i=0
while i<1000:
  i=i+1
  if i%N==0:
    continue
  print(i)

#   3
N=int(input("enter the number of lines:"))
i=1
while i<=N:
  p=0
  while p<i:
    print("*",end=" ")
    p=p+1
  i=i+1
  print()


i=1
while i<=N:
  k=N
  while (k>=i and k<=N) :
    print(" ",end=" ")
    k=k-1
  j=1
  while j<=i:
    print("*",end=" ")
    j=j+1
  print()
  i=i+1

i=1
while i<=N:
  k=N
  while k>i and k<=N:
    print(" ",end=" ")
    k=k-1
  p=1
  while p<=i:
    print("*",end=" ")
    p=p+1
  m=i-1
  while m>0 and m<=(i-1):
    print("*",end=" ")
    m=m-1
  i=i+1
  print()
  
#   4
N=int(input("Enter the positive no."))
p=1
count=0
count_1=0
while N!=-999 and p!=-999:
    p=int(input("enter the positive number:"))
    q=p%N
    if q==0:
        count=count+1
    else:
        count_1=count_1+1
print("no of divisible no.:",count)
print("no of non-divisible no.:",count_1)

# 5
a=int(input('enter the number:'))
b=int(input("enter the number:"))
num = 1
while True:
  if (num % a == 0) and (num % b == 0):
    break
  num = num + 1
print(num)

# 6
x = int(input("Insert first number: "))
y = int(input("Insert second number: "))
while x != 0 and y != 0:
 if x > y:
  x %= y
 else:
  y %= x
GCD = x + y
print("The greatest common divisor = ",GCD)

# 7
N=int(input('enter the no. of lines:'))
i=1
while i<=N:
  p=N 
  while p>i and p<=N:
    print("",end=" ")
    p=p-1
  k=1
  while k<=i :
    print("*",end=" ")
    k=k+1
  i=i+1
  print()