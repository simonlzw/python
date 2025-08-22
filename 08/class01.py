class BearToy:
    """It's a BearToy"""
    def speak(self):
        print("Hello!I'm a "+ self.color + " teddy")

# 创建对象
# bear = BearToy()
# 通过对象的引用调用方法
# bear.speak()

bear01 = BearToy()
bear01.color = "yellow"
bear01.speak()


