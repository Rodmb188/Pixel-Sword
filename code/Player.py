from code.Character import Character

class Player(Character):

    def update(self):
        self.move()

    def move(self):
        ...

    def attack(self):
        self.sword.attack()

    def change_guard(self, guard):
        self.guard = guard