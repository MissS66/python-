#求各位数字和
num=input("请输入一个自然数")
#map(int, num) 将将输入的字符串转换为整数，并返回一个迭代器
print(sum(map(int,num)))
#交集
#eval() 是一个内置函数，用于将字符串作为表达式进行求值。
setA=eval(input("请输入一个集合："))
setB=eval(input("请输入一个集合："))
print("交集：",setA&setB)
#并集
print('并集：',setA|setB)
#差集
print(setA-setB)
#进制表示
numm=int(input('请输入一个自然数：'))
print('二进制：',bin(numm))
print('八进制：',oct(numm))
print('十六进制：',hex(numm))
#取偶数列表

#字典结合两个列表为键与值（总数取决于最少的列表）

#降序排列表

#列表整数连乘