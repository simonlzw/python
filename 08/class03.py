class Role:
    def __init__(self,name,weapon):
        self.name = name
        self.weapon = weapon

    def attack(self,target):
        print("I'm %s,I'm attacking %s" % (self.name,target))

if __name__ == '__main__':
    alice = Role("Alice" , "Wooden Stick")
    print(alice.name , alice.weapon)
    alice.attack("Bob")