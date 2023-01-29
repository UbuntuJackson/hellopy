import pygame
from actors import Player
from global_class import glob

class Map:
    def __init__(self, _map):
        self.map = _map
    def draw_map(self):
        for y, row in enumerate(self.map):
            for x, col in enumerate(row):
                
                if col == "x": pygame.draw.rect(glob.screen, glob.YELLOW, pygame.Rect(x*16, y*16, 16, 16))
    def load_actors(self):
        for y, row in enumerate(self.map):
            for x, col in enumerate(row):
                if col == "p":
                    glob.actor_list.append(Player(x, y))