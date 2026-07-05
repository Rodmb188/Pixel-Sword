from code.Character import Character


class Enemy(Character):

    def update(self):
        self.update_hitboxes()
        self.update_invincibility()