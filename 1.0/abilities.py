#from globals import *
import random as R
import gstate
import math
import time
from renderable import *
from event import *
from animation import *
from aicomponent import *

from auxiliary_functions import *


class ability_abstract:
    def __init__(self, name, level, ability_type = " ", value = 0, area_of_effect = []):
        self.name = name
        self.level = level
        self.ability_type = ability_type
        self.value = value
        #animation([0,-1],"explosion",0),
        #self.animation = [animation(i[0],i[3],i[1]) for i in area_of_effect]
        self.animation = [[i[3],i[1]] for i in area_of_effect]
        if self.ability_type == "damage_per_tick":
            self.area_of_effect = [i[0] for i in area_of_effect]
            self.time_to_effect = [[j*gstate.get().tick_time for j in range(round(i[1]* 1/gstate.get().tick_time),round(i[2]* 1/gstate.get().tick_time))] for i in area_of_effect]
            #self.time_to_effect = [area_of_effect[1] + i*gstate.get().tick_time for i in range(0, area_of_effect[2] * round(1/gstate.get().tick_time))]

            print("aqui no damage per tick: " + str(len(range(0,round(area_of_effect[0][2]* 1/gstate.get().tick_time)))))
        elif self.ability_type == "damage":
            self.area_of_effect = [i[0] for i in area_of_effect]
            self.time_to_effect = area_of_effect[0][1]
        else:
            self.area_of_effect = [i[0] for i in area_of_effect]
            self.time_to_effect = [i[1] for i in area_of_effect]
    
    def define(self, target):
        return ability(self.name, self.level, self.ability_type,self.value,self.area_of_effect, target,self.time_to_effect, self.animation)


class ability:
    def __init__(self, name, level, ability_type = "", value = 0,area_of_effect = [], target = "",time_to_effect=0, animation = []):
        self.name = name
        self.level = level
        self.ability_type = ability_type
        self.value = value
        
        self.area_of_effect = area_of_effect
        self.target = target
        self.animation = animation
        self.time_to_effect = time_to_effect

        
        #self.targetnumber = targetnumber # the number of targets the ability has.
        #self.selftarget = selftarget # its suposed to be True or False, if the caster can target himself or not.
        #self.damage = damage #suposed to be True or False
        #self.abilitytype = abilitytype
        #self.worked = worked
        #self.cooldown = cooldown
        #self.channel = channel
        #self.Return = Return 
        #self.element = element
        #self.orbs = orbs
        #self.proficiencyneeded = proficiencyneeded
        #self.proficiencygiven = proficiencygiven
        #self.value = value
        #self.text = text
        
        
    #  [  [[pypgame.image.load("tank_explosion5.png"),0.5,1],[pypgame.image.load("tank_explosion5.png"),0.5,1]]   ,[pypgame.image.load("tank_explosion5.png"),1.5,1],[],[]] )
    
    # def create_animation(self):
        # #print(self.animation)
        # for i in range(len(self.animation)):
            
            # #print(self.animation[i])
            # square = self.calculate_area([self.animation[i][0]])[0]

            
            # x = gstate.get().arena.square_width * square[0]
            # y = gstate.get().arena.square_height * square[1]
            # for j in self.animation[i][1:]:
                # #print(j)
                # image = j[0]
                # time_to_start = j[1]
                # #time_to_end = time_to_start + j[2]
                # time_to_end = j[2]
                # gstate.get().arena.animations.append([imagerenderable(x,y,image),time_to_start,time_to_end,self.target.facing_index])
                
    # def create_animation(self):
        # #print(self.animation)
        # for i in range(len(self.animation)):
            
            # #print(self.animation[i])
            # square = self.calculate_area([self.animation[i].position])[0]

            
            # x = gstate.get().arena.square_width * square[0]
            # y = gstate.get().arena.square_height * square[1]
            # self.animation[i].animate([x,y],self.target.facing_index)

                
    # def create_animation(self):
        # #print(self.animation)
        # for i in range(len(self.animation)):
            
            # #print(self.animation[i])
            # square = self.calculate_area([self.animation[i][0]])[0]

            
            # x = gstate.get().arena.square_width * square[0]
            # y = gstate.get().arena.square_height * square[1]
            # for j in self.animation[i][1:]:
                # #print(j)
                # image = j[0]
                # time_to_start = j[1]
                # #time_to_end = time_to_start + j[2]
                # time_to_end = j[2]
                # gstate.get().arena.animations.append([imagerenderable(x,y,image),time_to_start,time_to_end])
    
    
    def calculate_area(self,area_of_effect):
    
        area = []
        facing = self.target.facing() # isto pode ser [0,-1],[1,0],[0,1],[-1,0]

        for i in area_of_effect:
            if facing == [0,-1]:
                actual_area_of_effect = i[:]
                
            elif facing == [1,0]:
                actual_area_of_effect = [-i[1],-i[0]]
                
            elif facing == [0,1]:
                actual_area_of_effect = [-i[0],-i[1]]
                
            elif facing == [-1,0]:
                actual_area_of_effect = [i[1],i[0]]
                
            area.append(add_lists(actual_area_of_effect,self.target.position))
        return area
        
    
    def effect(self):
        #print("aqui no effect")
        
        area = self.calculate_area(self.area_of_effect)
        
        
        
            
            
        #self.create_animation()
        #if self.name == "teleport":
            #print(str(self.target.position))
            #print(str(self.area_of_effect[0]))
        #    self.target.position = add_lists(self.target.position, self.area_of_effect[0]) 
            
            
        #elif self.name == "Walk":
            #print(str(self.target.position))
            #print(str(self.area_of_effect[0]))
        #    self.target.position = add_lists(self.target.position, self.target.ai_component.trajectory[0]) 
        
        if self.ability_type == "damage":
            for i in range(len(area)):
                #gstate.get().arena.events.append(event("damage",area[i],self.time_to_effect,self.value,self.animation[i]))
                gstate.get().arena.events.append(event("damage",area[i],0,self.value,self.animation[i],self.target.facing_index))
        
        elif self.ability_type == "damage_per_tick":
            for i in range(len(area)):
                gstate.get().arena.events.append(event("damage",area[i],0,0,self.animation[i],self.target.facing_index))
                for j in self.time_to_effect[i]:
                    value = self.value / len(self.time_to_effect[i])
                    gstate.get().arena.events.append(event("damage",area[i],j,value,["nothing",0],self.target.facing_index))
                    
        elif self.ability_type == "summon":
            print("time to effect no summon: " + str(self.time_to_effect))
            position = area[0]
            time_to_effect = self.time_to_effect[0]
            
            
            
            creature_summoned = [i for i in gstate.get().creatures_abstract if i.name == self.value][0].define(ai_component_zombie(gstate.get().id_creature,enemies = [i for i in gstate.get().arena.creatures if i.name != self.target.name]),position)
            gstate.get().arena.add_event(event("summon",position,time_to_effect+2, creature_summoned,["nothing",0],self.target.facing_index))
            gstate.get().arena.add_event(event("nothing",position,time_to_effect, 0,self.animation[0],self.target.facing_index))
            
            
        elif self.ability_type == "pull bow":
            print("pulling the bow -> abilities")
            self.target.ai_component.pulling_bow = True
        
        elif self.ability_type == "release bow":
            print("releasing the bow -> abilities")
            if self.target.ai_component.pulling_bow == True:
                [i for i in self.target.items if i.item_type == "bow"][0].effect(area[0],self.target.facing_index)
                #gstate.get().arena.events.append(event("projectile",))
            
            self.target.ai_component.pulling_bow = False
            
        elif self.ability_type == "projectile":
            print("firebolt -> abilities")
            gstate.get().arena.add_event(event("projectile",area[0],0.1, self.value,[self.animation[0][0],0],self.target.facing_index, value_2 = 13))
            
        elif self.ability_type == "lightning bolt":
            print("lightning bolt -> abilities")
            gstate.get().arena.add_event(event("lightning bolt",area[0],gstate.get().tick_time , self.value,[self.animation[0][0],0],self.target.facing_index, value_2 = 2))
        elif self.ability_type == "chain lightning":
            print("chain lightning -> abilities")
            gstate.get().arena.add_event(event("chain lightning",area[0],gstate.get().tick_time * 2, self.value,[self.animation[0][0],0],self.target.facing_index, value_2 = 200))
            
            #gstate.get().arena.add_creature(creature_summoned)
                    
        # elif self.name == "Fire Breath":
            
            # for i in range(len(area)):
                # for j in self.time_to_effect[i]:
                    # gstate.get().arena.events.append(event("damage",area[i],j,value = 0.5))
                # #bol, creatures = creature_in_place(i)
                # #if bol:
                # #    for j in creatures:
                # #        j.HP -= 5
                        
        # elif self.name == "Fireball":
            # for i in range(len(area)):
                # for j in self.time_to_effect[i]:
                    # gstate.get().arena.events.append(event("damage",area[i],j,value = 2))
            # #for i in area:
            # #    bol, creatures = creature_in_place(i)
            # #    if bol:
            # #        for j in creatures:
            # #            j.HP -= 20
        # elif self.name == "Infernal beam":
            # for i in range(len(area)):
                # for j in self.time_to_effect[i]:
                    # gstate.get().arena.events.append(event("damage",area[i],j,value = 4.9)) 

        # elif self.name == "Heat wave":
            # for i in range(len(area)):
                # gstate.get().arena.events.append(event("damage",area[i],self.time_to_effect[i],value = 25))  
        #elif self.name == "Pause":
        #    gstate.get().pause = True
                    
                
            
            
class movement_abstract:
    def __init__(self, name, level):
        self.name = name
        self.level = level
    
    def define(self, target):
        return movement(self.name, self.level, target)


class movement:
    
    def __init__(self, name, level, target,time_to_effect = 0):
        self.name = name
        self.level = level
        self.target = target
        self.time_to_effect = time_to_effect
    

    def effect(self):
        #print("aqui no effect")
        #if self.name == "teleport":
            #print(str(self.target.position))
            #print(str(self.area_of_effect[0]))
            #self.target.position = add_lists(self.target.position, self.area_of_effect[0]) 
            
            
        if self.name == "Walk":
            #print(str(self.target.position))
            #print(str(self.area_of_effect[0]))
            if anything_in_place(add_lists(self.target.position, self.target.ai_component.trajectory[0]))[0]:
                pass

            else:
                self.target.position = add_lists(self.target.position, self.target.ai_component.trajectory[0]) 
            self.target.ai_component.trajectory = self.target.ai_component.trajectory[1:]
            
        elif self.name == "Teleport":
            #print(str(self.target.position))
            #print(str(self.area_of_effect[0]))
            self.target.position = add_lists(self.target.position, self.target.ai_component.trajectory[0]) 
            self.target.ai_component.trajectory = self.target.ai_component.trajectory[1:]
            
        elif self.name == "Turn":
            self.target.facing_index = (self.target.facing_index + 1) % 4
            
        elif self.name == "Dash":
            hit = False
            for i in range(5):
                if not hit:
                    self.target.ai_component.trajectory.insert(0,self.target.facing())
                    if anything_in_place(add_lists(self.target.position, self.target.ai_component.trajectory[0]))[0]:
                        hit = True
                        self.target.ai_component.trajectory = self.target.ai_component.trajectory[1:]
                    else:
                        
                        self.target.decisions.append([self.target,i * 0.1,gstate.get().movements["walk"].define(self.target)])
                        #self.target.position = add_lists(self.target.position, self.target.ai_component.trajectory[0]) 
                    #self.target.ai_component.trajectory = self.target.ai_component.trajectory[1:]
                    
                    
        elif self.name == "Backflip":
            hit = False
            for i in range(3):
                if not hit:
                    self.target.ai_component.trajectory.insert(0,multiply_lists(self.target.facing(),[-1,-1]))
                    if anything_in_place(add_lists(self.target.position, self.target.ai_component.trajectory[0]))[0]:
                        hit = True
                        self.target.ai_component.trajectory = self.target.ai_component.trajectory[1:]
                    else:
                        
                        self.target.decisions.append([self.target,i * 0.1,gstate.get().movements["walk"].define(self.target)])
                        #self.target.position = add_lists(self.target.position, self.target.ai_component.trajectory[0]) 
                    #self.target.ai_component.trajectory = self.target.ai_component.trajectory[1:]
                    
        elif self.name == "High Jump":
            self.target.ai_component.trajectory.insert(0,self.target.facing())
            bol,a = anything_in_place(add_lists(self.target.position, self.target.ai_component.trajectory[0]))
            if [i for i in a if i.name == "edge_of_the_map"] == []:
                print("estive aqui no high jump")
                self.target.decisions.append([self.target,0.1,gstate.get().movements["teleport"].define(self.target)])
            else:
                self.target.ai_component.trajectory = self.target.ai_component.trajectory[1:]
                
            self.target.ai_component.trajectory.insert(0,self.target.facing())
            bol_1,a_1 = anything_in_place(add_lists(self.target.position, multiply_lists(self.target.ai_component.trajectory[0],[2,2])))
            if bol and bol_1:
                self.target.ai_component.trajectory = self.target.ai_component.trajectory[1:]
                self.target.ai_component.trajectory.insert(0,multiply_lists(self.target.facing(),[-1,-1]))
                self.target.decisions.append([self.target,0.1,gstate.get().movements["walk"].define(self.target)])
            else:
                self.target.decisions.append([self.target,0.1,gstate.get().movements["walk"].define(self.target)])
                
                    
                

            
    def show(self):
        return str([self.name,str(self.level),str(self.target.name)])
            

            
