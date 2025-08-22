def func_y():
    a = 1
    yield a
    b = "hello"
    yield b
    c = [1 , 2]
    yield c

gen = func_y()
print("gen: " , gen)
print(gen.__next__())
print(gen.__next__())
for item in gen :
    print("for:" , item)

