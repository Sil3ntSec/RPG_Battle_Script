import random

class Enemy:
    hp = 200

    def __init__(self, atkl, atkh):
        self.atkl = atkl
        self.atkh = atkh


    def getATK(self):
        print("atk is", self.atkl)

    def getHp(self):
        print("Hp is", self.hp)


enemy1 = Enemy(40, 49)
enemy1.getATK()
enemy1.getHp()

enemy2 = Enemy(75, 90)
enemy2.getATK()
enemy2.getHp()
