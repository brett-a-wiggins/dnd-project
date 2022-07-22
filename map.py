class Map(object):

    def __init__(self):
        
        self.map = {

        }

    def move(self, direction):
        pass

class Forest(object):
    
    def __init__(self, name, monsters, description):
        self.name = name
        self.loot = []
        self.monsters = monsters
        self.description = description

class Building(object):

    def __init__(self, name, type, monsters, description):
        self.type = type
        self.name = name
        self.loot = []
        self.monsters = monsters
        self.descritption = description


class Caverns(object):
    def __init__(self, name, type, monsters, description):
        self.type = type
        self.name = name
        self.loot = []
        self.monsters = monsters
        self.description = description
    