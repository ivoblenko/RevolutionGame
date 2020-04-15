import random
import config as c

class GenerateLevel:
    def __init__(self, width, hieght):
        self.width = width
        self.hieght = hieght
        self.maxJumpUp = 2
        self.maxJumpSide = 5
        self.block = "-"
        self.emptySpace = " "
        self.level = [[self.emptySpace for a in range(self.width)] for b in range(self.hieght)]
        self.maxLength = 4
        self.startPosition = "s"
        self.createFloor()
        self.blocksType = [1, 2, 3, 4, 5]
        self.createLevel()
        print(123)

    def createFloor(self):
        for a in range(self.width):
            self.level[13][a] = self.block

    def createLevel(self):
        for a in range(3):
            nowPosY = self.hieght - 1
            nowPosX = random.randint(0, 23)
            nowLen = 0
            while nowPosY - self.maxJumpUp > 0:
                nowBlock = random.choice(self.blocksType)
                x = random.randint(2, self.maxJumpSide)
                y = random.randint(1, self.maxJumpUp)
                direction = random.choice([1, -1])
                if direction > 0 and nowPosX + nowLen + x < self.width or direction < 0 and nowPosX - x < 0:
                    nowPosX += nowLen
                elif nowPosX - x >= 0:
                    x *= direction
                print(nowPosY, " ", nowPosX, " ", x, " ", nowBlock, " ", nowLen)
                for block in range(nowBlock):
                    if nowPosX + x + block >= self.width:
                        break
                    self.level[nowPosY - y][nowPosX + x + block] = self.block
                nowPosY = nowPosY - y
                nowPosX = nowPosX + x
                nowLen = nowBlock - 1


    def print(self):
        print(self.level)

