import random as R
#from globals import *
from creature import *
#from abilities import *
from renderable import *
from arena import *
from aicomponent import *
from event import *

import gstate
import math
import pygame


class state():

    def __init__(self):
        self.name = "0"
        self.renderables = [rectrenderable_changeble(lambda:0,lambda:0,lambda:gstate.get().current_width, lambda: gstate.get().current_height,lambda:gstate.get().light_grey)]
        
    
    def draw(self, screen):
        #pygame.draw.rect(screen, (0,0,0), (0,0, gstate.get().width, gstate.get().current_height))
        #print(len(self.renderables))
        for r in self.renderables:
            
            r.draw(screen)
            
    def effect(self):
        return self
            
    def receiveevent(self, event):
        print("cliquei aqui: " + str(event.pos))
        return self
        
    def receiveevent1(self, event, screen):
        return self
        
    def key_type(self, key):
        #print(key)
        
        if key == pygame.K_q:
            w, h = pygame.display.get_surface().get_size()
            print("tamanho aqui!: "+str(w) + " x " + str(h))
            print([gstate.get().width, gstate.get().height,gstate.get().current_width, gstate.get().current_height,gstate.get().full_width, gstate.get().full_height])
            
        elif key == pygame.K_F4:
            pygame.display.quit()
            pygame.display.init()
            if gstate.get().fullscreen:
                gstate.get().screen = pygame.display.set_mode((gstate.get().width, gstate.get().height))
                gstate.get().current_width, gstate.get().current_height = gstate.get().width, gstate.get().height
            else:
                gstate.get().screen = pygame.display.set_mode((gstate.get().full_width,gstate.get().full_height),pygame.FULLSCREEN)
                gstate.get().current_width, gstate.get().current_height = gstate.get().full_width, gstate.get().full_height
                
            gstate.get().arena_width = gstate.get().current_width - 300
            gstate.get().arena_height = gstate.get().current_height - 60
            
            gstate.get().arena = gstate.get().arena.recreate_arena()
            
            gstate.get().fullscreen = not gstate.get().fullscreen

        
        
    def write(self, surface, te, pos, width , font, color=(200,0,0)):
        words = [word.split(' ') for word in te.splitlines()]  # 2D array where each row is a list of words.
        space = font.size(' ')[0]  # The width of a space.
        x, y = pos
        max_width = x + width
        for line in words:
            for wo in line:

                wo_surface = font.render(wo, 0, color)
                wo_width, wo_height = wo_surface.get_size()
                if x + wo_width >= max_width:
                    x = pos[0]  # Reset the x.
                    y += wo_height  # Start on new row.
                a = textrenderable1(x, y, color, font, wo)
                self.renderables.append(a)
                #self.temporaryrenderables.append(a)
                x += wo_width + space
            x = pos[0]  # Reset the x.
            y += wo_height  # Start on new row.
            
    def write_centered(self, surface, te, pos, width , font, color=(200,0,0)):
        self.write(surface, te, [pos[0]-width/2,pos[1]],width,font,color)
       
class start_game(state):

    def __init__(self,):
        super().__init__()
        self.name = "start_game"
        self.write_centered(gstate.get().screen, "Click any letter",[gstate.get().current_width/2,20],gstate.get().current_width/2 - 100, gstate.get().fontend, gstate.get().black)
        #self.renderables.append(textrenderable(330, 295, gstate.get().light_grey, gstate.get().fontend, lambda: "click anywhere"))

            
    def effect(self): 
        return self


    def draw(self, screen):
        super().draw(screen)
    

    def key_type(self, key):
        super().key_type(key)
        
        return character_creation()
        

            
#__________________________________________________________________________________________________________________________________________________________________________________

class character_creation(state):

    def __init__(self,):
        super().__init__()
        self.name = "character_creation"
        self.write_centered(gstate.get().screen, "Time to create you character: \nAlia Jacta Est. \n\nclick any letter",[gstate.get().current_width/2,20],gstate.get().current_width/2 - 100, gstate.get().fontA, gstate.get().black)
        #self.renderables.append(textrenderable(330, 295, gstate.get().light_grey, gstate.get().fontend, lambda: "click anywhere"))

            
    def effect(self): 
        return self


    def draw(self, screen):
        super().draw(screen)
    

    def key_type(self, key):
        super().key_type(key)
        
        
        
        return decide_chalenge()


#__________________________________________________________________________________________________________________________________________________________________________________

class decide_chalenge(state):

    def __init__(self,):
        super().__init__()
        self.name = "decide_chalenge"
        #self.write_centered(gstate.get().screen, "Time to chose the chalenge, unfortunatly, you don't have a choice. \nclick any letter",[gstate.get().current_width/2,20],gstate.get().current_width/2 - 100, gstate.get().fontA, gstate.get().light_grey)
        
        self.write_centered(gstate.get().screen, 
        "Time to chose your chalenge, Click on the desired number to start the begining of your growth as a fantasy type gamer!\n1 - playground\n2 - target practice\n3 - race against The Bolt\n4 - chain lightning practice\n5 - Combat practice\n6 - Tunnel of death\n7 - now you are the target\n8 - Survival of the species\n9 - The ultimate survival",[gstate.get().current_width/2,20],gstate.get().current_width/2 - 100, gstate.get().fontA, gstate.get().black)
        #self.renderables.append(textrenderable(330, 295, gstate.get().light_grey, gstate.get().fontend, lambda: "click anywhere"))

            
    def effect(self): 
        return self


    def draw(self, screen):
        super().draw(screen)
    

    def key_type(self, key):
        super().key_type(key)
        gstate.get().vacaboy.restart()
        if key == pygame.K_1:
            self.make_arena(1)
            return chalenge("kill everything","Use this relaxed place to improve your skills and perfect your typing. And always remember... have fun! :D \n\nRemember that you can walk with the arrow keys (you can only walk every 0.3 seconds) and you can turn the way you are facing with the TAB key. This seems useless but is imperative once you start casting abilities, since they will be cast in the direction you are facing.\npress ESC when you feel like you are prepared to try other chalenges.\n\nPress enter to continue")
        elif key == pygame.K_2:
            self.make_arena(2)
            return chalenge("target practice","In this chalenge, you will need to use your bow and arrow to shoot all the targets in the map within 35 seconds.\nWhen learning to use the bow, acuracy and speed are imperative.\n\nabilities:\n->pull bow (prepares to shoot an arrow)\n->release bow (if your bow is pulled, send and arrow straigh in from of you)\n\nbow is an item, as such, it must recharge when used. When you release an arrow, you have to wait 1 second until you can shoot another one, but you can prepare the bow right away.\nprojectiles also have a range, the bow you are using sends arrows flying 15 meters\ni thought it was obvious but after some alpha testing i realized some players were trying to hit the target in a specific direction. hint:you can shoot the targets from ANY direction.\n\npress enter to start shooting.")
        elif key == pygame.K_3:
            self.make_arena(3)
            return chalenge("reach destination","In this chalenge, you will need to be fast... you will need to parkour your way through the forest to reach the golden tile before your oponnent!\n\nonly moviment abilities are used in this chalenge \nrememeber to use the arrow keys to walk, once you do, you can only walk again 0.3 seconds later\nuseful abilities:\n-> dash (dash forward)\n->high jump (can jump through obstacles like trees)\n\nboth these abilities are level 1 moviments, once you use a level 1 moviment, you ca only use another one 1 second later.\n\npress enter to start running against The Bolt")
        elif key == pygame.K_4:
            self.make_arena(4)
            return chalenge("chain lightning","This chalenge does not require speed nor acuracy. There are a lot of targets in the map, and you will use the power of eletricity to eletrify them all. Everything in fantasy world has energy, electricity can absorb that energy to spread farther.\n\nability:\n->chain lightning\n\nthis is a very powerfull ability that takes eons to master. When cast, it sends a lightning bolt straight ahead, when that lightning bolt hits something, it splits into two similar lightning bolts. You will understand when you see it. Give it a try!\n\nYou will only be able to cast the ability once, so when you do and want to retry the chalenge, click ESC to return to the previous screen.\n\njust one more thing... try not to fry yourself in the process ;)\nPress enter to continue")
        elif key == pygame.K_5:
            self.make_arena(5)
            return chalenge("kill everything",
            "This will be your first combat! The main objective in your mind should be... 'Kill them before they kill me'.\nIn this litle map a zombie with a hunger for brains will be released, as such, it will instantly start chasing you since you are so smart! Once it get near you it will scratch the hell out of your health bar. Try to keep your distance with the walk and dash abilities while slowly killing it with your damage abiliites. Abilities are divided in circles by how much energy they require to be cast, as such... when you cast an ability from a specific circle, you must recharge your energy before you cast another one. Circle 0 -> casting these abilities is like breathing, you don't need to rest. Circle 1 -> you must wait 5 seconds before casting another one. Circle 2 -> 20 seconds. There are more powerfull circles but you are still learning... everything at its own time.\n\nabilities:\n-pull bow (you already know this one)\n-release bow (you already know this one, and you also know that you can press 1 instead)\n-firebolt (circle 0 projectile)\n-fire breath(circle 1, damages everything in a cone in from of you.)\nfireball (circle 2, big explosion in from of you)\nslash (close combat circle 0 ability)\nthrust (close combat circle 0 ability)\nif you are confused, (it's tottaly normal you are, don't feel bad) head back to the playground to try these abilities out!)\n\nPress enter to continue",
            "You smacked that brain hungry undead ass! The world is now a better place :) later i will watch the recording to analyse your briliant moves again! that well timed fireball surprised me as much as that poor zombie. Keep practicing your typing and remember to always have fun ;) \n\nPress enter to continue",
            "You lost... but hey... at least that zombie got a meal! you just pushed humanity one step closer to ending world hunger, and that is very nobel of you. I know training to be a fantasy typer can be overwhelming at first, that is why we made a playgound so you can fireball trees to your heart's content! practice those fingers, so you can eventually have what you always wanted... pride in yourself.\n\nPress enter to continue")
        
        elif key == pygame.K_6:
            self.make_arena(6)
            return chalenge("kill everything",
            "In this chalenge you will have to be a master of the damage abilities you learned in the previous one. Again, a zombie will be created in from of you, and it wants your brainy brain. The problem now is that you have nowhere to run and... it hits much harder... i wouldn't let him get in close combat if i were you.\n'If your enemies ride tanks, sit in from of them, its better to die under their metal than have blood on your hands... But if they are a zombie, fireball the crap out of them' - Ghandi\n\nabilities (just a reminder of the ones you already know):\nslash\nthrust\nfirebolt\npull bow\nrelease bow\nfire breath\nfireball\n\nlightning bolt (circle 2, sends a lightning bolt in a straight line that splits when it hits the first obstacle, only splts once)\n\nPress enter to continue",
            "Well done fantasy typer, even when in a claustrophobic situation... you stayed cool and made some roasted undead meat, a delicious treat down in the south land of Eudora.\n\nPress enter to continue",
            "'I hated every minute of training, but i said: 'Don't give up, suffer now and live the rest of your life as a champion!'' - Muhammad ali (world champion boxer). take these world in your heart when you try to face this zombie once again my friend.\n\nPress enter to continue")
        elif key == pygame.K_7:
            self.make_arena(7)
            return chalenge("kill everything",
            "Skeletons escaped the zoo and are terrorizing the garden you were taking a nap in! From what you see they are fast! But they can only walk sideways...? Stupid skeletons... But the can also shoot with the bow and arrow... Save yourself by killing every single calcium enriched undead.\nabilities: (just a friendly reminder) \nslash\nthrust\npull bow\nrelease bow\nfirebolt\nfire breath\nfireball\nlightning bolt",
            "How did you...? When did you...? Where did you...? I will send a notification to the zoo report this incident, this is unaceptable! You are still training to be an adventurer and this could have resulted in you perishing! I mean... temporarily at least... we all know that when training, death isn't that big of an issue. Well... You amaze me again fantasy typer wannabe... From the bottom of my heart... good job!\n\nPress enter to continue",
            "Those squeletons came out of nowhere! I will sue the zoo for this so hard their bank acount will be fireballed! This chalenge a litle hard for your skills right now... And you were just taking a rest in the park as well... damn, i am sorry for that stress. Aren't we glad you can't die in this place.\n\nPress enter to continue")
        elif key == pygame.K_8:
            self.make_arena(8)
            return chalenge("survival",
            "This challenge requires endurance and stamina. Zombies and Skeletons will raise from the ground every 10 seconds, pummel ther undead bodies before you get obliterated by arrows and slashes. Defeat 10 enemies and you win! Good luck.\nabilities:\ndash\nhigh jump\nbackflip(a circle 1 moviment ability, you dash 3 meters in the oposite direction to the one you are facing)\npull bow\nrelease bow\nfirebolt\nslash\nthrust\nfire breath\nfireball\nlightning bolt\ninfernal beam (this is the first circle 3 spell you will learn. It sends a wall of fire in the direction you are facing, charring everything in its path)\n\nPress enter to continue",
            "'Victory belongs to those that believe in it most' - Randall Wallace. This might not be an universal truth... but I think you believed more than those zombies, and as such, I guess it applies to this ocasion. Good job young fantasy typer, you surprise me still... \n\nPress enter to continue",
            "Your previous body just became an undead delicacy. Remember the wise words of Mahatma Gandhi 'Strenght does not come from physical capacity. It comes from an indomitable will.'. Learning when to give up is a very important skill to develop. I believe you can do this with some practice, never falter friend... hope must be the last thing to disapear.\nPress enter to continue")
        elif key == pygame.K_9:
            self.make_arena(9)
            return chalenge("survival",
            "Are you sure you want to do this chalenge? Only real fantasy typer can even begin to have a shoot at the amount of undead that will rise from the ground. If you think you have what it takes... step forward... ready your fingers... I don't believe you are yet ready for the ultimate survival chalenge... but nevertheless... i wish you good luck, you will definitely need it.\nabilities:\ndash\nhigh jump\nbackflip\npull bow\nrelease bow\nfirebolt\nslash\nthrust\nfire breath\nfireball\nlightning bolt\ninfernal beam\n\nPress enter to continue",
            "Finaly... with every bit of sweat... you rise victorious! Breath for a second and realize the feelings rushing in your thoughts... grasp them with your hand... save them in your memory... that is what gaming is all about. Overcoming chalenges while brekaing your limits. \nFantasy typer... you are ready to start your adventure.\nPress enter to continue",
            "Did you believe in yourself hard enough? I don't think so... i mean... this is the ultimate survival chalenge, you don't have it in you... turn back fantasy typer... only real man can exterminate these undead.\nPress enter to continue")
        
        else:
            return self
            

        
        
        #return pause(self)
        #return chalenge()
        
        
    def make_arena(self,n):
    
        gstate.get().dummy = creature("dummy",ai_component = ai_component_circle(gstate.get().id_creature), color = gstate.get().cyan)
        #gstate.get().arena.add_creature(gstate.get().dummy)
        
      
        gstate.get().dummy2 = creature("dummy2",ai_component = ai_component_big_circle(gstate.get().id_creature), position = [4,4],color = gstate.get().grey, images = [pygame.image.load("skl1_bk1.gif"),pygame.image.load("skl1_rt2.gif"),pygame.image.load("skl1_fr1.gif"),pygame.image.load("skl1_lf2.gif")])
        #gstate.get().arena.add_creature(gstate.get().dummy2)
        
       
        gstate.get().doggo = creature("doggo",ai_component = ai_component_objective(gstate.get().id_creature, [10,10]), position = [10,10],color = gstate.get().light_brown)
        #gstate.get().arena.add_creature(gstate.get().doggo)
        
        gstate.get().doggo2 = creature("doggo2",ai_component = ai_component_chase(gstate.get().id_creature, gstate.get().dummy2), position = [15,15],color = gstate.get().caramel,images = [pygame.image.load("spd1_bk1.gif"),pygame.image.load("spd1_rt2.gif"),pygame.image.load("spd1_fr1.gif"),pygame.image.load("spd1_lf2.gif")])
        #gstate.get().arena.add_creature(gstate.get().doggo2)
    
        gstate.get().vacaboy.restart
        if n == 1:
            gstate.get().arena = arena(16,16,[],[gstate.get().dummy,gstate.get().dummy2,gstate.get().doggo,gstate.get().doggo2],[],[])
            gstate.get().vacaboy.position = [7,14]
            
        elif n == 2:
            a_1 = creature("target",ai_component = ai_component(gstate.get().id_creature),position = [15,1],images = [pygame.image.load("target_3.png"),pygame.image.load("target_1.png"),pygame.image.load("target_1.png"),pygame.image.load("target_3.png")])
            a_1.facing_index = 2
            a_2 = creature("target",ai_component = ai_component(gstate.get().id_creature),position = [15,19],images = [pygame.image.load("target_3.png"),pygame.image.load("target_1.png"),pygame.image.load("target_1.png"),pygame.image.load("target_3.png")])
            a_2.facing_index = 0
            a_3 = creature("target",ai_component = ai_component(gstate.get().id_creature),position = [1,10],images = [pygame.image.load("target_3.png"),pygame.image.load("target_1.png"),pygame.image.load("target_1.png"),pygame.image.load("target_3.png")])
            a_3.facing_index = 1
            a_4 = creature("target",ai_component = ai_component(gstate.get().id_creature),position = [28,12],images = [pygame.image.load("target_3.png"),pygame.image.load("target_1.png"),pygame.image.load("target_1.png"),pygame.image.load("target_3.png")])
            a_4.facing_index = 3
            a_5 = creature("target",ai_component = ai_component(gstate.get().id_creature),position = [2,2],images = [pygame.image.load("target_3.png"),pygame.image.load("target_1.png"),pygame.image.load("target_1.png"),pygame.image.load("target_3.png")])
            a_5.facing_index = 1
            a_6 = creature("target",ai_component = ai_component(gstate.get().id_creature),position = [2,19],images = [pygame.image.load("target_3.png"),pygame.image.load("target_1.png"),pygame.image.load("target_1.png"),pygame.image.load("target_3.png")])
            a_6.facing_index = 0
            a_7 = creature("target",ai_component = ai_component(gstate.get().id_creature),position = [29,15],images = [pygame.image.load("target_3.png"),pygame.image.load("target_1.png"),pygame.image.load("target_1.png"),pygame.image.load("target_3.png")])
            a_7.facing_index = 3
            
            # a_1.MAX_HP = 5
            # a_1.HP = 5
            # a_2.MAX_HP = 5
            # a_2.HP = 5
            # a_3.MAX_HP = 5
            # a_3.HP = 5
            # a_4.MAX_HP = 5
            # a_4.HP = 5
            # a_5.MAX_HP = 5
            # a_5.HP = 5
            # a_6.MAX_HP = 5
            # a_6.HP = 5
            # a_7.MAX_HP = 5
            # a_7.HP = 5
            
            gstate.get().arena = arena(30,20,[],[a_1,a_2,a_3,a_4,a_5,a_6,a_7],[],[])
            gstate.get().vacaboy.position = [15,11]
        
        elif n == 3:
            
            gstate.get().usain_bolt = creature("Usain Bolt",ai_component = ai_component_chalenge_3(gstate.get().id_creature),position = [14,11],images = [pygame.image.load("skl1_bk1.gif"),pygame.image.load("skl1_rt2.gif"),pygame.image.load("skl1_fr1.gif"),pygame.image.load("skl1_lf2.gif")])
            
            gstate.get().vacaboy.position = [11,11]
            obstacles = []
            

            for x in range(26):
                    for y in range(16):
                        if (x == 2 or x == 23) and (y >=1 and y <=11 and y!= 9):
                            pass
                        elif (x == 3 or x == 22) and (y ==1 or y ==11):
                            pass
                        elif (x == 4 or x == 21) and ((y >=3 and y <=11)): #or y == 1):
                            pass
                        elif ((x >= 5 and x <= 7) or (x <= 20 and x >= 18)) and (y ==3 or y == 1):
                            pass
                        elif (x == 8 or x == 17) and ((y >=3 and y <=11) or y == 1):
                            pass
                        elif (x == 9 or x == 16) and y ==1:
                            pass
                        elif (x == 10 or x == 15) and y ==1:
                            pass
                        elif (x == 11 or x == 14) and (y >=1 and y <=11 and y!=5 ):
                            pass
                        else:
                            obstacles.append(obstacle("tree",[x,y],[pygame.image.load("ima\map_green_obstacle_1.png")],[x*gstate.get().square_width,y*gstate.get().square_height-20]))
            #obstacles.append(obstacle("edge_of_the_map",[13,-1],[pygame.image.load("ima\map_green_obstacle_1.png")],[13*gstate.get().square_width,-1*gstate.get().square_height]))
            #obstacles.append(obstacle("edge_of_the_map",[13,16],[pygame.image.load("ima\map_green_obstacle_1.png")],[13*gstate.get().square_width,16*gstate.get().square_height]))
            gstate.get().arena = arena(26,16,[],[gstate.get().usain_bolt],[],obstacles = obstacles)
            gstate.get().arena.renderables.append(rectrenderable_changeble(lambda:8*gstate.get().arena.square_width,lambda:11*gstate.get().arena.square_height,lambda:gstate.get().arena.square_width,lambda:gstate.get().arena.square_height,lambda: gstate.get().golden))
            gstate.get().arena.renderables.append(rectrenderable_changeble(lambda:17*gstate.get().arena.square_width,lambda:11*gstate.get().arena.square_height,lambda:gstate.get().arena.square_width,lambda:gstate.get().arena.square_height,lambda: gstate.get().golden))
            
            #gstate.get().arena = arena(26,16,[],[],[],obstacles = obstacles)
            
        elif n == 4:
            a_1 = creature("target",ai_component = ai_component(gstate.get().id_creature),position = [4,4],images = [pygame.image.load("target_3.png"),pygame.image.load("target_1.png"),pygame.image.load("target_1.png"),pygame.image.load("target_3.png")])
            a_1.facing_index = 2
            a_2 = creature("target",ai_component = ai_component(gstate.get().id_creature),position = [7,4],images = [pygame.image.load("target_3.png"),pygame.image.load("target_1.png"),pygame.image.load("target_1.png"),pygame.image.load("target_3.png")])
            a_2.facing_index = 0
            a_3 = creature("target",ai_component = ai_component(gstate.get().id_creature),position = [7,1],images = [pygame.image.load("target_3.png"),pygame.image.load("target_1.png"),pygame.image.load("target_1.png"),pygame.image.load("target_3.png")])
            a_3.facing_index = 1
            a_4 = creature("target",ai_component = ai_component(gstate.get().id_creature),position = [5,1],images = [pygame.image.load("target_3.png"),pygame.image.load("target_1.png"),pygame.image.load("target_1.png"),pygame.image.load("target_3.png")])
            a_4.facing_index = 3
            a_5 = creature("target",ai_component = ai_component(gstate.get().id_creature),position = [5,6],images = [pygame.image.load("target_3.png"),pygame.image.load("target_1.png"),pygame.image.load("target_1.png"),pygame.image.load("target_3.png")])
            a_5.facing_index = 1
            a_6 = creature("target",ai_component = ai_component(gstate.get().id_creature),position = [1,6],images = [pygame.image.load("target_3.png"),pygame.image.load("target_1.png"),pygame.image.load("target_1.png"),pygame.image.load("target_3.png")])
            a_6.facing_index = 0
            a_7 = creature("target",ai_component = ai_component(gstate.get().id_creature),position = [1,3],images = [pygame.image.load("target_3.png"),pygame.image.load("target_1.png"),pygame.image.load("target_1.png"),pygame.image.load("target_3.png")])

            a_7 = creature("target",ai_component = ai_component(gstate.get().id_creature),position = [1,9],images = [pygame.image.load("target_3.png"),pygame.image.load("target_1.png"),pygame.image.load("target_1.png"),pygame.image.load("target_3.png")])

            a_8 = creature("target",ai_component = ai_component(gstate.get().id_creature),position = [8,9],images = [pygame.image.load("target_3.png"),pygame.image.load("target_1.png"),pygame.image.load("target_1.png"),pygame.image.load("target_3.png")])

            a_9 = creature("target",ai_component = ai_component(gstate.get().id_creature),position = [9,2],images = [pygame.image.load("target_3.png"),pygame.image.load("target_1.png"),pygame.image.load("target_1.png"),pygame.image.load("target_3.png")])

            a_10 = creature("target",ai_component = ai_component(gstate.get().id_creature),position = [1,2],images = [pygame.image.load("target_3.png"),pygame.image.load("target_1.png"),pygame.image.load("target_1.png"),pygame.image.load("target_3.png")])

            a_11 = creature("target",ai_component = ai_component(gstate.get().id_creature),position = [9,2],images = [pygame.image.load("target_3.png"),pygame.image.load("target_1.png"),pygame.image.load("target_1.png"),pygame.image.load("target_3.png")])
            
            a_12 = creature("target",ai_component = ai_component(gstate.get().id_creature),position = [9,0],images = [pygame.image.load("target_3.png"),pygame.image.load("target_1.png"),pygame.image.load("target_1.png"),pygame.image.load("target_3.png")])

            a_13 = creature("target",ai_component = ai_component(gstate.get().id_creature),position = [9,8],images = [pygame.image.load("target_3.png"),pygame.image.load("target_1.png"),pygame.image.load("target_1.png"),pygame.image.load("target_3.png")])
            a_14 = creature("target",ai_component = ai_component(gstate.get().id_creature),position = [8,7],images = [pygame.image.load("target_3.png"),pygame.image.load("target_1.png"),pygame.image.load("target_1.png"),pygame.image.load("target_3.png")])

            #a_7 = creature("target",ai_component = ai_component(gstate.get().id_creature),position = [1,3],images = [pygame.image.load("target_3.png"),pygame.image.load("target_1.png"),pygame.image.load("target_1.png"),pygame.image.load("target_3.png")])

            obstacles = []
            x,y = 2,4
            obstacles.append(obstacle("tree",[x,y],[pygame.image.load("ima\map_green_obstacle_1.png")],[x*gstate.get().square_width,y*gstate.get().square_height-20]))
            
            x,y = 2,3
            obstacles.append(obstacle("tree",[x,y],[pygame.image.load("ima\map_green_obstacle_1.png")],[x*gstate.get().square_width,y*gstate.get().square_height-20]))
            x,y = 6,3
            obstacles.append(obstacle("tree",[x,y],[pygame.image.load("ima\map_green_obstacle_1.png")],[x*gstate.get().square_width,y*gstate.get().square_height-20]))
            
            x,y = 9,9
            obstacles.append(obstacle("tree",[x,y],[pygame.image.load("ima\map_green_obstacle_1.png")],[x*gstate.get().square_width,y*gstate.get().square_height-20]))
            
            
            # a_1.MAX_HP = 5
            # a_1.HP = 5
            # a_2.MAX_HP = 5
            # a_2.HP = 5
            # a_3.MAX_HP = 5
            # a_3.HP = 5
            # a_4.MAX_HP = 5
            # a_4.HP = 5
            # a_5.MAX_HP = 5
            # a_5.HP = 5
            # a_6.MAX_HP = 5
            # a_6.HP = 5
            # a_7.MAX_HP = 5
            # a_7.HP = 5
            
            gstate.get().arena = arena(10,10,[],[a_1,a_2,a_3,a_4,a_5,a_6,a_7,a_8,a_9,a_10,a_11,a_12,a_13,a_14],[],[],obstacles = obstacles)
            gstate.get().vacaboy.position = [0,0]
            gstate.get().vacaboy.ai_component.time_since_ability_cast[4] = 10000
        elif n == 5:
            #zombie = creature("zombie",ai_component = ai_component_zombie(gstate.get().id_creature,enemies = [gstate.get().vacaboy]),position = [1,1],images = [pygame.image.load("skl1_bk1.gif"),pygame.image.load("skl1_rt2.gif"),pygame.image.load("skl1_fr1.gif"),pygame.image.load("skl1_lf2.gif")])
            #zombie = creature("zombie",ai_component = ai_component_zombie(gstate.get().id_creature,enemies = [gstate.get().vacaboy]),position = [1,1],images = [pygame.image.load("ima\zombie_1.jpg"),pygame.image.load("ima\zombie_0.jpg"),pygame.image.load("ima\zombie_0.jpg"),pygame.image.load("ima\zombie_1.jpg")])
            zombie = gstate.get().zombie.define(ai_component = ai_component_zombie(gstate.get().id_creature,enemies = [gstate.get().vacaboy]),position = [1,1])
            gstate.get().vacaboy.position = [1,7]
            
            
            #zombie.MAX_HP = 70
            #zombie.HP = 70
            gstate.get().arena = arena(8,8,[],[zombie],[],[])
        
        elif n == 6:
            zombie = creature("zombie",ai_component = ai_component_zombie(gstate.get().id_creature,enemies = [gstate.get().vacaboy]),position = [13,0],images = [pygame.image.load("ima\zombie_1.jpg"),pygame.image.load("ima\zombie_0.jpg"),pygame.image.load("ima\zombie_0.jpg"),pygame.image.load("ima\zombie_1.jpg")])
            gstate.get().vacaboy.position = [13,18]
            gstate.get().vacaboy.HP = 1
            zombie.MAX_HP = 70
            zombie.HP = 70
            obstacles = []
            
            #obstacle("tree",[x,y],[pygame.image.load("ima\map_green_obstacle_1.png")],[x_1,y_1],3)
            #x = 0
            #y = 0
            for x in range(26):
                if x != 13:
                    for y in range(19):
                        obstacles.append(obstacle("tree",[x,y],[pygame.image.load("ima\map_green_obstacle_1.png")],[x*gstate.get().square_width,y*gstate.get().square_height]))
            obstacles.append(obstacle("edge_of_the_map",[13,-1],[pygame.image.load("ima\map_green_obstacle_1.png")],[13*gstate.get().square_width,-1*gstate.get().square_height]))
            obstacles.append(obstacle("edge_of_the_map",[13,19],[pygame.image.load("ima\map_green_obstacle_1.png")],[13*gstate.get().square_width,19*gstate.get().square_height]))
            gstate.get().arena = arena(26,19,[],[zombie],[],obstacles = obstacles)
        
        elif n == 7:
            #skeleton_0 = creature("skeleton",ai_component = ai_component_skeleton(gstate.get().id_creature,enemies = [gstate.get().vacaboy]),position = [15,16],images = [pygame.image.load("skl1_bk1.gif"),pygame.image.load("skl1_rt2.gif"),pygame.image.load("skl1_fr1.gif"),pygame.image.load("skl1_lf2.gif")])
            
            skeleton_0 = gstate.get().skeleton.define(ai_component = ai_component_skeleton(gstate.get().id_creature,enemies = [gstate.get().vacaboy]),position = [15,16])
            skeleton_0.facing_index = 0
            
            skeleton_1 = creature("skeleton",ai_component = ai_component_skeleton(gstate.get().id_creature,enemies = [gstate.get().vacaboy]),position = [0,1],images = [pygame.image.load("skl1_bk1.gif"),pygame.image.load("skl1_rt2.gif"),pygame.image.load("skl1_fr1.gif"),pygame.image.load("skl1_lf2.gif")])
            skeleton_1.facing_index = 1
            
            
            skeleton_2 = creature("skeleton",ai_component = ai_component_skeleton(gstate.get().id_creature,enemies = [gstate.get().vacaboy]),position = [1,0],images = [pygame.image.load("skl1_bk1.gif"),pygame.image.load("skl1_rt2.gif"),pygame.image.load("skl1_fr1.gif"),pygame.image.load("skl1_lf2.gif")])
            skeleton_2.facing_index = 2
            
            skeleton_3 = creature("skeleton",ai_component = ai_component_skeleton(gstate.get().id_creature,enemies = [gstate.get().vacaboy]),position = [16,15],images = [pygame.image.load("skl1_bk1.gif"),pygame.image.load("skl1_rt2.gif"),pygame.image.load("skl1_fr1.gif"),pygame.image.load("skl1_lf2.gif")])
            skeleton_3.facing_index = 3
            
            gstate.get().vacaboy.position = [8,8]
            
            #zombie.MAX_HP = 70
            #zombie.HP = 70
            obstacles = []
            
            #obstacle("tree",[x,y],[pygame.image.load("ima\map_green_obstacle_1.png")],[x_1,y_1],3)
            #x = 0
            #y = 0
            #for x in range(26):
            #    if x != 13:
            #        for y in range(19):
            #            obstacles.append(obstacle("tree",[x,y],[pygame.image.load("ima\map_green_obstacle_1.png")],[x*gstate.get().square_width,y*gstate.get().square_height]))
            #obstacles.append(obstacle("edge_of_the_map",[13,-1],[pygame.image.load("ima\map_green_obstacle_1.png")],[13*gstate.get().square_width,-1*gstate.get().square_height]))
            #obstacles.append(obstacle("edge_of_the_map",[13,19],[pygame.image.load("ima\map_green_obstacle_1.png")],[13*gstate.get().square_width,19*gstate.get().square_height]))
            gstate.get().arena = arena(17,17,[],[skeleton_0,skeleton_1,skeleton_2,skeleton_3],[],obstacles = obstacles)
        
        elif n == 8:
        
            ev = event("survival",[0,0],1,10)
            gstate.get().vacaboy.position = [8,8]
            
            #skeleton_0 = gstate.get().skeleton.define(ai_component = ai_component_skeleton(gstate.get().id_creature,enemies = [gstate.get().vacaboy]),position = [15,16])
            #skeleton_0.facing_index = 0
            
            
            #zombie = creature("zombie",ai_component = ai_component_zombie(gstate.get().id_creature,enemies = [gstate.get().vacaboy]),position = [8,0],images = [pygame.image.load("ima\zombie_1.jpg"),pygame.image.load("ima\zombie_0.jpg"),pygame.image.load("ima\zombie_0.jpg"),pygame.image.load("ima\zombie_1.jpg")])
            
            gstate.get().arena = arena(28,20,[],creatures = [],events = [ev])
            #gstate.get().arena = arena(28,20,[],creatures = [skeleton_0],events = [])
        elif n == 9:
        
            ev = event("survival2",[0,0],1,20)
            gstate.get().vacaboy.position = [8,8]
            
            #skeleton_0 = gstate.get().skeleton.define(ai_component = ai_component_skeleton(gstate.get().id_creature,enemies = [gstate.get().vacaboy]),position = [15,16])
            #skeleton_0.facing_index = 0
            
            
            #zombie = creature("zombie",ai_component = ai_component_zombie(gstate.get().id_creature,enemies = [gstate.get().vacaboy]),position = [8,0],images = [pygame.image.load("ima\zombie_1.jpg"),pygame.image.load("ima\zombie_0.jpg"),pygame.image.load("ima\zombie_0.jpg"),pygame.image.load("ima\zombie_1.jpg")])
            
            gstate.get().arena = arena(28,20,[],creatures = [],events = [ev])

        #gstate.get().vacaboy.position = [2,2]


        
        gstate.get().arena.add_creature(gstate.get().vacaboy)
        #pillar = Object()
        #gstate.get().arena.add_object(pillar)

        



#__________________________________________________________________________________________________________________________________________________________________________________

class beginning_chalenge(state):

    def __init__(self, previous_state,text = "press enter to start"):
        self.name = "beginning_chalenge"
        self.previous_state = previous_state
        
        self.renderables = []
        
        #self.renderables.append(text.renderable_changeble(lambda: ))
        self.surface = pygame.Surface((gstate.get().current_width,gstate.get().current_height))
        self.surface.set_alpha(128) 
        self.surface.fill(gstate.get().light_grey) 
        self.write_centered(self.surface, "PAUSE",[gstate.get().current_width/2,0],gstate.get().current_width/2 - 1, gstate.get().font_pause, gstate.get().black)
        self.text = text
        self.write_centered(gstate.get().screen, self.text,[gstate.get().current_width/2-200,200],gstate.get().current_width/2 - 100, gstate.get().fontA, gstate.get().black)
        
        #self.renderables.append(textrenderable(330, 295, gstate.get().light_grey, gstate.get().fontend, lambda: "click anywhere"))
        
        
        
        gstate.get().previous_arena = gstate.get().arena.recreate_arena()
            
    def effect(self): 
        return self


    def draw(self, screen):
        
        self.previous_state.draw(screen)
        for r in self.renderables:
            r.draw(screen)
        gstate.get().screen.blit(self.surface, (0,0))
    

    def key_type(self, key):
        super().key_type(key)
        
        if key == pygame.K_RETURN:

            self.write_centered(self.surface, "3",[gstate.get().current_width/2-300,200],gstate.get().current_width/2 - 1, gstate.get().font_pause_2, gstate.get().black)
            self.draw(gstate.get().screen)
            pygame.display.update()
            pygame.time.delay(1000)

            self.write_centered(self.surface, "2",[gstate.get().current_width/2-300,300],gstate.get().current_width/2 - 1, gstate.get().font_pause_2, gstate.get().black)
            self.draw(gstate.get().screen)
            pygame.display.update()
            pygame.time.delay(1000)

            self.write_centered(self.surface, "1",[gstate.get().current_width/2-300,400],gstate.get().current_width/2 - 1, gstate.get().font_pause_2, gstate.get().black)
            self.draw(gstate.get().screen)
            pygame.display.update()
            pygame.time.delay(1000)
            pygame.event.get()
            return self.previous_state
            
        elif key == pygame.K_F4:
            self.surface = pygame.Surface((gstate.get().current_width,gstate.get().current_height))
            self.surface.set_alpha(128) 
            self.surface.fill(gstate.get().light_grey) 
            gstate.get().arena.clock()
        
        return self


class chalenge(state):

    def __init__(self,
    objective = "kill everything",
    start_text = "",
    end_text_win = "Time to receive your hardly earned rewards! \nfirst of all, you get this beautiful text. \n\nyou algo get my undying admiration! \n\nyou have killed all the squares, now all the circles in the world love you for ending the 'quadratura do circulo' problem\n\npress enter to continue",
    end_text_lose = "You lost"):
        super().__init__()
        self.name = "chalenge"
        self.write_centered(gstate.get().screen, "Time to FIGHT! \nclick any letter",[gstate.get().current_width/2,20],gstate.get().current_width/2 - 100, gstate.get().fontA, gstate.get().light_grey)
        #self.renderables.append(textrenderable(330, 295, gstate.get().light_grey, gstate.get().fontend, lambda: "click anywhere"))
        self.time = 0
        self.renderables.append(rectrenderable_changeble(lambda: gstate.get().arena_width, lambda: 0, lambda: gstate.get().current_width - gstate.get().arena_width, lambda: gstate.get().current_height,lambda: gstate.get().caramel))
        self.renderables.append(textrenderable_changeble(lambda: gstate.get().current_width-80, lambda: 5, lambda: (255,0,0), lambda: gstate.get().fonttime, lambda: str(math.ceil(self.time))))
        
        self.objective = objective
        self.chalenge_complete = False
        self.ready_to_start = False
        self.start_text = start_text
        self.end_text_win = end_text_win
        self.end_text_lose = end_text_lose
            
    def effect(self):

        #clock:
        
        
        if not gstate.get().pause:
            #pygame.time.delay(gstate.get().tick)
            pygame.time.wait(gstate.get().tick)
            
            gstate.get().arena.clock()
            
            
            self.time += gstate.get().tick_time
            
        if not self.ready_to_start:
            self.ready_to_start = True
            return beginning_chalenge(self,self.start_text)
        
        #verify if objective is achieved, ending the chalenge:
        
        if self.objective == "kill everything":
            if gstate.get().arena.creatures == [gstate.get().vacaboy]:
                self.chalenge_complete = True
                self.end_text = self.end_text_win
            elif gstate.get().vacaboy not in gstate.get().arena.creatures:
                self.chalenge_complete = True
                self.end_text = self.end_text_lose

        elif self.objective == "reach destination":
            if gstate.get().vacaboy.position == [8,11]:
                if [i for i in gstate.get().arena.creatures if i.name == "Usain Bolt"][0].position == [17,11]:
                    self.chalenge_complete = True

                    pygame.time.wait(2000)
                    return rewards("You were not fast enough... I mean... He IS the world record holder... what did you expect? \nClick enter to proceed and give it another try! \n\nhint... when you can't be faster than your opponent... be smarter ;)")
                else:
                    self.chalenge_complete = True
                    pygame.time.wait(2000)
                    return rewards("YOU WON!\nYou are a fast fantasy type gamer indeed! I never stopped believing in you...\nWhat does a world record holding have against your mighty fantasy type fingers!?\n\nclick enter to proceed")
        elif self.objective == "target practice":
            if gstate.get().arena.creatures == [gstate.get().vacaboy]:
                self.chalenge_complete = True
                if self.time < 35:
                    return rewards(" - 'You dont trust my skill? Put an apple on your head and i will show you'\n\nCareful folks, we have a Robin Hood amongst us.\nDon't let this get into you head though... those target weren't moving a lot and they were not trying to kill you...\nIf you want to be true a fantasy type adventurer, you need to be able to do this chalenge in your sleep...\nNevertheless... good job my friend. You have my respect.\n\nPress enter to continue")
                else:
                    return rewards("You were not fast enough... \nDon't let your courage fade fantasy typer... These targets were suposed to be stationary... But i am pretty sure i saw one move during your chalenge. You'll get them next time champ!\n\nhint: when you ready your bow, instead of typing release bow... you can simply press 1 to shoot your arrow. as you see... itens are usefull BECAUSE they can be used by typing numbers.\n\nPress enter to continue")
        elif self.objective == "chain lightning":
            if gstate.get().arena.creatures == [gstate.get().vacaboy]:
                self.chalenge_complete = True
                return rewards("Good job fantasy typer! we have a bunch of fryed targets that need changing now... i will send someone to take care of that, dont worry. Now... i wasn't watching so i realy dont know if you cheated by using other abilities to kill the targets... but i trust you... you seem like a trustworthy fantasy type adventurer! Have fun typing! \n\nPress enter to continue")
        
        if self.objective == "survival":
            if gstate.get().arena.creatures == [gstate.get().vacaboy] and [i for i in gstate.get().arena.events if i.name == "survival"]==[]:
                self.chalenge_complete = True
                self.end_text = self.end_text_win
            elif gstate.get().vacaboy not in gstate.get().arena.creatures:
                self.chalenge_complete = True
                self.end_text = self.end_text_lose
        
        if self.chalenge_complete:
            pygame.time.wait(2000)
            return rewards(self.end_text)
            
        else:
            return self


    def draw(self, screen):
        super().draw(screen)
        #print(len(self.renderables))
        #gstate.get().arena.draw(screen)
        for r in self.renderables:
            
            r.draw(screen)
        
        gstate.get().arena.draw(screen)
            
        if self.objective != "chain lightning":
        
            for i in range(len(gstate.get().arena.creatures)): # isto identifica quantos creatures estao em campo e as suas ultimas habilidades usadas. e a sua vida.
                textrenderable(gstate.get().arena_width + 1, i * 80, gstate.get().red, gstate.get().fontA, lambda: gstate.get().arena.creatures[i].name).draw(screen)
                textrenderable(gstate.get().arena_width + 1, i * 80 + 25, gstate.get().red, gstate.get().fontA, lambda: gstate.get().arena.creatures[i].used_abilities[0].name).draw(screen)
                
                barrenderable(gstate.get().arena_width + 1 + 5, i * 80 + 50, gstate.get().current_width - gstate.get().arena_width - 10, 10, gstate.get().redest,gstate.get().greenest,lambda: (gstate.get().arena.creatures[i].HP, gstate.get().arena.creatures[i].MAX_HP)).draw(screen)
            
            for i in range(len(gstate.get().arena.corpses)): # isto identifica quantos corpses estao em campo e as suas ultimas habilidades usadas. e a sua vida.
                aux_1 = len(gstate.get().arena.creatures)
                textrenderable(gstate.get().arena_width + 1, (i + aux_1) * 80, gstate.get().red, gstate.get().fontA, lambda: gstate.get().arena.corpses[i].name).draw(screen)
                textrenderable(gstate.get().arena_width + 1, (i + aux_1) * 80 + 25, gstate.get().red, gstate.get().fontA, lambda: gstate.get().arena.corpses[i].used_abilities[0].name).draw(screen)
                
                barrenderable(gstate.get().arena_width + 1 + 5, (i + aux_1) * 80 + 50, gstate.get().current_width - gstate.get().arena_width - 10, 10, gstate.get().redest,gstate.get().greenest,lambda: (gstate.get().arena.corpses[i].HP, gstate.get().arena.corpses[i].MAX_HP)).draw(screen)

        
    def key_type(self, key):
        super().key_type(key)
        #for i in gstate.get().arena.creatures:
        #    i.decisions.append(decision(i,2,"right_1"))
        
        gstate.get().vacaboy.ai_component.key_type(key)
        
        if key == pygame.K_F1:
            print("aqui no state key_type")
            return pause(self)
        if key == pygame.K_ESCAPE:
            print("aqui no state key_type")
            return rewards("You just gave up... but never falter, with practice comes perfection, I believe in you... \nyou should too <3 \n\npress enter to continue")
        
        
        #if gstate.get().doggo2.ai_component.creature_to_chase == gstate.get().dummy:
        #    gstate.get().doggo2.ai_component.creature_to_chase = gstate.get().dummy2
        #elif gstate.get().doggo2.ai_component.creature_to_chase == gstate.get().dummy2:
        #    gstate.get().doggo2.ai_component.creature_to_chase = gstate.get().doggo
        #elif gstate.get().doggo2.ai_component.creature_to_chase == gstate.get().doggo:
        #    gstate.get().doggo2.ai_component.creature_to_chase = gstate.get().dummy
        
        return self


#__________________________________________________________________________________________________________________________________________________________________________________

class rewards(state):

    def __init__(self,text = "Time to receive your hardly earned rewards! \nfirst of all, you get this beautiful text. \n\nyou algo get my undying admiration! \n\nyou have killed all the squares, now all the circles in the world love you for ending the 'quadratura do circulo' problem\n\npress enter to continue"):
        super().__init__()
        self.name = "rewards"
        self.text = text
        self.write_centered(gstate.get().screen, self.text,[gstate.get().current_width/2,20],gstate.get().current_width/2 - 100, gstate.get().fontA, gstate.get().black)
        #self.renderables.append(textrenderable(330, 295, gstate.get().light_grey, gstate.get().fontend, lambda: "click anywhere"))
        
        
        
        gstate.get().previous_arena = gstate.get().arena.recreate_arena()
            
    def effect(self): 
        return self


    def draw(self, screen):
        super().draw(screen)
    

    def key_type(self, key):
        super().key_type(key)
        
        if key == pygame.K_RETURN:
            print("aqui no state key_type")
            return decide_chalenge()
        
        return self


#__________________________________________________________________________________________________________________________________________________________________________________

class pause(state):

    def __init__(self, previous_state):
        self.name = "pause"
        self.previous_state = previous_state
        
        self.renderables = []
        
        #self.renderables.append(text.renderable_changeble(lambda: ))
        self.surface = pygame.Surface((gstate.get().current_width,gstate.get().current_height))
        self.surface.set_alpha(128) 
        self.surface.fill(gstate.get().light_grey) 
        self.write_centered(self.surface, "PAUSE",[gstate.get().current_width/2,0],gstate.get().current_width/2 - 1, gstate.get().font_pause, gstate.get().grey)
        #self.renderables.append(textrenderable(330, 295, gstate.get().light_grey, gstate.get().fontend, lambda: "click anywhere"))
        
        
        
        gstate.get().previous_arena = gstate.get().arena.recreate_arena()
            
    def effect(self): 
        return self


    def draw(self, screen):
        
        self.previous_state.draw(screen)
        for r in self.renderables:
            r.draw(screen)
        gstate.get().screen.blit(self.surface, (0,0))
    

    def key_type(self, key):
        super().key_type(key)
        
        if key == pygame.K_F1:

            self.write_centered(self.surface, "3",[gstate.get().current_width/2,200],gstate.get().current_width/2 - 1, gstate.get().font_pause_2, gstate.get().grey)
            self.draw(gstate.get().screen)
            pygame.display.update()
            pygame.time.delay(1000)

            self.write_centered(self.surface, "2",[gstate.get().current_width/2,300],gstate.get().current_width/2 - 1, gstate.get().font_pause_2, gstate.get().grey)
            self.draw(gstate.get().screen)
            pygame.display.update()
            pygame.time.delay(1000)

            self.write_centered(self.surface, "1",[gstate.get().current_width/2,400],gstate.get().current_width/2 - 1, gstate.get().font_pause_2, gstate.get().grey)
            self.draw(gstate.get().screen)
            pygame.display.update()
            pygame.time.delay(1000)
            pygame.event.get()
            return self.previous_state
            
        elif key == pygame.K_F4:
            self.surface = pygame.Surface((gstate.get().current_width,gstate.get().current_height))
            self.surface.set_alpha(128) 
            self.surface.fill(gstate.get().light_grey) 
            gstate.get().arena.clock()
        
        return self


#__________________________________________________________________________________________________________________________________________________________________________________


#s = pygame.Surface((1000,750))  # the size of your rect
#s.set_alpha(128)                # alpha level
#s.fill((255,255,255))           # this fills the entire surface
#windowSurface.blit(s, (0,0))

