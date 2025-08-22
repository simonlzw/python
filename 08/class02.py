class BearToy:
    def __init__(self,color):
        print("Initializing")
        self.color = color
        self.size = "big"

    def speak(self):
        print("Color: " + self.color + " ,Size: " + self.size)

if __name__ == "__main__":
    tidy01 = BearToy("red")
    tidy01.speak()
