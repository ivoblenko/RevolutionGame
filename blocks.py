from game_object import GameObject


class Block(GameObject):
    def __init__(self, x, y, type, sprite):
        GameObject.__init__(self, x, y, 64, 64, type, sprite, (0, 0))

    def draw(self, surface):
        surface.blit(self.sprites, (self.rect.x, self.rect.y))
