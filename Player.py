import sys

import pygame
from pygame import sprite
from pygame.rect import Rect

from game_object import GameObject

playerWalkRight = [pygame.image.load('images/player_walk1.png'), pygame.image.load('images/player_walk2.png'),
                   pygame.image.load('images/player_walk1.png'), pygame.image.load('images/player_walk2.png'),
                   pygame.image.load('images/player_walk1.png'), pygame.image.load('images/player_walk2.png')]
playerWalkLeft = [pygame.image.load('images/player_walkLeft1.png'), pygame.image.load('images/player_walkLeft2.png'),
                  pygame.image.load('images/player_walkLeft1.png'), pygame.image.load('images/player_walkLeft2.png'),
                  pygame.image.load('images/player_walkLeft1.png'), pygame.image.load('images/player_walkLeft2.png')]

playerJump = pygame.image.load('images/player_jump.png')
playerJumpLeft = pygame.image.load('images/player_jumpLeft.png')
playerFall = pygame.image.load('images/player_fall.png')
playerFallLeft = pygame.image.load('images/player_fallLeft.png')
playerStand = pygame.image.load('images/player_stand.png')


class Player(GameObject):
    def __init__(self, xStart, yStart, width, height, speed, sprites):
        GameObject.__init__(self, xStart, yStart, width, height, "Player", sprites, speed)
        self.xvel = 0
        self.yvel = 0
        self.moving_power = 5
        self.isJump = False
        self.fall = False
        self.jumpPower = 10
        self.moving_right = False
        self.moving_left = False
        self.lastMove = "right"
        self.animCount = 0
        self.onGround = True
        self.gravity = 0.6
        self.PWIN = False
        self.sprite_jump = False

    def handle(self, keys):
        if keys[pygame.K_ESCAPE]:
            sys.exit()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.moving_left = True
            self.moving_right = False
            self.lastMove = "left"
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.moving_right = True
            self.moving_left = False
            self.lastMove = "right"
        else:
            self.moving_right = False
            self.moving_left = False
            self.animCount = 0

        if keys[pygame.K_UP]:
            if self.onGround:
                self.isJump = True
                self.sprite_jump = True

        if not self.onGround:
            self.isJump = False
            if self.yvel > 1.3:
                self.fall = True
            elif self.yvel >= 0:
                self.fall = False
                self.sprite_jump = False

        self.onGround = False

    def collisions(self, objects, xvel, yvel):
        for o in objects:
            if o.type == "Player":
                continue
            if sprite.collide_rect(self, o):
                if o.type == "winBlock":
                    self.PWIN = True
                if xvel < 0:
                    self.rect.left = o.rect.right
                if xvel > 0:
                    self.rect.right = o.rect.left
                if yvel > 0:
                    self.rect.bottom = o.rect.top
                    self.onGround = True
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = o.rect.bottom
                    self.yvel = 0

    def update(self, keys, objects):
        self.handle(keys)
        if self.moving_left:
            self.xvel = -self.moving_power
        elif self.moving_right:
            self.xvel = self.moving_power
        if self.isJump:
            self.yvel = -self.jumpPower

        self.rect.x += self.xvel
        self.collisions(objects, self.xvel, 0)
        self.xvel = 0
        self.rect.y += self.yvel
        self.collisions(objects, 0, self.yvel)
        self.yvel += self.gravity

    def draw(self, win):
        if self.animCount + 1 > 30:
            self.animCount = 0
        if self.sprite_jump and self.moving_right:
            win.blit(playerJump, (self.rect.x, self.rect.y))
        elif self.sprite_jump and self.moving_left:
            win.blit(playerJumpLeft, (self.rect.x, self.rect.y))
        elif self.fall and self.moving_right:
            win.blit(playerFall, (self.rect.x, self.rect.y))
        elif self.fall and self.moving_left:
            win.blit(playerFallLeft, (self.rect.x, self.rect.y))
        elif self.moving_left:
            win.blit(playerWalkLeft[self.animCount // 5], (self.rect.x, self.rect.y))
            self.animCount += 1
        elif self.moving_right:
            win.blit(playerWalkRight[self.animCount // 5], (self.rect.x, self.rect.y))
            self.animCount += 1
        else:
            win.blit(playerStand, (self.rect.x, self.rect.y))

