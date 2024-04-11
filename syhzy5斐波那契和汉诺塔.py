
""" def F(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return F(n-1)+F(n-2)
s=int(input("请输入想求的斐波那契项数："))
if s<1:
    print("输入格式错误，请输入整数")
else:
    print("数列为：")
    for n in range(1,s+1):
      print(F(n)) """

def hanoi(n,A,B,C):
     if n==1:
          print(A,'-->',C,' ',n)
     else:
          hanoi(n-1,A,C,B)
          print(A,'-->',C,' ',n)
          hanoi(n-1,B,A,C)
hanoi(3,'A','B','C')

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

    
    def bar():
       a=0
       print(a)
       pass
    def main():
    # Todo: Add your code here
       b=10
       print(b)
       pass
    
    if __name__ == '__main__':
       bar()
