def matrix(m, n):
    o = []
    for i in range(m):
        row = []
        for j in range(n):
            inp = int(input(f"Enter O[{i}][{j}]"))
            row.append(inp)
        o.append(row)
    return o

# [1, 2, 3], [4, 5, 6], [7, 8, 9]


def Sum(A, B):
    output = []
    for i in range(len(A)):  # number of rows
        row = []
        for j in range(len(A[0])):  # number of columns
            row.append(A[i][j] + B[i][j])
        output.append(row)
    return output


m = int(input("Enter the value of m\n"))
n = int(input("Enter the value of n\n"))

print("Enter the Matrix A")
A = matrix(m, n)
print(A)

print("Enter the Matrix B")
B = matrix(m, n)
print(B)

s = Sum(A, B)
print(s)
