import pygame
import math
from global_class import glob
from keyboard_ import keyboard

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.xspeed = 0
        self.yspeed = 0
        self.grounded = False
        self.contacts = [False, False, False, False]
    def update(self):
        if keyboard.is_held(pygame.K_RIGHT):
            self.xspeed += 0.01
        if keyboard.is_held(pygame.K_LEFT):
            self.xspeed -= 0.01
        if keyboard.is_held(pygame.K_UP):
            self.yspeed -= 0.01
        if keyboard.is_held(pygame.K_DOWN):
            self.yspeed += 0.01
        if keyboard.is_pressed(pygame.K_z) and self.contacts[0] == True:
            self.yspeed = -0.3
        
        self.yspeed += 0.01

        self.x += self.xspeed
        self.y += self.yspeed

        self.contacts = [False, False, False, False]

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
                        
                         
                    #BOTTOM RIGHT
                    if math.floor(self.x+1.0) == x and math.floor(self.y+1.0) == y:
                        if 1 - abs(self.x+1 - x) <= 1 - abs(self.y+1 - y):
                            self.yspeed = 0.0
                            self.y = y - 1
                            
                        else:
                            self.xspeed = 0.0
                            self.x = x - 1
                            self.contacts[0] = True
                        
                    
                    #TOP RIGHT
                    if math.floor(self.x+1.0) == x and math.floor(self.y) == y:
                        if 1 - abs(self.x+1 - x) <= self.y - y:
                            self.yspeed = 0.0
                            self.y = y + 1
                        else:
                            self.xspeed = 0.0
                            self.x = x - 1
                    #TOP LEFT
                    if math.floor(self.x) == x and math.floor(self.y) == y:
                        if self.x - x <= self.y - y:
                            self.yspeed = 0.0
                            self.y = y + 1
                        else:
                            self.xspeed = 0.0
                            self.x = x + 1

    def draw(self):
        pygame.draw.rect(glob.screen, glob.GREEN, pygame.Rect(self.x*16, self.y*16, 16, 16))