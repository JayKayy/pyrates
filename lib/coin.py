class Coin:
    """ Definition for coins """
    def __init__(self, x_coord, y_coord, loot={}):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.type = "coin"
        self.loot = loot

    def set_loot(self,loot):
        self.loot = loot
    def get_loot(self):
        return self.loot
    def get_x(self):
        return self.x_coord
    def get_y(self):
        return self.y_coord
    def get_type(self):
        return self.type
