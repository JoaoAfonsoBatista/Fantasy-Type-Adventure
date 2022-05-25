import random as R
from creature import *
from abilities import *
from renderable import *
import gstate
import pygame


#decisions are list [creature, time until effect, ability]


class ai_component_abstract:

    def __init__(self, name):
        self.name = name
        
    def define(self, id ,enemies = []):
        if self.name == "zombie":
            return ai_component_zombie(id,enemies)
        elif self.name == "skeleton":
            return ai_component_skeleton(id,enemies)
        
        #ai_component_skeleton(gstate.get().id_creature,enemies = [gstate.get().vacaboy]

class ai_component:
    def __init__(self, id):
    
        self.id = id
        #self.creature = [][0]
        self.found_creature = False
        self.time_until_decision_ability = 1
        self.time_until_decision_movement = 1
        #self.trajectory = [[0,0]]
        self.trajectory = []
        self.i = -1
        self.renderables = []
        
        #self.time_between_ability = [0, 5, 20, 60, 65]
        self.time_between_ability = [0, 5, 10, 60, 60 * 10]
        
        self.time_since_ability_cast = [0,0,0,0,0]
        
        self.time_between_movement = [0, 0.2, 1, 10, 60]
        
        self.time_since_movement_cast = [0,0,0,0,0]
        
        self.pulling_bow = False
        
    def restart(self):
        self.time_since_movement_cast = [0,0,0,0,0]
        self.time_since_ability_cast = [0,0,0,0,0]
        self.i = -1
        self.time_until_decision_ability = 1
        self.time_until_decision_movement = 1
        
    def draw(self,screen):
        for r in self.renderables:
            r.draw(screen)
        
    def decide_ability(self):
        pass
        #if self.time_until_decision <= 0:
        #    self.time_until_decision = 1
        #    self.i = (self.i + 1) % len(self.trajectory)
        #    self.creature.decisions.append([self.creature, 0, ability("teleport", 5, [self.trajectory[self.i]], self.creature)])
    
    def decide_movement(self):
        pass
        #if self.time_until_decision <= 0:
        #    self.time_until_decision = 1
        #    self.i = (self.i + 1) % len(self.trajectory)
        #    self.creature.decisions.append([self.creature, 0, ability("teleport", 5, [self.trajectory[self.i]], self.creature)])    
            
    def clock(self):
        if not self.found_creature:
            self.creature = [i for i in gstate.get().arena.creatures if i.id == self.id][0]
            self.found_creature = True
        self.time_until_decision_ability -= gstate.get().tick_time
        self.time_until_decision_movement -= gstate.get().tick_time
        
        if self.time_until_decision_ability <= 0:
            self.decide_ability()
        if self.time_until_decision_movement <= 0:
            self.decide_movement()
        #print(str(self.time_until_decision))
        #print("aqui no clock do ai component")
        self.time_since_ability_cast = [i + gstate.get().tick_time for i in self.time_since_ability_cast]    
        self.time_since_movement_cast = [i + gstate.get().tick_time for i in self.time_since_movement_cast]    
        
    def send_decision_ability(self,decision):
        self.creature.decisions.append(decision)
        level = decision[2].level
        self.time_since_ability_cast[level] = 0
    
    def send_decision_movement(self,decision):
        self.creature.decisions.append(decision)
        level = decision[2].level
        self.time_since_movement_cast[level] = 0
        
    def verify_decision_ability(self,decision):
        level = decision[2].level
        if self.time_since_ability_cast[level] < self.time_between_ability[level]:
            #print("You can't cast this yet, you need to recharge. give it some time friend (aqui no ai_component -> verify_decision), faltam "+ str(self.time_between_ability[level] - self.time_since_ability_cast[level]) +" secs btw")
            return False
        else:
            return True
            
    def verify_decision_movement(self,decision):
        level = decision[2].level
        if self.time_since_movement_cast[level] < self.time_between_movement[level]:
            #print("You can't cast this yet, you need to recharge. give it some time friend (aqui no ai_component -> verify_decision), faltam "+ str(self.time_between_ability[level] - self.time_since_ability_cast[level]) +" secs btw")
            return False
        else:
            return True
        
        
class ai_component_player(ai_component):

    def __init__(self, id):
        super().__init__(id)
        self.writing = False
        self.text = ""
        self.letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," ","'"]
        self.pygame_letters = [pygame.K_a,pygame.K_b,pygame.K_c,pygame.K_d,pygame.K_e,pygame.K_f,pygame.K_g,pygame.K_h,pygame.K_i,pygame.K_j,pygame.K_k,pygame.K_l,pygame.K_m,pygame.K_n,pygame.K_o,pygame.K_p,pygame.K_q,pygame.K_r,pygame.K_s,pygame.K_t,pygame.K_u,pygame.K_v,pygame.K_w,pygame.K_x, pygame.K_y,pygame.K_z,pygame.K_SPACE, pygame.K_BACKQUOTE]
        
        self.renderables.append(barrenderable_changeble(lambda: gstate.get().arena_width + 5, lambda:gstate.get().current_height - 35 * 1, lambda: gstate.get().current_width - gstate.get().arena_width - 10, lambda: 30, lambda: gstate.get().caramel, lambda: gstate.get().violet, lambda: (min(self.time_since_ability_cast[1],self.time_between_ability[1]),self.time_between_ability[1])))
        self.renderables.append(textrenderable_changeble(lambda: gstate.get().arena_width + 5 + 5, lambda:gstate.get().current_height - 35 * 1 +5, lambda: self.creature.color, lambda: gstate.get().font_magneto, lambda: "Circle 1 - " + str(math.ceil(max(self.time_between_ability[1]-self.time_since_ability_cast[1],0)))+" seconds"))
        
        self.renderables.append(barrenderable_changeble(lambda: gstate.get().arena_width + 5, lambda:gstate.get().current_height - 35 * 2, lambda: gstate.get().current_width - gstate.get().arena_width - 10, lambda: 30, lambda: gstate.get().caramel, lambda: gstate.get().violet, lambda: (min(self.time_since_ability_cast[2],self.time_between_ability[2]),self.time_between_ability[2])))
        self.renderables.append(textrenderable_changeble(lambda: gstate.get().arena_width + 5 + 5, lambda:gstate.get().current_height - 35 * 2 +5, lambda: self.creature.color, lambda: gstate.get().font_magneto, lambda: "Circle 2 - " + str(math.ceil(max(self.time_between_ability[2]-self.time_since_ability_cast[2],0)))+" seconds"))
        
        self.renderables.append(barrenderable_changeble(lambda: gstate.get().arena_width + 5, lambda:gstate.get().current_height - 35 * 3, lambda: gstate.get().current_width - gstate.get().arena_width - 10, lambda: 30, lambda: gstate.get().caramel, lambda: gstate.get().violet, lambda: (min(self.time_since_ability_cast[3],self.time_between_ability[3]),self.time_between_ability[3])))
        self.renderables.append(textrenderable_changeble(lambda: gstate.get().arena_width + 5 + 5, lambda:gstate.get().current_height - 35 * 3 +5, lambda: self.creature.color, lambda: gstate.get().font_magneto, lambda: "Circle 3 - " + str(math.ceil(max(self.time_between_ability[3]-self.time_since_ability_cast[3],0)))+" seconds"))
        
        self.renderables.append(barrenderable_changeble(lambda: gstate.get().arena_width + 5, lambda:gstate.get().current_height - 35 * 4, lambda: gstate.get().current_width - gstate.get().arena_width - 10, lambda: 30, lambda: gstate.get().caramel, lambda: gstate.get().violet, lambda: (min(self.time_since_ability_cast[4],self.time_between_ability[4]),self.time_between_ability[4])))
        #time_left = self.calculate_time_left(4)
        self.renderables.append(textrenderable_changeble(lambda: gstate.get().arena_width + 5 + 5, lambda:gstate.get().current_height - 35 * 4 +5, lambda: self.creature.color, lambda: gstate.get().font_magneto, lambda: "Circle 4 - " + self.calculate_time_left(4)))
        
        self.renderables.append(barrenderable_changeble(lambda: 4, lambda:gstate.get().current_height - 12, lambda:gstate.get().arena_width - 9, lambda: 10, lambda: gstate.get().light_grey, lambda: self.creature.color, lambda: (1 if self.writing else 0,1)))
        
        self.renderables.append(rectrenderable_changeble(lambda: 3, lambda:gstate.get().current_height - 12, lambda:2, lambda: 10, lambda: gstate.get().light_grey))
        
    def calculate_time_left(self,numero):
        time = self.time_between_ability[numero] - self.time_since_ability_cast[numero]
        if time > 3600 * 24:
            return str(math.ceil(time/(3600 * 24))) + "days"
        elif time > 3600:
            return str(math.ceil(time/3600)) + "hours"
        elif time > 60:
            return str(math.ceil(time/60)) + "minutes"
        else:
            return str(math.ceil(max(time,0))) + " seconds"
        #str(math.ceil(max(self.time_between_ability[4]-self.time_since_ability_cast[4],0))) + " seconds"
    
    def key_type(self,key):
    
        if self.writing:
            if key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif key in self.pygame_letters:
                self.text += self.letters[self.pygame_letters.index(key)]
            
        if key == pygame.K_RIGHT:
            decision = [self.creature, 0, gstate.get().movements["walk"].define(self.creature)]
            if self.verify_decision_movement(decision):
                self.trajectory.append([1,0])
                self.send_decision_movement(decision)
            #self.creature.decisions.append([self.creature, 0, gstate.get().movements["walk"].define(self.creature)])
            
        elif key == pygame.K_LEFT:
            
            decision = [self.creature, 0, gstate.get().movements["walk"].define(self.creature)]
            if self.verify_decision_movement(decision):
                self.trajectory.append([-1,0])
                self.send_decision_movement(decision)
        elif key == pygame.K_UP:
            
            decision = [self.creature, 0, gstate.get().movements["walk"].define(self.creature)]
            if self.verify_decision_movement(decision):
                self.trajectory.append([0,-1])
                self.send_decision_movement(decision)
        elif key == pygame.K_DOWN:
            
            decision = [self.creature, 0, gstate.get().movements["walk"].define(self.creature)]
            if self.verify_decision_movement(decision):
                self.trajectory.append([0,1])
                self.send_decision_movement(decision)
        
            #self.creature.decisions.append([self.creature, 0, gstate.get().movements["walk"].define(self.creature)])
            
        elif key == pygame.K_RETURN:
            if self.writing:
                self.decide()

            self.writing = not self.writing
            
        elif key == pygame.K_1:
            decision = [self.creature,0,gstate.get().abilities["release bow"].define(self.creature)]
            if self.verify_decision_ability(decision):
                self.send_decision_ability(decision)
            #self.creature.decisions.append([self.creature, 0, gstate.get().abilities["fire breath"].define(self.creature)])
            
        elif key == pygame.K_TAB:
            self.creature.decisions.append([self.creature, 0, gstate.get().movements["turn"].define(self.creature)])
        
    def decide(self):
        decision = [self.creature, 0, gstate.get().abilities["misstype"].define(self.creature)]
        is_ability = False
        for a in gstate.get().abilities:
            if a == self.text:
                is_ability = True
                decision = [self.creature, 0, gstate.get().abilities[a].define(self.creature)]
                print(decision[2].level)
        
        is_movement = False
        if not is_ability:
            for a in gstate.get().movements:
                if a == self.text:
                    is_movement = True
                    decision = [self.creature, 0, gstate.get().movements[a].define(self.creature)]
                    print(decision[2].level)
        
        self.text = ""
        
        if is_ability:
            if self.verify_decision_ability(decision):
                self.send_decision_ability(decision)
        elif is_movement:
            if self.verify_decision_movement(decision):
                self.send_decision_movement(decision)
            #creature.decisions.append(decision)
            

            
            
            
    def draw(self,screen):
        super().draw(screen)
        
    
    def clock(self):
        if not self.found_creature:
            self.creature = [i for i in gstate.get().arena.creatures if i.id == self.id][0]
            self.found_creature = True
            self.creature.renderables.append(textrenderable_changeble(lambda: 10, lambda: gstate.get().current_height - 77, lambda:self.creature.color, lambda:gstate.get().font_type, lambda: self.text))
        #self.time_until_decision -= gstate.get().tick_time
        #self.decide()
        
        self.time_since_ability_cast = [i + gstate.get().tick_time for i in self.time_since_ability_cast]
        self.time_since_movement_cast = [i + gstate.get().tick_time for i in self.time_since_movement_cast]


class ai_component_circle(ai_component):
    def __init__(self, id):
        super().__init__(id)
        #self.creature = creature
        self.time_until_decision = 1
        self.trajectory = [[1,0], [1,0], [0,1], [0,1], [-1,0], [-1,0], [0,-1], [0,-1]]

        
    def decide(self):
        if self.time_until_decision <= 0:
            self.time_until_decision = 1
            self.i = (self.i + 1) % len(self.trajectory)
            self.creature.decisions.append([self.creature, 0, gstate.get().abilities["walk"]])
            
            
    def draw(self,screen):
        super().draw(screen)
    
    def clock(self):
        super().clock()
        
class ai_component_big_circle(ai_component):
    def __init__(self, id):
        super().__init__(id)
        #self.creature = creature
        self.time_until_decision = 1.3
        self.trajectory = [[1,0], [1,0], [1,0], [1,0], [1,0], [1,0], [0,1], [0,1], [0,1], [0,1], [0,1], [0,1], [-1,0], [-1,0], [-1,0], [-1,0], [-1,0], [-1,0], [0,-1], [0,-1], [0,-1], [0,-1], [0,-1], [0,-1]]

        
    def decide(self):
        if self.time_until_decision <= 0:
            self.time_until_decision = 0.1
            self.i = (self.i + 1) % len(self.trajectory)
            self.creature.decisions.append([self.creature, 0, gstate.get().abilities["walk"]])
            #self.creature.decisions.append([self.creature, 0, ability("teleport", 0, area_of_effect = [self.trajectory[self.i]], target = self.creature)])
            
    def draw(self,screen):
        super().draw(screen)
        
    def clock(self):
        super().clock()
        
class ai_component_chalenge_3(ai_component):
    def __init__(self, id):
        super().__init__(id)
        #self.creature = creature
        self.time_until_decision = 1.3
        self.trajectory = [[0,-1] for i in range(8)] + [[1,0] for i in range(7)] + [[0,1] for i in range(8)] + [[-1,0] for i in range(2)] + [[0,-1] for i in range(8)] + [[-1,0] for i in range(4)]+ [[0,1] for i in range(8)]
    
    def decide_ability(self):
        pass
    
    def decide_movement(self):
        if self.creature.position == [14,6] or self.creature.position == [20,1] or self.creature.position == [23,8]:
            self.time_since_movement_cast[2] = 10
            self.time_until_decision_movement = 0.5
            decision = [self.creature, 0, gstate.get().movements["high jump"].define(self.creature)]
            if self.verify_decision_movement(decision):
                self.send_decision_movement(decision)
                
        elif anything_in_place(add_lists(self.creature.position,self.creature.facing()))[0]:
            decision = [self.creature, 0, gstate.get().movements["turn"].define(self.creature)]
            if self.verify_decision_movement(decision):
                self.send_decision_movement(decision)
                
        if self.time_until_decision_movement <= 0:
            self.time_since_movement_cast[1] = 1
            self.time_until_decision_movement = 0.19
            #self.i = (self.i + 1) % len(self.trajectory)
            if len(self.trajectory) > 0:
                decision = [self.creature, 0, gstate.get().movements["walk"].define(self.creature)]
                if self.verify_decision_movement(decision):
                    self.send_decision_movement(decision)
            #self.creature.decisions.append([self.creature, 0, gstate.get().abilities["walk"]])
            #self.creature.decisions.append([self.creature, 0, ability("teleport", 0, area_of_effect = [self.trajectory[self.i]], target = self.creature)])
            
    def draw(self,screen):
        super().draw(screen)
        
    def clock(self):
        super().clock()
        
class ai_component_objective(ai_component):
    def __init__(self, id, objective = [15,10]):
        super().__init__(id)
        #self.creature = creature
        self.time_until_decision = 1
        self.trajectory = []
        self.want_to_face = 2
        self.objective = objective
        self.got_trajectory = False
        self.on_objective = False
    
    def turn_until_want_to_face(self):
        #print("no ai_component objevtive " + str(self.trajectory[0]))
        #print("no ai_component objevtive " + str(gstate.get().facing_cycle.index(self.trajectory[0])))
        self.want_to_face = gstate.get().facing_cycle.index(self.trajectory[0])
    
    def decide_ability(self):
        pass    

    def decide_movement(self):
        #if self.time_until_decision_mo <= 0:
        #    self.time_until_decision = 0.3
            
            #self.turn_until_want_to_face()
            
            
            
        if self.creature.position == self.objective:
            self.on_objective = True
        else:
            self.on_objective = False
        if not self.on_objective:
            
            
                #self.i = (self.i + 1) % len(self.trajectory)
                #print("no ai_component objevtive " + str(self.creature.facing_index))
            decision = [self.creature, 0, gstate.get().movements["walk"].define(self.creature)]
            if self.verify_decision_movement(decision):
                self.calculate_trajectory()
                self.turn_until_want_to_face()
                self.send_decision_movement(decision)
            #self.creature.decisions.append([self.creature, 0, gstate.get().movements["walk"].define(self.creature)])
                
                for i in range((self.want_to_face - self.creature.facing_index)%4):
                    self.creature.decisions.append([self.creature, 0, gstate.get().movements["turn"].define(self.creature)])
                    
    
    
    def calculate_trajectory(self):
        position = self.creature.position[:]
        self.trajectory = []
        #if position == self.objective:
        #    on_target = True
        #else:
        #    on_target = False
        done = False
        r = 0
        while not done:
            a = R.random()
        
            if a < 0.5:
                bol_1,a_1 = anything_in_place(add_lists(position,[1,0]))
                bol_2,a_2 = anything_in_place(add_lists(position,[-1,0]))
                if (position[0] < self.objective[0] and not bol_1) or add_lists(position,[1,0]) == self.objective:
                    self.trajectory.append([1,0])
                    position[0] += 1
                
                
                elif (position[0] > self.objective[0] and not bol_2) or add_lists(position,[-1,0]) == self.objective:
                    self.trajectory.append([-1,0])
                    position[0] -= 1
                    
            else:
                bol_1,a_1 = anything_in_place(add_lists(position,[0,1]))
                bol_2,a_1 = anything_in_place(add_lists(position,[0,-1]))
                if (position[1] < self.objective[1]  and not bol_1) or add_lists(position,[0,1]) == self.objective:
                    self.trajectory.append([0,1])
                    position[1] += 1
                
                elif (position[1] > self.objective[1] and not bol_2) or add_lists(position,[0,-1]) == self.objective:
                    self.trajectory.append([0,-1])
                    position[1] -= 1
                    
            r += 1
            if r > 20:
                self.trajectory.append(R.choice([[1,0],[-1,0],[0,1],[0,-1]]))
                done = True
            if position == self.objective:
                done = True
            #else:
            #    on_target = False

    def draw(self,screen):
        super().draw(screen)
        
    def clock(self):
        super().clock()
        
        
        
class ai_component_chase(ai_component_objective):

    def __init__(self, id, creature_to_chase):
        
        self.creature_to_chase = creature_to_chase
        super().__init__(id, objective = self.creature_to_chase.position)
        
    def decide(self):
        if self.time_until_decision <= 0:
            self.objective = self.creature_to_chase.position
            super().decide()
            
    def draw(self,screen):
        super().draw(screen)
        
    def clock(self):
        super().clock()       
        
      

        
class ai_component_zombie(ai_component_objective):

    def __init__(self, id, enemies = []):
    
        self.enemies = enemies
        self.creature_to_chase = enemies[0]
            
        
        #self.creature_to_chase = creature_to_chase
        super().__init__(id, objective = [0,0])
        
    def decide_ability(self):
        if add_lists(self.creature.position, self.creature.facing()) == self.creature_to_chase.position:
            decision = [self.creature, 0, gstate.get().abilities["zombie_slash"].define(self.creature)]
            if self.verify_decision_ability(decision):
                self.time_until_decision_ability = 2
                self.send_decision_ability(decision)
                    #self.creature.decisions.append()
                    
    def decide_movement(self):
        self.time_until_decision_movement = 1.5
        self.creature_to_chase = self.find_closest_enemy()
        self.objective = self.creature_to_chase.position
        super().decide_movement()
            
    def find_closest_enemy(self):
        self.enemies = [i for i in self.enemies if i in gstate.get().arena.creatures]
        enemy = self.creature
        distance = 100000000
        for i in self.enemies:
            pos_1 = i.position
            pos_2 = self.creature.position
            distance_aux = sum_mod_list(subtract_lists(pos_1,pos_2))
            
            if distance_aux < distance:
                enemy = i
                distance = distance_aux
            
        return enemy    
            
    def draw(self,screen):
        super().draw(screen)
        
    def clock(self):
        super().clock()  
            
class ai_component_skeleton(ai_component):

    def __init__(self, id, enemies = []):
    
        self.enemies = enemies
        self.creature_to_chase = enemies[0]
        self.facing_index = 0
        self.found_facing_index = False
            
        
        #self.creature_to_chase = creature_to_chase
        super().__init__(id)
        
    def decide_ability(self):
        if self.facing_index == 0 or self.facing_index == 2:
            if self.creature.position[0] == self.creature_to_chase.position[0]:
                decision = [self.creature, 0, gstate.get().abilities["pull bow"].define(self.creature)]
                decision1 = [self.creature, 0, gstate.get().abilities["release bow"].define(self.creature)]
                if self.verify_decision_ability(decision) and self.verify_decision_ability(decision1):
                    self.time_until_decision_ability = 3
                    self.send_decision_ability(decision)
                    self.send_decision_ability(decision1)
        elif self.facing_index == 1 or self.facing_index == 3:
            if self.creature.position[1] == self.creature_to_chase.position[1]:
                decision = [self.creature, 0, gstate.get().abilities["pull bow"].define(self.creature)]
                decision1 = [self.creature, 0, gstate.get().abilities["release bow"].define(self.creature)]
                if self.verify_decision_ability(decision) and self.verify_decision_ability(decision1):
                    self.time_until_decision_ability = 3
                    self.send_decision_ability(decision)
                    self.send_decision_ability(decision1)
                    
    def decide_movement(self):
        self.time_until_decision_movement = 0.15
        self.creature_to_chase = self.find_closest_enemy()
        if self.facing_index == 0 or self.facing_index == 2:
            if self.creature.position[0] == self.creature_to_chase.position[0]:
                pass
            if self.creature.position[1] < self.creature_to_chase.position[1] and self.creature.facing_index == 0:
                decision = [self.creature, 0, gstate.get().movements["turn"].define(self.creature)]
                if self.verify_decision_movement(decision):
                    self.send_decision_movement(decision)
                    self.send_decision_movement(decision)
            elif self.creature.position[1] > self.creature_to_chase.position[1] and self.creature.facing_index == 2:
                decision = [self.creature, 0, gstate.get().movements["turn"].define(self.creature)]
                if self.verify_decision_movement(decision):
                    self.send_decision_movement(decision)
                    self.send_decision_movement(decision)
            if self.creature.position[0] < self.creature_to_chase.position[0]:
                self.trajectory.insert(0,[1,0])
                decision = [self.creature, 0, gstate.get().movements["walk"].define(self.creature)]
                
                if self.verify_decision_movement(decision):
                    self.send_decision_movement(decision)
                    
            elif self.creature.position[0] > self.creature_to_chase.position[0]:
                self.trajectory.insert(0,[-1,0])
                decision = [self.creature, 0, gstate.get().movements["walk"].define(self.creature)]
                
                if self.verify_decision_movement(decision):
                    self.send_decision_movement(decision)
                    
        elif self.facing_index == 1 or self.facing_index == 3:
            if self.creature.position[1] == self.creature_to_chase.position[1]:
                pass
            if self.creature.position[0] > self.creature_to_chase.position[0] and self.creature.facing_index == 1:
                decision = [self.creature, 0, gstate.get().movements["turn"].define(self.creature)]
                if self.verify_decision_movement(decision):
                    self.send_decision_movement(decision)
                    self.send_decision_movement(decision)
            elif self.creature.position[0] < self.creature_to_chase.position[0] and self.creature.facing_index == 3:
                decision = [self.creature, 0, gstate.get().movements["turn"].define(self.creature)]
                if self.verify_decision_movement(decision):
                    self.send_decision_movement(decision)
                    self.send_decision_movement(decision)
            if self.creature.position[1] < self.creature_to_chase.position[1]:
                self.trajectory.insert(0,[0,1])
                decision = [self.creature, 0, gstate.get().movements["walk"].define(self.creature)]
                
                if self.verify_decision_movement(decision):
                    self.send_decision_movement(decision)
                    
            elif self.creature.position[1] > self.creature_to_chase.position[1]:
                self.trajectory.insert(0,[0,-1])
                decision = [self.creature, 0, gstate.get().movements["walk"].define(self.creature)]
                
                if self.verify_decision_movement(decision):
                    self.send_decision_movement(decision)
                    
        
    def find_closest_enemy(self):
        self.enemies = [i for i in self.enemies if i in gstate.get().arena.creatures]
        enemy = self.creature
        distance = 100000000
        for i in self.enemies:
            pos_1 = i.position
            pos_2 = self.creature.position
            distance_aux = sum_mod_list(subtract_lists(pos_1,pos_2))
            
            if distance_aux < distance:
                enemy = i
                distance = distance_aux
            
        return enemy    
            
    def draw(self,screen):
        super().draw(screen)
        
    def clock(self):
        super().clock()  
        if not self.found_facing_index:
            if self.found_creature:
                self.facing_index = self.creature.facing_index
                self.found_facing_index = True
        
class ai_component_corpse(ai_component):
    def __init__(self, id):
        super().__init__(id)
        self.found_corpse = False
        #self.creature = creature
        self.time_until_decision = 1
        self.trajectory = []
        
    def decide(self):
        if self.time_until_decision <= 0:
            self.time_until_decision = R.randint(1,10)
            
            choice = R.choice([i for i in gstate.get().death_abilities])
            self.creature.decisions.append([self.creature, 0, gstate.get().death_abilities[choice].define(self.creature)])
            
            
    def draw(self,screen):
        super().draw(screen)
                
    def clock(self):
        if not self.found_corpse:
            self.creature = [i for i in gstate.get().arena.corpses if i.id == self.id][0]
            self.found_creature = True
            
            
        for i in self.time_since_ability_cast:
            i += gstate.get().tick_time     
    