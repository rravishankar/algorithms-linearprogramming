# python3

import math
import numpy as np

EPS = 1e-6
PRECISION = 20



def readEquation():
    size = int(input())
    a = []
    b = []
    # print("Size", size)
    for row in range(size):
        line = list(map(float, input().split()))
        # print("Line", line)
        a.append(line[:size])
        # print("a:",a)
        b.append(line[size])
        # print("b:",b)
    return a,b


def swap_row(A_g, b_g, p, max):
    # print("A, b before swapping", A_g, b_g)
    temp = A_g[p]
    A_g[p] = A_g[max]
    A_g[max] = temp
    temp = b_g[p] 
    b_g[p] = b_g[max]
    b_g[max] = temp
    # print("A, b after swapping", A_g, b_g)
    return A_g, b_g


def gaussElim(a, b):
    A_g = a[:]
    b_g = b[:]
    N = len(A_g)
    for p in range(N):
        max = p
        for i in range (p+1, N):
            if math.fabs(A_g[i][p]) > math.fabs(A_g[max][p]):
                max = i
        
        if math.fabs(A_g[max][p]) <= 0.000001:
            raise ValueError
        if max != p:
            A_g, b_g = swap_row(A_g, b_g, p, max)
        for i in range(p+1, N):
            alpha = A_g[i][p]/A_g[p][p]
            b_g[i] -= alpha * b_g[p]
            for j in range (p, N):
                A_g[i][j] -= alpha*A_g[p][j]

    # print("Got A:", A_g)
    # print("Got b:", b_g)        
    solution = [0]*N
    for i in range(N-1,-1,-1):
        # print("Got i:",i)
        sum = 0.0
        for j in range(i+1, N):
            # print("Got j:", j)
            # print("Got A[i][j]:",A_g[i][j])
            # print("Got solution[j]:",solution[j])
            sum += A_g[i][j] * solution[j]
            # print("Got sum:", sum)

        solution[i] = (b_g[i] - sum)/A_g[i][i]
        # print("Setting solution[i] to (b[i] - sum) / A[i][i]:",solution[i])


    return solution



if __name__ == "__main__":
    a,b = readEquation()
    #For below user older readEuqation method
    # equation = [[3.0, 2.0, -4.0, 3.0], [2.0, 3.0, 3.0, 15.0], [5.0, -3, 1.0, 14.0]]
    # print(equation)

    # gaussianElimination(equation)
    answer = gaussElim(a,b)
    # answer = list(np.linalg.solve(a, b))
    for i in answer:
        print (i, end = " ")
    # print(answer)

    exit(0)
