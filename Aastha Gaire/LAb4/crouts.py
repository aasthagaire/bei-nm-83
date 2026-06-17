import numpy as np

# Input matrix A and vector B
A = np.array([
    [2, -1, -2],
    [-4, 6, 3],
    [-4, -2, 8]
], dtype=float)

B = np.array([-2, 9, -5], dtype=float)

n = len(A)

# Initialize L and U
L = np.zeros((n, n))
U = np.eye(n)

# ---------------------------
# LU Decomposition (Crout)
# ---------------------------
for j in range(n):

    # Compute L (Lower Triangular)
    for i in range(j, n):
        sum1 = 0
        for k in range(j):
            sum1 += L[i][k] * U[k][j]
        L[i][j] = A[i][j] - sum1

    # Compute U (Upper Triangular)
    for i in range(j + 1, n):
        sum2 = 0
        for k in range(j):
            sum2 += L[j][k] * U[k][i]
        U[j][i] = (A[j][i] - sum2) / L[j][j]

# ---------------------------
# Display L and U
# ---------------------------
print("Lower Matrix L:")
print(L)

print("\nUpper Matrix U:")
print(U)

# ---------------------------
# Forward Substitution: Ly = B
# ---------------------------
Y = np.zeros(n)

for i in range(n):
    sumy = 0
    for j in range(i):
        sumy += L[i][j] * Y[j]
    Y[i] = (B[i] - sumy) / L[i][i]

# ---------------------------
# Backward Substitution: Ux = Y
# ---------------------------
X = np.zeros(n)

for i in range(n - 1, -1, -1):
    sumx = 0
    for j in range(i + 1, n):
        sumx += U[i][j] * X[j]
    X[i] = Y[i] - sumx

# ---------------------------
# Final Solution
# ---------------------------
print("\nSolution X:")
print(X)

# ---------------------------
# Verification (IMPORTANT)
# ---------------------------
print("\nCheck A * X:")
print(np.dot(A, X))

print("Original B:")
print(B)