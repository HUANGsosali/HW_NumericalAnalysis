import math 
import matplotlib.pyplot as plt
from sympy import *

#原函数
def func(x):
    return c*math.sin(d*x)+e*math.cos(f*x)

#计算平均误差
def Average_error(origin,inter):
    error = 0.0
    for i in range(m):
        error += inter[i] - origin[i]
    average_error = error / m
    return average_error

#分段线性插值
def PiecewiseLinear(xx):
    case = int ( (xx-a) / ( (b-a)/(n+2) ) )#位于[x[case-1],x[case]]
    if case <= n :
        x1=x[case] - (b-a)/(n+2)
        y1=func(x1)
        x2=x[case]
        y2=func(x2)
    elif case == n+1 :
        x1=x[n]
        y1=func(x1)
        x2=b
        y2=func(x2)
    yP = y1 + (xx-x1) * (y2-y1)/(x2-x1)
    return yP
    
if __name__ == "__main__":
    a = input("请输入插值区间左端点a(default:0)：") or 0
    b = input("请输入插值区间右端点b(default:5)：") or 5
    c = input("请输入函数c*sindx+e*cosfx的参数c(default:1)：") or 1
    d = input("请输入函数c*sindx+e*cosfx的参数d(default:1)：") or 1
    e = input("请输入函数c*sindx+e*cosfx的参数e(default:1)：") or 1
    f = input("请输入函数c*sindx+e*cosfx的参数f(default:1)：") or 1
    n = input("请输入采样点个数(n+1) n(default:10)：") or 10
    m = input("请输入实验点个数m(default:30)：") or 30
    
    #采样点x，y值
    #x = [0 for p in range(n+1)]
    #y = [0 for p in range(n+1)]
    x = [0] * (n+1)
    y = [0] * (n+1)


    for p in range(n+1):
        x[p]= a + (p+1)*(b-a)/(n+2)
        y[p]=  func(x[p])
    
    #测试点上原函数的值
    print("-------------------m个测试点-------------------")
    testpoint_x = [0 for p in range(m)]
    testpoint_y = [0 for p in range(m)]
    for p in range(m):
        testpoint_x[p]= a + (p+1)*(b-a)/(m+1)
        testpoint_y[p]=  func(testpoint_x[p])
    print(testpoint_x)
    print("-------------------测试点对应的函数值-------------------")
    print(testpoint_y)
        
    print("-------------------分段线性插值-------------------")
    PiecewiseLinear_y = [0 for p in range(m)]
    for p in range(m):
        PiecewiseLinear_y[p]= PiecewiseLinear(testpoint_x[p])
    print(PiecewiseLinear_y)
    average_error = Average_error(testpoint_y,PiecewiseLinear_y)
    print("-------------------平均误差为-------------------")
    print(average_error)
        
    #对比原函数与分段线性插值函数
    plt.title("PiecewiseLinear_interpolation")
    plt.plot(testpoint_x,testpoint_y,'b-o',label="original")
    plt.plot(testpoint_x,PiecewiseLinear_y,'r:.',label='PiecewiseLinear')
    plt.xlabel('x')  
    plt.ylabel('y')  
    plt.legend(loc=4)
    plt.show()
        
        