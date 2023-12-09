# 1
name=input("enter the sentance:")
p=(len(name))
voval="AEIOUaeiou"
count=0
counts=0
x=len(voval)
for i in range(p):
  if name[i]==" ":
    counts+=1
  for k in range(x):
    if name[i]==voval[k]:
      count=count+1
print("vowals:",count)
# print(counts+1)
print("constance:",p-count-counts)
print("total words:",p-counts)

# 2
# 1
n=int(input("ENTER THE NO OF TERMS:"))
sum=0
i=1
while i<=n:
  sum=sum+(1/i)
  i=i+1
print(f"sum of {n} terms is:{sum:.9f}")

# 2
n=int(input("ENTER THE NO OF TERMS:"))
sum=0
fact=1
i=1
while i<=n:
  fact=fact*i
  i+=1
  sum=sum+(1/fact)
print(f"sum of {n} terms is:{sum:.9f}")

#3
n=int(input("ENTER THE NO OF TERMS:"))
x=int(input("enter the vale of x:"))
sum=0
i=1
while i<=n:
  sum=sum+(x**i)/i
  i+=1
print(f"sum of series {n} is:{sum:.9f}")

# 3
n=int(input("enter the no. of terms:"))
i=1
total=0
while i<=n:
    total+=(1/2)**i
    i+=1
print(f"the sum of the series of {n} terms is:{total}")


n=int(input())
x=int(input())
fact=1
sum=1
i=0
for i in range(n):
    fact=fact*(2*n+1)
    a=((-1)**n)*((x)(2*n+1))/(fact)
    sum=sum+a
print(sum)


n=int(input())
x=int(input())
fact=1
sum=0
i=1
for i in range(n):
    fact=fact*(2*n-2)
    a=(-1)*(n-1)*((x)(2*n-2)/(fact))
    sum=sum+a
print(sum)