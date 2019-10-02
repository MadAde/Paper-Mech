class Enemy():
    def __init__(
        self, type, weapon, weapon_range, position, mobile, health, colour, time_value, distance
    ):
        self.type = type
        self.weapon = weapon
        self.weapon_range = weapon_range
        self.position = position
        self.mobile = mobile
        self.health = health
        self.colour = colour
        self.time_value = time_value
        self.distance = distance

    def get_pos(self):
        return self.position

    def turn_left(self):

        if self.mobile is False:
            return self.position
        else:

            if self.position[1] == "0":
                new_position = self.position[0] + "1"
                return new_position
            elif self.position[1] == "1":
                new_position = self.position[0] + "2"
                return new_position
            elif self.position[1] == "2":
                new_position = self.position[0] + "3"
                return new_position
            elif self.position[1] == "3":
                new_position = self.position[0] + "4"
                return new_position
            elif self.position[1] == "4":
                new_position = self.position[0] + "5"
                return new_position
            elif self.position[1] == "5":
                new_position = self.position[0] + "6"
                return new_position
            elif self.position[1] == "6":
                new_position = self.position[0] + "7"
                return new_position
            elif self.position[1] == "7":
                new_position = self.position[0] + "1"
                return new_position

    def turn_right(self):

        if self.mobile is False:
            return self.position
        else:
            if self.position[1] == "0":
                new_position = self.position[0] + "7"
                return new_position
            elif self.position[1] == "1":
                new_position = self.position[0] + "0"
                return new_position
            elif self.position[1] == "2":
                new_position = self.position[0] + "1"
                return new_position
            elif self.position[1] == "3":
                new_position = self.position[0] + "2"
                return new_position
            elif self.position[1] == "4":
                new_position = self.position[0] + "3"
                return new_position
            elif self.position[1] == "5":
                new_position = self.position[0] + "4"
                return new_position
            elif self.position[1] == "6":
                new_position = self.position[0] + "5"
                return new_position
            elif self.position[1] == "7":
                new_position = self.position[0] + "6"
                return new_position

    def walk_forward(self):

        if self.mobile is False:
            return self.position
        else:
            if self.position == "A0":
                return ("A0")
            elif self.position == "A1":
                return ("A0")
            elif self.position == "A2":
                return ("A1")
            elif self.position == "A3":
                return ("B3")
            elif self.position == "A4":
                return ("B4")
            elif self.position == "A5":
                return ("A6")
            elif self.position == "A6":
                return ("A7")
            elif self.position == "A7":
                return ("A7")

            elif self.position == "B0":
                return ("A0")
            elif self.position == "B1":
                return ("B0")
            elif self.position == "B2":
                return ("B1")
            elif self.position == "B3":
                return ("C3")
            elif self.position == "B4":
                return ("C4")
            elif self.position == "B5":
                return ("B6")
            elif self.position == "B6":
                return ("B7")
            elif self.position == "B7":
                return ("A7")

            elif self.position == "C0":
                return ("B0")
            elif self.position == "C1":
                return ("C0")
            elif self.position == "C2":
                return ("C1")
            elif self.position == "C3":
                return ("D3")
            elif self.position == "C4":
                return ("D4")
            elif self.position == "C5":
                return ("C6")
            elif self.position == "C6":
                return ("C7")
            elif self.position == "C7":
                return ("B7")

            elif self.position == "D0":
                return ("C0")
            elif self.position == "D1":
                return ("D0")
            elif self.position == "D2":
                return ("D1")
            elif self.position == "D3":
                return ("D2")
            elif self.position == "D4":
                return ("D5")
            elif self.position == "D5":
                return ("D6")
            elif self.position == "D6":
                return ("D7")
            elif self.position == "D7":
                return ("C7")

    def walk_backwards(self):

        if self.mobile is False:
            return self.position
        else:
            if self.position == "A0":
                return ("B0")
            elif self.position == "A1":
                return ("A2")
            elif self.position == "A2":
                return ("A3")
            elif self.position == "A3":
                return ("A3")
            elif self.position == "A4":
                return ("A4")
            elif self.position == "A5":
                return ("A4")
            elif self.position == "A6":
                return ("A5")
            elif self.position == "A7":
                return ("B7")

            elif self.position == "B0":
                return ("C0")
            elif self.position == "B1":
                return ("B2")
            elif self.position == "B2":
                return ("B3")
            elif self.position == "B3":
                return ("A3")
            elif self.position == "B4":
                return ("A4")
            elif self.position == "B5":
                return ("B4")
            elif self.position == "B6":
                return ("B5")
            elif self.position == "B7":
                return ("C7")

            elif self.position == "C0":
                return ("D0")
            elif self.position == "C1":
                return ("C2")
            elif self.position == "C2":
                return ("C3")
            elif self.position == "C3":
                return ("B3")
            elif self.position == "C4":
                return ("B4")
            elif self.position == "C5":
                return ("C4")
            elif self.position == "C6":
                return ("C5")
            elif self.position == "C7":
                return ("D7")

            elif self.position == "D0":
                return ("D1")
            elif self.position == "D1":
                return ("D2")
            elif self.position == "D2":
                return ("D3")
            elif self.position == "D3":
                return ("C3")
            elif self.position == "D4":
                return ("C4")
            elif self.position == "D5":
                return ("D4")
            elif self.position == "D6":
                return ("D5")
            elif self.position == "D7":
                return ("D6")

    def advance(self):
        if self.mobile is False:
            return self.position
        else:
            if self.position[0] == "A":
                if self.weapon_range == 'Medium' or self.weapon_range == 'Short' or self.weapon_range == 'Close':
                    new_position = "B" + self.position[1]
                    self.distance = "Medium"
                    return new_position
                else:
                    return(self.position)
            elif self.position[0] == "B":
                if self.weapon_range == 'Short' or self.weapon_range == 'Close':
                    new_position = "C" + self.position[1]
                    self.distance = "Short"
                    return new_position
                else:
                    return(self.position)
            elif self.position[0] == "C":
                if self.weapon_range == 'Close':
                    new_position = "D" + self.position[1]
                    self.distance = "Close"
                    return new_position
                else:
                    return(self.position)
            elif self.position[0] == "D":
                new_position = "D" + self.position[1]
                self.distance = "Close"
                return new_position
