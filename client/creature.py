import sprite_handler
import time

class Creature(object):

    SPEED = 5
    ATTACK_DURATION = 0.5

    def __init__(self, x, y):
        self.direction = 0
        self.x = x
        self.y = y
        self.ticks = 0
        self.moving = False
        self.time = 0
        self.attackTime = 0

    def attack(self):
        self.attackTime = self.time + Creature.ATTACK_DURATION

    def moveLeft(self):
        self.x -= Creature.SPEED

    def moveRight(self):
        self.x += Creature.SPEED

    def moveUp(self):
        self.y -= Creature.SPEED

    def moveDown(self):
        self.y += Creature.SPEED

    def setTime(self, t):
        self.time = t

    def getSpriteName(self):
        if self.attackTime != 0 and self.attackTime > self.time:
            return self.attackSprite

        breathing = int(self.time) % 2 == 0
        armSwings = int(self.moving) and (int(self.time) % 2 == 0)
        return self.sprites[self.direction][armSwings][breathing]

class Ghost(Creature):

    def __init__(self, x, y, spriteHandler):
        super(Ghost, self).__init__(x, y)
        self.sprites = [[
                [sprite_handler.Sprites.GHOST11,
                    sprite_handler.Sprites.GHOST12],
                [sprite_handler.Sprites.GHOST21,
                    sprite_handler.Sprites.GHOST22]]]

class PerLarsson(Creature):

    def __init__(self, x, y, spriteHandler):
        super(PerLarsson, self).__init__(x, y)
        self.sprites = [[
                [sprite_handler.Sprites.PER_LARSSON11,
                    sprite_handler.Sprites.PER_LARSSON11],
                [sprite_handler.Sprites.PER_LARSSON11,
                    sprite_handler.Sprites.PER_LARSSON11]],
                [[sprite_handler.Sprites.PER_LARSSON11,
                    sprite_handler.Sprites.PER_LARSSON11],
                [sprite_handler.Sprites.PER_LARSSON11,
                    sprite_handler.Sprites.PER_LARSSON11]]]

        self.attackSprite = sprite_handler.Sprites.ALEX_MILLER_ATTACK


class MattGarret(Creature):

    def __init__(self, x, y, spriteHandler):
        super(MattGarret, self).__init__(x, y)
        self.sprites = [[
                [sprite_handler.Sprites.MATT_GARRET11,
                    sprite_handler.Sprites.MATT_GARRET11],
                [sprite_handler.Sprites.MATT_GARRET11,
                    sprite_handler.Sprites.MATT_GARRET11]],
                [[sprite_handler.Sprites.MATT_GARRET11,
                    sprite_handler.Sprites.MATT_GARRET11],
                [sprite_handler.Sprites.MATT_GARRET11,
                    sprite_handler.Sprites.MATT_GARRET11]]]

        self.attackSprite = sprite_handler.Sprites.ALEX_MILLER_ATTACK


class AlexMiller(Creature):

    def __init__(self, x, y, spriteHandler):
        super(AlexMiller, self).__init__(x, y)
        self.sprites = [[
                [sprite_handler.Sprites.ALEX_MILLER11,
                    sprite_handler.Sprites.ALEX_MILLER12],
                [sprite_handler.Sprites.ALEX_MILLER21,
                    sprite_handler.Sprites.ALEX_MILLER22]],
                [[sprite_handler.Sprites.ALEX_MILLER_UP11,
                    sprite_handler.Sprites.ALEX_MILLER_UP12],
                [sprite_handler.Sprites.ALEX_MILLER_UP11,
                    sprite_handler.Sprites.ALEX_MILLER_UP12]]]

        self.attackSprite = sprite_handler.Sprites.ALEX_MILLER_ATTACK
