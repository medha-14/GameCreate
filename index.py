import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock =pygame.time.Clock()
sky=pygame.image.load('graphics/Sky.png')
font=pygame.font.Font('font\Pixeltype.ttf',50)
ground=pygame.image.load('graphics/ground.png')

text=font.render('RatRace',False,'Pink')
snail=pygame.image.load('graphics\snail\snail1.png')
snail_x=600

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(sky,(0,0))
    screen.blit(ground,(0,300))
    screen.blit(text,(300,50))
    snail_x-=5
    if snail_x<-100:
         snail_x=800
    screen.blit(snail,(snail_x,260))

    pygame.display.update()
    clock.tick(60)



