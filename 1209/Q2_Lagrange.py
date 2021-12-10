import math 
import matplotlib.pyplot as plt
from sympy import *
import numpy
import random


#原函数
def func(x):
    return c*math.sin(d*x)+e*math.cos(f*x)

#计算平均误差
def Average_error(origin,inter):

    error = sum(inter) - sum(origin)
    average_error = error / m
    return average_error
    
#拉格朗日插值
#输入x，返回此处插值函数对应的值
def Lagrange(xx,x,y):
    yL = 0.0
    for i in range(n+1):
        lk =1.0
        for j in range(n+1):
            if i != j:
                # if((x[i] - x[j])==0):
                #     print(i)
                #     print(x[i])
                #     print(x[j])
                lk *=  (xx - x[j]) / (x[i] - x[j])
        yL += y[i] * lk
    return yL

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
    # print(x_c)
    # print(y_c)
        
        
    
    #测试点上原函数的值
    
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

    #print("-------------------随机取样点--拉格朗日插值-------------------")
    Lagrange_y_a = [0 for p in range(m)]
    for p in range(m):
        Lagrange_y_a[p]= Lagrange(testpoint_x[p],x_a,y_a)
    #print(Lagrange_y_a)
    
    #print("------------------切比雪夫多项式零点--拉格朗日插值-------------------")
    Lagrange_y_c = [0 for p in range(m)]
    for p in range(m):
        Lagrange_y_c[p]= Lagrange(testpoint_x[p],x_c,y_c)
    #print(Lagrange_y_c)
    
    
    
    
    print("-------------------随机取样点--平均误差为-------------------")
    average_error = Average_error(testpoint_y,Lagrange_y_a)
    print(average_error)
    
    print("-------------------切比雪夫多项式零点--平均误差为-------------------")
    average_error = Average_error(testpoint_y,Lagrange_y_c)
    print(average_error)
    
    
    
    #对比原函数与拉格朗日插值函数
    plt.title("Lagrange_interpolation")
    plt.plot(testpoint_x,testpoint_y,'b:.',label="original")
    plt.plot(testpoint_x,Lagrange_y_a,'r:',label='Lagrange_random')
    plt.plot(testpoint_x,Lagrange_y_c,'g:.',label='Lagrange_Chebyshev')
    plt.xlabel('x')  
    plt.ylabel('y')  
    plt.legend(loc=4)
    plt.show()
