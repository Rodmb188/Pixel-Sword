from abc import ABC

class Entity(ABC):

    def __init__(self, name, image, position):
        self.name = name
        self.image = image

        self.rect = self.image.get_rect()
        self.rect.topleft = position

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)