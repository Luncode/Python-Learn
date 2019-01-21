#二元一次方程函数

#导入math包
import math

#定义函数quadratic
def quadratic(a,b,c):
    #计算b*b-4ac
    dr = b*b-4*a*c
    #判断dr的值是否大于0
    if dr >= 0:
        #计算值
        s1 = int(-b+math.sqrt(dr))/(2*a)
        s2 = int(-b-math.sqrt(dr))/(2*a)
        #输出
        print('s1 = '"%.2f"%s1,'s2 = '"%.2f"%s2)
    else:
        print('无解')
quadratic(10,20,30)