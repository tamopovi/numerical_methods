import numpy as np
from pprint import pprint
import scipy.linalg


if __name__ == '__main__':
    n = int(input("Enter N: "))
    A = np.random.randint(-5,5, size=(n,n))

    X_spr = np.ones(n,dtype=int)

    print("A:")
    print(A)
    print()

    print("Pradinis X_spr:")
    print(X_spr)
    print()

    print(scipy.linalg.solve(A,X_spr))

    X = np.zeros((n,1))

    print(X)