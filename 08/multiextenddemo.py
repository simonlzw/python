class A :
    def fun1(self):
        print('A func')

    def fun4(self):
        print('A func')

class B :
    def fun2(self):
        print('B func')

    def fun4(self):
        print('A func')

class C(A, B):
    def fun3(self):
        print('C func')

if __name__ == '__main__':
    c1 = C()
    c1.fun1()   # A func
    c1.fun2()   # B func
    c1.fun3()   # C func
    c1.fun4()   # A func

