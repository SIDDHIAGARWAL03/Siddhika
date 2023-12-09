# 1
k=int(input("enter the arbitrary length:"))
x=[]
for i in range(k):
    p=int(input("enter the element:"))
    x.append(p)
print(x)
y=0
for i in range(k):
  y=y+x[i]
print("sum of all elements:",y)
a=1
for i in range(k):
   a=a*x[i]
print("multiple of all no. is:",a)
# x.sort
v=x[0]
for i in range(0,len(x)):
   v=x[i]
print("maximun element is:",v)

# 2
k=int(input("enter the arbitrary length:"))
x=[]
for i in range(k):
    p=int(input("enter the element:"))
    x.append(p)
print(x)
c=[]
for i in range(k):
    s=min(x)
    c.append(s)
    x.remove(s)
print(c)

# 3
k=int(input("enter the arbitrary length:"))
x=[]
for i in range(k):
    p=int(input("enter the element:"))
    x.append(p)
print(x)
# c=[]
for i in range(k):
    s=min(x)
    x[i].append(s)
    x.remove(s)
print(x)

# 4
R=int(input("enetr the number of rows:"))
C=int(input("enter number of columns:"))
matrix1=[]
for i in range(R):
    row=[]
    for j in range(C):
        x=float(input("enter the number:"))
        row.append(x)
    matrix1.append(row)

matrix2=[]
for i in range(R):
    row=[]
    for j in range(C):
        x=float(input("enter the number:"))
        row.append(x)
    matrix2.append(row)   

sum_matrix=[]
for i in range(R):
    row=[]
    for j in range(C):
        sum=matrix1[i][j]+matrix2[i][j]
        row.append(sum)
    sum_matrix.append(row)

print("Matrix1")
for i in matrix1:
    print(i)

print("Matrix2")
for i in matrix2:
    print(i)

print("Sum Matrix")
for i in sum_matrix:
    print(i)

#2
R1=int(input("enetr the number of rows for 1st matrix:"))
C1=int(input("enter number of columns for 1st matrix:"))
matrix1=[]
for i in range(R1):
    row=[]
    for j in range(C1):
        x=float(input("enter the number:"))
        row.append(x)
    matrix1.append(row)

R2=int(input("enetr the number of rows for 2nd matrix:"))
C2=int(input("enter number of columns for 2nd matrix:"))
matrix2=[]
for i in range(R2):
    row=[]
    for j in range(C2):
        x=float(input("enter the number:"))
        row.append(x)
    matrix2.append(row)   

if C2==R1:
    multiply_matrix=[]
    for i in range(R1):
        row=[]
        for j in range(C2):
            sum=0
            for k in range(C1):
                sum+=matrix1[i][k]*matrix2[k][j]
            row.append(sum)
        multiply_matrix.append(row) 
else:
    print("invalid input ,cannot multiply a matrix with column of 1st != row of 2nd")       

print("Matrix1")
for i in matrix1:
    print(i)

print("Matrix2")
for i in matrix2:
    print(i)

print("multiply Matrix")
for i in multiply_matrix:
    print(i)

# 5
x=input("space seaparated strings:")
y=x.split()
sample_string=input("enter a sample_string:")
count=0
for i in y:
    if i==sample_string:
        count+=1
print(f"count of string that contain {sample_string} as substring",count)  

#2
n=int(input("enter a number of elements:"))
list1=[]
for i in range (n):
    element=float(input("enter the value :"))
    list1.append(element)

#Method1
list2=[]
for i in (list1):
    if i <0:
        list2.append(0)
    else:
        y=i**2
        list2.append(y)
print(list2)

#Method2
list2= [0 if i <0 else i**2 for i in list1]
print(list2)
#3
n=int(input("enter a number of elements:"))
list1=[]
for i in range (n):
    element=float(input("enter the value :"))
    list1.append(element)
list2=[]
for i in list1:
    if i >10 and i <=20:
        y=i**2
        list2.append(y)
    else:
        list2.append(i)
print(list2) 

#4
x=input("space seaparated strings:")
y=x.split()
list2=[]
for i in y:
    if not i [0].istitle():
        list2.append(i.title())
    else:
        list2.append(i)
print(list2)
 
#  6
n = int(input("Enter the number of students: "))
records= []
for i in range(n):
    name = input("Enter student name: ")
    rollno = input("Enter roll number: ")
    marks = int(input("Enter total marks (out of 100) for {}: ".format(name)))
    records.append({'Name','RollNo', 'Marks'})
print('The records are',records)
for student in records:
    print(f"Name: {student['Name']}")
    print(f"Roll No: {student['Roll No']}")
    print(f"Total Marks: {student['Total Marks']}")
    print()



    max_marks_student = records[0]
    for student in records:
        if student["Total Marks"] > max_marks_student["Total Marks"]:
            max_marks_student = student

    print(max_marks_student)



    if max_marks_student:
        print("Student with Maximum Marks:")
        print(f"Name: {max_marks_student['Name']}")
        print(f"Roll No: {max_marks_student['Roll No']}")
        print(f"Total Marks: {max_marks_student['Total Marks']}")
    else:
        print("No student records found.")

#part 2 of the question
for i in range(len(records)):
        rank = 1
        for j in range(len(records)):
            if records[j]["Total Marks"] > records[i]["Total Marks"]:
                rank += 1
        records[i]["Rank"] = rank

    # Display student details in ascending order of ranks
print("Student Details in Ascending Order of Ranks:")
for rank in range(1, len(records) + 1):
    for student in records:
        if student["Rank"] == rank:
            print(f"Rank: {student['Rank']}")
            print(f"Name: {student['Name']}")
            print(f"Roll No: {student['Roll No']}")
            print(f"Total Marks: {student['Total Marks']}")
            print()