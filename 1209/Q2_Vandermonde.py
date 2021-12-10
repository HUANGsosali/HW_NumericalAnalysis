import math 
import numpy
from scipy import linalg
import matplotlib.pyplot as plt
from sympy import *
import random

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

#范德蒙德插值    
def VandermondeFunc(x,y):
    #系数矩阵
    VA = [[0 for i in range(n+1)] for j in range(n+1)]
    for i in range(n+1):#第k行
        for j in range(n+1):#第l列
            VA[i][j] = pow(x[i],j)
    tmp = numpy.linalg.pinv(VA)#系数矩阵的逆
    Coefficient = numpy.dot(tmp, y)#多项式的系数 
    #print (Coefficient)
    return Coefficient
    
#输入x，返回范德蒙德插值函数的函数值
def Vandermonde(xx,Coefficient):
    yV = 0.0
    for r in range(n+1):
        yV += Coefficient[r]*(pow(xx,r))
    return yV
    
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
    #随机取采样点
    x_a_0 = [0.0] * (n+1)
    y_a = [0] * (n+1)
    x_a_0 = random.sample(range(1, 99999), n+1)
    for p in range(n+1):
        x_a_0[p] = a + (b-a) * 0.00001 * x_a_0[p]
    x_a = numpy.sort(x_a_0)
    for p in range(n+1):
        y_a[p]=  func(x_a[p])
    
    #选取切比雪夫多项式零点作为采样点
    x_c = [0] * (n+1)
    y_c = [0] * (n+1)
    #区间要化为[-1,1]
    for p in range(n+1):
        x_c[p]= ((b+a)/2) + ((b-a)/2)*( math.cos(((2*p+1)*math.pi)/(2*(n+1))) )
        y_c[p]=  func(x_c[p])
    
    
    

    #测试点上原函数的值
    #print("-------------------随机取m个测试点-------------------")
    testpoint_x_0 = [0] * m
    testpoint_y = [0] * m
    testpoint_x_0 = random.sample(range(1, 99999), m)
    for p in range(m):
        testpoint_x_0[p] = a + (b-a) * 0.00001 * testpoint_x_0[p]
    testpoint_x = numpy.sort(testpoint_x_0)
    for p in range(m):
        testpoint_y[p]=  func(testpoint_x[p])
    #print(testpoint_x)
    #print("-------------------测试点对应的函数值-------------------")
    #print(testpoint_y)
    
    #print("-------------------随机取样点--范德蒙德插值-------------------")
    Vandermonde_y_a = [0 for p in range(m)]
    Coefficient_a = VandermondeFunc(x_a,y_a)
    for p in range(m):
        Vandermonde_y_a[p]= Vandermonde(testpoint_x[p],Coefficient_a)
    #print(Vandermonde_y_a)
    
    #print("-------------------切比雪夫多项式零点--范德蒙德插值-------------------")
    Vandermonde_y_c = [0 for p in range(m)]
    Coefficient_c = VandermondeFunc(x_c,y_c)
    for p in range(m):
        Vandermonde_y_c[p]= Vandermonde(testpoint_x[p],Coefficient_c)
    #print(Vandermonde_y_c)
    
    
    print("-------------------随机取样点--平均误差为-------------------")
    average_error_a = Average_error(testpoint_y,Vandermonde_y_a)
    print(average_error_a)
    
    print("-------------------切比雪夫多项式零点--平均误差为-------------------")
    average_error_c = Average_error(testpoint_y,Vandermonde_y_c)
    print(average_error_c)
    
    #对比原函数与范德蒙德插值函数
    plt.title("Vandermonde_interpolation")
    plt.plot(testpoint_x,testpoint_y,'b:.',label="original")
    plt.plot(testpoint_x,Vandermonde_y_a,'r:.',label='Vandermonde_random')
    plt.plot(testpoint_x,Vandermonde_y_c,'g:.',label='Vandermonde_Chebyshev')
    plt.xlabel('x')  
    plt.ylabel('y')  
    plt.legend(loc=4)
    plt.show()
    
