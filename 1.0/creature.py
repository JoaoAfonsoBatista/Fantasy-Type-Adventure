import gstate
from abilities import *

from renderable import *
#from abilities import *
from aicomponent import *
from item import *

class creature_abstract:

    def __init__(self, name,images):
        self.name = name
        #self.color = color
        self.images = images
    def define(self, ai_component ,position = [0,0]):
        return creature(self.name,ai_component, position = position, images = self.images)
        
        
class creature:
    def __init__(self,name, ai_component, STR = 0,DEX = 0,CON = 0,INT = 0, WIS = 0, SOUL = 0, position = [5,5],color = (0,0,0), images = []):
        
        self.id = gstate.get().id_creature
        gstate.get().id_creature += 1
        print("id_creature: " + str(gstate.get().id_creature))
        
        self.name = name
            
        self.STR = STR
        self.DEX = DEX
        self.CON = CON
        self.INT = INT
        self.WIS = WIS
        self.SOUL = SOUL
        
        self.color = color
        
        self.images = images
        
        self.facing_index = 0

        self.abilities = []
        self.EXP = []
        self.items = []
        
        #self.time_between_ability = [0, 5, 20, 60]
        
        #self.time_since_ability_cast = [0,0,0,0]
        
        
        
        
        self.position = position
        
        self.coordenates = [gstate.get().arena.square_width * self.position[0], gstate.get().arena.square_height * self.position[1]]
        
        if self.images != []:
            self.renderables = [imagerenderable_changeble(lambda: self.coordenates[0], lambda: self.coordenates[1], lambda:self.images[self.facing_index])]
        
        else:
        
            self.renderables = [rectrenderable_changeble(lambda: self.coordenates[0], lambda: self.coordenates[1], lambda: gstate.get().arena.square_width, lambda:gstate.get().arena.square_height, lambda:self.color)]
        
        
        
        self.decisions = []
        
        #self.used_abilities = []
        
        self.used_abilities = [gstate.get().abilities["born"]]
        
        self.ai_component = ai_component
        
        self.MAX_HP = self.calculate_MAX_HP()

        self.HP = self.calculate_HP()

        if self.name == "skeleton":
            self.items.append(item(name = "regular bow", item_type = "bow", cooldown = 1, damage = 6))
            
        
        #self.image = rectrenderable(self.coordenates[0], self.coordenates[1], gstate.get().arena.square_width, gstate.get().arena.square_height, gstate.get().cyan)
        
    
    def restart(self):
        self.facing_index = 0
        self.HP = self.calculate_HP()
        self.ai_component.restart()
    
    def facing(self):
        return gstate.get().facing_cycle[self.facing_index]
    
    def draw(self,screen):
        
        for r in self.renderables:
            r.draw(screen)
            
        self.ai_component.draw(screen)
        
    def clock(self):
        #print(self.name + " " + str(self.HP))
        for r in self.items:
            r.clock()
            
        self.ai_component.clock()
        for i in self.decisions:
            i[1] -= gstate.get().tick_time
            if i[1] <= 0:
                #print("aqui no clock do creature")
                #if self.name == "vacaboy":
                    #print(i[2].show())
                    #print(self.ai_component.trajectory)
                i[2].effect()
                self.used_abilities.insert(0,i[2])
        self.decisions = [i for i in self.decisions if i[1]>0]
        
        
        
        self.coordenates = [gstate.get().arena.square_width * self.position[0], gstate.get().arena.square_height * self.position[1]]
        
        #a = ai_component_corpse(gstate.get().id_creature)
        
        #veify if this creature is dead:
        if self.HP <= 0:
            self.death()
            
    def death(self):
        #gstate.get().arena.corpses.append(corpse(self.name + "-dead", self.MAX_HP, self.position, self.color))
        #gstate.get().arena.corpses.append(corpse(self.name + "-dead", self.MAX_HP, ai_component_corpse(gstate.get().id_creature), self.position, self.color))
        #gstate.get().arena.corpses.append(corpse(self.name + "-dead", self.MAX_HP, ai_component_objective(gstate.get().id_creature, [10,10]), self.position, self.color))
        gstate.get().arena.creatures.remove(self)

    def start_round(self):
        self.power = self.calculate_power()
        self.initiative = self.calculate_initiative()
        
    def calculate_power(self):
        pass
        
    def calculate_initiative(self):
        pass
        
    def calculate_MAX_HP(self):
        if self.name == "zombie":
            
            return 70
        elif self.name == "skeleton":
            return 20
        elif self.name == "target":
            return 1
        return 50
        return self.CON*10

    def calculate_HP(self):
        if self.name == "zombie":
            return 70
        elif self.name == "skeleton":
            return 20
        elif self.name == "target":
            return 1
        return 45
        return self.MAX_HP
        
        
class corpse:
    def __init__(self,name, MAX_HP, ai_component, position = [5,5],color = (0,0,0),abilities = [], EXP = [], items = []):
        
        self.id = gstate.get().id_creature
        gstate.get().id_creature += 1
        print("id_creature: " + str(gstate.get().id_creature))
        
        self.name = name
            
        
        self.color = color

        self.abilities = abilities
        self.EXP = EXP
        self.items = items
        
        self.HP = 0
        self.MAX_HP = MAX_HP
        
        
        
        
        self.position = position
        
        self.coordenates = [gstate.get().arena.square_width * self.position[0], gstate.get().arena.square_height * self.position[1]]
        
        self.renderables = [rectrenderable_changeble(lambda: self.coordenates[0], lambda: self.coordenates[1], lambda: gstate.get().arena.square_width, lambda:gstate.get().arena.square_height, lambda:self.color)
                            ,textrenderable_changeble(lambda: self.coordenates[0] + 5,lambda: self.coordenates[1] + 5, lambda: gstate.get().black, lambda: gstate.get().fontHP, lambda: "R.I.P")]
        
        
        self.decisions = []
        
        self.used_abilities = [ability("die", 1, [], self)]
        
        self.ai_component = ai_component
        
        
    def draw(self,screen):
        
        for r in self.renderables:
            r.draw(screen)
            
        self.ai_component.draw(screen)
        
        
    def clock(self):
        self.ai_component.clock()
        for i in self.decisions:
            i[1] -= gstate.get().tick_time
            if i[1] <= 0:
                #print("aqui no clock do creature")
                #if self.name == "vacaboy":
                    #print(i[2].show())
                    #print(self.ai_component.trajectory)
                i[2].effect()
                self.used_abilities.insert(0,i[2])
        self.decisions = [i for i in self.decisions if i[1]>0]
        
        
        
        self.coordenates = [gstate.get().arena.square_width * self.position[0], gstate.get().arena.square_height * self.position[1]]
        
  