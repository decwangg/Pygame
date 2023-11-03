import pygame
from sys import exit
import random
import math
from pygame import mixer
mixer.init()
pygame.init()
mixer.music.load("game-over-134053.mp3.crdownload")
mixer.music.play(-1)

screen_width = 100
screen_height = 500

screen = pygame.display.set_mode((620,350))
pygame.display.set_caption("Flower shooter game")

background = pygame.image.load("360_F_556244850_wd7HG1vSaPXPQ56iIYtEnyGVWcdtQKLF.jpg")
 
flowerimg = pygame.image.load("mini1.png")
flowerimg = pygame.transform.scale(flowerimg, (100, 200))  # Resize the image to 50x50 pixels

villianimg=[]
villianX=[]
villianY=[]
villianspeedX=[]
villianspeedY=[]

no_of_villians=7

for i in range(no_of_villians):
 villianimg.append(pygame.image.load("flower ll.png"))
#  villianimg.append (pygame.transform.scale(villianimg, (50, 50)))
 villianimg[i] = pygame.transform.scale(villianimg[i], (50, 50))
 villianX.append(random.randint(0,270))
 villianY.append(random.randint(30,50))
 villianspeedX.append(-0.1)
 villianspeedY.append(40)



score=0


bulletimg= pygame.image.load("blue 3.png")
bulletimg = pygame.transform.scale(bulletimg,(40,40))
check=False
bulletX = 300
bulletY = 260

flowerX = 270
flowerY = 200
changeX= 0
running=True

def collision():
    distance=math.sqrt(math.pow(bulletX-villianX,2)+math.pow(bulletY-villianY,2))
    if distance<27:
        return True
    

font=pygame.font.SysFont('Arial',25,'italic')



def score_text():
    img=font.render(f'Score:{score}',True,'black')
    screen.blit(img,(10,10))

font_gameover=pygame.font.SysFont('Arial',65,'Italic')

def gameover():
    img_gameover=font_gameover.render('GAME OVER',True,'Red')
    screen.blit(img_gameover,(150,100))


         
while True:
   screen.blit(background,(0,0))
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
         exit()
      if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_LEFT:
               changeX = -50
          if event.key == pygame.K_RIGHT:
               changeX = 50
          if event.key ==pygame.K_SPACE:
               if check is False:
                check=True
               bulletX=flowerX+30
      if event.type == pygame.KEYUP:
           channgeX=0


           flowerX+=changeX   # flowerX= flowerX-change X
   if flowerX<=0:
          flowerX=0
   elif flowerX>=520:
          flowerX=520


   for i in range(no_of_villians): 
     if villianY[i]>200:
       for j in range(no_of_villians):
        villianY[j]=2000
       gameover()
       break
       
        
       villianX[i]+=villianspeedX[i]
   if villianX[i]<=0:
        villianspeedX[i]=0.1
        villianY[i]+=villianspeedY[i]
   if villianX[i]>=520:
        villianspeedX[i]=-0.1 
        villianY[i]+=villianspeedY[i]

#    distance=math.sqrt(math.pow(bulletX-villianX,2)+math.pow(bulletY-villianY,2))
   distance = math.sqrt(math.pow(bulletX - villianX[i], 2) + math.pow(bulletY - villianY[i], 2))
   if distance<27:
   
       bulletY=260
       check=False
       villianX[i]=random.randint(0, 270)
       villianY[i]=random.randint(30,50)
       score+=1
       screen.blit(villianimg[i],(villianX[i], villianY[i]))

   if bulletY<=0:
        bulletY=260
        check=False
   if check:
     screen.blit(bulletimg,(bulletX,bulletY))
     bulletY-=0.3
     

   

   screen.blit(flowerimg,(flowerX,flowerY))
#    screen.blit(villianimg[i],(villianX[i], villianY[i]))
   for i in range(no_of_villians):
    screen.blit(villianimg[i],(villianX[i], villianY[i]))
   score_text()                       

   pygame.display.update()


   
   