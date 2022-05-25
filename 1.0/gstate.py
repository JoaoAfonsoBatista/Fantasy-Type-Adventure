import pygame
from arena import *
from abilities import *

class gstate():
    def __init__(self):
        self.players = [] #has all the players
        self.npcs = [] #has all player except craos. note: "player" and "npc" are different classes
        self.availabletargets = []
         #isto é um dicionário onde a chave é o nome da habilidade e isso leva para a habilidade em si.
        self.starterpacks = [[],[],[],[],[],[]] #starter packs are the elemental abilities they gain when they level. there is fire and ice now.
        self.deadcorpses = [] #has all the dead folk
        self.log = [] #isto mantem, ao longo de cada turno, quem da dano a quem. [caster, damage, target]
        
        self.run = True
        self.buffs = [[], [[],[]], [[],[]]] #buffs, cada lista, correspondentes aos buffs de cada stage, tem 2 listas, os buffs normais, e os legendary.
        
        self.undecided = []
        self.decisionlist = []


        self.abilities = {}
        self.movements = {}
        self.death_abilities = {}
        
        self.creatures_abstract = []
        
        self.fullscreen = False
        
        self.pause = False
        
        
        
        self.width = 1400
        self.height = 750
        
        self.current_width = self.width
        self.current_height = self.height
        
        self.arena_width = self.current_width - 300
        self.arena_height = self.current_height - 80
        
        self.square_width = 40
        
        self.square_height = 40
        
        
        #self.basic_arena = arena(16,16)

        #self.arena = self.basic_arena
        
        
        self.facing_cycle = [[0,-1],[1,0],[0,1],[-1,0]]
        
        self.tick = 50
        
        self.tick_time = self.tick * 0.001


        self.id_creature = 0
        
        
        self.fonttime = pygame.font.SysFont("comicsans", 50, True)
        self.fontwrite = pygame.font.SysFont("comicsans", 20, True)
        self.fontA = pygame.font.SysFont("mayence", 30, False, True)
        self.fontHP = pygame.font.SysFont("comicsans",20 ,False ,True)
        self.fontend = pygame.font.SysFont("mayence", 180, True)
        
        self.font_type = pygame.font.SysFont("lucidacalligraphy", 45, False, True)
        
        self.font_magneto = pygame.font.SysFont("magneto", 23, False, True)
        
        self.font_pause = pygame.font.SysFont("calisto", 150, False, False)
        self.font_pause_2 = pygame.font.SysFont("calisto", 75, False, False)

        self.light_grey = (210,210,210)
        self.grey = (170,170,170)
        self.light_orange = (255,200,150)
        self.cyan = (50, 255, 255)
        self.caramel = (218,165,32)
        self.red = (255,50,50)
        self.redest = (255,0,0)
        self.greenest = (0,255,0)
        self.light_brown = (200,150,100)
        self.white = (255,255,255)
        self.black = (0,0,0)
        self.violet = (204,153,255)
        self.golden = (255,223,0)
        
        

        
        
_s = None

def init():
    global _s
    if _s is not None:
        raise Exception("Initialized gstate more than once")
    _s = gstate()

def get():
    return _s
    

