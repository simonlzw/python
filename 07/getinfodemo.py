def get_info(name,age=20):
    print('%s is %s years old' %(name,age))
# 按照位置传参
get_info("nfx")
get_info("nfx",18)
get_info(18,"nfx")

# 关键字传参，可以不按顺序
get_info(age=18,name="nfx")

# 关键字参数后不能有位置参数
get_info("nfx" , age=20)
# get_info(name="nfx" , 20)   报错

print("hello", "world" ,sep="---",end="!!\n")