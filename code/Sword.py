#from code.Const import ATTACK_START, ATTACK_TIME
#
#class Sword:
#
#    def __init__(self, owner):
#
#        self.owner = owner
#
#        self.attacking = False
#
#        self.attack_time = ATTACK_TIME
#
#        self.attack_start = ATTACK_START
#
#        self.hitbox = None

class Sword:

    def __init__(self, owner):
        self.owner = owner

    def attack(self):
        print(f"{self.owner.name} atacou!")