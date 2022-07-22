class Monster(object):
    def __init__(self, monster_class, hit_points, armor, magic, weapon, description):
        self.monster_class = monster_class
        self.hit_points = hit_points
        self.armor = armor
        self.magic = magic
        self.weapon = weapon
        self.description = description

    def attack(self, dice_roll):
        pass

    def defend(self, dice_roll):
        pass