class Player():
    #preset variables
    stance = "stand"   
    player_T = 0
    
    def __init__(self):
        pass
    
    def move_forward(self):
        pass
    
    def move_backwards(self):
        pass
    
    def turn_left(self):
        pass
    
    def turn_right(self):
        pass
    
    def change_stance(self, stance):
        if stance == "stand":
            stance = "squat"
        else:
            stance = "stand"
    
    def turn_left_and_squat(self):
        pass
    
    def turn_right_and_squat(self):
        pass
            
    def attack(self, target):
        pass
    
class Enemy():
    def __init__(self):
        pass
    
    def attack(self):
        pass
    
    def move(self):
        pass