def copy(src_name, dst_name):  # 定义函数copy()，实现任意文件的拷贝操作
    # 以只读字节的方式打开源文件，赋值给变量fr
    # 以写入字节的方式打开源文件，赋值给变量fw
    fr = open(src_name, mode='rb')
    fw = open(dst_name, mode='wb')
    while True:
        data = fr.read(4096)
        if len(data) == 0:
            break
        fw.write(data)
    fr.close()
    fw.close()


