# s1 = "Hello World"
# print(s1.startswith('abc')) -> False
# print(s1.startswith('h')) -> False
# print(s1.startswith('H')) -> True
# print(s1.endswith('abc')) -> False
# print(s1.endswith('rld')) -> True

# s2 = "hello world"
# s3 = "HELLO WORLD"
#
# print(s2.islower()) -> True
# print(s3.isupper()) -> True

# s4 = '          Hello World        '
# print(s4,end='#\n')
# print(s4.strip(),end='#\n')
# print(s4.lstrip(),end='#\n')
# print(s4.rstrip(),end='#\n')

# s2 = 'hello world'
# s3 = 'hello.tar.gz'
# print(s2.split())
# print(s3.split('.'))

strlist = ['alice' , 'bob' , 'charlie']
print(','.join(strlist))
print(" ".join(strlist))