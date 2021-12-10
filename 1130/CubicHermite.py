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

#分段三次Hermite插值
def CubicHermite(xx):
    yC = 0.0
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
    deriv_y1 = c*d*math.cos(d*x1) - e*f*math.sin(f*x1)
    deriv_y2 = c*d*math.cos(d*x2) - e*f*math.sin(f*x2)
        
    yC = ((xx - x2) / (x1 - x2))**2 * (1 + 2* (xx - x1) / (x2 - x1)) * y1 +\
         ((xx - x1) / (x2 - x1))**2 * (1 + 2 * (xx - x2) / (x1 - x2) )*y2 + \
         ((xx - x2) / (x1 - x2))**2 * (xx - x1) * deriv_y1 + \
         ((xx - x1) / (x2 - x1))**2 * (xx - x2) * deriv_y2
    return yC
    
    
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
        
    
    print("-------------------分段三次Hermite插值-------------------")
    CubicHermite_y = [0 for p in range(m)]
    #Deriv = Deriv()
    for p in range(m):
        CubicHermite_y[p]= CubicHermite(testpoint_x[p])
    print(CubicHermite_y)
    average_error = Average_error(testpoint_y,CubicHermite_y)
    print("-------------------平均误差为-------------------")
    print(average_error)


    #对比原函数与分段三次Hermite插值函数
    plt.title("CubicHermite_interpolation")
    plt.plot(testpoint_x,testpoint_y,'b-o',label="original")#原函数曲线
    plt.plot(testpoint_x,CubicHermite_y,'r:*',label='CubicHermite')#插值曲线
    plt.xlabel('x')  
    plt.ylabel('y')  
    plt.legend(loc=4)#右下角显示图例
    plt.show()
