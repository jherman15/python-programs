import random
import numpy as np

# Generating a random matrix
a = random.randint(1,25)
matrix = np.random.randint(100, size=(a, a))

# Displaying the generated matrix
print("Matrix is: ")
print(matrix)

# Calculating the determinant of a matrix
det = np.linalg.det(matrix)

# Printing the determinant
print("\nDeterminant of the given " + str(a) + "x" + str(a) + " matrix:")
print(int(det))