import sys


def argstest(args) :
    print(args)

argstest("你好")
# 与 shell 脚本类似，程序名以及参数都以位置参数的方式传递给 python 程序，使用 sys 模块的 argv 列表接收

def sysargtest() :
    print(sys.argv[0])
    print(sys.argv[1])

sysargtest()

# (.venv) PS D:\python> python .\03\argsdemo.py 100
# 你好
# .\03\argsdemo.py
# 100


