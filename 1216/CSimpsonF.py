#复合辛普森求积公式  
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

def func2():
    x = symbols('x')
    result = diff(sin(x)/(x), x, 2)
    return -result

def Standerd(func,a,b):
    StanderdResult,StanderdRemainder = integrate.quad(func, a, b)
    return StanderdResult,StanderdRemainder


def CSimpsonF(a,b,n):
    h = (float)(b-a)/n
    f1 = 0.0
    f2 = 0.0
    for k in range (1,n):
        x = a + k * h
        f1 += 2* func(x)
        #print(f1)
    for k in range (0,n):
        x = a + k * h + h/2
        f2 += 4* func(x)
        #print(f2)
    result = (func(a) + f2 + f1 + func(b)) * (h/6)
    
    
    return result
    
    
if __name__ == "__main__":
    a = input("请输入积分区间左端点a(default:0)") or 0
    a = float(a)
    b = input("请输入积分右端点b(default:1)") or 1
    b = float(b)
    n = input("请输入区间n等分(default:40)") or 40
    n = int(n)
    
    result = CSimpsonF(a,b,n)
    StanderdResult,StanderdRemainder = Standerd(func,a,b)
    error1 = StanderdResult - result
    print("算法积分结果")
    print(result)
    print("标准积分结果")
    print(StanderdResult)
    print("误差")
    print(error1)
