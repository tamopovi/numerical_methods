import numpy as np
import math
from pprint import pprint
import scipy.linalg


def getLU(n,matrix):
    identity_matrix = np.identity(n, dtype=int)
    L = identity_matrix
    U = matrix

    for i in range(n):
        for j in range(i+1, n):
            print((i,j))
            pagr = U[i,i]
            taikinys = U[j,i]
            koef = taikinys / pagr
            print("pagr: %d", pagr)
            print("taikinys: %d", taikinys)
            print("koef: %d", koef)
            nauja_eilute_j = U[j] - U[i] * koef
            U[j] = nauja_eilute_j
            L[j,i] = koef
            print("---------------------")

    return (L,U)


if __name__ == '__main__':
    print('LU decomposition')
    n = int(input("Enter N: "))
    initial_matrix = np.zeros((n, n), dtype=int)
    np.fill_diagonal(initial_matrix, 30)
    # np.diag(initial_matrix)
    diag_16 = np.empty(n-1, dtype=int)
    diag_16.fill(-16)
    indexes_of_diag_16 = np.arange(n-1)
    initial_matrix[indexes_of_diag_16, indexes_of_diag_16+1] = diag_16
    initial_matrix[indexes_of_diag_16+1, indexes_of_diag_16] = diag_16

    diag_1 = np.empty(n-2, dtype=int)
    diag_1.fill(1)
    indexes_of_diag_1 = np.arange(n-2)
    initial_matrix[indexes_of_diag_1, indexes_of_diag_1+2] = diag_1
    initial_matrix[indexes_of_diag_1+2, indexes_of_diag_1] = diag_1

    c = 1/math.pow(n+2, 2)

    # print(initial_matrix)

    identity_matrix = np.identity(n, dtype=int)

    ex_matrix = np.array([[2,4,3,5],[-4,-7,-5,-8],[6,8,2,9],[4,9,-2,14]])
    ex_matrix_1 = np.array([[2,4,3,5],[-4,-7,-5,-8],[6,8,2,9],[4,9,-2,14]])
    print(ex_matrix)

    (ex_L,ex_U) = getLU(4,ex_matrix)
    print("L: ")
    print(ex_L)
    print()
    print("U: ")
    print(ex_U)
    print()
    print("ex_matrix_1: ")
    print(ex_matrix_1)
    print()
    print("MATMUL ex: ")
    print(np.matmul(ex_L,ex_U))
    # print(identity_matrix)
    
    # L = identity_matrix


    # for i in range(n-1):
    #     for j in range(i+1, n):
    #         pagr = initial_matrix[i,i]
    #         taikinys = initial_matrix[j,i]
    #         koef = taikinys / pagr
    #         nauja_eilute_j = initial_matrix[j] - initial_matrix[i] * koef
    #         initial_matrix[j] = nauja_eilute_j
    #         L[j,i] = koef




    # U = np.array([])

    # for i in range(0,n):
    #     U[0,i] = initial_matrix[0,i]
    # print(U)



    # a = np.array([1,2,3])
    # b = np.array([10,5,8])
    # c = a - b
    # print(c)

    P, L, U = scipy.linalg.lu(np.round(ex_matrix_1,decimals=3))

    print("A:")
    pprint(ex_matrix_1)

    print("P:")
    pprint(P)

    print("L:")
    pprint(L)

    print("U:")
    pprint(U)
