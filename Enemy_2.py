class Enemy():
    def __init__(
        self,
        enemy_type,
        enemy_health,
        weapon1,
        weapon_range1,
        weapon_power1,
        weapon_original_time_value1,
        weapon_time_value1,
        weapon_health1,
        weapon_status1,
        weapon2,
        weapon_range2,
        weapon_power2,
        weapon_original_time_value2,
        weapon_time_value2,
        weapon_health2,
        weapon_status2,
        weapon3,
        weapon_range3, 
        weapon_power3,
        weapon_original_time_value3,
        weapon_time_value3, 
        weapon_health3, 
        weapon_status3, 
        enemy_pos, 
        mobile, 
        enemy_colour, 
        enemy_distance,
        armour
    ):
        self.enemy_type = enemy_type
        self.health = enemy_health
        self.weapon1 = weapon1
        self.weapon_range1 = weapon_range1
        self.weapon_power1 = weapon_power1
        self.weapon_time_value1 = weapon_time_value1
        self.weapon_original_time_value1 = weapon_original_time_value1
        self.weapon_health1 = weapon_health1
        self.weapon_status1 = weapon_status1

        self.weapon2 = weapon2
        self.weapon_range2 = weapon_range2
        self.weapon_power2 = weapon_power2
        self.weapon_time_value2 = weapon_time_value2
        self.weapon_original_time_value2 = weapon_original_time_value2
        self.weapon_health2 = weapon_health2
        self.weapon_status2 = weapon_status2

        self.weapon3 = weapon3
        self.weapon_range3 = weapon_range3
        self.weapon_power3 = weapon_power3
        self.weapon_original_time_value3 = weapon_original_time_value3
        self.weapon_time_value3 = weapon_time_value3
        self.weapon_health3 = weapon_health3
        self.weapon_status3 = weapon_status3

        self.position = enemy_pos
        self.mobile = mobile
        self.colour = enemy_colour
        self.distance = enemy_distance
        self.armour = armour

        if weapon_status1 == 'Active':
            self.active_weapon = weapon1
            self.active_weapon_time_value = weapon_time_value1
            self.active_weapon_original_time_value = weapon_original_time_value1
            self.active_weapon_power = weapon_power1
            self.active_weapon_range = weapon_range1
            self.active_weapon_health = weapon_health1

        if weapon_status2 == 'Active':
            self.active_weapon = weapon2
            self.active_weapon_time_value = weapon_time_value2
            self.active_weapon_original_time_value = weapon_original_time_value2
            self.active_weapon_power = weapon_power2
            self.active_weapon_range = weapon_range2
            self.active_weapon_health = weapon_health2

        if weapon_status3 == 'Active':
            self.active_weapon = weapon3
            self.active_weapon_time_value = weapon_time_value3
            self.active_weapon_original_time_value = weapon_original_time_value3
            self.active_weapon_power = weapon_power3
            self.active_weapon_range = weapon_range3
            self.active_weapon_health = weapon_health3
        

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

    def update_distance(self):
        if self.position[0] == A:
            return("Long")
        if self.position[0] == B:
            return("Medium")
        if self.position[0] == C:
            return("Short")
        if self.position[0] == D:
            return("Close")


    def walk_forward(self):

        if self.mobile is False:
            return self.position
        else:
            if self.position == "A0":
                self.distance = "Long"
                return ("A0")
            elif self.position == "A1":
                self.distance = "Long"
                return ("A0")
            elif self.position == "A2":
                self.distance = "Long"
                return ("A1")
            elif self.position == "A3":
                self.distance = "Medium"
                return ("B3")
            elif self.position == "A4":
                self.distance = "Medium"
                return ("B4")
            elif self.position == "A5":
                self.distance = "Long"
                return ("A6")
            elif self.position == "A6":
                self.distance = "Long"
                return ("A7")
            elif self.position == "A7":
                self.distance = "Long"
                return ("A7")

            elif self.position == "B0":
                self.distance = "Long"
                return ("A0")
            elif self.position == "B1":
                self.distance = "Medium"
                return ("B0")
            elif self.position == "B2":
                self.distance = "Medium"
                return ("B1")
            elif self.position == "B3":
                self.distance = "Short"
                return ("C3")
            elif self.position == "B4":
                self.distance = "Short"
                return ("C4")
            elif self.position == "B5":
                self.distance = "Medium"
                return ("B6")
            elif self.position == "B6":
                self.distance = "Medium"
                return ("B7")
            elif self.position == "B7":
                self.distance = "Long"
                return ("A7")

            elif self.position == "C0":
                self.distance = "Medium"
                return ("B0")
            elif self.position == "C1":
                self.distance = "Short"
                return ("C0")
            elif self.position == "C2":
                self.distance = "Short"
                return ("C1")
            elif self.position == "C3":
                self.distance = "Close"
                return ("D3")
            elif self.position == "C4":
                self.distance = "Close"
                return ("D4")
            elif self.position == "C5":
                self.distance = "Short"
                return ("C6")
            elif self.position == "C6":
                self.distance = "Short"
                return ("C7")
            elif self.position == "C7":
                self.distance = "Medium"
                return ("B7")

            elif self.position == "D0":
                self.distance = "Short"
                return ("C0")
            elif self.position == "D1":
                self.distance = "Close"
                return ("D0")
            elif self.position == "D2":
                self.distance = "Close"
                return ("D1")
            elif self.position == "D3":
                self.distance = "Close"
                return ("D2")
            elif self.position == "D4":
                self.distance = "Close"
                return ("D5")
            elif self.position == "D5":
                self.distance = "Close"
                return ("D6")
            elif self.position == "D6":
                self.distance = "Close"
                return ("D7")
            elif self.position == "D7":
                self.distance = "Short"
                return ("C7")

    def walk_backwards(self):

        if self.mobile is False:
            return self.position
        else:
            if self.position == "A0":
                self.distance = "Medium"
                return ("B0")
            elif self.position == "A1":
                self.distance = "Long"
                return ("A2")
            elif self.position == "A2":
                self.distance = "Long"
                return ("A3")
            elif self.position == "A3":
                self.distance = "Long"
                return ("A3")
            elif self.position == "A4":
                self.distance = "Long"
                return ("A4")
            elif self.position == "A5":
                self.distance = "Long"
                return ("A4")
            elif self.position == "A6":
                self.distance = "Long"
                return ("A5")
            elif self.position == "A7":
                self.distance = "Medium"
                return ("B7")

            elif self.position == "B0":
                self.distance = "Short"
                return ("C0")
            elif self.position == "B1":
                self.distance = "Medium"
                return ("B2")
            elif self.position == "B2":
                self.distance = "Medium"
                return ("B3")
            elif self.position == "B3":
                self.distance = "Long"
                return ("A3")
            elif self.position == "B4":
                self.distance = "Long"
                return ("A4")
            elif self.position == "B5":
                self.distance = "Medium"
                return ("B4")
            elif self.position == "B6":
                self.distance = "Medium"
                return ("B5")
            elif self.position == "B7":
                self.distance = "Short"
                return ("C7")

            elif self.position == "C0":
                self.distance = "Close"
                return ("D0")
            elif self.position == "C1":
                self.distance = "Short"
                return ("C2")
            elif self.position == "C2":
                self.distance = "Short"
                return ("C3")
            elif self.position == "C3":
                self.distance = "Medium"
                return ("B3")
            elif self.position == "C4":
                self.distance = "Medium"
                return ("B4")
            elif self.position == "C5":
                self.distance = "Short"
                return ("C4")
            elif self.position == "C6":
                self.distance = "Short"
                return ("C5")
            elif self.position == "C7":
                self.distance = "Close"
                return ("D7")

            elif self.position == "D0":
                self.distance = "Close"
                return ("D1")
            elif self.position == "D1":
                self.distance = "Close"
                return ("D2")
            elif self.position == "D2":
                self.distance = "Close"
                return ("D3")
            elif self.position == "D3":
                self.distance = "Short"
                return ("C3")
            elif self.position == "D4":
                self.distance = "Short"
                return ("C4")
            elif self.position == "D5":
                self.distance = "Close"
                return ("D4")
            elif self.position == "D6":
                self.distance = "Close"
                return ("D5")
            elif self.position == "D7":
                self.distance = "Close"
                return ("D6")

    def advance(self):
        if self.mobile is False:
            return self.position
        else:
            if self.position[0] == "A":
                if self.active_weapon_range == 'Medium' or self.active_weapon_range == 'Short' or self.active_weapon_range == 'Close':
                    new_position = "B" + self.position[1]
                    self.distance = "Medium"
                    return new_position
                else:
                    return(self.position)
            elif self.position[0] == "B":
                if self.active_weapon_range == 'Short' or self.active_weapon_range == 'Close':
                    new_position = "C" + self.position[1]
                    self.distance = "Short"
                    return new_position
                else:
                    return(self.position)
            elif self.position[0] == "C":
                if self.active_weapon_range == 'Close':
                    new_position = "D" + self.position[1]
                    self.distance = "Close"
                    return new_position
                else:
                    return(self.position)
            elif self.position[0] == "D":
                new_position = "D" + self.position[1]
                self.distance = "Close"
                return new_position
