# 1
n=int(input("the length of the list:"))
l=[]
q=[]
for i in range(n):
    p=int(input("enter the element:"))
    l.append(p)
print(l)
for x in l:
    if x not in q:
        q.append(x)
print(q)

# 2
n=int(input("the length of the list:"))
l=[]
for i in range(n):
    p=int(input("enter the element:"))
    l.append(p)
print(l)
l=set(l)
l=list(l)
print(l)

# 2
#1
n=int(input("enter the length of lists:"))
a=[]
b=[]
c=[]
for i in range(n):
    x=int(input("enter the element of a:"))
    a.append(x)
for i in range(n):
    y=int(input("enter the element of b:"))
    b.append(y)
a=set(a)
b=set(b)
print(a)
print(b)
# #2

print("union",a.union(b))
print("intersection",a.intersection(b))
print("differance",a.difference(b))
print(" symmetric set difference",a^b)
#3
for x in a:
    if x in b:
        c.append(x)
print(c)  
#4
a=list(a)
b=list(b)
c=a+b
c=set(c)
c=list(c)
print(c)

# 3
N = int(input("Enter the value of N: "))
matrix = []
for i in range(N):
    matrix.append(list(map(int, input().split())))
print(f'Matrix: {matrix}')
is_symmetric = all(matrix[i][j] == matrix[j][i] for i in range(N) for j in range(N))
print("Symmetric" if is_symmetric else "Not Symmetric")
principal_diagonal_sum = sum(matrix[i][i] for i in range(N))
non_principal_diagonal_sum = sum(matrix[i][N-i-1] for i in range(N))
print("Sum of Principal Diagonal elements:", principal_diagonal_sum)
print("Sum of Non-Principal Diagonal elements:", non_principal_diagonal_sum)
is_upper_triangular = all(matrix[i][j] == 0 for i in range(1, N) for j in range(i))
is_lower_triangular = all(matrix[i][j] == 0 for i in range(N) for j in range(i+1, N))
print("Upper Triangular" if is_upper_triangular else "Not Upper Triangular")
print("Lower Triangular" if is_lower_triangular else "Not Lower Triangular")
transpose = [[matrix[j][i] for j in range(N)] for i in range(N)]
print("Transpose of the matrix:")
for row in transpose:
    print(' '.join(map(str, row)))

# 4
N = int(input("Enter the value of N: "))
matrix = []
for i in range(N):
    matrix.append(list(map(int, input().split())))
print(f'Matrix: {matrix}')



lead = 0
rowCount = len(matrix)
columnCount = len(matrix[0])

for r in range(rowCount):
    if lead >= columnCount:
        break
    i = r
    while matrix[i][lead] == 0:
        i += 1
        if i == rowCount:
            i = r
            lead += 1
            if columnCount == lead:
                break
    matrix[i], matrix[r] = matrix[r], matrix[i]
    lv = matrix[r][lead]
    matrix[r] = [mrx / float(lv) for mrx in matrix[r]]
    for i in range(rowCount):
        if i != r:
            lv = matrix[i][lead]
            matrix[i] = [iv - lv * rv for rv, iv in zip(matrix[r], matrix[i])]
    lead += 1
