import sys
# Take inputs
N, B = map(int, input().split())
A = []
for _ in range(N):
    A.append(list(map(int, sys.stdin.readline().split())))
# Function to multiply two matrices
def mat_multiply(N, A, C):
    result = []
    # Create empty matrix
    for _ in range(N):
        result.append([0] * N)
    # Multiply two matrices
    for i in range(len(A)):
        for j in range(len(C[0])):
            for k in range(len(C)):
                result[i][j] += A[i][k] * C[k][j]
                result[i][j] %= 1000 # take remainder of 1000
    return result
def mat_power(N, A, B):
    if B == 1:
        # Take remainder of 1000
        for i in range(N):
            for j in range(N):
                A[i][j] = A[i][j] % 1000
        return A
    else:
        tmp = mat_power(N, A, B // 2)
        if B % 2 == 0:
            return mat_multiply(N, tmp, tmp)
        else:
            return mat_multiply(N, mat_multiply(N, tmp, tmp), A)
ans = mat_power(N, A, B)
for i in range(N):
    print(*ans[i])


