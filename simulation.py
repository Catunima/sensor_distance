import pygame, sys
from pygame.locals import *
from joblib import load

def whereIsObjectX(rY,rX):
    ob1Y = obj1[1]
    ob3Y = obj3[1]
    #obj1 = [200,200,100,50]
    if rX >= (200-100) and rX <= (200+100):
        if rY >= (200+50):
            result = rY - ob1Y
        elif rX >= (300-50) and rX <= (300+50):
            result = rY -ob3Y
        else:
            result = rY - 0
    #obj3 = [300,60,50,50]
    elif rX >= (300-50) and rX <= (300+50):
        result = rY -ob3Y
    else:
        result = rY - 0
    return result
def whereIsObjectY(rY,rX):
    #obj2 = [110,250,50,50]
    ob2X = obj2[0]
    x = rX -50
    if rY >= (250-50) and rY <= (250+50):
        result = x - ob2X
    else:
        result = 50
    return result  

def whereIsObjectYR(rY,rX):
    
    ob4X = obj4[0]
    x = rX +50
    #obj4 = [450,110,50,50]
    if rY >= (110-50) and rY <= (110+50):
        result = ob4X - x

    else:
        result = (1*(x))
    return result  

def textDisplay(screen, msg, pos):
    font = pygame.font.SysFont('Barber Street_PersonalUseOnly', 20)
    text = font.render(msg,1,(255,255,255))
    screen.blit(text,pos)

direction = load('direction.joblib')

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

speed_robot = 0
ask = 0
s_front = 50
s_left = 10
s_right = 60
distant = 80
pygame.init()
screen = pygame.display.set_mode((500, 500))

running = True
robot = [200,450,50,50]
obj1 = [200,200,100,50]
obj2 = [110,250,50,50]
obj3 = [300,60,50,50]
obj4 = [450,110,50,50]


clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or robot[1] == 58:
            running = False
            sys.exit()
    
    screen.fill(black)
    pygame.draw.rect(screen,white,[0,0,500,5])
    pygame.draw.rect(screen,blue, obj1)
    pygame.draw.rect(screen,blue,obj2)
    pygame.draw.rect(screen,blue,obj3)
    pygame.draw.rect(screen,blue,obj4)

    pygame.draw.rect(screen,red,robot)
    speed_robot = 2
    sl = str(s_left)
    sr = str(distant)
    sf = str(s_front)

    textDisplay(screen,"Sensor front: " + sf, [5, 45])
    
    s_front = whereIsObjectX(robot[1],robot[0])
    s_left = whereIsObjectY(robot[1],robot[0])
    
    if s_front >=60:
        ask = 0
        speed_robot = -2
        robot[1] += speed_robot
    else:
        if(ask == 0):
            ask = 1
            d = direction.predict([[s_left,s_right]])
        print(s_left)
        if(d == 1):
            speed_robot = 2
        else:
            speed_robot = -2
        robot[0] += speed_robot
            

    pygame.display.flip()
    clock.tick(60)

pygame.quit()