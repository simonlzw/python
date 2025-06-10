# fr = open("test.txt" , mode="r")
# # print(fr.read(5))
# # print(fr.read(6))
#
# print(fr.readline() , end="")
# print(fr.readline() , end="?")
# fr.close()

# rd = open("/python/README.md" , mode="r")
# print(rd.read())

fr = open("test.txt" , mode="r")
while True:  # 死循环
    data = fr.readline()  # 某一行数据
    if len(data) == 0:  # 文件读取完毕,终止循环
        break
    print("data:", data, end="")
fr.close()

print("\n---------------------------------------------")

fr = open("test.txt" , mode="r")

# 和for连用
# data = fr2.readlines()
# print("data:", data)
# print(data[0])  # 第一行
# print(data[1])  # 第二行
for item in fr:  # 相当于：for item in fr.readlines():
    print(item, end="")
fr.close()