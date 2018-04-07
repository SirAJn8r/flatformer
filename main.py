import pygame as pg
from pygame.locals import *
import sys
import random

from platform import *
from player import *

pg.init()

size = (width, height) = (pg.display.Info().current_w, pg.display.Info().current_h)
screen = pg.display.set_mode(size)
clock = pg.time.Clock()
color = (100, 100, 200)
platforms = pg.sprite.Group()
num = 4*8
for i in range(4):
    for j in range(8):
        platforms.add(Platform((random.randint(50, width-50), j * height/8)))
score = 0
p = Player((width/2, height/6))
pgroup = pg.sprite.Group()
pgroup.add(p)

def main():
    global screen, color, score, num
    while True:
        clock.tick(60)
        for event in pg.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_f:
                    screen = pg.display.set_mode(size, FULLSCREEN)
                if event.key == K_ESCAPE:
                    screen = pg.display.set_mode(size)
                if event.key == K_a:
                    p.a = True
                if event.key == K_d:
                    p.d = True
                if event.key == K_SPACE:
                    p.space = True
            if event.type == KEYUP:
                if event.key == K_a:
                    p.a = False
                if event.key == K_d:
                    p.d = False
                if event.key == K_SPACE:
                    p.space = False
        p.coll = False
        if len(pg.sprite.spritecollide(p, platforms, False)) > 0:
            for i in pg.sprite.spritecollide(p, platforms, False):
                if(p.rect.bottom <= i.rect.top + p.vy + 1):
                    p.coll = True
                    p.rect.bottom = i.rect.top + 1
                    break
        if(p.rect.top <= height/4):
            for platform in platforms:
                platform.rect.y += height/4 - p.rect.top
            score += height/4 - p.rect.top
            p.rect.y += height/4 - p.rect.top
        if(p.rect.bottom >= height):
            for platform in platforms:
                platform.rect.y -= p.vy
        for platform in platforms:
            if platform.rect.top >= height or platform.rect.bottom <= 0:
                platform.kill()
        for i in range(num - len(platforms)):
            platforms.add(Platform((random.randint(50, width-50), 0)))
        platforms.update()
        p.update()
        screen.fill(color)
        platforms.draw(screen)
        pgroup.draw(screen)
        pg.display.flip()

if __name__ == "__main__":
    main()