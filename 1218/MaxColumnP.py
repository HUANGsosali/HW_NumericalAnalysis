#列主消元法Elimination with Maximal Column Pivoting
from sympy import *
import scipy.integrate as integrate
from scipy import linalg
import random

def CError(x,stardand_x):
    N = len(x)
    sum = 0
    for i in range (N):
        sum = sum + (x[i] - stardand_x[i]) / stardand_x[i]
    sum = sum /N
    return sum

def MaxColumnP(A,b):
    flag = 1
    N = len(A)
    x = [0] * N

    for k in range(N-1):#最后一行不用
        # print("--------------------------")
        # print(k)
        # 找出第k列最大的元素
        # 它的行数maxIndex
        # 从第k行开始
        maxValue = abs(A[k][k])
        maxIndex = k
        for i in range(k,N):
            if(abs(A[i][k]) > maxValue):
                maxValue = abs(A[i][k])
                maxIndex = i
        
        # 交换第maxIndex行与第k行
        for i in range(N):
            tmp = A[maxIndex][i]
            A[maxIndex][i] = A[k][i]
            A[k][i] = tmp
            
        if A[k][k] == 0:
            flag = 0
            return x,flag
        # print("--------------------------")
        # print(A)

        # 消元
        for i in range(k+1,N): # 对第k+1行到最后一行
            m = A[i][k] / A[k][k]
            for j in range(k,N): # 对第k列到最后一列
                A[i][j] = A[i][j] - A[k][j] * m
            b[i] = b[i] - b[k] * m
        # print("--------------------------")
            
        if A[k][k] == 0:
            flag = 0
            return x,flag
        
        # print(A)
        #print(b)
    # print("-------------开始回代----------------")
    # 回代
    x[N-1] = b[N-1] / A[N-1][N-1]
    for i in range(N-2,-1,-1): # 从倒数第二行开始从下向上迭代
        sum = 0
        for j in range(i+1,N): # 已求得解的项的和
            sum = sum + A[i][j] * x[j]
        x[i] = (b[i] - sum) / A[i][i]


    return x,flag


if __name__ == "__main__":
    
    A = [[31,-13,0,0,0,-10,0,0,0],
         [-13,35,-9,0,-11,0,0,0,0],
         [0,-9,31,-10,0,0,0,0,0],
         [0,0,-10,79,-30,0,0,0,-9],
         [0,0,0,-30,57,-7,0,-5,0],
         [0,0,0,0,-7,47,-30,0,0],
         [0,0,0,0,0,-30,41,0,0],
         [0,0,0,0,-5,0,0,27,-2],
         [0,0,0,-9,0,0,0,-2,29]]

    b = [-15,27,-23,0,-20,12,-7,7,10]
    
    x,flag = MaxColumnP(A,b)
    
    if flag ==0 :
        print("no answer")
    else:
        print("--------------计算得 Ax = b 的解为 :--------------")
        print(x)
        
    print("--------------python库 计算得 Ax = b 的解为 :--------------")
    Sx = linalg.solve(A,b)
    print(Sx)
    
    if flag != 0 :
        print("--------------平均相对误差为 :--------------")
        error = CError(x,Sx)
        print(error)    

    
#//////////////////////////////////////////////////////////////////////////////////

    N = input("输入矩阵阶数 N (default=30):") or 30
    N = int(N)
    A = [[0 for i in range(N)] for j in range(N)]
    b = [0 for i in range(N)]
    for i in range (N):
        for j in range (N):
            A[i][j] = random.randint(-100,100)
        b[i] = random.randint(-100,100)
    print("--------------生成随机矩阵A :--------------")
    print(A)
    print("--------------生成随机向量b :--------------")
    print(b)
    
    x,flag = MaxColumnP(A,b)
    
    if flag == 0:
        print("no answer")
    else:
        print("--------------计算得 Ax = b 的解为 :--------------")
        print(x)
        
    print("--------------python库 计算得 Ax = b 的解为 :--------------")
    Sx = linalg.solve(A,b)
    print(Sx)
    
    if flag != 0 :
        print("--------------平均相对误差为 :--------------")
        error = CError(x,Sx)
        print(error)    
    
    

    