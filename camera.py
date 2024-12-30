import global_class

class Camera:

    def __init__(self,_parent, _local_x, _local_y):
        self.parent = _parent
        self.local_x = _local_x
        self.local_y = _local_y
        self.on = False
        global_class.glob.active_camera = self

    def update(self):
        self.x = self.parent.x + self.local_x - 800/16
        self.y = self.parent.y + self.local_y - 400/16
    
    def get_screen_coordinates(self,_x, _y):
        return (_x - self.x, _y - self.y)