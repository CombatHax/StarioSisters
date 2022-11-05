from object import *
import coin

class Player(Object):
    def __init__(self, pos):
        self.rect = pos
        self.dire = 1
        things = ['imgs/dude-left.png', 'imgs/dude-right.png']
        self.img = [pg.Surface.convert_alpha(pg.image.load(things[i])) for i in range(2)]
        self.vel = [0, 0]
        self.coins = 0
    def move(self, level, movement):
        ret = []
        self.vel[1] += 0.25
        collision = self.check_collision(level)
        if not (collision[2] and self.vel[0] + movement <= 0):
            self.rect[0] += self.vel[0] + movement
        if not (collision[3] and self.vel[0] + movement >= 0):
            self.rect[0] += self.vel[0] + movement
        if collision[0]:
            self.vel[1] = 0.1
            self.coins += 1
            coin_pos = list(collision[4])
            coin_pos[0] += 25
            ret.append(coin.Coin(coin_pos))
        if not collision[1]:
            self.rect[1] += self.vel[1]
        else:
            self.vel[1] = 0
        return ret
    def jump(self, level):
        if self.check_collision(level)[1]:
            self.vel[1] -= 10
            self.rect[1] -= 0.1
    def check_collision(self, level):
        collide = [0, 0, 0, 0, []]
        for cube in level:
            # RIGHT D. > LEFT C.
            # LEFT C. <- RIGHT D.
            # AND
            # LEFT D. <- RIGHT C.
            if self.rect[1] + self.rect[3] <= cube.rect[1] and self.rect[1] <= cube.rect[1] + cube.rect[3]:
                # RIGHT D. RIGHT LEFT C.
                if self.rect[0] + self.rect[2] >= cube.rect[0]:
                    # RIGHT D. LEFT RIGHT C.
                    if self.rect[0] + self.rect[2] <= cube.rect[0] + cube.rect[2]:
                        collide[2] = 1
                        collide[4] = cube.rect
                    # LEFT D. LEFT RIGHT C.
                    if self.rect[0] <= cube.rect[0] + cube.rect[2]:
                        # LEFT D. RIGHT LEFT C.
                        if self.rect[0] >= cube.rect[0]:
                            collide[3] = 1
                            collide[4] = cube.rect
            if self.rect[0] + self.rect[2] >= cube.rect[0] and self.rect[0] <= cube.rect[0] + cube.rect[2]:
                # BOTTOM D. LOWER TOP C.
                # TOP.C ^ BOTTOM D.
                if self.rect[1] + self.rect[3] >= cube.rect[1]:
                    # BOTTOM D. ^ BOTTOM C.
                    if self.rect[1] + self.rect[3] <= cube.rect[1] + cube.rect[3]:
                        collide[1] = 1
                        self.rect[1] = cube.rect[1] - self.rect[3]
                        collide[4] = cube.rect
                # TOP D. ^ BOTTOM C.
                # AND
                # TOP C. ^ TOP D.
                if self.rect[1] <= cube.rect[1] + cube.rect[3] <= self.rect[1] + cube.rect[3]:
                    self.rect[1] = cube.rect[1] + cube.rect[3]
                    collide[0] = 1
                    collide[4] = cube.rect
            
        print(collide)
        return collide
    def draw(self, surf, dire):
        if dire != 0.5:
            self.dire = int(dire)
        surf.blit(self.img[self.dire], (self.rect[0], self.rect[1]))
