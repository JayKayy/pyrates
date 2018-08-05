class Island:
    """ Definition for islands """
    def __init__(self, name, x_coord, y_coord, kind, loot={}):
        self.name = name
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.island_type = kind
        self.loot = loot

    def get_name(self):
        return self.name
    def get_type(self):
        return self.island_type
    def get_items(self):
        return self.name
    def set_loot(self,loot):
        self.loot = loot
    def get_loot(self):
        return self.loot
    def get_x(self):
        return self.x_coord
    def get_y(self):
        return self.y_coord
