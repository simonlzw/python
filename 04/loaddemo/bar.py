import foo
# foo.py -> __main__ 当模块文件直接执行时，__name__的值为‘__main__’
# bar.py -> foo 当模块被另一个文件导入时，__name__的值就是该模块的名字