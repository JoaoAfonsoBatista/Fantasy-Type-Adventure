from renderable import *
from event import *
import gstate

class arena():
    def __init__(self,width,height, objects = [], creatures = [], events = [], corpses = [], animations = []):
        self.width = width
        self.height = height
        self.objects = objects
        self.creatures = creatures
        self.events = events
        self.corpses = corpses
        
        self.animations = animations #animation é [renderable.image, time_to_start, time_to_end]
        
        self.square_width = gstate.get().arena_width/self.width
        
        self.square_height = gstate.get().arena_height/self.height

        
        self.renderables = self.create_map_renderables()
        
        
        
    def create_map_renderables(self):
        r = []

        
        #r.append(imagerenderable(0,0,pygame.image.load("ima\map_green.png")))
        x = 0
        for i in range(self.width):
            y = 0
            for i in range(self.height):
                r.append(imagerenderable(x,y,pygame.image.load("ima\map_green.png")))
                y = y + gstate.get().arena_height/self.height
            x = x + gstate.get().arena_width/self.width
            
        x = 0
        for i in range(self.width):
            r.append(rectrenderable(x,0,1,gstate.get().arena_height,gstate.get().light_orange))
            x = x + gstate.get().arena_width/self.width
        #este ultimo é colocado à parte para estar um pixel mais para dentro do ecra para aparecer
        r.append(rectrenderable(x-1,0,1,gstate.get().arena_height,gstate.get().light_orange)) 
            
            
        y = 0
        for i in range(self.height):
            r.append(rectrenderable(0,y,gstate.get().arena_width,1,gstate.get().light_orange))
            y = y + gstate.get().arena_height/self.height
        r.append(rectrenderable(0,y-1,gstate.get().arena_width,1,gstate.get().light_orange))
        
        
        

        
        return r
        
        
    def recreate_arena(self):
        return arena(self.width,self.height,self.objects,self.creatures,self.events,self.corpses,self.animations)
        
    def clock(self):
        #rint(len(self.events))
        for r in self.events:
            r.clock()
            r.time_to_effect -= gstate.get().tick_time
            if r.time_to_effect <= 0:
                r.effect()
            
        self.events = [i for i in self.events if i.time_to_effect > 0]
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


    def draw(self,screen):
    
        for r in self.renderables:
            r.draw(screen)
        
        for r in self.objects:
            r.draw(screen)
        for r in self.corpses:
            r.draw(screen)
        for r in self.creatures:
            r.draw(screen)
        
        for r in [i for i in self.animations if i[1] <= 0]:
            r[0].draw(screen)
    
