# import pygame 
# pygame.init()

# win=pygame.display.set_mode((700,500))
# pygame.display.set_caption("fighting game")

# walkRight=[
#            pygame.image.load("pics\\NR2.png"),
#            pygame.image.load("pics\\NR3.png"),
#            pygame.image.load("pics\\NR4.png")
# ]
# walkLeft=[
#           pygame.image.load("pics\\NL1.png"),
#           pygame.image.load("pics\\NL2.png"),
#           pygame.image.load("pics\\NL3.png")
# ]

# bg=pygame.image.load("pics\\bg (1).png")
# stan=pygame.image.load("pics\\Nstanding.png")

# Clock=pygame.time.Clock()

# #class bnayn gy tak weapon and character k variables mai confusioin na ho
# class player():
#        def __init__(self,x,y,width,height):
#            self.x=x
#            self.y=y
#            self.height=height
#            self.width=width
#            self.speed=10
#            self.isjump=False
#            self.jumpheight=10
#            self.left=False
#            self.right=False
#            self.walkCount=0
#            #in sab ko class mai rkh dia hai phly simple variables bnay thy baad mai class bnai
           
           
#        def draw(self,win): #ab yahan variables k sath selsf lgayngy bcz uper calss mai unka name self. hai
#            if self.walkCount +1>6:
#             self.walkCount=0 #matlab agar walkciunt 6 hogya hai to +1 krny ki bjay usko 0 krk dubara start kro otherwise indexing eroor ajayga
    
#            if self.left and self.isjump==False:  #remember yahan left true hai And ki wja se   True ni likha but left mai jarhy but jumo ni krrhy
#             win.blit(walkLeft[self.walkCount//2],(self.x,self.y))
#             self.walkCount+=1
        
#            elif self.right and self.isjump==False: #right true and isjump false
#             win.blit(walkRight[self.walkCount//2],(self.x,self.y)) #in dono mai 2 oictures ko switch krwaya jarha hai tak animation show ho sky
#             self.walkCount+=1
        
#            elif self.right and self.isjump: #matlab dono True hon
#             win.blit(walkRight[2],(self.x,self.y))
      
        
#            elif self.left and self.isjump: #matlab dono True hon
#             win.blit(walkLeft[2],(self.x,self.y))
        
#            else:#agar jump wali position hai hi nhi to stand wali image dikha do
#              win.blit(stan,(self.x,self.y))
           
class weapons():
    def __init__(self,x,y,width,height,facing):
        self.x=x
        self.y=y
        self.height=height
        self.width=width
        self.facing=facing
        self.vel=8*facing
        
    def draw(self,win):
        win.blit(pygame.image.load("pics\\shur.png"), (self.x, self.y))
        

run=True

# def redrawgamewindow():
#     win.blit(bg,(0,0)) #blit kisi image ko kahin p lgany k use hota hai yahn p yeh window k uper bg wali pic lga rha hai
#     naruto.draw(win)
#     for shurikane in shurikanes:
#         shurikane.draw(win) #image aygi hr shoot p matlab jitni weapon phenjy ga utni pics
    
# naruto=player(500,400,100,100) #uper jo x y height width di thi ab unki values din
# shurikanes=[]
# throwspeed=0 

# while run: #matlab run==TRUE hai
    
#     # pygame.time.delay(50) #actually mai frames per second decide kry ga kitny second mai kitni picture render krni hain
#     Clock.tick(50)
#     #weapon kab phenkni
#     if throwspeed>0:
#         throwspeed+=1
        
#     if throwspeed>3:
#         throwspeed=0
 
    
    
#     for event in pygame.event.get(): 
#         if event.type==pygame.QUIT:
#             run=False
            
#     for shurikane in shurikanes:
#         if shurikane.x<760 and shurikane.x>0: #yahan whi boujndry set ki hai jo neechy ki thi
#             shurikane.x+=shurikane.vel
#         else:
#             shurikanes.pop(shurikanes.index(shurikane)) #otherwise usko delete krdo
            
     
#     keys=pygame.key.get_pressed() #konsi key dab rhi hai user se
    
    
#     #shooting
#     if keys[pygame.K_SPACE] and throwspeed==0:
#         if naruto.left==True:
#             facing=-1 #matlab agar character left hua to weapon ka face bhi left and same for right
#         else:
#             facing=1
#         if len(shurikanes)<5: #calss tabhi kaam ay jab shoot krna ho isiliy loop mai object bna rhy
#              shurikanes.append(weapons(round(naruto.x+naruto.width//2),round(naruto.y+naruto.height//2),40,40,facing)) #issy weapon character k center se ayngi matkab width or x k centre se and height or y k center se and usk baad dimension dali pic ki
#         throwspeed=1
    
    
    
    
    
    
#     if keys[pygame.K_LEFT] and naruto.x>naruto.speed: #yeh pygame ka format hai jo k documentation p availiable hai sab keys ka
#         naruto.x-=naruto.speed #agar left jana hai to x axis k ulta utni hi speed k - mai jany lag jaygato
#         naruto.left= True #CHARACRER aninmation k liy ab yeh add kia
#         naruto.right= False
#     elif keys[pygame.K_RIGHT] and naruto.x<760-naruto.width-naruto.height: #and k baad wala actually mai left right ki boundry set krrha again equations are already made by someone hum sirf change krk dekh skty kissy kia hota
#         naruto.x+=naruto.speed 
#         naruto.right=True
#         naruto.left=False
#     else:
#          naruto.left=False
#          naruto.right=False
#          naruto.walkCount=0
    
    
#     if naruto.isjump==False: #matlab cahracter khara hai koi jump ni lgai #remember idher assigment operator use kia hua hai kafi dfa eroor aya tha is wja se 
#          if keys[pygame.K_UP]: #jump k liy UP lgayngy ab space se shoot
#             naruto.isjump=True
#             naruto.left=False
#             naruto.right=False
#             naruto.walkCount=0
#     else:
#         if naruto.jumpheight >=-10: #humny space dba k jump krwaya uper jaty huy g ki value + hoti hai neechy aty huy same value - hojati hai humny physics mai prha hua hai to matlab actually mai 10 ka jump lag gya ab same 10 - mai yani neechy ly k ao isko
#             neg=1
#             if naruto.jumpheight<0:
#                   neg=-1  
          
#             naruto.y-=(naruto.jumpheight**2)*0.5*neg #yeh equaion already kisi ne test krk bnai hai no such explanation for this
#             naruto.jumpheight-=1
#         else:
#             naruto.isjump=False 
#             naruto.jumpheight=10 #matlab ab jump nhi kia to jump ki value wapis 10 hogai matlab agli abri + direction yani uper hi jayga

   

#     redrawgamewindow()
#     pygame.display.update()
# pygame.Quit()
   
