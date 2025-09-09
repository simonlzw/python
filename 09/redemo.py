import re

result01 = re.match(r"\d{3}" , "123aavvfdfgs")
print(result01)
print(result01.group())

# 输出:
# <re.Match object; span=(0, 3), match='123'>
# 123

result02 = re.search(r"\d{3}" , "abc666def456qqq")
print(result02)
print(result02.group())

# 输出:
# <re.Match object; span=(3, 6), match='666'>
# 666

result03 = re.findall(r"\d{3}" , "abc666def456qqq")
print(result03)

# 输出:
# ['666', '456']

result04 = re.finditer(r"\d{3}" , "abc666def456qqq")
for item in result04 :
    print(item)
    print(item.group())

# 输出:
# <re.Match object; span=(3, 6), match='666'>
# 666
# <re.Match object; span=(9, 12), match='456'>
# 456

result05 = re.split(r"-|\.", "hello-tar.gz")
print(result05)

# 输出:
# ['hello', 'tar', 'gz']

result06 = re.sub(r"\d{3}", "benben", "Hi~123, nice to meet you, 456")
print(result06)

# 输出:
# Hi~benben, nice to meet you, benben

patt_obj = re.compile(r"\d{3}")
result07 = patt_obj.search("abc666def456qqq")
print(result07)
print(result07.group())

# 输出:
# <re.Match object; span=(3, 6), match='666'>
# 666

result08 = patt_obj.split("abc123qwer789aaa")
print(result08)

# 输出:
# ['abc', 'qwer', 'aaa']
