class Item(object):
    def __init__(self, item_name, damage, hit_points, defence):
        self.item_name = item_name
        self.damage = damage
        self.hit_points = hit_points
        self.defence = defence

class MagicItem(Item):
    def __init__(self,item_name, damage, hit_points, defence, magic):
        super(MagicItem, self).__init__(item_name, damage, hit_points, defence)
        self.magic = magic

class Armor(Item):
    def __init__(self, item_name, damage,hit_points, defence,armor_points):
        super(Armor, self).__init__(item_name, damage, hit_points, defence)
        self.armor_points = armor_points

class Spell(Item):
    def __init__(self, item_name, damage, hit_points, defence, magic_points):
        super(Spell, self).__init__(item_name, damage, hit_points, defence)
        self.magic_points = magic_points

class Weapon(Item):
    def __init__(self, item_name, damage, hit_points, defence, attack_points):
        super(Weapon, self).__init__(item_name, damage, hit_points, defence)
        self.attack_points = attack_points

class Treasure():
    def __init__(self, name, value, description):
        self.name = name
        self.value = value
        self.description = description
        
