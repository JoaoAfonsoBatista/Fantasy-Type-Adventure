import gstate
from event import *
from auxiliary_functions import *

class item:
    def __init__(self,name,item_type,cooldown, damage):
        self.name = name
        self.item_type = item_type
        self.cooldown = cooldown
        self.damage = damage
        self.in_cooldown_for = 0
    
    def clock(self):
        self.in_cooldown_for -= gstate.get().tick_time
    
    def effect(self,position,facing):
        print("boas enviado do effect no item")
        if self.in_cooldown_for <= 0:
            if self.item_type == "bow":
                gstate.get().arena.add_event(event("projectile",position,0.1, self.damage,["arrow",0],facing, value_2 = 15))
            
            self.in_cooldown_for = self.cooldown
    
            