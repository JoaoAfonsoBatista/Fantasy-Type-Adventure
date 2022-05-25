import gstate
from auxiliary_functions import *
from animation import *
#from creature import *
#from aicomponent import *
import random as R

class event:
    def __init__(self, name, square, time_to_effect,value = 0, animation = [],facing = 0, value_2 = 0):
        self.name = name
        self.square = square
        self.time_to_effect = time_to_effect
        self.value = value
        self.animation = animation
        self.facing = facing
        self.value_2 = value_2
        
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
    def create_animation(self):
        #print(self.animation)

            
            #print(self.animation[i])

        if self.animation != []:
            x = gstate.get().arena.square_width * self.square[0]
            y = gstate.get().arena.square_height * self.square[1]
            #print("coisas no create_animation do event:")
            #print(str(self.square) + " " + str(self.animation[0])+ " " + str(self.animation[1]))
            animation(self.square,self.animation[0],self.animation[1]).animate([x,y],self.facing)

    def clock(self):
        pass
        #self.time_to_effect -= gstate.get().tick_time
            
    
    def effect(self):
        #print("aqui no effect")
        
        self.create_animation()
        
        
        if self.name == "teleport":
            #print(str(self.target.position))
            #print(str(self.area_of_effect[0]))
            self.target.position = add_lists(self.target.position, self.area_of_effect[0]) 
            
            
        elif self.name == "damage":
            #print(str(self.target.position))
            #print(str(self.area_of_effect[0]))
            bol, creatures = creature_in_place(self.square)
            if bol:
                for j in creatures:
                    j.HP -= self.value
                   
        elif self.name == "summon":
            gstate.get().arena.add_creature(self.value)
            
        elif self.name == "survival":
            if self.value > 0:
                x_max = gstate.get().arena.width - 1
                y_max = gstate.get().arena.height - 1
                x = R.randint(0,x_max)
                y = R.randint(0,y_max)
                
                a = R.randint(0,1)
                
                creatures = [gstate.get().zombie,gstate.get().skeleton]
                ai_components = [gstate.get().ai_component_zombie.define(gstate.get().id_creature,[gstate.get().vacaboy]),gstate.get().ai_component_skeleton.define(gstate.get().id_creature,[gstate.get().vacaboy])]
                
                position = [x,y]
                creature = creatures[a].define(ai_components[a],position)
                creature.facing_index = R.randint(0,3)
                if creature.name == "zombie":
                    creature.HP = 40
                gstate.get().arena.add_event(event("summon",position,0, creature,["nothing",0]))
                gstate.get().arena.add_event(event("survival",[0,0],8,self.value -1))
            
        elif self.name == "survival2":
            if self.value > 0:
                x_max = gstate.get().arena.width - 1
                y_max = gstate.get().arena.height - 1
                x = R.randint(0,x_max)
                y = R.randint(0,y_max)
                
                a = R.randint(0,1)
                
                creatures = [gstate.get().zombie,gstate.get().skeleton]
                ai_components = [gstate.get().ai_component_zombie.define(gstate.get().id_creature,[gstate.get().vacaboy]),gstate.get().ai_component_skeleton.define(gstate.get().id_creature,[gstate.get().vacaboy])]
                
                position = [x,y]
                creature = creatures[a].define(ai_components[a],position)
                creature.facing_index = R.randint(0,3)
                if creature.name == "zombie":
                    creature.HP = 40
                gstate.get().arena.add_event(event("summon",position,0, creature,["nothing",0]))
                gstate.get().arena.add_event(event("survival2",[0,0],6,self.value -1))
            
            
        elif self.name == "projectile":
            print("aqui no projectile")
            if self.value_2 <= 0:
                pass
            else:
                bol, a = anything_in_place(self.square)
                if bol:
                    for i in a:
                        i.HP -= self.value
                else:
                    gstate.get().arena.add_event(event("projectile",add_lists(self.square,gstate.get().facing_cycle[self.facing]),0.1, self.value,self.animation,self.facing, value_2 = self.value_2-1))
                    
        elif self.name == "lightning bolt":
            #print("aqui no lightning bolt -> events")
            if self.value_2 <= 0:
                pass
            else:
                bol, a = anything_in_place(self.square)
                if bol:
                    spread = False
                    for i in a:
                        i.HP -= self.value
                        if i.name != "edge_of_the_map" and not spread and self.value_2 > 1:
                            gstate.get().arena.add_event(event("lightning bolt",add_lists(self.square,gstate.get().facing_cycle[(self.facing+1)%4]),gstate.get().tick_time, self.value,self.animation,(self.facing+1)%4, value_2 = self.value_2-1))
                            gstate.get().arena.add_event(event("lightning bolt",add_lists(self.square,gstate.get().facing_cycle[(self.facing-1)%4]),gstate.get().tick_time, self.value,self.animation,(self.facing-1)%4, value_2 = self.value_2-1))
                            spread = True
                else:
                    gstate.get().arena.add_event(event("lightning bolt",add_lists(self.square,gstate.get().facing_cycle[self.facing]),gstate.get().tick_time, self.value,self.animation,self.facing, value_2 = self.value_2))
        
        elif self.name == "chain lightning":
            #print("aqui no chain lightning -> events")
            if self.value_2 <= 0:
                pass
            else:
                bol, a = anything_in_place(self.square)
                if bol:
                    spread = False
                    for i in a:
                        i.HP -= self.value
                        if i.name != "edge_of_the_map" and not spread and self.value_2 > 1:
                            gstate.get().arena.add_event(event("chain lightning",add_lists(self.square,gstate.get().facing_cycle[(self.facing+1)%4]),gstate.get().tick_time*2, self.value,self.animation,(self.facing+1)%4, value_2 = self.value_2-1))
                            gstate.get().arena.add_event(event("chain lightning",add_lists(self.square,gstate.get().facing_cycle[(self.facing-1)%4]),gstate.get().tick_time*2, self.value,self.animation,(self.facing-1)%4, value_2 = self.value_2-1))
                            spread = True
                else:
                    gstate.get().arena.add_event(event("chain lightning",add_lists(self.square,gstate.get().facing_cycle[self.facing]),gstate.get().tick_time*2, self.value,self.animation,self.facing, value_2 = self.value_2-1))
                    
        
        
        
        elif self.name == "nothing":
            pass   
        # elif self.name == "Fire Breath":
            
            # for i in range(len(area)):
                # gstate.get().arena.events.append(event(damage,5,rea[i],self.time_to_effect[i]))
                # #bol, creatures = creature_in_place(i)
                # #if bol:
                # #    for j in creatures:
                # #        j.HP -= 5
                        
        # elif self.name == "Fireball":
            
            # for i in area:
                # bol, creatures = creature_in_place(i)
                # if bol:
                    # for j in creatures:
                        # j.HP -= 20
                        
        #elif self.name == "Pause":
        #    gstate.get().pause = True
                    