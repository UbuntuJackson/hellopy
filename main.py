import pygame
from global_class import glob
from keyboard_ import keyboard
from map_ import Map

pygame.display.set_caption('Braid')

glob.map = Map(glob.map_0)
glob.map.load_actors()

# game loop
while glob.running:
    
    for event in pygame.event.get():
      
        # Check for QUIT event      
        if event.type == pygame.QUIT:
            glob.running = False
        
        keyboard.handle_event(event)

    for act in glob.actor_list:
        act.update()
    
    glob.screen.fill(glob.BLUE)
    glob.map.draw_map()
    for act in glob.actor_list:
        act.draw()
    glob.clock.tick(60)

    pygame.display.update()