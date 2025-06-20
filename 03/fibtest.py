def get_fib() :
    fib = [0, 1]
    n = int(input("Length:"))
    for i in range(n-2) :
        fib.append(fib[-1] + fib[-2])
    print(fib)

# get_fib()
# get_fib()

def get_fib_2() :
    fib = [0, 1]
    n = int(input("Length:"))
    for i in range(n - 2):
        fib.append(fib[-1] + fib[-2])
    return fib

# print(get_fib_2())

def fib(n) :
    fib = [0, 1]
    for i in range(n - 2):
        fib.append(fib[-1] + fib[-2])
    return fib
nlist = [10, 8, 6]
for i in nlist :
    print("fib[" + str(i) + "]=" , end="")
    print(fib(i))