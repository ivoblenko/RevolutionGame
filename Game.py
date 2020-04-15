import sys
from collections import defaultdict

import pygame

from blocks import Block
from game_object import GameObject


class Game:
    def __init__(self, bg, width, height, caption, frame_rate, levels):
        self.width = width
        self.height = height
        pygame.init()
        self.surface = pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN | pygame.DOUBLEBUF)
        #pygame.mouse.set_visible(False)
        self.platform = pygame.image.load('images/block.png').convert()
        self.platform_win = pygame.image.load('images/win.png').convert()
        self.bg = pygame.image.load(bg).convert()
        pygame.display.set_caption(caption)
        self.frame_rate = frame_rate
        self.clock = pygame.time.Clock()
        self.game_over = False
        self.keydown_handlers = defaultdict(list)
        self.keyup_handlers = defaultdict(list)
        self.mouse_handlers = []
        self.objects = []
        self.moving_objects = []
        self.keys = []
        self.roundWin = False
        self.level = None
        self.levelCount = 0
        self.xStart = 0
        self.yStart = 0
        self.levels = levels

    def update(self):
        for o in self.objects:
            if o.type == "Player":
                o.update(self.keys, self.objects)
                self.roundWin = o.PWIN
            else:
                o.update()

    def draw(self):
        for o in self.objects:
            o.draw(self.surface)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                for handler in self.keydown_handlers[event.key]:
                    handler(event.key)
            elif event.type == pygame.KEYUP:
                for handler in self.keyup_handlers[event.key]:
                    handler(event.key)
            elif event.type in (pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEMOTION):
                for handler in self.mouse_handlers:
                    handler(event.type, event.pos)

    def createLevel(self):
        x = 0
        y = 0
        for raw in self.levels:
            for col in raw:
                if col == "1":
                    self.levelCount = int(raw)
                    self.objects.append(Block(x, y, "winBlock", self.platform_win))
                elif col == "s":
                    self.xStart = x
                    self.yStart = y
                elif col == "-":
                    self.objects.append(Block(x, y, "block", self.platform))
                elif col == "c":
                    self.objects.append(GameObject(x, y, 10, 10, "Coin", 0, 0))
                x += 64
            x = 0
            y += 64

    def run(self):
        while not self.game_over:
            if self.roundWin:
                self.startNewRound()
            self.keys = pygame.key.get_pressed()
            self.surface.blit(self.bg, (0, 0))
            self.handle_events()
            # self.move()

            self.update()
            self.draw()

            pygame.display.update()
            self.clock.tick(self.frame_rate)
