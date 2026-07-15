row1 = int(input("Rows of Matrix A: "))
col1 = int(input("Columns of Matrix A: "))
A = []
print("Enter Matrix A:")
for i in range(row1):
    row = list(map(int, input().split()))
    A.append(row)
row2 = int(input("Rows of Matrix B: "))
col2 = int(input("Columns of Matrix B: "))

B = []
print("Enter Matrix B:")
for i in range(row2):
    row = list(map(int, input().split()))
    B.append(row)

if col1 != row2:
    print("Multiplication not possible")
else:
    result = [[0] * col2 for i in range(row1)]

    for i in range(row1):
        for j in range(col2):
            for k in range(col1):
                result[i][j] += A[i][k] * B[k][j]

    print("Result:")
    for row in result:
        print(row)