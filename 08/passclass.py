class Role:
    def __init__(self, name, weapon):
        self.name = name
        self.waepon = weapon

    def show_weapon(self):
        print("Name: %s Weapon: %s" % (self.name, self.waepon))

class Warrior(Role):
    def __init__(self, name, weapon, ride):
        Role.__init__(self, name, weapon)
        self.ride = ride

    def attack(self, target):
        print("%s short-range attack %s by %s" % (self.name, target, self.waepon))

class Mage(Role):
    def attack(self, target):
        print("%s ranged attack %s by %s" % (self.name, target, self.waepon))

if __name__ == '__main__':
    a = Warrior("Alice", "Sword", "Horse")
    b = Mage("Bob", "staff")
    a.show_weapon()
    b.show_weapon()
    a.attack("Charlie")
    b.attack("Diana")
    print(a.ride)