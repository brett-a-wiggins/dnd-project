class Player(object):
    
    def __init__(self, name, player_class):
        self.name = name
        self.player_class = player_class
        self.items = []
        self.hit_points = 100
        self.gold = 50
        
    def pick_up_item(self, item):
        self.items.append(item)
        print(f"{item} has been added to your inventory")

    def drop_item(self, item_name):
        self.items.remove(item_name)
        print(f"{item_name} has been removed from your inventory")

    def attack(self, die_roll):
        pass

    def defend(self, die_roll):
        pass

    


