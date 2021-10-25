import numpy as np

if __name__ == '__main__':
    print('LU decomposition')
    n = int(input("Enter N: "))
    initial_matrix = np.zeros((n,n),dtype=int)
    np.fill_diagonal(initial_matrix,30)
    # np.diag(initial_matrix)
    diag_16 = np.empty(n-1,dtype=int)
    diag_16.fill(-16)
    indexes_of_diag_16 = np.arange(n-1)
    initial_matrix[indexes_of_diag_16,indexes_of_diag_16+1] = diag_16
    initial_matrix[indexes_of_diag_16+1,indexes_of_diag_16] = diag_16

    diag_1 = np.empty(n-2,dtype=int)
    diag_1.fill(1)
    indexes_of_diag_1 = np.arange(n-2)
    initial_matrix[indexes_of_diag_1,indexes_of_diag_1+2] = diag_1
    initial_matrix[indexes_of_diag_1+2,indexes_of_diag_1] = diag_1




    print(initial_matrix)

