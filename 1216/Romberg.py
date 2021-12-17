#龙贝格求积公式
import math
import matplotlib.pyplot as plt
from sympy import *
import scipy.integrate as integrate
from scipy import optimize
import sys   
import numpy as np


#原函数
def func(x):
    if x == 0:
        result = 1
    else :
        result = math.sin(x)/(x)
    return result

def Standerd(func,a,b):
    StanderdResult,StanderdRemainder = integrate.quad(func, a, b)
    return StanderdResult,StanderdRemainder

#将区间n次二等分
def trapezoid(a, b, n):

    num = 2**n +1
    x = [0]*num
    y = x
    for i in range(0,num):
        x[i] = a + i * (b-a)/(num-1)
    for i in range (0,num):
        y[i] = func(x[i])
    
    h = (b - a) / (2 * (num-1))
    result = h * ( 2 * np.sum(y) - y[0] - y[n])
    
    return result


#龙贝格求积算法
def Romberg(a, b, eps, max_iter = 30):
    T = [[0 for i in range(max_iter+1)] for j in range(max_iter+1)]
    #T = [[0]*(max_iter)] * (max_iter)


    for k in range(0, max_iter+1):
        for j in range(0,k+1):
            if (j == 0):
                T[k][j] = trapezoid(a, b, k)
            else:
                T[k-j][j] = (4**j / (4**j - 1))*T[k-j+1][j-1] - (1 / (4**j - 1))*T[k-j][j-1]
        if (abs(T[0][k] - T[0][k-1]) < eps):

            return T[0][k]

    return T[0][max_iter]


'''
    for k in range(0, max_iter+1):
        tmp = trapezoid(a, b, k)
        T[k][0] = tmp
        print(T[k][0])
    print (T)

    #每个k对应的不是一行
    for k in range(1, max_iter+1):
        for j in range(1,k+1):
            T[k-j][j] = ( ( 4**j * T[k-j+1][j-1] ) - T[k-j][j-1]  ) / (4**j - 1)
        print (T)
        if (abs(T[0][k] - T[0][k-1]) < eps):
            print("------")
            print(k)
            print(T[0][k])
            print(T[0][k-1])
            return T[0][k],0
'''    

    
    
if __name__ == "__main__":
    a = input("请输入积分区间左端点a(default:0)") or 0
    a = float(a)
    b = input("请输入积分右端点b(default:1)") or 1
    b = float(b)
    eps = input("请输入精度eps(default:0.000001)") or 0.000001
    eps = float(eps)
    # a =  0
    # b =  1
    # eps = 0.000001
    
    result = Romberg(a, b, eps)
    StanderdResult,StanderdRemainder = Standerd(func,a,b)
    error1 = StanderdResult - result

    #print("-----------")
    print("算法积分结果")
    print(result)
    print("标准积分结果")
    print(StanderdResult)
    print("误差")
    print(error1)