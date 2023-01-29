import pygame

class Global:
    def __init__(self):
        self.BLUE = (100,140,200)
        self.GREEN = (0,255,0)
        self.RED = (255,0,0)
        self.PURPLE = (205,50,200)
        self.YELLOW = (205,250,0)

        self.screen = pygame.display.set_mode((1600, 800))
        self.running = True
        self.clock = pygame.time.Clock()
        
        self.actor_list = []
        self.map = None

        self.map_0 = [
            "..............................................................................x",
            "..............................................................................x",
            "..............................................................................x",
            "..............................................................................x",
            "...........................................xxxxxxxxxxxx.......................x",
            "......................................................x.......................x",
            "......................................................x.......................x",
            "x..........xxxxxxxxxxxxx..............................x.......................x",
            "x..........x...........x..............................x.......................x",
            "x..........x...........x..............................x.......................x",
            "x..........x...........x..............................x.......................x",
            "x..........x...........x.............................xxx......................x",
            "x..p.......x...........x................xxxxxxxx..xxxxxxx.....................x",
            "x..........x...........x................x.........x...........................x",
            "xxxxxxxxxxxx...........x...x...x........xxxxxxxxxxx...........................x",
            "..............................................................................x",
            "..............................................................................x",
            "..............................................................................x",
            "..............................................................................x",
            "..............................................................................x",
            "..............................................................................x",
            "..............................................................................x",
            "..............................................................................x",
            "..............................................................................x",
            "..............................................................................x",
            "..............................................................................x",
            "..............................................................................x"
        ]
    
    
        

glob = Global()