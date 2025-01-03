import pygame
from actors import Player, Goomba
from global_class import glob, actor_list, dead_list

class Map:
    def __init__(self, _map):
        self.map = _map
    def draw_map(self):
        for y, row in enumerate(self.map):
            for x, col in enumerate(row):
                if glob.active_camera.on == False:
                    if col == "x": pygame.draw.rect(glob.screen, glob.YELLOW, pygame.Rect(x*16, y*16, 16, 16))
                else:
                    loc_camera_coord = glob.active_camera.get_screen_coordinates(x,y)

                    if col == "x": pygame.draw.rect(glob.screen, glob.YELLOW, pygame.Rect(loc_camera_coord[0]*16, loc_camera_coord[1]*16, 16, 16))
    def load_actors(self):
        for y, row in enumerate(self.map):
            for x, col in enumerate(row):
                if col == "p":
                    actor_list.list.append(Player(x, y))
                if col == "e":
                    actor_list.list.append(Goomba(x, y))