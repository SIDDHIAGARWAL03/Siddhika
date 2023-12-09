# 1
i=65
for i in range(65,91):
    print(chr(i))

# 2
x=input("enter the sentance:")
count=0
for a in x:
    count+=1
print(count)

# 3
x=input("enter the sentence:")
print(x.replace(" ","-"))
print(x.title().replace(' ',""))
print(x.lower().replace(' ','_'))

# 4
n=str(input("enter the sentence:"))
m=n[::-1]
if m==n:
    print("no. is pallindrome")
else:
    print("not  pallidrome")

# 5
x=str(input("enter the paragraph:"))
di_count=0
al_count=0
al_count1=0
s_count=0
for i in x:
    if i.islower():
        al_count+=1
    elif i.isupper():
        al_count1+=1
    elif i.isdigit():
        di_count+=1
    else:
        s_count+=0

print("the lower characters are",al_count)
print("the upper characters are",al_count1)
print("the digit characters are",di_count)
print("the special characters are",s_count)

# 6
x=str(input("enter the sentance:"))
y=x.split()
print("orginal",x)
L=len(y)

for i in range(-1,(-L-1),-1):
    print(y[i],end=" ")

# 7
s=str(input("enter the sentnce:"))
t=' '
for i in s:
    if i not in t:
        t=t+i
print(t)

# 8
x=str(input("enter the sentance:"))
word=str(input("enter the words:"))
y=x.split()
p=len(y)
print(p)
count=0
print(y[1])
if word in x:
    # x=x.count(x)
    print("present")
else:
    print("not present")
for i in range(0,p,1):
    if word==y[i]:
        count=count+1
print(count)

# 10
x=input("please enter a hyphen separated sentence:")
b=x.split("-")
s=len(b)
for i in range(s):
    for j in range (0,s-i-1):
        if b[j] > b[j+1]:
           b[j],b[j+1]=b[j+1],b[j]   
Z="-".join(b)
print("sorted sentence",Z)

# 11
count1,count2,count3,count4,count5=0,0,0,0,0
while True:
   X=int(input("enter a number:"))
   if X==-1:
      break
   if X>=1 and X<=10:
      if X>=1 and X<=2:
         count1+=1
      elif X>=3 and X<=4:
         count2+=1
      elif X>=5 and X<=6:
         count3+=1 
      elif X>=7 and X<=8:
         count4+=1
      elif X>=9 and X<=10:
         count5+=1 
total=count1+count2+count3+count4+count5             
print("#"*count1,end=" ") 
print(f"{(count1/total)*100:.2f}%") 
print("#"*count2,end=" ") 
print(f"{(count2/total)*100:.2f}%")  
print("#"*count3,end=" ") 
print(f"{(count3/total)*100:.2f}%")   
print("#"*count4,end=" ") 
print(f"{(count4/total)*100:.2f}%")   
print("#"*count5,end=" ") 
print(f"{(count5/total)*100:.2f}%") 

# 12
N=int(input("enter string")) 
horizontal_line = " +/" +"\/" *(N-2) +"+"
vertical_line = " |" +"  "*(N-2) +" |"

for i in range(N):
        if i == 0 or i == N - 1:
            print(horizontal_line)
        else:
            print(vertical_line)

t=int(input())
count=0
count_1=0
for i in range(t):
    a1,a2,a3,a4,a5,a6,a7=map(int,input().split())
    list=[a1,a2,a3,a4,a5,a6,a7]
    for k in range(7):
        if list[k]==1:
            count=count+1
        elif list[k]==0:
            count_1+=1
    if count>count_1:
        print("yes")
    else:
        print("no")