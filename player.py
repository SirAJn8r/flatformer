import pygame as pg


class Player(pg.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pg.image.load("sprites/bunny1_walk2.png")
        self.image = pg.transform.smoothscale(self.image, (30, 60))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.vx = 0
        self.vy = 0
        self.a = False
        self.d = False
        self.space = False
        self.coll = False

    def update(self):
        (width, height) = (pg.display.Info().current_w, pg.display.Info().current_h)
        if(self.coll == False):
            self.vy += .35
        if self.a and not self.d:
            self.vx = -5
        elif self.d and not self.a:
            self.vx = 5
        else:
            self.vx = 0
        if self.coll:
            if self.space:
                self.vy = -9
            else:
                self.vy = 0
        self.rect.x += self.vx
        self.rect.y += self.vy
        if self.rect.centerx <= 0:
            self.rect.x += width
        if self.rect.centerx >= width:
            self.rect.x -= width