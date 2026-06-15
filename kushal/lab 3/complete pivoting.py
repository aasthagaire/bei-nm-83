import numpy as np

A = np.array([
    [2, 1, -1],
    [-3, -1, 2],
    [-2, 1, 2]
], dtype=float)

B = np.array([8, -11, -3], dtype=float)

n = len(B)

col_order = np.arange(n)

print("Initial Augmented Matrix:")
print(np.column_stack((A, B)))

# Forward Elimination with Complete Pivoting
for k in range(n - 1):

    sub_matrix = abs(A[k:, k:])

    row_idx, col_idx = np.unravel_index(
        np.argmax(sub_matrix),
        sub_matrix.shape
    )

    max_row = row_idx + k
    max_col = col_idx + k

    # Row swap
    A[[k, max_row]] = A[[max_row, k]]
    B[[k, max_row]] = B[[max_row, k]]

    # Column swap
    A[:, [k, max_col]] = A[:, [max_col, k]]
    col_order[[k, max_col]] = col_order[[max_col, k]]

    print(f"\nAfter Pivot Step {k+1}:")
    print(np.column_stack((A, B)))

    # Elimination
    for i in range(k + 1, n):

        factor = A[i][k] / A[k][k]

        for j in range(k, n):
            A[i][j] -= factor * A[k][j]

        B[i] -= factor * B[k]

    print(f"\nAfter Elimination Step {k+1}:")
    print(np.column_stack((A, B)))

# Back Substitution
x_temp = np.zeros(n)

for i in range(n - 1, -1, -1):

    sum_ax = 0

    for j in range(i + 1, n):
        sum_ax += A[i][j] * x_temp[j]

    x_temp[i] = (B[i] - sum_ax) / A[i][i]

# Restore original variable order
x = np.zeros(n)

for i in range(n):
    x[col_order[i]] = x_temp[i]

print("\nSolution:")
print(x)