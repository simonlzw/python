def get_info(name,age):
    if not 0 < age < 120:
        raise ValueError('Invalid Age (1~119)')
    else:
        print('%s is %s years old' %(name,age))

if __name__ == '__main__' :
    get_info('lzw',25)
    get_info('someone', -1)