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

#牛顿插值
#得到均差
def get_f_table(x, y):
    i = 0
    f = [0]*(n+1)
    f[0]=y[0]
    while i < n:
        j =  n
        while j > i:
            if i == 0:
                f[j]=((y[j]-y[j-1])/(x[j]-x[j-1]))
            else:
                f[j] = (f[j]-f[j-1])/(x[j]-x[j-1-i])
            j -= 1
        i += 1
    return f;    

#计算x点的插值,输出牛顿插值结果
def Newton(xx,f):
    yN = f[0]
    for i in range(1,n):
        tmp = 1.0
        for j in range(i):
            tmp *= (xx-x[j])
        yN += f[i] * tmp
    return yN
    
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



    print("-------------------牛顿插值-------------------")
    Newton_y = [0 for p in range(m)]
    f = get_f_table(x,y)
    for p in range(m):
        Newton_y[p]= Newton(testpoint_x[p],f)
    print(Newton_y)
    average_error = Average_error(testpoint_y,Newton_y)
    print("-------------------平均误差为-------------------")
    print(average_error)
    
    #对比原函数与牛顿插值函数
    plt.title("Newton_interpolation")
    plt.plot(testpoint_x,testpoint_y,'b-o',label="original")
    plt.plot(testpoint_x,Newton_y,'r:.',label='Newton')
    plt.xlabel('x')  
    plt.ylabel('y')  
    plt.legend(loc=4)
    plt.show()

        
