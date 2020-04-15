from pygame import sprite
from pygame.rect import Rect


class GameObject(sprite.Sprite):
    def __init__(self, x, y, width, height, type, sprites, speed=(0, 0)):
        sprite.Sprite.__init__(self)
        self.rect = Rect(x, y, width, height)
        self.type = type
        self.speed = speed
        self.sprites = sprites

    @property
    def left(self):
        return self.rect.left

    @property
    def right(self):
        return self.rect.right

    @property
    def top(self):
        return self.rect.top

    @property
    def bottom(self):
        return self.rect.bottom

    @property
    def width(self):
        return self.rect.width

    @property
    def height(self):
        return self.rect.height

    @property
    def center(self):
        return self.rect.center

    @property
    def centerx(self):
        return self.rect.centerx

    @property
    def centery(self):
        return self.rect.centery

    def draw(self, surface):
        pass

    def move(self, xvel, yvel):
        self.rect = self.rect.move(xvel, yvel)

    def update(self):
        """"""
        if self.speed == [0, 0]:
            return

        self.move(*self.speed)
