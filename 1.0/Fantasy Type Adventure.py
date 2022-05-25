import random as R
import sys
import pygame


import gstate

from state import *
from auxiliary_functions import *
from abilities import *

import do_the_stuff


#from win32api import GetSystemMetrics

#print("Width =", GetSystemMetrics(0))
#print("Height =", GetSystemMetrics(1))

import ctypes
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
print(screensize)

pygame.init()
gstate.init()

gstate.get().full_width, gstate.get().full_height = screensize

#ctypes.windll.user32.SetProcessDPIAware()
#true_res = (windll.user32.GetSystemMetrics(0),windll.user32.GetSystemMetrics(1))
#pygame.display.set_mode(true_res,pygame.Fullscreen)

#screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
gstate.get().screen = pygame.display.set_mode((gstate.get().current_width, gstate.get().current_height))
#screen = pygame.display.set_mode((200, 60))
#global game_phase



#game_phase = start_game()
game_phase = decide_chalenge()



#gstate.get().arena = arena(16,16)

do_the_stuff.do_the_stuff(gstate.get())

#gstate.get().dummy = creature("dummy",ai_component = ai_component_circle(gstate.get().id_creature), color = gstate.get().cyan)








gstate.get().abilities["misstype"] = ability_abstract("Misstype",0,[[0,0]])

gstate.get().abilities["pause"] = ability_abstract("Pause",0,[[0,0]])

#gstate.get().movements["walk"] = movement_abstract("Walk", 1)

#gstate.get().movements["dash"] = movement_abstract("Dash", 2)

#gstate.get().movements["turn"] = movement_abstract("Turn", 0)

gstate.get().death_abilities["pretending to be dead"] = ability_abstract("Pretending to be dead",0,[[0,0]])



#______________________________________________________________________________________________________________________________________________________________________
global run
#main loop
gstate.get().run = True
while gstate.get().run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gstate.get().run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: #nao sei como ver se se clicou no lado esquerdo ou direito do rato... o lado esquerdo é 1 e o lado esquerdo é 3
                
                game_phase = game_phase.receiveevent(event)

            elif event.button == 3:
                print(str(event.pos))
                game_phase = game_phase.receiveevent1(event, gstate.get().screen)
                
        if event.type == pygame.KEYDOWN:
                
            game_phase = game_phase.key_type(event.key)

            if event.key == pygame.K_DELETE:
                gstate.get().run = False
            #elif event.key == pygame.K_o:
            #    game_phase.renderables.append(rectrenderable(100,100,200,200,(255,0,0,150)))
            #elif event.key == pygame.K_i:
            #    print(game_phase.name)
            elif event.key == pygame.K_F2:
                print(gstate.get().vacaboy.ai_component.time_since_ability_cast)
                gstate.get().vacaboy.ai_component.time_since_ability_cast = gstate.get().vacaboy.ai_component.time_between_ability[:]
                gstate.get().vacaboy.ai_component.time_since_movement_cast = gstate.get().vacaboy.ai_component.time_between_movement[:]
                print(gstate.get().vacaboy.ai_component.time_since_ability_cast)
            elif event.key == pygame.K_F3:
                for i in gstate.get().arena.creatures:
                    i.HP = i.MAX_HP
    #game_phase = game_phase.clock()
    game_phase = game_phase.effect()
    game_phase.draw(gstate.get().screen)
    pygame.display.update()
    

pygame.quit()
