import pygame
from global_class import glob, actor_list, dead_list
from keyboard_ import keyboard
from map_ import Map

pygame.display.set_caption('Roaster')

glob.map = Map(glob.map_0)
glob.map.load_actors()

#GAME LOOP
while glob.running:
    
#UPDATING
    for event in pygame.event.get():   
        if event.type == pygame.QUIT:
            glob.running = False        
        keyboard.handle_event(event)
    
    for act in actor_list.list:
        
        if keyboard.is_held(pygame.K_a):
            
            act.rewind()
        else:
            act.record()
            act.update()
    
    if keyboard.is_held(pygame.K_a):
        dead_list.rewind()
        actor_list.rewind()
        
    else:
        dead_list.record()
        actor_list.record()
        
    
#DRAWING
    glob.screen.fill(glob.BLUE)
    glob.map.draw_map()

    for act in actor_list.list:
        act.draw()
    
    glob.clock.tick(60)

    pygame.display.update()