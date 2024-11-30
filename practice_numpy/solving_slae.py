import numpy as np

a = np.array([[1, 4, 2, 0, 0], [0, 0, 1, 1, 1], [0, 3, 0, 1, 1], [1, 0, 1, 0, 1], [0, 5, 5, 0, 5]])
b = np.array([[220], [180], [200], [160], [600]])
 
res = np.linalg.solve(a, b)

A = np.array(
    [[-1, 1, 2], [0, -1, -3], [4, -3, 2]]
)
B = np.array(
    [[1], [-4], [7]]
)

# Function to solve system by math method
def solve_inv_matrix(a, b, verbose=False):
    a_inv = np.linalg.inv(a)
    res = np.array(a_inv).dot(b)
    if not verbose:
        return res
    else:
        print(f'First of all find inverse matrix by using numpy (numpy.linalg.inv(a)) that equal: \n{a_inv}')
        print(f'Than by using mathematical method need to multiply founded inverse matrix to matrix b (numpy.array(a_inv).dot(b))')
        return f'Result: \n{res}'

print(f"Vector of the solving: \r\n {solve_inv_matrix(A, B, True)}")

# Function to solve system by Cramer method
def solve_cramer(a:list, b: list, verbose=False):
    mA, mb = np.copy(a), np.copy(b)
    n = len(mb)
    det_A = np.linalg.det(mA)

    if det_A == 0:
        return None  #Matrix a is degenerated matrix, can't solve it

    x = np.zeros(n)
    for i in range(n):
        Ai = mA.copy()
        for y in range(len(mb)):
            if type(int(Ai[y][i])) == 'int':
                raise ValueError
            else:
                Ai[y][i] = mb[y]
        x[i] = np.linalg.det(Ai) / det_A

    if not verbose:
        return x
    else:
        print('Firstly copy matrixes')
        print(f"Find determinant of matrix a and if it's 0 return None: {det_A}")
        print('Create row vector x which length equal to the length of array b')
        print('In cycle fill row vector, by finding determinant of Ai and diverse it to determinant of matrix A')
        return f'Result: \n{x}'

    
print(f"Vector of the solving: \r\n {solve_cramer(A, B, True)}")