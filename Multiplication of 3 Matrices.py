import numpy as np

A = np.array([[1, 1, 1],
              [2, 2, 2],
              [3, 3, 3]])

B = np.array([[1, 1, 1],
              [2, 2, 2],
              [3, 3, 3]])

C = np.array([[1, 1, 1],
              [2, 2, 2],
              [3, 3, 3]])

# Multiply: (A × B) × C
result = np.matmul(np.matmul(A, B), C)

print("Multiplication of the 3 matrices:")
print(result)
