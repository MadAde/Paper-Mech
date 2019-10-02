# Import

import os
import random
import sys

import pygame
import pygame.event as GAME_EVENTS
import pygame.locals as GAME_GLOBALS
import pygame.time as GAME_TIME
import pygame.freetype

import math

from prettytable import PrettyTable

import Enemy_2
import Weapons

windowWidth = 1676
windowHeight = 882

radar_ref_x = 50
radar_ref_y = 54

radar_centre_x = 338
radar_centre_y = 342

radar_radius = 287

radar_long = int(radar_radius * 7 / 8)
radar_medium = int(radar_radius * 5 / 8)
radar_short = int(radar_radius * 3 / 8)
radar_close = int(radar_radius * 1 / 8)

Player = {"stance": "stand", "health": 4, "player_t": 0}

pygame.init()

MSG_X = 750
MSG_Y = 550
MSG_WIDTH = 800
MSG_HEIGHT = 40

game_msgs = []
active_action = ""

DISPLAY_TEXT_X = 400
DISPLAY_TEXT_Y = 400

myfont = pygame.freetype.SysFont('Lucida Console', 15)

WAVE_1 = (338, 740, 73, 130)
WAVE_2 = (410, 740, 73, 130)
WAVE_3 = (482, 740, 73, 130)
WAVE_4 = (554, 740, 73, 130)

STAND = (1085, 24, 40, 40)
SQUAT = (1251, 24, 40, 40)

weapon_1 = Weapons.Weapon(
    'Shoulder Mount Left',
    'Defend',
    0,
    1,
    2,
    4,
    "Long",
    (728, 69, 34, 34),
)

weapon_2 = Weapons.Weapon(
    'Shoulder Mount Left',
    'Defend',
    0,
    1,
    2,
    4,
    "Long",
    (728, 118, 34, 34)
)

weapon_3 = Weapons.Weapon(
    'Shoulder Mount Left',
    'Defend',
    0,
    1,
    2,
    4,
    "Long",
    (728, 166, 34, 34)
)

weapon_4 = Weapons.Weapon(
    'Shoulder Mount Right',
    'Single Launch',
    2,
    2,
    2,
    3,
    "Long",
    (1369, 74, 34, 34),
)

weapon_5 = Weapons.Weapon(
    'Shoulder Mount Right',
    'Multi Launch',
    4,
    3,
    2,
    3,
    "Long",
    (1369, 122, 34, 34)
)

weapon_6 = Weapons.Weapon(
    'Shoulder Mount Right',
    'Full Salvo',
    6,
    4,
    2,
    3,
    "Long",
    (1369, 170, 34, 34)
)
weapon_7 = Weapons.Weapon(
    'Arm Mount Left',
    'Quick Beam',
    2,
    2,
    2,
    3,
    "Medium",
    (728, 304, 34, 34),
)

weapon_8 = Weapons.Weapon(
    'Arm Mount Left',
    'Laser Blast',
    3,
    3,
    2,
    3,
    "Medium",
    (728, 352, 34, 34)
)

weapon_9 = Weapons.Weapon(
    'Arm Mount Left',
    'Full Charge',
    4,
    4,
    2,
    3,
    "Medium",
    (728, 400, 34, 34)
)

weapon_10 = Weapons.Weapon(
    'Arm Mount Right',
    'Punch',
    3,
    2,
    2,
    3,
    "Close",
    (1368, 307, 34, 34),
)

weapon_11 = Weapons.Weapon(
    'Arm Mount Right',
    'Uppercut',
    5,
    3,
    2,
    3,
    "Close",
    (1368, 355, 34, 34)
)

weapon_12 = Weapons.Weapon(
    'Arm Mount Right',
    'Crush',
    1,
    3,
    2,
    3,
    "Close",
    (1368, 403, 34, 34)
)

movement_option_1 = Weapons.Movement(
    'Turn and Squat',
    1,
    1,
    (1057, 334, 32, 32)
)

movement_option_2 = Weapons.Movement(
    'Walk Backwards',
    1,
    1,
    (1057, 379, 32, 32)
)

movement_option_3 = Weapons.Movement(
    'Walk Forwards',
    1,
    1,
    (1057, 423, 32, 32)
)

movement_option_4 = Weapons.Movement(
    'Turn or Change Stance',
    1,
    1,
    (1057, 465, 32, 32)
)

list_of_weapons = [weapon_1, weapon_2, weapon_3, weapon_4, weapon_5, weapon_6, weapon_7, weapon_8, weapon_9, weapon_10, weapon_11, weapon_12, movement_option_1, movement_option_2, movement_option_3, movement_option_4]

TORSO = (1082, 88, 1291-1083, 216-88)

TIME_VALUE_0 = (49, 655, 73, 66)
TIME_VALUE_1 = (122, 655, 73, 66)
TIME_VALUE_2 = (195, 655, 73, 66)
TIME_VALUE_3 = (268, 655, 73, 66)
TIME_VALUE_4 = (341, 655, 73, 66)
TIME_VALUE_5 = (414, 655, 73, 66)
TIME_VALUE_6 = (487, 655, 73, 66)
TIME_VALUE_7 = (560, 655, 73, 66)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (245, 138, 66)
GREY = (78, 97, 82)
PURPLE = (188, 14, 227)
BLACK =  (0,0,0)



if pygame.mixer and not pygame.mixer.get_init():
    print("Warning - no sound")
    pygame.mixer = None
pygame.font.init()
# clock = pygame.time.Clock()
surface = pygame.display.set_mode((windowWidth, windowHeight)) #, pygame.FULLSCREEN)

pygame.display.set_caption("Paper Mech")
# icon = pygame.transform.scale(Alien.images[0], (32, 32))
# pygame.display.set_icon(icon)
textFont = pygame.font.SysFont("monospace", 50)

gameStarted = False
gameStartTime = 0
gameFinishTime = 0
gameOver = False

enemy_list = ["bike", "artillary", "helo", "firethrower", "tank", "mech"]

active_enemy_list = []
selected_enemy = ""

background = pygame.image.load("assets/pmbg3.png")

# see if we can load more than standard BMP
if not pygame.image.get_extended():
    raise SystemExit("Sorry, extended image module required")

# Variables

wave = 1

def quitGame():
    pygame.quit()
    sys.exit()

def message(new_msg, color = RED):
    t = [new_msg, color]
    game_msgs.append(t)
    if len(game_msgs) > 12:
        del game_msgs[0]


def generate_enemy(enemy_type):
    #global number_of_enemies
    roll_1 = random.randint(1, 6)  # enemy type not required
    
    if enemy_type == "random":

        if roll_1 == 1:
            enemy_type = "Bike"
        elif roll_1 == 2:
            enemy_type = "Artillary"
        elif roll_1 == 3:
            enemy_type = "Helo"
        elif roll_1 == 4:
            enemy_type = "Firethrower"
        elif roll_1 == 5:
            enemy_type = "Tank"
        elif roll_1 == 6:
            enemy_type = "Mech"

    # roll_1 = random.randint(1, 6)  # enemy type not required except for testing
    roll_2 = random.randint(1, 6)  # enemy weapon
    roll_3 = random.randint(1, 6)  # enemy position

    # roll = [str(roll_1), str(roll_2), str(roll_3)]

    # print(":".join(roll))

    # roll 1 is already sorted in Generate Wave...

    if enemy_type == 'Bike':

        weapon1 = "Machine Gun"
        weapon_range1 = "Short"
        weapon_power1 = 1
        weapon_original_time_value1 = 1
        weapon_time_value1 = 1
        weapon_health1 = 2
        weapon_status1 = 'Active'

        weapon2 = 'none'
        weapon_range2 = 0
        weapon_power2 = 0
        weapon_original_time_value2 = 0
        weapon_time_value2 = 0
        weapon_health2 = 0
        weapon_status2 = 'Disabled'

        weapon3 = 'none'
        weapon_range3 = 0
        weapon_power3 = 0
        weapon_original_time_value3 = 0
        weapon_time_value3 = 0
        weapon_health3 = 0
        weapon_status3 = 'Disabled'

        enemy_health = 2
        enemy_colour = 'RED'
        armour = 2

    elif enemy_type == "Artillary":
        weapon1 = "Mortar"
        weapon_range1 = "Long"
        weapon_power1 = 5
        weapon_original_time_value1 = 5
        weapon_time_value1 = 5
        weapon_health1 = 3
        weapon_status1 = 'Active'

        weapon2 = 'none'
        weapon_range2 = 0
        weapon_power2 = 0
        weapon_original_time_value2 = 0
        weapon_time_value2 = 0
        weapon_health2 = 0
        weapon_status2 = 'Disabled'

        weapon3 = 'none'
        weapon_range3 = 0
        weapon_power3 = 0
        weapon_original_time_value3 = 0
        weapon_time_value3 = 0
        weapon_health3 = 0
        weapon_status3 = 'Disabled'

        enemy_health = 3
        enemy_colour = 'GREEN'
        armour = 3

    elif enemy_type == "Helo":

        weapon1 = "Machine Gun"
        weapon_range1 = "Short"
        weapon_power1 = 2
        weapon_original_time_value1 = 2
        weapon_time_value1 = 2
        weapon_health1 = 2
        weapon_status1 = 'Dsiabled'

        weapon2 = "Missiles"
        weapon_range2 = "Medium"
        weapon_power2 = 4
        weapon_original_time_value2 = 4
        weapon_time_value2 = 4
        weapon_health2 = 2
        weapon_status2 = 'Disabled'

        weapon3 = 'none'
        weapon_range3 = 0
        weapon_power3 = 0
        weapon_original_time_value3 = 0
        weapon_time_value3 = 0
        weapon_health3 = 0
        weapon_status3 = 'Disabled'

        enemy_health = 4
        armour = 2
        enemy_colour = 'BLUE'

    elif enemy_type == "Firethrower":
        weapon1 = "Laser"
        weapon_range1 = "Medium"
        weapon_power1 = 3
        weapon_original_time_value1 = 3 
        weapon_time_value1 = 3
        weapon_health1 = 2
        weapon_status1 = 'Disabled'

        weapon2 = "Flame Gun"
        weapon_range2 = "Short"
        weapon_power2 = 4
        weapon_original_time_value2 = 2
        weapon_time_value2 = 2
        weapon_health2 = 2
        weapon_status2 = 'Disabled'

        weapon3 = 'none'
        weapon_range3 = 0
        weapon_power3 = 0
        weapon_original_time_value3 = 0
        weapon_time_value3 = 0
        weapon_health3 = 0
        weapon_status3 = 'Disabled'

        enemy_health = 4
        armour = 3
        enemy_colour = 'ORANGE'


    elif enemy_type == "Tank":
        
        weapon1 = "Laser"
        weapon_range1 = "Medium"
        weapon_power1 = 3
        weapon_original_time_value1 = 3 
        weapon_time_value1 = 3
        weapon_health1 = 3
        weapon_status1 = 'Disabled'

        weapon2 = "PPC"
        weapon_range2 = "Long"
        weapon_power2 = 4
        weapon_original_time_value2 = 4
        weapon_time_value2 = 4
        weapon_health2 = 2
        weapon_status2 = 'Disabled'

        weapon3 = 'none'
        weapon_range3 = 0
        weapon_power3 = 0
        weapon_original_time_value3 = 0
        weapon_time_value3 = 0
        weapon_health3 = 0
        weapon_status3 = 'Disabled'

        enemy_health = 5
        armour = 3
        enemy_colour = 'GREY'
        
    elif enemy_type == "Mech":

        weapon1 = "Fist"
        weapon_range1 = "Close"
        weapon_power1 = 5
        weapon_original_time_value1 = 2 
        weapon_time_value1 = 2
        weapon_health1 = 2
        weapon_status1 = 'Disabled'

        weapon2 = "Laser"
        weapon_range2 = "Medium"
        weapon_power2 = 3
        weapon_original_time_value2 = 3
        weapon_time_value2 = 3
        weapon_health2 = 3
        weapon_status2 = 'Disabled'

        weapon3 = "Missiles"
        weapon_range3 = "Long"
        weapon_original_time_value3 = 4
        weapon_time_value3 = 4
        weapon_health3 = 2
        weapon_status3 = 'Disabled'

        enemy_health = 7
        armour = 4
        enemy_colour = 'PURPLE'

    # roll 2

    if enemy_type == "Helo" and roll_2 < 4:
        weapon_status1 = 'Active'
    else:
        if enemy_type == "Helo":
            weapon_status2 = 'Active'

    if enemy_type == "Firethrower" and roll_2 < 4:
        weapon_status1 = 'Active'
    else:
        if enemy_type == "Firethrower":
            weapon_status2 = 'Active'

    if enemy_type == "Tank" and roll_2 < 4:
        weapon_status1 = 'Active'
    else:
        if enemy_type == "Tank":
            weapon_status2 = 'Active'

    if enemy_type == "Mech" and roll_2 < 3:
        weapon_status1 = 'Active'
        if enemy_type == "Mech" and roll_2 > 4:
            weapon_status3 = 'Active'
        else:
            if enemy_type == "Mech":
                weapon_status2 = 'Active'

    # roll 3

    if roll_3 == 1:
        enemy_pos = "A1"
    elif roll_3 == 2:
        enemy_pos = "A2"
    elif roll_3 == 3:
        enemy_pos = "A3"
    elif roll_3 == 4:
        enemy_pos = "A4"
    elif roll_3 == 5:
        enemy_pos = "A5"
    elif roll_3 == 6:
        enemy_pos = "A6"

    if enemy_type == "artillary":
        mobile = False
    else:
        mobile = True

    enemy_distance = "Long"

    enemy = Enemy_2.Enemy(
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
        armour,
    )

    active_enemy_list.append(enemy)

    if weapon_status1 == 'Active':
        ew = weapon1
    elif weapon_status2 == 'Active':
        ew = weapon2
    elif weapon_status3 == 'Active':
        ew = weapon3

    message("Enemy Generated: " + enemy_type + " : " + ew, RED)

    pygame.display.update()


def print_enemy_list_parameters():

    t = PrettyTable(
        [
            "Type",
            "Weapon",
            "Weapon Range",
            "Position",
            "Mobile?",
            "Health",
            "Colour",
            "Time_value",
            "Distance",
        ]
    )
    for e in active_enemy_list:
        t.add_row(
            [
                e.enemy_type,
                e.active_weapon,
                e.active_weapon_range,
                e.position,
                e.mobile,
                e.health,
                e.colour,
                e.active_weapon_time_value,
                e.distance,
            ]
        )

    print(t)


def draw_wave_box():
    if wave == 1:
        pygame.draw.rect(surface, RED, (WAVE_1), 2)
    if wave == 2:
        pygame.draw.rect(surface, RED, (WAVE_2), 2)
    if wave == 3:
        pygame.draw.rect(surface, RED, (WAVE_3), 2)
    if wave == 4:
        pygame.draw.rect(surface, RED, (WAVE_4), 2)


def change_stance():
    if Player["stance"] == "stand":
        Player["stance"] = "squat"
        message("Stance is now 'Squat'", BLACK)
    elif Player["stance"] == "squat":
        Player["stance"] = "stand"
        message("Stance is now 'Stand'", BLACK)


def draw_stance():
    if Player["stance"] == "stand":
        pygame.draw.rect(surface, RED, (STAND), 2)
    else:
        pygame.draw.rect(surface, RED, (SQUAT), 2)

def enemy_attack(e):
    roll_A = random.randint(1,6)
    # if enemy attack is either front or back:
    front = [3,4,0,7]
    left = [1,2]
    right = [5,6]
    back = [0,7]

    if e.position[1] in front:
        side = "Front"
        if roll_A == 1:
            Target = "Torso"
        elif roll_A == 2: 
            Target = "Left Shoulder Mount"
        elif roll_A == 3: 
            Target = "Right Shoulder Mount"
        elif roll_A == 4: 
            Target = "Left Arm Mount"
        elif roll_A == 5: 
            Target = "Right Arm Mount"
        elif roll_A == 6: 
            Target = "Legs"

    # if enemy attack is from the side:
    elif e.position[1] in left:
        side = "Left"
        if roll_A == 1: Target = "Left Shoulder Mount"
        elif roll_A == 2: Target = "Left Shoulder Mount"
        elif roll_A == 3: Target = "Left Arm Mount"
        elif roll_A == 4: Target = "Left Arm Mount"
        elif roll_A == 5: Target = "Left Arm Mount"
        elif roll_A == 6: Target = "Legs"

    else:
        side = "Right"
        if roll_A == 1: Target = "Right Shoulder Mount"
        elif roll_A == 2: Target = "Right Shoulder Mount"
        elif roll_A == 3: Target = "Right Arm Mount"
        elif roll_A == 4: Target = "Right Arm Mount"
        elif roll_A == 5: Target = "Right Arm Mount"
        elif roll_A == 6: Target = "Legs"

    message("Roll A = " + str(roll_A), BLACK)
    message("Enemy is to the " + side, BLACK)
    message("Enemy has targeted the " + Target, BLACK)

    # Calculate damage
    roll_B = []
    for pow in range(e.active_weapon_power):
        roll = random.randint(1,6)
        roll_B.append(roll)
        # check damage decreasing armour by 1 if to the rear

    message(str(roll_B), RED)
    e.active_weapon_time_value = e.active_weapon_original_time_value

def check_enemy_active(e):
    message(e.enemy_type + " Active!", BLUE)
    if e.distance == e.active_weapon_range:
        #enemy_attack(enemy)
        message("Enemy in range - Action: attack!", RED)
        enemy_attack(e)

    else:
        message("Enemy out of range - Action: Move", RED)
        e.position = e.advance()
        e.active_weapon_time_value = e.active_weapon_original_time_value # is this correct??
        # enemy_move(enemy)

def destroy_enemy(en):
    global wave
    message("Enemy Destroyed", RED)
    active_enemy_list.remove(en)
    selected_enemy = ""
    active_action = "" 
    if len(active_enemy_list) < 1:
        message("All enemies destroyed!", BLACK)
        message("Make repaires", BLACK)
        if wave < 4:
            message("Get ready for next wave...")
            wave += 1
        else:
            message("All waves complete - the Enemy is defeated!", BLACK)

        




def mech_attack(active_action, selected_enemy):
    if active_action.range == "Medium" and selected_enemy.distance == "Long":
        message("Enemy out of range")
        return
    elif active_action.range == "Short" and (selected_enemy.distance == "Medium" or selected_enemy.distance == "Long"):
        message("Enemy out of range")
        return

    elif active_action.range == "Close" and selected_enemy.distance != "Close":
        message("Enemy out of range")
        return
    ### Check Firing Arc ###
    else:
        message("Mech Weapon Attack!", RED)
        message("Power: " + str(active_action.power) + ". " + "Enemy Armour: " + str(selected_enemy.armour), RED)
        roll = []
        
        for r in range(int(active_action.power)):
            roll.append(random.randint(1,6))
        message(str(roll), ORANGE)
        for i in roll:
            if i > selected_enemy.armour:
                message("Mech hit Enemy!", RED)
                selected_enemy.health -= 1
                if selected_enemy.health < 1:
                    destroy_enemy(selected_enemy)
            else:
                message("Miss!", ORANGE)
                message("Select Next Action", RED)


def check_player_active():
    message("Mech Active!", RED)
    message("Choose to Move or Attack")
    if selected_enemy == "":
        message("Select Enemy Target")
    if active_action == "":
        message("Choose Action")
    if selected_enemy != "" and active_action != "":
        mech_attack(active_action, selected_enemy)


def generate_wave():
    message("Generate Wave " + str(wave), RED)
    if wave == 1:
        a = random.randint(1,6)
        if a == 1 or a == 2:
            generate_enemy('Bike')
        elif a == 3 or a == 4:
            generate_enemy('Helo')
        elif a == 5 or a == 6:
            generate_enemy('Firethrower') 
    elif w == 2:
        pass
    elif w == 3:
        pass
    elif w == 4:
        pass


def advance_time():
    message("Time advanced", ORANGE)
    if len(active_enemy_list) > 0:
        for enemy in active_enemy_list:
            if enemy.active_weapon_time_value > 0:
                enemy.active_weapon_time_value -= 1
                if enemy.active_weapon_time_value == 0:
                    check_enemy_active(enemy)

    if Player["player_t"] > 0:
        Player["player_t"] -= 1
        if Player["player_t"] == 0:
            check_player_active()

def calculate_coords(enemy_position):
    if enemy_position[0] == "A":
            dist = radar_long
    elif enemy_position[0] == "B":
        dist = radar_medium
    elif enemy_position[0] == "C":
        dist = radar_short
    elif enemy_position[0] == "D":
        dist = radar_close

    if enemy_position[1] == "6":
        angle = ((360 * 0 / 8) + 22.5) * math.pi / 180
    elif enemy_position[1] == "7":
        angle = ((360 * 1 / 8) + 22.5) * math.pi / 180
    elif enemy_position[1] == "0":
        angle = ((360 * 2 / 8) + 22.5) * math.pi / 180
    elif enemy_position[1] == "1":
        angle = ((360 * 3 / 8) + 22.5) * math.pi / 180
    elif enemy_position[1] == "2":
        angle = ((360 * 4 / 8) + 22.5) * math.pi / 180
    elif enemy_position[1] == "3":
        angle = ((360 * 5 / 8) + 22.5) * math.pi / 180
    elif enemy_position[1] == "4":
        angle = ((360 * 6 / 8) + 22.5) * math.pi / 180
    elif enemy_position[1] == "5":
        angle = ((360 * 7 / 8) + 22.5) * math.pi / 180

    pos_x, pos_y = pygame.math.Vector2(dist, angle) # is this line needed?
    pos_x, pos_y = (
        radar_centre_x + dist * math.cos(angle),
        radar_centre_y + dist * math.sin(angle),
    )
    return pos_x, pos_y


def draw_enemy_positions():
    if len(active_enemy_list) > 0:
        for e in active_enemy_list:
            # pos_x, pos_y = e.get_pos()
            enemy_position = e.position
            pos_x, pos_y = calculate_coords(enemy_position)

            enemy_colour = e.colour

            if e.colour == 'RED':
                enemy_colour = (255, 0, 0)
            elif e.colour == 'GREEN':
                enemy_colour = (0, 255, 0)
            elif e.colour == 'BLUE':
                enemy_colour = (0, 0, 255)
            elif e.colour == 'ORANGE':
                enemy_colour = (245, 138, 66)
            elif e.colour == 'GREY':
                enemy_colour = (78, 97, 82)
            elif e.colour == 'PURPLE':
                enemy_colour = (188, 14, 227)

            time_value = e.active_weapon_time_value

            if time_value == 0:
                time_value_pos = TIME_VALUE_0
            elif time_value == 1:
                time_value_pos = TIME_VALUE_1
            elif time_value == 2:
                time_value_pos = TIME_VALUE_2
            elif time_value == 3:
                time_value_pos = TIME_VALUE_3
            elif time_value == 4:
                time_value_pos = TIME_VALUE_4
            elif time_value == 5:
                time_value_pos = TIME_VALUE_5
            elif time_value == 6:
                time_value_pos = TIME_VALUE_6
            elif time_value == 7:
                time_value_pos = TIME_VALUE_7
            # draw_radar
            pygame.draw.circle(
                surface,
                enemy_colour,
                (int(pos_x), int(pos_y)),
                10,
                3,
            )
            # draw_time_value
            pygame.draw.rect(surface, enemy_colour, (time_value_pos), 2)

def draw_player_time():
    time_value = Player["player_t"]

    if time_value == 0:
        time_value_pos = TIME_VALUE_0
    elif time_value == 1:
        time_value_pos = TIME_VALUE_1
    elif time_value == 2:
        time_value_pos = TIME_VALUE_2
    elif time_value == 3:
        time_value_pos = TIME_VALUE_3
    elif time_value == 4:
        time_value_pos = TIME_VALUE_4
    elif time_value == 5:
        time_value_pos = TIME_VALUE_5
    elif time_value == 6:
        time_value_pos = TIME_VALUE_6
    elif time_value == 7:
        time_value_pos = TIME_VALUE_7
        
    # draw_time_value
    pygame.draw.rect(surface, RED, (time_value_pos), 4)

# def main():

#Set up
message("Mech Active", BLACK)
message("Stance: Standing", BLACK)
message("Selected Action: None", BLACK)
generate_wave()

while True:

    #global wave
    pygame.event.get()  # used to stop not responding - may be deleted later...?

    if gameStarted is True and gameOver is False:
        print("OK")

    surface.blit(background, (0, 0))

    # Setting Up 1: Choose Starting Equipment

    # Setting Up 2: Place Player Active Space, Stand Space, Torso Box - done 
    #message("Setting Up....", BLUE)
    
    draw_player_time()
    
    draw_stance()
    
    if active_action == "":
        
        pygame.draw.rect(surface, RED, (TORSO), 2)

    # Setting Up 3: Generate First Wave of enemies and place cubes...

    

    # Setting up 4: Choose first action and place time cube..

    draw_wave_box()
    draw_enemy_positions()




    # find radar reference point
    # pygame.draw.circle(surface, RED, (50,54), 10, 1)
    # find f1
    # pygame.draw.circle(surface, BLUE, (radar_ref_x + 522 ,radar_ref_y + 382), 10, 1)

    # find radar centre
    #pygame.draw.circle(surface, GREEN, (radar_centre_x, radar_centre_y), 5, 1)
    # check
    # pygame.draw.circle(surface, GREEN, (radar_centre_x, radar_centre_y - radar_close), 5, 1)

    mouse_x, mouse_y = pygame.mouse.get_pos()
    # Display mouse to ease fixing boxes
    # myfont.render_to(surface, (40, 350), (str(mouse_x)), GREEN)
    # myfont.render_to(surface, (40, 400), (str(mouse_y)), GREEN)

    # find Mech Weapon Positions
    def weapon_select_check(box_check):
        global active_action
        box = box_check.coords
        if mouse_x > box[0] and mouse_x < (box[0] + box[2]):
            if mouse_y > box[1] and mouse_y < (box[1] + box[3]):
                pygame.draw.rect(surface, RED, (box), 2)
                
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONUP:
                        message("Enemy Targeted: " + box_check.name + ", Range: " + box_check.range, BLACK)
                        active_action = box_check
                        Player["player_t"] = box_check.time  # is this correct?

    #weapon_select_check(SHOULDER_MOUNT_LEFT_1)
    for w in list_of_weapons:
        #mouse_select_check(w.coords)
        weapon_select_check(w)

    def enemy_select_check(enemy_box):
        global selected_enemy
        pos = enemy_box.position
        box = calculate_coords(pos)
        info1 = enemy_box.enemy_type
        info2 = enemy_box.active_weapon
        info3 = "Range: "+ enemy_box.active_weapon_range 
        info4 = "Health: " + str(enemy_box.health)
        #print(box[0])
        if mouse_x > box[0] - 20 and mouse_x < box[0] + 20:
            if mouse_y > box[1] - 20 and mouse_y < box[1] + 20:
                pygame.draw.rect(surface, BLACK, (box[0] - 20, box[1] - 20, 40, 40), 2)
                myfont.render_to(surface, (box[0] + 30, box[1] -45 + 0), info1, BLACK)
                myfont.render_to(surface, (box[0] + 30, box[1] -45 + 15), info2, BLACK)
                myfont.render_to(surface, (box[0] + 30, box[1] -45 + 30), info3, BLACK)
                myfont.render_to(surface, (box[0] + 30, box[1] -45 + 45), info4, BLACK)

                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONUP:
                        message("Selected: " + enemy_box.enemy_type, BLACK)
                        selected_enemy = enemy_box
                        # Player["player_t"] = box_check.time # is this needed?


    for es in active_enemy_list:
        enemy_select_check(es)




    # Message Block
    i = 0
    for i, (line, color) in enumerate(game_msgs):
        myfont.render_to(surface, (MSG_X, MSG_Y + (i*15)), line, color)

    # Set display mode

    # Load images

    # create the background

    ### KEYS

    for event in GAME_EVENTS.get():
        #        if event.type == pygame.KEYDOWN:
        #            deltax, deltay = delta.get(event.key, (0, 0))
        #            speed[0] += deltax
        #            speed[1] += deltay
        #
        if event.type == pygame.key.get_pressed():
            if keys[pygame.K_UP]:
                pass  # y1 -= 1
        #            if keys[pygame.K_DOWN]:
        #                pass#y1 += 1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            #            if event.key == pygame.K_b:
            #                generate_enemy('Bike')
            #            if event.key == pygame.K_a:
            #                generate_enemy('Artillery')
            #            if event.key == pygame.K_h:
            #                generate_enemy('Helo')
            #            if event.key == pygame.K_f:
            #                generate_enemy('Firethrower')
            #            if event.key == pygame.K_t:
            #                generate_enemy('Tank')
            #            if event.key == pygame.K_m:
            #                generate_enemy('Mech')
            if event.key == pygame.K_r:
                generate_enemy("random")
                #message("Random Enemy Generated", RED)

            if event.key == pygame.K_s:
                change_stance()
                message("Mech CHANGED STANCE", BLACK)

            if event.key == pygame.K_SPACE:
                advance_time()

            if event.key == pygame.K_e:
                print_enemy_list_parameters()

            if event.key == pygame.K_LEFTBRACKET:
                wave -= 1
                print(wave)

            if event.key == pygame.K_RIGHTBRACKET:
                wave += 1
                print(wave)

            if event.key == pygame.K_LEFT:
                #print("Mech turned LEFT")
                message("Mech turned LEFT", BLACK)
                for e in active_enemy_list:
                    e.position = e.turn_left()

            if event.key == pygame.K_RIGHT:
                #print("Mech turned RIGHT")
                message("Mech turned RIGHT", BLACK)
                for e in active_enemy_list:
                    e.position = e.turn_right()

            if event.key == pygame.K_UP:
                #print("Mech WALK FORWARD")
                message("Mech WALK FORWARD", BLACK)
                for e in active_enemy_list:
                    e.position = e.walk_forward()

            if event.key == pygame.K_DOWN:
                #print("Mech WALK BACKWARDS")
                message("Mech WALK BACKWARDS", BLACK)
                for e in active_enemy_list:
                    e.position = e.walk_backwards()

            if event.key == pygame.K_a:
                #print("Enemies Advance")
                message("Enemies ADVANCE", RED)
                for e in active_enemy_list:
                    e.position = e.advance()

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def choose_starting_equipment():
        pass

    def generate_wave():
        if wave == 0:
            pass

        if wave == 1:
            pass

        if wave == 2:
            pass

    # for event in pygame.event.get():
    # if GAME_GLOBALS.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
    # quitGame()
    # keystate = pygame.key.get_pressed()

    # clock.tick(60)
    pygame.display.update()

#    display_message("Press Space to Advance Time")
#    x = input()

# call the "main" function if running this script
# if __name__ == '__main__':
#    gameStarted = True
#    main()
