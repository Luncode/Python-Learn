print('学习:Python-dict')
#定义字典列表
d = {'Bob':95,'Lisa':96,'Luncode':100}
#修改key的值
d['Bob'] = 99
#检查key是否在列表中
print('Lisa' in d)
#输出对应key的value
print(d['Bob'])
#删除列表中的key和value
d.pop('Lisa')
#输出列表
print(d)


#小结
d = {'Michael': 95,'Bob': 75,'Tracy': 85}
print('d[\'Michael\'] =', d['Michael'])
print('d[\'Bob\'] =', d['Bob'])
print('d[\'Tracy\'] =', d['Tracy'])
print('d.get(\'Thomas\', -1) =', d.get('Thomas', -1))
