import gstate
import pygame
from renderable import *

class animation:

    def __init__(self,position,animation_type,time_to_start):
    
        self.position = position
        self.animation_type = animation_type
        self.time_to_start = time_to_start
        self.animation = []
        
            
            
    def animate(self,coordenates,facing):    
        #if self.animation_type == "explosion":
        #    self.animation = [[pygame.image.load("tank_explosion5.png"),0,0.3],[pygame.image.load("tank_explosion2.png"),0.3,0.6],[pygame.image.load("tank_explosion3.png"),0.6,1]]
        if self.animation_type == "explosion":
            self.animation = [[pygame.image.load("ima\explosion1.png"),0,0.2],[pygame.image.load("ima\explosion2.png"),0.2,0.4],[pygame.image.load("ima\explosion3.png"),0.4,0.7],[pygame.image.load("ima\explosion4.png"),0.7,1]]
        
        elif self.animation_type == "slash":
            print("ima\slash_"+str(facing)+".png")
            self.animation = [[pygame.image.load("ima\slash_"+str(facing)+".png"),0,0.4]]
        elif self.animation_type == "thrust":
            print("ima\sword_"+str(facing)+".png")
            self.animation = [[pygame.image.load("ima\sword_"+str(facing)+".png"),0,0.5]]    
        
        elif self.animation_type == "arrow":
            print("aqui no animation -> arrow")
            self.animation = [[pygame.image.load("arrow_"+str(facing)+".png"),0,0.1]]    
        
        elif self.animation_type == "firebolt":
            print("aqui no animation")
            self.animation = [[pygame.image.load("ima\explosion1.png"),0,0.1]]  
            
        elif self.animation_type == "lightning bolt":
            print("aqui no animation")
            self.animation = [[pygame.image.load("ima\lightning_"+str(facing)+".png"),0,gstate.get().tick_time * 3]]  

        elif self.animation_type == "create zombie":
            self.animation = [[pygame.image.load("ima\zombie_hand.png"),0,0.5],[pygame.image.load("ima\zombie_17.jpg"),0.5,0.65],[pygame.image.load("ima\zombie_16.jpg"),0.65,0.8],[pygame.image.load("ima\zombie_15.jpg"),0.8,0.95],[pygame.image.load("ima\zombie_14.jpg"),0.95,1.1],[pygame.image.load("ima\zombie_13.jpg"),1.1,1.25],[pygame.image.load("ima\zombie_12.jpg"),1.25,1.4],[pygame.image.load("ima\zombie_11.jpg"),1.4,1.65],[pygame.image.load("ima\zombie_10.jpg"),1.65,2]]  
        elif self.animation_type == "nothing":
            pass
        for j in self.animation:
            image = j[0]

            time_to_start = j[1] + self.time_to_start
                #time_to_end = time_to_start + j[2]
            time_to_end = j[2] + self.time_to_start
            gstate.get().arena.animations.append([imagerenderable(coordenates[0],coordenates[1],image),time_to_start,time_to_end])