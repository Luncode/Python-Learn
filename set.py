print('学习:Python-set')
#创建一个set
s = set([1,2,3,4])
s1 = set ([2,3,4])
#输出相同的数
print(s & s1)
#合并输出
print(s | s1)
#添加
s.add(1)
#删除移除
s.remove(1)
#输出
print(s)


#再议不可变的对象

#可变对象
a = ['c','b','a']
a.sort()
print(a)
#不可变对象
a = 'abc'
print(a.replace('a','A'))
print(a)



#小结
d = {(1,2,3)}
print(d)
#不能运行[]这个只能在list里面使用
#d = {(1,[2,3])}
s1 = set((1,2,3))
print(s1)
#不能运行[]这个只能在list里面使用
#s2 = set((1,[2,3]))
