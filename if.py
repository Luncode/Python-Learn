#定义height的输入
height = input('输入身高，如1.50m：')
#定义weight的输入
weight = input('输入体重，如50kg：')
#定义age的输入
age = input('你的年龄：')
#定义name的输入
name = input('输入你的名字：')
#定义height为float类型
height = float(height)
#定义weight为float类型
weight = float(weight)
#定义age为int类型
age = int(age)
bmi = weight/(height*2)
bmi = int(bmi)
#输出
print('你的名字:',name,'\n你的年龄',age,'\n你的体重是：',weight,'\n你的身高是：',height,'BMI:',bmi)
#if、elif判断
if bmi <= 18.5:
    print('体重过轻')
elif 18.5 < bmi <25:
    print('体重正常')
elif 25< bmi <28:
    print('体重过重')
elif 28< bmi <32:
    print('体重肥胖')
elif bmi > 32:
    print('体重严重肥胖')
