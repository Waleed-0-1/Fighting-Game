import pygame 
pygame.init()

win=pygame.display.set_mode((700,500))
pygame.display.set_caption("fighting game")

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

bg=pygame.image.load("pics\\bg (1).png")
stan=pygame.image.load("pics\\Nstanding.png")

#adding logo
Nh=pygame.image.load("pics\\Nh.png")
Sh=pygame.image.load("pics\\Sh.png")

#adding bgm
# hitsound=pygame.mixer.Sound("pics\\hit.wav") #hit effect p chalyga isko chalany k liy jahan sasuke.hit ko call kiya neechy wahan isko call kro
bgm=pygame.mixer.music.load("pics\\theme.wav")  #bg theme

# pygame.mixer.music.play() #play ka function hai builtin yeh bgm ko chalayga


Clock=pygame.time.Clock()

#class bnayn gy tak weapon and character k variables mai confusioin na ho
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
           #in sab ko class mai rkh dia hai phly simple variables bnay thy baad mai class bnai
           #healthbar
           self.hitbox=(self.x+10,self.y+5,80,80) #80,80 =width,height #yeh actually mai hum characters ka around rectangel bnayngy or jab unk rectangles collide hingy to impact hoga. ab +10 or +5 yeh change krk khud sety krni ptyngi k konsi value pury character ko cover krrhi hai
           self.health=200
            
           
       def draw(self,win): #ab yahan variables k sath selsf lgayngy bcz uper calss mai unka name self. hai
           #dead player ki pic
           if self.health<=0:
             text=font.render("Noob",True,(255,50,50))
             win.blit(text,(180,200))
             win.blit(pygame.image.load("pics\\Sd.png"),(self.x,self.y))
             win.blit(pygame.image.load("pics\\Nd.png"),(self.x,self.y))
             return #issy agy wala code rukjayga 
            
             
             
           if self.walkCount +1>6:
            self.walkCount=0 #matlab agar walkciunt 6 hogya hai to +1 krny ki bjay usko 0 krk dubara start kro otherwise indexing eroor ajayga
    
           if self.left and self.isjump==False:  #remember yahan left true hai And ki wja se   True ni likha but left mai jarhy but jumo ni krrhy
            win.blit(walkLeft[self.walkCount//2],(self.x,self.y))
            self.walkCount+=1
        
           elif self.right and self.isjump==False: #right true and isjump false
            win.blit(walkRight[self.walkCount//2],(self.x,self.y)) #in dono mai 2 oictures ko switch krwaya jarha hai tak animation show ho sky
            self.walkCount+=1
        
           elif self.right and self.isjump: #matlab dono True hon
            win.blit(walkRight[2],(self.x,self.y))
      
        
           elif self.left and self.isjump: #matlab dono True hon
            win.blit(walkLeft[2],(self.x,self.y))
        
           else:#agar jump wali position hai hi nhi to stand wali image dikha do
             win.blit(stan,(self.x,self.y))
           
           #rectangle ko draw function mai ly ay
           self.hitbox=(self.x+10,self.y+5,80,80)
        #  pygame.draw.rect(win,(255,0,0),self.hitbox,2) #ab character k around red rectangle agya
           #isko hide krrhy ta k rectangle nazar na ay
           #health bar of player
           pygame.draw.rect(win,(255,0,0),(80,45,200,20)) #color red x y width height
           pygame.draw.rect(win,(255,255,0),(80,45,self.health,20))
           
              
       def hit(self):
           if self.health>0:
               self.health-=5
           else:
               print("naruto died")
                
        
           
           
           
           
        
class weapons():
    def __init__(self,x,y,width,height,facing):
        self.x=x
        self.y=y
        self.height=height
        self.width=width
        self.facing=facing
        self.vel=8*facing
        self.hitbox=(self.x,self.y,40,40) #yahan hitbox bnaya weapons k liy uski apni values set ki hain
        
        
    def draw(self,win):
        win.blit(pygame.image.load("pics\\shur.png"), (self.x, self.y))
     #   rectangle ko draw function mai ly ay
        self.hitbox=(self.x,self.y,40,40)
        # pygame.draw.rect(win,(255,0,0),self.hitbox,2) #ab weapon k around red rectangle agya
        
        
        
class enemy():
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
        self.end=end #agar woh boundry p jarha to usko automatically turn bhi krwana pryga
        self.path=[self.x,self.end] #enemy ka path set krrhy 
        self.speed=4
        self.walkkcount=0 
        self.hitbox=(self.x+10,self.y+5,80,80) #enemy k liy rectangle
        self.health=200
        
       
    def draw(self,win):
        #player damage k lit
         if self.health>0:
          self.move()
            
         if self.health>0:
                if self.walkkcount +1 >=6:
                    self.walkkcount=0 #yeh sirf is liy tak character ki image bahir na hojay
                if self.speed>0:
                    win.blit(self.walkRight_E[self.walkkcount//2],(self.x,self.y))
                    self.walkkcount +=1
                
                else:
                    win.blit(self.walkLeft_E[self.walkkcount//2],(self.x,self.y))
                    self.walkkcount +=1 
                self.hitbox=(self.x+10,self.y+5,80,80)
                # pygame.draw.rect(win,(255,0,0),self.hitbox,2)  #enemy k around bhi agya rectangle
                #rectangle ki form mai bnayn gy healthbar
                pygame.draw.rect(win,(255,0,0),(410,45,200,20)) #color red x y width height
                pygame.draw.rect(win,(255,255,0),(410,45,self.health,20))
            #doossry rect ko yellow color mai bnaya hai uper health 200 di thi usmai se minus hota jayga
         else:
                
                self.health=0
                #ab yahan usk harny p text dalyngy
                text=font.render("You Won",True,(50,255,50)) #phly wala text ka color hai dusry wala usk bg ka color hai jo k blue rkha hai
                win.blit(text,(180,200))
                win.blit(pygame.image.load("pics\\Sd.png"),(self.x,self.y))
            
            
    def move(self):
            if self.speed>0:
                
                if self.x+self.speed<self.path[1]: #movement k liy hai agar to end point jo 600 rkha wahan tak enemy nhi phncha to uski speed milti jay and woh move krta jay ab [1] p end point hoga jo uper humny 600 pass kiya hai
                    self.x+=self.speed
                else:
                    self.speed=self.speed * -1 #otherwise uski direction flip krdo
                    self.walkkcount=0
            else:   
                if self.x-self.speed>self.path[0]: #matlab list mai [0] wala initial point hoga jo k humny 30 set bhi kia hai to initial se agy jany k liy soeed zyada hoti rhy
                    self.x+=self.speed
                else:
                    self.speed=self.speed * -1
                    self.walkkcount=0
                    #player k marny ki pic dalyngy
                    
                
    def hit(self):
        print("hit") #ab weapon se health kam kryngy
        if self.health > 0:
             self.health -= 10     #health kam kryngy
        else:
            print("sasuke died")
            
            
run=True

def redrawgamewindow():
    win.blit(bg,(0,0)) #blit kisi image ko kahin p lgany k use hota hai yahn p yeh window k uper bg wali pic lga rha hai
    naruto.draw(win)
    sasuke.draw(win)
    win.blit(Nh,(10,10))
    win.blit(Sh,(600,10))
    for shurikane in shurikanes:
        shurikane.draw(win) #image aygi hr shoot p matlab jitni weapon phenjy ga utni pics
    
naruto=player(500,400,100,100) #uper jo x y height width di thi ab unki values din
sasuke=enemy(30,400,100,100,600)
shurikanes=[]
throwspeed=0 

#lose win bhi add kryndy

font=pygame.font.SysFont("arialblack",60,True) #Builtin hai or font ai se puchlo

while run: #matlab run==TRUE hai
    
    # pygame.time.delay(50) #actually mai frames per second decide kry ga kitny second mai kitni picture render krni hain
    Clock.tick(50)
    #weapon kab phenkni
    if throwspeed>0:
        throwspeed+=1
        
    if throwspeed>3:
        throwspeed=0
 
    
    
    for event in pygame.event.get(): 
        if event.type==pygame.QUIT:
            run=False
    #idher player damage start
    if naruto.health>0 and sasuke.health>0: #maltab dono alive hain otherwise collision hoga hi ni
        if naruto.hitbox[1]<sasuke.hitbox[1]+sasuke.hitbox[3] and naruto.hitbox[1]+naruto.hitbox[3] > sasuke.hitbox[1]:
            if naruto.hitbox[0]+naruto.hitbox[2]>sasuke.hitbox[0] and naruto.hitbox[0]<sasuke.hitbox[0]+sasuke.hitbox[2]:
                naruto.hit() 
                hitsound.play()
        
        if naruto.health<=0:
            naruto.speed=0
            

    for shurikane in shurikanes: #ab yahan collision k liy add kryngy
        if sasuke.health>0:
         if shurikane.hitbox[1]+round(shurikane.hitbox[3]/2)>sasuke.hitbox[1] and shurikane.hitbox[1]+round(shurikane.hitbox[3]/2)< sasuke.hitbox[1] + sasuke.hitbox[3]: 
           #[1] p humny y rkha [3] p humny height rkhi wagaira wagaira
           if shurikane.hitbox[0] + shurikane.hitbox[2]>sasuke.hitbox[0] and shurikane.hitbox[0] + shurikane.hitbox[2]<sasuke.hitbox[0] +sasuke.hitbox[2]:
               sasuke.hit() #function called
               hitsound.play()
               shurikanes.pop(shurikanes.index(shurikane)) #ta k jab weapon lgy to wph gayab hojay
        #    else:
        #     sasuke.speed=0
        
        if shurikane.x<760 and shurikane.x>0: #yahan whi boujndry set ki hai jo neechy ki thi
            shurikane.x+=shurikane.vel
        else:
            shurikanes.pop(shurikanes.index(shurikane)) #otherwise usko delete krdo
            
     
    keys=pygame.key.get_pressed() #konsi key dab rhi hai user se
    
    
    #shooting
    if keys[pygame.K_SPACE] and throwspeed==0:
        if naruto.left==True:
            facing=-1 #matlab agar character left hua to weapon ka face bhi left and same for right
        else:
            facing=1
        if len(shurikanes)<5: #calss tabhi kaam ay jab shoot krna ho isiliy loop mai object bna rhy
             shurikanes.append(weapons(round(naruto.x+naruto.width//2),round(naruto.y+naruto.height//2),40,40,facing)) #issy weapon character k center se ayngi matkab width or x k centre se and height or y k center se and usk baad dimension dali pic ki
        throwspeed=1
    
    
    
    
    
    
    if keys[pygame.K_LEFT] and naruto.x>naruto.speed: #yeh pygame ka format hai jo k documentation p availiable hai sab keys ka
        naruto.x-=naruto.speed #agar left jana hai to x axis k ulta utni hi speed k - mai jany lag jaygato
        naruto.left= True #CHARACRER aninmation k liy ab yeh add kia
        naruto.right= False
    elif keys[pygame.K_RIGHT] and naruto.x<760-naruto.width-naruto.height: #and k baad wala actually mai left right ki boundry set krrha again equations are already made by someone hum sirf change krk dekh skty kissy kia hota
        naruto.x+=naruto.speed 
        naruto.right=True
        naruto.left=False
    else:
         naruto.left=False
         naruto.right=False
         naruto.walkCount=0
    
    
    if naruto.isjump==False: #matlab cahracter khara hai koi jump ni lgai #remember idher assigment operator use kia hua hai kafi dfa eroor aya tha is wja se 
         if keys[pygame.K_UP]: #jump k liy UP lgayngy ab space se shoot
            naruto.isjump=True
            naruto.left=False
            naruto.right=False
            naruto.walkCount=0
    else:
        if naruto.jumpheight >=-10: #humny space dba k jump krwaya uper jaty huy g ki value + hoti hai neechy aty huy same value - hojati hai humny physics mai prha hua hai to matlab actually mai 10 ka jump lag gya ab same 10 - mai yani neechy ly k ao isko
            neg=1
            if naruto.jumpheight<0:
                  neg=-1  
          
            naruto.y-=(naruto.jumpheight**2)*0.5*neg #yeh equaion already kisi ne test krk bnai hai no such explanation for this
            naruto.jumpheight-=1
        else:
            naruto.isjump=False 
            naruto.jumpheight=10 #matlab ab jump nhi kia to jump ki value wapis 10 hogai matlab agli abri + direction yani uper hi jayga

   

    redrawgamewindow()
    pygame.display.update()
pygame.quit()
   
