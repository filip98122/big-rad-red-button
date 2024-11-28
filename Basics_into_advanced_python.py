import pygame
import random
import math
pygame.init()
pygame.mixer.init()
def kolizija_krugova(x1,y1,r1,x2,y2,r2):
    dx = x2 - x1
    dy = y2 - y1
    dist  = dx * dx + dy * dy
    dist = math.sqrt(dist)
    if dist >= r1 + r2:
        return False
    else:
        return True
def kolizija_pravougaonika(rect1 : pygame.Rect,rect2):
    if rect1.colliderect(rect2):
        return True
    return False
clock = pygame.time.Clock()
WIDTH,HEIGHT = 1200,765
window = pygame.display.set_mode((WIDTH,HEIGHT))
def highlight_dugme(width,height,x,y,mousePos):
    if mousePos[0] > x and mousePos[0] < x + width and mousePos[1] > y and mousePos[1] < y + height:
        return True
    else:
        return False
def dugme_proveravac(width,height,x,y,mousePos,mouseState):
    if mousePos[0] > x and mousePos[0] < x + width and mousePos[1] > y and mousePos[1] < y + height and mouseState[0] == True:
        return True
    else:
        return False
class Big_red_button:
    def __init__(self,clicked):
        self.clicked = clicked
        self.image = pygame.image.load("big red button.png")
        self.height = self.image.get_height()*1.5
        self.width = self.image.get_width()*1.5
        self.scaled_img = pygame.transform.scale(self.image, (self.width, self.height))
    def draw(self,window):
        window.blit(self.scaled_img,(525,500))
class Nuclear_bomb:
    def __init__(self,x,y,dy): 
        self.x = x
        self.y = y
        self.dy = dy
        self.h = 317
        self.w = 144
        self.alive=True
        self.image = pygame.image.load("nuclear.png")
        self.height = self.image.get_height()*0.99
        self.width = self.image.get_width()*0.99
        self.scaled_img = pygame.transform.scale(self.image, (self.width, self.height))
    def draw(self,window):
        if self.alive==True:
            window.blit(self.scaled_img,(self.x,self.y))
            self.height =self.h
            self.width = self.w
            self.scaled_img = pygame.transform.scale(self.image, (self.width, self.height))
            self.h-=0.2
            self.w -=0.2
            self.x+=0.1
            if self.y == 100:
                self.alive =False
            else:
                self.y+=self.dy
class Explosions:
    def __init__(self,x,y,koji):
        self.x = x
        self.y = y
        self.koji = koji
        self.alive=True
    def draw(self,window):
        if self.alive==True:
            if self.koji//5<0 or self.koji//5>6:
                pass
            else:
                self.image = pygame.image.load(f"explosion{self.koji//5}.png")
                self.height = self.image.get_height()*2
                self.width = self.image.get_width()*2
                self.scaled_img = pygame.transform.scale(self.image, (self.width, self.height))
                window.blit(self.scaled_img,(self.x,self.y))
            self.koji+=1
            if self.koji==35:
                self.alive=False
def background(window):
    image = pygame.image.load("house.png")
    height = 765
    width = 1200
    scaled_img = pygame.transform.scale(image, (width, height))
    window.blit(scaled_img,(0,0))
def death_of_bomb(indexofbomb):
    lexplosions.append(Explosions(random.randint(int(lbombs[indexofbomb].x)-40,int(lbombs[indexofbomb].x)+int(lbombs[indexofbomb].w))+25,50,random.randint(1,15)*-1))
    lexplosions.append(Explosions(random.randint(int(lbombs[indexofbomb].x)-40,int(lbombs[indexofbomb].x)+int(lbombs[indexofbomb].w))+25,100,random.randint(1,15)*-1))
    lexplosions.append(Explosions(random.randint(int(lbombs[indexofbomb].x)-40,int(lbombs[indexofbomb].x)+int(lbombs[indexofbomb].w))+25,150,random.randint(1,15)*-1))
    lexplosions.append(Explosions(random.randint(int(lbombs[indexofbomb].x)-40,int(lbombs[indexofbomb].x)+int(lbombs[indexofbomb].w))+25,200,random.randint(1,15)*-1))
    

lbombs = []
lexplosions=[]
button = Big_red_button(False)
while True:
    window.fill("black")
    background(window)
    keys = pygame.key.get_pressed()
    events = pygame.event.get()
    mouseState = pygame.mouse.get_pressed()
    mousePos = pygame.mouse.get_pos()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
    if keys[pygame.K_ESCAPE]:
        exit()
    button.draw(window)
    if dugme_proveravac(80,80,560,540,mousePos,mouseState):
        lbombs.append(Nuclear_bomb(630,-315,1))
    for i in range(len(lbombs)):
        lbombs[i].draw(window)
    g = 0
    for i in range(len(lbombs)):
        if lbombs[g].alive ==False:
            death_of_bomb(g)
            del lbombs[g]
            
            g-=1
        g+=1
    for i in range(len(lexplosions)):
        lexplosions[i].draw(window)
    g = 0
    for i in range(len(lexplosions)):
        if lexplosions[g].alive==False:
            del lexplosions[g]
            g-=1
        g+=1
    pygame.display.update()
    clock.tick(60)
    
    

    