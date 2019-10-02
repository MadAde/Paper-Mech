class Weapon():
    def __init__(
        self,
        location, 
        name,
        power, 
        time,
        health,
        armour,
        range,
        coords,):

        self.location = location
        self.name = name
        self.power = power
        self.time = time
        self.health = health
        self.armour = armour
        self.range = range
        self.coords = coords


class Movement():
    def __init__(
        self,
        name,
        time,
        health,
        coords,):

        self.name = name
        self.time = time
        self.health = health
        self.coords = coords
