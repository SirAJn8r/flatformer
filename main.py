import pygame as pg
from pygame.locals import *
import sys

from platform import *
from player import *

pg.init()

size = (width, height) = (pg.display.Info().current_w, pg.display.Info().current_h)
screen = pg.display.set_mode(size)
clock = pg.time.Clock()
color = (100, 100, 200)
platforms = pg.sprite.Group()
for i in range(20):
    platforms.add(Platform((width/40*i*2, height*3/4-i*16)))
p = Player((width/4, height/4))
pgroup = pg.sprite.Group()
pgroup.add(p)

def main():
    global screen, color
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
            p.coll = True
        if(p.rect.top <= height/4):
            p.rect.y += height/4 - p.rect.top
            for platform in platforms:
                platform.rect.y += height/4 - p.rect.top
        platforms.update()
        p.update()
        screen.fill(color)
        platforms.draw(screen)
        pgroup.draw(screen)
        pg.display.flip()

if __name__ == "__main__":
    main()