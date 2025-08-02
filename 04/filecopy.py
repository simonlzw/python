def copy(src_name , dst_name):
    src_file = open(src_name, 'rb')
    dst_file = open(dst_name, 'wb')
    while 1 :
        data = src_file.read(4096)
        if not data :
            break
        dst_file.write(data)
    src_file.close()
    dst_file.close()
