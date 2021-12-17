#复合梯形公式
import math
import matplotlib.pyplot as plt
from sympy import *
import scipy.integrate as integrate
from scipy import optimize


#原函数
def func(x):
    if x == 0:
        x = 0.00000001
    result = math.sin(x)/(x)
    return result



def Standerd(func,a,b):
    StanderdResult,StanderdRemainder = integrate.quad(func, a, b)
    return StanderdResult,StanderdRemainder

def CTrapezoidalF(a,b,n):
    h = (float)(b-a)/n
    fk0 = 0.0
    for k in range (1,n):
        x = a + k * h
        fk0 += 2* func(x)
        #print(fk0)
    result = (func(a) + fk0 + func(b)) * (h/2)
    f2=0
    #f2 = optimize.fminbound(func2, a, b)
    return result


    
    
if __name__ == "__main__":
    a = input("请输入积分区间左端点a(default:0)") or 0
    a = float(a)
    b = input("请输入积分右端点b(default:1)") or 1
    b = float(b)
    n = input("请输入区间n等分(default:40)") or 40
    n = int(n)

    # a =  0
    # b =  1
    # n =  50
    
    result = CTrapezoidalF(a,b,n)
    StanderdResult,StanderdRemainder = Standerd(func,a,b)
    error1 = StanderdResult - result
    print("算法积分结果")
    print(result)
    print("标准积分结果")
    print(StanderdResult)
    print("误差")
    print(error1)
