import pygame 
pygame.init()
#maaking window
win=pygame.display.set_mode((700,500))
#making title
pygame.display.set_caption("naruto vs sasuke by Waleed")

#adding players sprites
walkRight=[
           pygame.image.load("pics\\NR2.png"),
           pygame.image.load("pics\\NR3.png"),
           pygame.image.load("pics\\NR4.png")
]
walkLeft=[
          pygame.image.load("pics\\NL1.png"),
          pygame.image.load("pics\\NL2.png"),
          pygame.image.load("pics\\NL3.png")
]
stan=pygame.image.load("pics\\Nstanding.png")

#backgroundd pic
bg=pygame.image.load("pics\\bg (1).png")

#adding logo
Nh=pygame.image.load("pics\\Nh.png")
Sh=pygame.image.load("pics\\Sh.png")

#adding bgm
hitsound=pygame.mixer.Sound("pics\\hit.wav") 
# bgm=pygame.mixer.music.load("pics\\theme.wav") 

# pygame.mixer.music.play()

Clock=pygame.time.Clock()

#making player class
class player():
       def __init__(self,x,y,width,height):
           self.x=x
           self.y=y
           self.height=height
           self.width=width
           self.speed=10
           self.isjump=False
           self.jumpheight=10
           self.left=False
           self.right=False
           self.walkCount=0
           self.hitbox=(self.x+10,self.y+5,80,80) 
           self.health=200
            
    #draw function for player 
       def draw(self,win):
           if self.health<=0:
             text=font.render("Noob",True,(255,50,50))
             win.blit(text,(180,200))
             win.blit(pygame.image.load("pics\\Nd.png"),(self.x,self.y))
             return

           if self.walkCount +1>6:
            self.walkCount=0 
    
           if self.left and self.isjump==False:  
            win.blit(walkLeft[self.walkCount//2],(self.x,self.y))
            self.walkCount+=1
        
           elif self.right and self.isjump==False: 
            win.blit(walkRight[self.walkCount//2],(self.x,self.y)) 
            self.walkCount+=1
        
           elif self.right and self.isjump: 
            win.blit(walkRight[2],(self.x,self.y))
      
        
           elif self.left and self.isjump: 
            win.blit(walkLeft[2],(self.x,self.y))
        
           else:
             win.blit(stan,(self.x,self.y))
           
           
           self.hitbox=(self.x+10,self.y+5,80,80)
           pygame.draw.rect(win,(255,0,0),(80,45,200,20)) 
           pygame.draw.rect(win,(255,255,0),(80,45,self.health,20))
           
              
       def hit(self):
           if self.health>0:
               self.health-=5
           else:
               print("naruto died")
               
#class for weapons
class weapons():
    def __init__(self,x,y,width,height,facing):
        self.x=x
        self.y=y
        self.height=height
        self.width=width
        self.facing=facing
        self.vel=8*facing
        self.hitbox=(self.x,self.y,40,40) 
    #draw function for weapons   
    def draw(self,win):
        win.blit(pygame.image.load("pics\\shur.png"), (self.x, self.y))
        self.hitbox=(self.x,self.y,40,40)
        
#class for Enemy
class enemy():
#enemy sprites within class
    walkRight_E=[
           pygame.image.load("pics\\SR1.png"),
           pygame.image.load("pics\\SR2.png"),
           pygame.image.load("pics\\SR3.png")
]
    walkLeft_E=[
          pygame.image.load("pics\\SL1.png"),
          pygame.image.load("pics\\SL2.png"),
          pygame.image.load("pics\\SL3.png")
]

    def __init__(self,x,y,width,height,end):
        self.x=x
        self.y=y
        self.height=height
        self.width=width
        self.end=end 
        self.path=[self.x,self.end] 
        self.speed=4
        self.walkkcount=0 
        self.hitbox=(self.x+10,self.y+5,80,80) 
        self.health=200
     #draw function for enemy   
    def draw(self,win):      
         if self.health>0:
          self.move()
            
         if self.health>0:
                if self.walkkcount +1 >=6:
                    self.walkkcount=0 
                if self.speed>0:
                    win.blit(self.walkRight_E[self.walkkcount//2],(self.x,self.y))
                    self.walkkcount +=1
                
                else:
                    win.blit(self.walkLeft_E[self.walkkcount//2],(self.x,self.y))
                    self.walkkcount +=1 
                self.hitbox=(self.x+10,self.y+5,80,80)
            
                pygame.draw.rect(win,(255,0,0),(410,45,200,20)) 
                pygame.draw.rect(win,(255,255,0),(410,45,self.health,20))
         else:
                self.health=0
                text=font.render("You Won",True,(50,255,50)) 
                win.blit(text,(180,200))
                win.blit(pygame.image.load("pics\\Sd.png"),(self.x,self.y))
            
    #making move funcion for enemy as it has to move itself        
    def move(self):
            if self.speed>0:
                
                if self.x+self.speed<self.path[1]: 
                    self.x+=self.speed
                else:
                    self.speed=self.speed * -1 
                    self.walkkcount=0
            else:   
                if self.x-self.speed>self.path[0]: 
                    self.x+=self.speed
                else:
                    self.speed=self.speed * -1
                    self.walkkcount=0
    def hit(self):
        print("hit") 
        if self.health > 0:
             self.health -= 10
        else:
            print("sasuke died")
            
            
run=True

def redrawgamewindow():
    win.blit(bg,(0,0)) 
    naruto.draw(win)
    sasuke.draw(win)
    win.blit(Nh,(10,10))
    win.blit(Sh,(600,10))
    for shurikane in shurikanes:
        shurikane.draw(win) 
    
naruto=player(500,400,100,100) 
sasuke=enemy(30,400,100,100,600)
shurikanes=[]
throwspeed=0 

font=pygame.font.SysFont("arialblack",60,True) 

while run: 
    Clock.tick(50)

    if throwspeed>0:
        throwspeed+=1
        
    if throwspeed>3:
        throwspeed=0
    
    for event in pygame.event.get(): 
        if event.type==pygame.QUIT:
            run=False
    #collision algorithm for player
    if naruto.health>0 and sasuke.health>0: 
        if naruto.hitbox[1]<sasuke.hitbox[1]+sasuke.hitbox[3] and naruto.hitbox[1]+naruto.hitbox[3] > sasuke.hitbox[1]:
            if naruto.hitbox[0]+naruto.hitbox[2]>sasuke.hitbox[0] and naruto.hitbox[0]<sasuke.hitbox[0]+sasuke.hitbox[2]:
                naruto.hit() 
                hitsound.play()
        
        if naruto.health<=0:
            naruto.speed=0
            
    #collision algorithm for enemy
    for shurikane in shurikanes: 
        if sasuke.health>0:
         if shurikane.hitbox[1]+round(shurikane.hitbox[3]/2)>sasuke.hitbox[1] and shurikane.hitbox[1]+round(shurikane.hitbox[3]/2)< sasuke.hitbox[1] + sasuke.hitbox[3]: 
          
           if shurikane.hitbox[0] + shurikane.hitbox[2]>sasuke.hitbox[0] and shurikane.hitbox[0] + shurikane.hitbox[2]<sasuke.hitbox[0] +sasuke.hitbox[2]:
               sasuke.hit() 
               hitsound.play()
               shurikanes.pop(shurikanes.index(shurikane)) 
        
        if shurikane.x<760 and shurikane.x>0: 
        
            shurikane.x+=shurikane.vel
        else:
            shurikanes.pop(shurikanes.index(shurikane)) 
            
    #adding keys 
    keys=pygame.key.get_pressed() 
    if keys[pygame.K_SPACE] and throwspeed==0:
        if naruto.left==True:
            facing=-1 
        else:
            facing=1
        if len(shurikanes)<5: 
             shurikanes.append(weapons(round(naruto.x+naruto.width//2),round(naruto.y+naruto.height//2),40,40,facing)) 
        throwspeed=1
 
    if keys[pygame.K_LEFT] and naruto.x>naruto.speed: 
        naruto.x-=naruto.speed
        naruto.left= True 
        naruto.right= False
    elif keys[pygame.K_RIGHT] and naruto.x<760-naruto.width-naruto.height: 
    
        naruto.x+=naruto.speed 
        naruto.right=True
        naruto.left=False
    else:
         naruto.left=False
         naruto.right=False
         naruto.walkCount=0
    
    
    if naruto.isjump==False: 
         if keys[pygame.K_UP]: 
            naruto.isjump=True
            naruto.left=False
            naruto.right=False
            naruto.walkCount=0
    else:
        if naruto.jumpheight >=-10: 
            neg=1
            if naruto.jumpheight<0:
                  neg=-1  
            naruto.y-=(naruto.jumpheight**2)*0.5*neg 
            naruto.jumpheight-=1
        else:
            naruto.isjump=False 
            naruto.jumpheight=10 

    redrawgamewindow()
    pygame.display.update()
pygame.quit()
   
