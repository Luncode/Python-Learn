#定义函数
def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('只能输入数字')
    if x >=0:
        return x
    else:
        return -x
