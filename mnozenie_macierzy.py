import numpy as np

matrix1 = np.random.rand(8, 8)

#test correctness alternative:
#matrix1 = np.ones(shape=(8, 8), dtype=int)

matrix2 = np.random.rand(8, 8)

dot_product_matrices =  matrix1 * matrix2

print('matrix1:\n', matrix1, '\n')
print('matrix2:\n', matrix2, '\n')
print('dot_product_matrices\n', dot_product_matrices, '\n')
