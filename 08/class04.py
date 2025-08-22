class Weapon:
    def __init__(self, wname, strength):
        self.wname = wname
        self.strength = strength

class Role:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

if __name__ == '__main__':
    ws = Weapon("Wooden stick", 1)
    alice = Role("alice" , ws)
    print(ws.wname, ws.strength)
    print(alice.weapon.wname, alice.weapon.strength)
        