import gstate
import pygame


def add_lists(l1, l2):
    r = []
    for i in range(len(l1)):
        r += [l1[i] + l2[i]]
    return r
        
def subtract_lists(l1, l2):
    r = []
    for i in range(len(l1)):
        r += [l1[i] - l2[i]]
    return r
    
def multiply_lists(l1, l2):
    r = []
    for i in range(len(l1)):
        r += [l1[i] * l2[i]]
    return r

def sum_list(l):
    r = 0
    for i in l:
        r += i
    return r
    
def sum_mod_list(l):
    r = 0
    for i in l:
        r += abs(i)
    return r
    
def creature_in_place(place):
    bol = False
    r = []
    for i in gstate.get().arena.creatures:
        if i.position == place:
            bol = True
            r.append(i)
    return bol, r

def obstacle_in_place(place):
    bol = False
    r = []
    for i in gstate.get().arena.obstacles:
        if i.position == place:
            bol = True
            r.append(i)
    return bol, r
    
def anything_in_place(place):
    bol = False
    r = []
    for i in gstate.get().arena.obstacles + gstate.get().arena.creatures:
        if i.position == place:
            bol = True
            r.append(i)
    return bol, r