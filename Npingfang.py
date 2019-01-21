#计算平方
#定义一个power的函数
def power(x, n):
    #定义s=1
    s = 1
    #判断n是否大于0，的循环条件
    while n > 0:
        n = n - 1
        s = s * x
    #返回值s
    return s
#power(数值，多少平方的数值)
