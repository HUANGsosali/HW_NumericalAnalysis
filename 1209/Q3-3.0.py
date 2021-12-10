# 输入参数区间[a,b]，参数c,d,e,f作为标准函数f(x)=c*sindx+e*cosfx，参数n+1作为采样点的个数，参数m作为实验点的个数

# 利用最小二乘法进行曲线拟合，利用m个实验点求出误差。

# 对Y加一点扰动，观察拟合曲线的变化

#ordinary least squares


import math 
import numpy
from scipy import linalg
import matplotlib.pyplot as plt
from sympy import *
import random


#原函数
def func(x):
    #return 3*x
    return c*math.sin(d*x)+e*math.cos(f*x)

#计算平均误差
def Average_error(origin,inter):
    error = 0.0
    for i in range(m):
        error += inter[i] - origin[i]
    average_error = error / m
    return average_error

def func_OLS(x,mm,alpha,beta,a_asterisk):
    output = 0
    for i in range(mm+1):
        output += a_asterisk[i] * Px(x,i,alpha,beta)

    return output

#计算多项式Pk(x)的值
def Px(x,k,alpha,beta):
    if k == 0 :
        output = 1
    elif k == 1 :
        output = Px(x,k-1,alpha,beta) * (x - alpha[k])
    else :
        output = Px(x,k-1,alpha,beta) * (x - alpha[k]) - Px(x,k-2,alpha,beta) * beta[k-1]
    return output


def Alpha_Beta(x_ori,y_ori,n,mm):
    alpha = [0] * (mm+1)
    beta = [0] * mm
    a_asterisk = [0] * (mm+1) #系数
    #计算alpha[1]
    numerator = 0 
    denominator = 0 
    numerator_aa = 0 
    denominator_aa = 0 
    for i in range(n+1):
        numerator += Px(x_ori[i],0,alpha,beta) * Px(x_ori[i],0,alpha,beta) * x_ori[i]
        denominator += Px(x_ori[i],0,alpha,beta) * Px(x_ori[i],0,alpha,beta)
        numerator_aa += Px(x_ori[i],0,alpha,beta) * y_ori[i]
        denominator_aa += Px(x_ori[i],0,alpha,beta) * Px(x_ori[i],0,alpha,beta)
    alpha[1] = numerator / denominator
    a_asterisk[0] = numerator_aa / denominator_aa
    for k in range (1,mm):
        numerator_a = 0 
        denominator_a = 0 
        numerator_b = 0 
        denominator_b = 0 
        numerator_aaa = 0 
        denominator_aaa = 0 
        for i in range(n+1):
            numerator_a += Px(x_ori[i],k,alpha,beta) * Px(x_ori[i],k,alpha,beta) * x_ori[i]
            denominator_a += Px(x_ori[i],k,alpha,beta) * Px(x_ori[i],k,alpha,beta)
            numerator_b = denominator_a
            denominator_b += Px(x_ori[i],k-1,alpha,beta) * Px(x_ori[i],k-1,alpha,beta)
            numerator_aaa += Px(x_ori[i],k,alpha,beta) * y_ori[i]
            denominator_aaa += Px(x_ori[i],k,alpha,beta) * Px(x_ori[i],k,alpha,beta)
        alpha[k+1] = numerator_a / denominator_a
        beta[k] = numerator_b / denominator_b
        a_asterisk[k] = numerator_aaa / denominator_aaa

    return alpha,beta,a_asterisk

    
    
    
if __name__ == "__main__":  
    a = input("请输入区间左端点a(default:-5)：") or -5
    b = input("请输入区间右端点b(default:5)：") or 5
    c = input("请输入函数c*sindx+e*cosfx的参数c(default:1)：") or 1
    d = input("请输入函数c*sindx+e*cosfx的参数d(default:1)：") or 1
    e = input("请输入函数c*sindx+e*cosfx的参数e(default:1)：") or 1
    f = input("请输入函数c*sindx+e*cosfx的参数f(default:1)：") or 1
    n = input("请输入采样点个数(n+1) n(default:10)：") or 15
    m = input("请输入实验点个数m(default:30)：") or 30
    mm = input("请输入拟合曲线次数mm(default:6)") or 6


    #采样点x，y值
    #随机取采样点
    x_a_0 = [0.0] * (n+1)
    y_a = [0.0] * (n+1)
    x_a_0 = random.sample(range(1, 99999), n+1)
    for p in range(n+1):
        x_a_0[p] = a + (b-a) * 0.00001 * x_a_0[p]
    x_a = numpy.sort(x_a_0)
    for p in range(n+1):
        y_a[p]=  func(x_a[p])#+random.uniform(-1,1)

    

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
    #print("-------------------测试点对应的原函数函数值-------------------")
    #print(testpoint_y)
    
    
    #print("------------------最小二乘法-----------------------")
    alpha = [0] * (mm+1)
    beta = [0] * mm
    a_asterisk = [0] * (mm+1) #系数
    
    alpha,beta,a_asterisk = Alpha_Beta(x_a,y_a,n,mm)
    
    #print("-------------------测试点对应的拟合函数函数值-------------------")
    testpoint_y_ols = [0.0] * m
    for p in range(m):
        testpoint_y_ols[p]=  func_OLS(testpoint_x[p],mm,alpha,beta,a_asterisk)
        
        
        
        
    #print("------------------最小二乘法--加一点扰动---------------------")
    y_a[13] = -2
    alpha,beta,a_asterisk = Alpha_Beta(x_a,y_a,n,mm)
    
    testpoint_y_ols_s = [0.0] * m
    for p in range(m):
        testpoint_y_ols_s[p]=  func_OLS(testpoint_x[p],mm,alpha,beta,a_asterisk)
    # print("testpoint_y_ols_s=")    
    # print(testpoint_y_ols_s)
    
    
    print("-------------------无扰动时平均误差为-------------------")
    average_error_a = Average_error(testpoint_y,testpoint_y_ols)
    print(average_error_a)
    
   
    #对比原函数与范德蒙德插值函数
    plt.title("Ordinary Least Squares")
    plt.plot(x_a,y_a,'y:.',label="original")
    plt.plot(testpoint_x,testpoint_y,'b:.',label="test")
    plt.plot(testpoint_x,testpoint_y_ols,'r:.',label='OLS')
    plt.plot(testpoint_x,testpoint_y_ols_s,'g:.',label='OLS_s')
    plt.plot(x_a[13],y_a[13],'g-s') 
    plt.xlabel('x')  
    plt.ylabel('y')  
    plt.legend(loc=4)
    plt.show()
    
