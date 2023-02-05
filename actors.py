import pygame
import math
from global_class import glob, actor_list, dead_list
from keyboard_ import keyboard

class Actor:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.xspeed = 0
        self.yspeed = 0
        self.grounded = False
        self.contacts = [False, False, False, False]
        self.facing = 1
        self.states = []
    def collision(self):
        for y, row in enumerate(glob.map.map):
            for x, col in enumerate(row):
                
                if col == "x":
                    
                    #BOTTOM LEFT - BOTTOM RIGHT
                    if (math.floor(self.x) == x and math.floor(self.y+1.0) == y and
                        math.floor(self.x+1) == x+1 and glob.map.map[y][x+1] == "x" and math.floor(self.y+1.0) == y):
                        self.yspeed = 0.0
                        self.y = y - 1
                    #TOP LEFT - TOP RIGHT
                    if (math.floor(self.x) == x and math.floor(self.y) == y and
                        math.floor(self.x+1) == math.floor(x+1) and glob.map.map[y][x+1] == "x" and math.floor(self.y) == math.floor(y)):
                        self.yspeed = 0.0
                        self.y = y + 1
                    #TOP LEFT - BOTTOM LEFT
                    if (math.floor(self.x) == x and math.floor(self.y) == y and
                        math.floor(self.x) == x and math.floor(self.y+1) == y+1 and glob.map.map[y+1][x] == "x"):
                        self.xspeed = 0.0
                        self.x = x + 1
                        
                    #TOP RIGHT - BOTTOM RIGHT
                    if (math.floor(self.x+1) == x and math.floor(self.y) == y and
                        math.floor(self.x+1) == x and math.floor(self.y+1) == y+1 and glob.map.map[y+1][x+1] == "x"):
                        self.xspeed = 0.0
                        self.x = x - 1
                    
                    #BOTTOM LEFT
                    if math.floor(self.x) == x and math.floor(self.y+1.0) == y:
                        if self.x - x <= 1 - abs(self.y+1 - y):
                            self.yspeed = 0.0
                            self.y = y - 1
                            self.contacts[0] = True
                            
                        else:
                            self.xspeed = 0.0
                            self.x = x + 1
                            self.contacts[2] = True
                        
                        
                         
                    #BOTTOM RIGHT
                    if math.floor(self.x+1.0) == x and math.floor(self.y+1.0) == y and self.x+1.0 != x:
                        if 1 - abs(self.x+1 - x) <= 1 - abs(self.y+1 - y):
                            self.yspeed = 0.0
                            self.y = y - 1
                            self.contacts[0] = True
                            
                        else:
                            self.xspeed = 0.0
                            self.x = x - 1
                            self.contacts[3] = True
                        
                    #TOP RIGHT
                    if math.floor(self.x+1.0) == x and math.floor(self.y) == y and self.x+1.0 != x:
                        if 1 - abs(self.x+1 - x) <= self.y - y:
                            self.yspeed = 0.0
                            self.y = y + 1
                        else:
                            self.xspeed = 0.0
                            self.x = x - 1
                            self.contacts[3] = True
                    #TOP LEFT
                    if math.floor(self.x) == x and math.floor(self.y) == y:
                        if self.x - x <= self.y - y:
                            self.yspeed = 0.0
                            self.y = y + 1
                        else:
                            self.xspeed = 0.0
                            self.x = x + 1
                            self.contacts[2] = True

    def record(self):
        self.states.append((self.x, self.y, self.xspeed, self.yspeed, self.contacts, self.facing))
    
    def rewind(self):
        for _ in range(4):
            if len(self.states) > 0: self.x, self.y, self.xspeed, self.yspeed, self.contacts, self.facing = self.states.pop()

class Player(Actor):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y
        self.xspeed = 0
        self.yspeed = 0
        self.grounded = False
        self.contacts = [False, False, False, False]
        self.facing = 1
        self.dashes = 1
        

    def update(self):
        

        if keyboard.is_held(pygame.K_RIGHT):
            self.facing = 1
            self.xspeed += 0.02
        if keyboard.is_held(pygame.K_LEFT):
            self.facing = -1
            self.xspeed -= 0.02
        
        if keyboard.is_pressed(pygame.K_z) and self.contacts[0] == True:
            self.yspeed = -0.3

        if self.contacts[0] == True and abs(self.xspeed) < 0.2: self.dashes = 1

        if keyboard.is_pressed(pygame.K_x) and self.dashes > 0:
            self.xspeed = 0.9 * self.facing
            
            if self.dashes > 0: self.dashes -= 1
        
        self.yspeed += 0.01
        
        self.xspeed *= 0.8

        self.x += self.xspeed
        self.y += self.yspeed

        self.contacts = [False, False, False, False]

        self.collision()

        for act in actor_list.list:
            if act.__class__.__name__ != "Player":
                if ((act.x <= self.x <= act.x+1 and act.y <= self.y <= act.y+1) or
                    (act.x <= self.x+1 <= act.x+1 and act.y <= self.y <= act.y+1) or
                    (act.x <= self.x+1 <= act.x+1 and act.y <= self.y+1 <= act.y+1) or
                    (act.x <= self.x <= act.x and act.y <= self.y+1 <= act.y+1) and
                    self.yspeed > 0
                ):
                    
                    dead_list.list.append(act)
                    
                    actor_list.list.remove(act)

    def draw(self):
        pygame.draw.rect(glob.screen, glob.GREEN, pygame.Rect(self.x*16, self.y*16, 16, 16))

class Goomba(Actor):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y
        self.xspeed = 0.0
        self.yspeed = 0.0
        self.grounded = False
        self.contacts = [False, False, False, False]
        self.facing = 1

    def update(self):
        

        self.xspeed = 0.05 * self.facing

        self.yspeed += 0.01
        
        self.xspeed *= 0.95

        self.x += self.xspeed
        self.y += self.yspeed

        self.contacts = [False, False, False, False]

        if self.x < 0 or self.x > len(glob.map.map[0]):
            return
        if self.y < 0 or self.y > len(glob.map.map):
            return

        if glob.map.map[math.floor(self.y)][math.floor(self.x+1)] == "x":
            self.facing = -1
        if glob.map.map[math.floor(self.y)][math.floor(self.x)] == "x":
            self.facing = 1

        self.collision()

        

        #if self.contacts[2]: self.facing = 1
        #if self.contacts[3]: self.facing = -1

        

    def draw(self):
        pygame.draw.rect(glob.screen, glob.RED, pygame.Rect(self.x*16, self.y*16, 16, 16))