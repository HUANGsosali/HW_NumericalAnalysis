#LU分解法
from sympy import *
from scipy import linalg
import numpy as np
import random

def CError(x,stardand_x):
    N = len(x)
    sum = 0
    for i in range (N):
        sum = sum + (x[i] - stardand_x[i]) / stardand_x[i]
    sum = sum /N
    return sum
        

def LU(A,b):
    N = len(A)
    x = [0] * N
    y = [0] * N
    
    L = np.zeros([N,N])
    U = np.zeros([N,N])

    #第一行与第一列
    for i in range(0,N):
        U[0][i] = A[0][i]
    for i in range(1,N):
        L[i][0] = A[i][0] / U[0][0]


    for r in range(1,N):
        #u的第r行
        for i in range (r,N):
            sum = 0
            for k in range(0,r):
                sum = sum + L[r][k] * U[k][i]
            U[r][i] = A[r][i] - sum
        #l的第r列
        for i in range (r+1,N):
            sum = 0
            for k in range(0,r):
                sum = sum + L[i][k] * U[k][r]
            L[i][r] = (A[i][r] - sum) / U[r][r]
            
    #print(L)
    #print(U)
                
    y[0] = b[0]
    for i in range(1,N):
        sum = 0
        for k in range (0,i):
            sum = sum + L[i][k] * y[k]
        y[i] = b[i] - sum
    #print (y)
    
    x[N-1] = y[N-1] / U[N-1][N-1]
    for i in range(N-2,-1,-1):
        sum = 0
        for k in range (i,N):
            sum = sum + U[i][k] * x[k]
        x[i] = ( y[i] - sum ) / U[i][i]
            
    return x


if __name__ == "__main__":
    
    A = [[30,33,-43,-11,-38,-29,37,28,23] ,
         [-480,-523,644,128,621,480,-618,-489,-329],
         [60,266,-1862,-1991,464,546,-968,-1567,1652],
         [540,624,-782,290,-893,123,567,5,-122],
         [-450,-675,2245,2326,-1512,1230,-822,129,-189],
         [-300,-120,-1114,-1295,1946,302,-376,-1540,-609],
         [1080,998,508,2460,-1628,-1358,2896,2828,-2002],
         [-1080,-1408,3340,2267,21,-1202,866,-2690,-1351],
         [-300,-435,1594,1685,340,2279,-27,2917,-2336]
         ]

    b = [188,-3145,-4990,580,7845,1876,9712,-11599,10127]
    
    # A = [[1,2,3] ,[2,5,2],[3,1,5]]
    # b = [14,18,20]
    # y = [14,-10,-27]
    # x = [1,2,3]
    
    print("--------------计算得 Ax = b 的解为 :--------------")
    x = LU(A,b)
    print(x)
    
    print("--------------python库 计算得 Ax = b 的解为 :--------------")
    Sx = linalg.solve(A,b)
    print(Sx)
    
    print("--------------平均相对误差为 :--------------")
    error = CError(x,Sx)
    print(error)    
    
    
#//////////////////////////////////////////////////////////////////////////////////
    N = input("输入矩阵阶数 N (default=30):")or 30
    N = int(N)
    A = [[0 for i in range(N)] for j in range(N)]
    b = [0 for i in range(N)]
    for i in range (N):
        for j in range (N):
            A[i][j] = random.randint(-10000,10000)
        b[i] = random.randint(-10000,10000)
    print("--------------生成随机矩阵A :--------------")
    print(A)
    print("--------------生成随机向量b :--------------")
    print(b)
    
    print("--------------计算得 Ax = b 的解为 :--------------")
    x = LU(A,b)
    print(x)
    
    print("--------------python库 计算得 Ax = b 的解为 :--------------")
    Sx = linalg.solve(A,b)
    print(Sx)
    
    print("--------------平均相对误差为 :--------------")
    error = CError(x,Sx)
    print(error)
    
    

    