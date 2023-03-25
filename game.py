import pygame as pg 
from random import randint
pg.init()
window=pg.display.set_mode((800,600))
pg.display.set_caption("Ping Pong")
x2=randint(-5,5)
y2=randint(-5,5)
while x2==0 and y2==0:
    x2=randint(-5,5)
    y2=randint(-5,5)
class GameSprite():
    def __init__(self,image,x,y,width,height,speed):
        self.image=pg.transform.scale(pg.image.load(image),(width,height))
        self.width=width
        self.height=height
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.speed=speed
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Ball(GameSprite):
    def move(self):
        global player,player2,x2,y2
        self.rect.x+=x2
        self.rect.y+=y2
        if self.rect.y>600:
            y2=-5
        if self.rect.y<0:
            y2=5
        if pg.sprite.collide_rect(self,player2):
            x2=5
        if pg.sprite.collide_rect(self,player):
            x2=-5

class Player(GameSprite):
    def control(self):
        keys=pg.key.get_pressed()
        if keys [pg.K_UP] and self.rect.y>0 :
            self.rect.y-=self.speed 
        if keys [pg.K_DOWN] and self.rect.y<500 :
            self.rect.y+=self.speed 
    def control2(self):
        keys=pg.key.get_pressed()
        if keys [pg.K_w] and self.rect.y>0 :
            self.rect.y-=self.speed 
        if keys [pg.K_s] and self.rect.y<500 :
            self.rect.y+=self.speed
player = Player("blue.png",760,250,20,100,6)
player2 = Player("orange.png",20,245,20,100,6)
ball=Ball("ball.png",400,300,80,80,2)
bg=GameSprite("fon.jpg",0,0,800,600,0)
label=pg.font.SysFont("ComicSans",50).render("Orange win",True,(0,250,154))
label2=pg.font.SysFont("ComicSans",50).render("Blue win",True,(0,250,154))
window.blit(label,(700,20))
game=True
while game:
    pg.time.Clock().tick(60)
    for i in pg.event.get():
        if i.type==pg.QUIT:
            exit()
    bg.reset()
    player.reset()
    player.control()
    player2.reset()
    player2.control2()
    ball.reset()
    ball.move()
    if ball.rect.x < 0:
        window.blit(label2,(250,150))
    if ball.rect.x > 800:
        window.blit(label,(250,150))
    pg.display.flip()