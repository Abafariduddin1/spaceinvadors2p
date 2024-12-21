import pygame
import sys
pygame.init()
screen1=pygame.display.set_mode((900,500))
pygame.display.set_caption("New1")
font = pygame.font.SysFont("Italic",60)


bg = pygame.image.load("L.4/space.jpg")
backg = pygame.transform.scale(bg,(900,500))


rectonyship = pygame.Rect(50,250,60,60)
rectonrship = pygame.Rect(790,250,60,60)


yship = pygame.image.load("L.4/yelowship.jpg")
yeship = pygame.transform.scale(yship,(60,60))
yeeship = pygame.transform.rotate(yeship,90)

rship = pygame.image.load("L.4/redship.jpg")
reship = pygame.transform.scale(rship,(60,60))
reeship = pygame.transform.rotate(reship,270)

yhealth=5
rhealth=5

def bitl():
    screen1.blit(backg,(0,0))
    screen1.blit(reeship,(rectonrship.x,rectonrship.y))
    screen1.blit(yeeship,(rectonyship.x,rectonyship.y))
    ret = pygame.Rect(425,0,50,500)
    pygame.draw.rect(screen1,"black",ret)
    for bullet in ybullet:
        pygame.draw.rect(screen1,"yellow",bullet)
    for bullet in rbullet:
        pygame.draw.rect(screen1,"red",bullet)
    fynt = font.render("Health :"+str(yhealth),True,"black")
    frnt = font.render("Health :"+str(rhealth),True,"black")
    screen1.blit(fynt,(50,50))
    screen1.blit(frnt,(650,50))
            


def ymove():
    keyp = pygame.key.get_pressed()
    if keyp[pygame.K_w]:
        rectonyship.y=rectonyship.y-3
    if keyp[pygame.K_s]:
        rectonyship.y=rectonyship.y+3
    if keyp[pygame.K_a]:
        rectonyship.x=rectonyship.x-3
    if keyp[pygame.K_d]:
        rectonyship.x=rectonyship.x+3
    if rectonyship.y<0:
        rectonyship.y=500   
    if rectonyship.y>500:
        rectonyship.y=0
    if rectonyship.x<0:
        rectonyship.x=400
    if rectonyship.x>400:
        rectonyship.x=0 

    if keyp[pygame.K_UP]:
        rectonrship.y=rectonrship.y-3
    if keyp[pygame.K_DOWN]:
        rectonrship.y=rectonrship.y+3
    if keyp[pygame.K_LEFT]:
        rectonrship.x=rectonrship.x-3
    if keyp[pygame.K_RIGHT]:
        rectonrship.x=rectonrship.x+3
    if rectonrship.y<0:
        rectonrship.y=500   
    if rectonrship.y>500:
        rectonrship.y=0
    if rectonrship.x>900:
        rectonrship.x=450
    if rectonrship.x<450:
        rectonrship.x=900        

ybullet = []
rbullet = []         


def bulletmove():
    global rhealth
    global yhealth
    for bullet in ybullet:
        bullet.x=bullet.x+3
        if rectonrship.colliderect(bullet):
            ybullet.remove(bullet)
            if rhealth>0:
               rhealth=rhealth-1
        if bullet.x>899:
            ybullet.remove(bullet)       

    for i in rbullet:
        i.x=i.x-3
        if i.colliderect(rectonyship):
            rbullet.remove(i)
            if yhealth>0:
               yhealth=yhealth-1         
        if i.x<0:
            rbullet.remove(i) 

def healthings():
    if rhealth<=0:
            fyint = font.render("Game over! Yellow has Won!",True,"black")
            screen1.blit(fyint,(400,200))
            pygame.display.update()
            
            
    if yhealth<=0:
            frint = font.render("Game over! Red has won!",True,"Black")
            screen1.blit(frint,(400,200))
            pygame.display.update()
                    



    


clock = pygame.time.Clock()
while True:
    clock.tick(60)
    ymove()
    bitl()
    bulletmove()
    healthings()
    if yhealth==0 or rhealth==0:
        pygame.time.delay(5000)
        break
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_e and len(ybullet)<3:
                yebullet=pygame.Rect(rectonyship.x+55,rectonyship.y+25,25,10)
                ybullet.append(yebullet)
            if event.key==pygame.K_SPACE and len(rbullet)<3:
                rebullet=pygame.Rect(rectonrship.x-5,rectonrship.y+25,25,10)        
                rbullet.append(rebullet)    
    pygame.display.update()