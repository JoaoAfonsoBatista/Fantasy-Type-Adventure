from renderable import *
from event import *
from obstacle import *
import gstate
import random as R

class arena():
    def __init__(self,width,height, objects = [], creatures = [], events = [], corpses = [], animations = [],obstacles = []):
        self.width = width
        self.height = height
        
        
        self.animations = animations #animation é [renderable.image, time_to_start, time_to_end]
        
        #self.square_width = gstate.get().arena_width/self.width
        
        #self.square_height = gstate.get().arena_height/self.height


        self.square_width = 40
        
        self.square_height = 40
        
        self.real_width = width * self.square_width
        
        self.real_height = height * self.square_height
        
        
        if objects !=[]:
            self.objects = objects
        else:
            self.objects = self.create_objects()
        self.creatures = creatures
        self.events = events
        self.corpses = corpses
        if obstacles != []:
            self.obstacles = obstacles
        else:
            self.obstacles = self.create_obstacles()
        self.create_edge_of_the_map()
        self.renderables = self.create_map_renderables()
        
    def create_objects(self):
        return []
        
    def create_edge_of_the_map(self):
        x = -1
        y_0 = -1
        y_1 = self.height
        for i in range(self.width+2):

            
            coor_x = x*self.square_width
            coor_y_0 = y_0*self.square_height 
            coor_y_1 = y_1*self.square_height 
            
            #r.append(imagerenderable(coor_x,coor_y_1,pygame.image.load("ima\map_green_obstacle_1.png")))#    transparent.png
            self.obstacles.append(obstacle("edge_of_the_map",[x,y_0],[pygame.image.load("transparent.png")],[coor_x,coor_y_0]))
            self.obstacles.append(obstacle("edge_of_the_map",[x,y_1],[pygame.image.load("transparent.png")],[coor_x,coor_y_1]))
            x += 1
        
        x_0 = -1
        y = 0
        x_1 = self.width
        for i in range(self.width):
            coor_x_0 = x_0*self.square_width
            coor_y = y*self.square_height 
            coor_x_1 = x_1*self.square_width 
            #r.append(imagerenderable(x,y,pygame.image.load("ima\map_green_obstacle_1.png")))
            self.obstacles.append(obstacle("edge_of_the_map",[x_0,y],[pygame.image.load("transparent.png")],[coor_x_0,coor_y]))
            self.obstacles.append(obstacle("edge_of_the_map",[x_1,y],[pygame.image.load("transparent.png")],[coor_x_1,coor_y]))
            y += 1
            
    def create_obstacles(self):
        obs = []
        for i in range(5):
            x = R.randint(0,self.width-2)
            y = R.randint(0,self.height-2)
            
            
            x_1 = x*self.square_width
            y_1 = y*self.square_height - 20
            #r.append(imagerenderable(x,y,pygame.image.load("ima\map_green_obstacle_1.png")))
            obs.append(obstacle("tree",[x,y],[pygame.image.load("ima\map_green_obstacle_1.png")],[x_1,y_1],3))
            
        x = -1
        y_0 = -1
        y_1 = self.height
        for i in range(self.width+2):

            
            coor_x = x*self.square_width
            coor_y_0 = y_0*self.square_height 
            coor_y_1 = y_1*self.square_height 
            
            #r.append(imagerenderable(coor_x,coor_y_1,pygame.image.load("ima\map_green_obstacle_1.png")))#    transparent.png
            obs.append(obstacle("edge_of_the_map",[x,y_0],[pygame.image.load("transparent.png")],[coor_x,coor_y_0]))
            obs.append(obstacle("edge_of_the_map",[x,y_1],[pygame.image.load("transparent.png")],[coor_x,coor_y_1]))
            x += 1
        
        x_0 = -1
        y = 0
        x_1 = self.width
        for i in range(self.width):
            coor_x_0 = x_0*self.square_width
            coor_y = y*self.square_height 
            coor_x_1 = x_1*self.square_width 
            #r.append(imagerenderable(x,y,pygame.image.load("ima\map_green_obstacle_1.png")))
            obs.append(obstacle("edge_of_the_map",[x_0,y],[pygame.image.load("transparent.png")],[coor_x_0,coor_y]))
            obs.append(obstacle("edge_of_the_map",[x_1,y],[pygame.image.load("transparent.png")],[coor_x_1,coor_y]))
            y += 1
        return obs
        
    def create_map_renderables(self):
        r = []

        
        #r.append(imagerenderable(0,0,pygame.image.load("ima\map_green.png")))
        x = 0
        for i in range(self.width):
            y = 0
            for i in range(self.height):
                r.append(imagerenderable(x,y,pygame.image.load("ima\map_green.png")))
                y = y + self.square_height
            x = x + self.square_width
        
        for i in range(5):
            x = R.randint(0,self.real_width-64)
            y = R.randint(0,self.real_height-64)
            r.append(imagerenderable(x,y,pygame.image.load("ima\map_green_1.png")))
        for i in range(75):
            x = R.randint(0,self.real_width-32)
            y = R.randint(0,self.real_height-32)
            r.append(imagerenderable(x,y,pygame.image.load("ima\map_green_2.png")))
            
        

            
            
            
        #x = 0
        #for i in range(self.width):
        #    r.append(rectrenderable(x,0,1,self.real_height,gstate.get().light_orange))
        #    x = x + self.square_width
        #este ultimo é colocado à parte para estar um pixel mais para dentro do ecra para aparecer
        #r.append(rectrenderable(x-1,0,1,self.real_height,gstate.get().light_orange)) 
            
            
        #y = 0
        #for i in range(self.height):
        #    r.append(rectrenderable(0,y,self.real_width,1,gstate.get().light_orange))
        #    y = y + self.square_height
        #r.append(rectrenderable(0,y-1,self.real_width,1,gstate.get().light_orange))
        
        
        

        
        return r
        
        
    def recreate_arena(self):
        return arena(self.width,self.height,self.objects,self.creatures,self.events,self.corpses,self.animations,self.obstacles)
        
    def clock(self):
        #rint(len(self.events))
        for r in self.events:
            r.clock()
            r.time_to_effect -= gstate.get().tick_time
            if r.time_to_effect <= 0:
                r.effect()
            
        self.events = [i for i in self.events if i.time_to_effect > 0]
        for r in self.obstacles:
            r.clock()
            
        for r in self.objects:
            r.clock()
            
        for r in self.creatures:
            r.clock()
            
        for r in self.corpses:
            r.clock()
            
        for r in self.animations:
            if r[2] <= 0:
                pass
            else:
                #r.time_to_start -= gstate.get().tick_time
                r[1] -= gstate.get().tick_time
                #r.time_to_end -= gstate.get().tick_time
                r[2] -= gstate.get().tick_time
        self.animations = [i for i in self.animations if i[2] > 0]    


    def add_object(self,Object):
        self.objects.append(Object)

    def add_creature(self,creature):
        self.creatures.append(creature)
        
    def add_event(self,event):
        self.events.append(event)
    def add_object(self,obstacle):
        self.obstacles.append(obstacle)

    def draw(self,screen):
        for r in self.renderables:
            r.draw(screen)
        for r in self.obstacles:
            r.draw(screen)
        for r in self.objects:
            r.draw(screen)
        for r in self.corpses:
            r.draw(screen)
        for r in self.creatures:
            r.draw(screen)
        
        for r in [i for i in self.animations if i[1] <= 0]:
            r[0].draw(screen)
    
