import config as c
from Game import Game
from GenerateLevel import GenerateLevel
# from Levels import Level
from Player import Player


class Testing(Game):
    def __init__(self):
        Game.__init__(self, c.bg, c.width, c.height, "Testing", 60, c.levels)
        self.score = 0
        self.hero = None
        self.blocks = []
        self.coins = []
        self.enemies = []
        self.generateLevel()
        self.create_objects()

    def add_coin(self):
        self.coins += 1

    def generateLevel(self):
        GL = GenerateLevel(c.width // 64, c.height // 64)
        self.levels = GL.level
        GL.print()
        print(self.levels)

    def create_objects(self):
        self.createLevel()
        self.hero = Player(self.xStart, self.yStart, 29, 40, 5, c.sprites)
        self.objects.append(self.hero)
        self.moving_objects.append(self.hero)


def main():
    Testing().run()


if __name__ == '__main__':
    print(123)
    main()
