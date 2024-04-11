def fac(n,m=1):
    s=1
    for i in range(1,n+1):
        s*=i
    return s//m
print(fac(3,1))    
from random import randint


def roll_dice(n=2):
    """
    摇色子
    
    :param n: 色子的个数
    :return: n颗色子点数之和
    """
    total = 0
    for _ in range(n):
        total += randint(1, 6)
    return total


def add(a=0, b=0, c=0):
    return a + b + c


# 如果没有指定参数那么使用默认值摇两颗色子
print(roll_dice())
# 摇三颗色子
print(roll_dice(3))
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
# 传递参数时可以不按照设定的顺序进行传递
print(add(c=50, a=100, b=200))
def foo():
    print('hello, world!')


def foo():
    print('goodbye, world!')
# 下面的代码会输出什么呢？
foo()
def foo():
    pass


def bar():
    pass


# __name__是Python中一个隐含的变量它代表了模块的名字
# 只有被Python解释器直接执行的模块的名字才是__main__
if __name__ == '__main__':
    print('call foo()')
    foo()
    print('call bar()')
    bar()

    def foo():
    b = 'hello'

    def bar():  # Python中可以在函数内部再定义函数
        c = True
        print(a)
        print(b)
        print(c)

    bar()
    # print(c)  # NameError: name 'c' is not defined


if __name__ == '__main__':
    a = 100
    # print(b)  # NameError: name 'b' is not defined
    foo()
#yihoujinliangyongzhezhongxingshi
def main():
    # Todo: Add your code here
    pass


if __name__ == '__main__':
    main()

# 方法1：
nums = input('请输入以逗号间隔的一连串数字：')
spnums = nums.split(',')  # 以空格为分隔符，遇到空格就拆一次，总共对names变量的值拆分两次，那么返回的列表中就有三个元素。
print(spnums)
intspnums = list(map(int, spnums))  # 使用map函数，将spnums列表中的元素映射成指定的int类型，再使用list()将它们转换成列表。
print(intspnums)

# 方法2：考虑使用for循环，将list1按照指定字符切片后返回的列表list2的元素依次取出来，强制转化为int，然后再依次追加到一个空列表list3中并打印出来
list1 = input('请输入以逗号间隔的一连串数字：')
list2 = list1.split(',')
list3 = []
for i in list2:
    i = int(i)
    list3.append(i)
print('未转化为整型：', list2)
print('转化为整型后：', list3)

append函数没有返回值，如果其返回值定义为修改后的新列表的话就可以写成一行了。
append只是列表的一个方法，使用append是添加了列表list的一个对象引用（浅拷贝），
但是“lst.append('Allen')”本身是不指向任何对象的，如果你要对其赋值或者输出，自然也就是空值，python万物皆对象还是要仔细琢磨一下
列表的append方法没有返回值，即def定义体内部没有return关键字
l=input().split()
l.append('Allen')#但是如若让a=l.append('Allen') print（a）是错误的
print(l)

通过输入的多个连续字符串创建列表，以空格间隔，使用insert函数将“Allen”加到列表最前面，输出完整列表。
a=input().split()
a.insert(0,'Allen')#注意此处insert的格式
print(a)
（1）输入
        使用input()函数获取用户输入
（2）创建列表
        使用split函数，对获取到的用户输入，以空格为间隔，创建一个列表
（3）添加到列表最前面
        使用insert函数，将需要添加的内容（字符串'Allen'），添加到列表最前面
        函数用法：需要添加内容的列表.insert(添加的位置，添加的内容)

#删除列表元素：
第一种是大家都在用的pop：虽然不是题目要求的del，但是简单高效
a=input().split()
a.pop_(0)
print(a)
第二种是用remove：这个适用性弱，只能指定某个值进行删除
a=input().split()
a.remove('Baidu')
print(a)
第三种是用--delitem--:
a=input().split()
a.__delitem__(0)
print(a)

#排序
sort 与 sorted 区别：
sort 是应用在 list 上的方法，属于列表的成员方法，sorted 可以对所有可迭代的对象进行排序操作。
list 的 sort 方法返回的是对已经存在的列表进行操作，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。
sort使用方法为ls.sort()，而sorted使用方法为sorted(ls)
使用sort函数对列表降序排序
        旧列表.sort(reverse = True)        
        sort函数用法：
        列表名.sort(reverse = False)  其中，reverse = True 降序， reverse = False 升序（默认）    
#反转
列表.reverse()
#map
s = ''.join(map(str,list1))
# map(函数，可迭代对象，···)
# 函数会作用于map的所有可迭代对象中的每一个元素
# 可迭代对象指的是：列表，元组，字符串等等，由一些元素组成的集合
# map后面的···表示可以有很多个可迭代对象
# map最后返回了一个字符串列表
# 不用map转换成字符串列表，使用join会出错
 
# join方法对字符串进行合并
# 规范：newstr = str.join(iterable)
# 将str字符串作为分隔符插入到iterable字符串列表中（也可以是字符串元组）
# 返回合并后的字符串到newstr
print(s)

#比两个数大小
a,b=input().split()#获取一行输入的数字赋值给 a b
print("True") if int(a)>int(b) else print("False"  )
#三元目式（建议用三行的if #else）
print("True") if int(a)<int(b) else print("False")

#与或非
x与y（and），x或y（or），非x（not），非y

#名字是否在内可以用in
a=input().split(' ')
f=input()
print(f in a)（重点）