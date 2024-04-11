#文件的使用方式
tf=open("10.26.txt","rt",encoding="utf-8")
print(tf.readline())
tf.close()

fname=input("请输入要打开的文件名：")
fo=open(fname,"r",encoding="utf-8")
txt=fo.read()
print(txt)
fo.close()

fname=input("请输入要打开的文件名：")
fo=open(fname,"r",encoding="utf-8")
for line in fo.readlines():
   print(line)
fo.close

#函数的应用
def fac(n):
   s=1
   for i in range(1,1+n):
     s*=i
     return s
print(fac(20))

def fac(n,m=1): #m为可变参数，在使用时可以不写默认为1，写了就改变值
   s=1
   for i in range(1,1+n):
     s*=i
     return s//m
#n的阶乘
def fact(n, *b) :
   s = 1
   for i in range(1, n+1):   
      s *= i
   for item in b:
      s *= item
   return s
print(fact(10,3))
#lambda函数，匿名函数
#递归法求阶乘
def fact(n):
 if n == 0 :
  return 1
 else :
  return n*fact(n-1)


