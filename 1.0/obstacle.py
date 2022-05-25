from renderable import *

class obstacle:
    def __init__(self,name,position = [5,5],images = [],coordenates = [],height = 1000):
  
        self.name = name
        self.images = images
 
        self.position = position
        self.height = height
        
            
        if coordenates == []:
            self.coordenates = [gstate.get().arena.square_width * self.position[0], gstate.get().arena.square_height * self.position[1]]
        else:
            self.coordenates = coordenates
        

        self.HP = 1000
        self.renderables = []
        
        for i in self.images:
            self.renderables.append(imagerenderable(self.coordenates[0],self.coordenates[1],i))
        
    def draw(self,screen):
        
        for r in self.renderables:
            r.draw(screen)
            
        
    def clock(self):
        pass