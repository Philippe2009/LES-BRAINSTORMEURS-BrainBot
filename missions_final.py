
from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math

# THE LIBRARY FOR THE BRAIN BOT 2.0

# Create your objects here.
hub = MSHub()
# Write your program here.
hub.speaker.beep()
# capteur de couleur de gauche
color = ColorSensor('D')
# la variable des moteurs du robot
brain_bot = MotorPair('B', 'C')
# moteur de droite
right_motor = Motor('C')
right_motor.set_degrees_counted(0)
left_motor = Motor('B')
left_motor.set_degrees_counted(0)
#capteur de couleur de gauche
left_color_sensor = ColorSensor('A')
right_color_sensor = ColorSensor('D')
#le moteur du module du haut
motor_pair = MotorPair('E', 'F')
# nous définissons que quand le robot s'arrête, il ne freine pas
brain_bot.set_stop_action('coast')

# la fonction pour avancer une certaine distance fluidement avec un certain nombre de degrés
# le paramètre "robot" prends la MotorPair
# le paramètre "robot_sensor_degrees" prends la variable du moteur qui vaservir de capteur pour le nombre de degrés parcouru
# le paramère "degrees" prends le nombre de degrés que l'on va parcourrir
# le paramètre "speed" pends en compte la vitesse
#pour avancer tout droit
def move_until_straight(robot,motor_sensor_degrees, distance_degrees,speed,stop_when_destination_reached = False):
    while abs(motor_sensor_degrees.get_degrees_counted()) <= abs(distance_degrees):
        robot.start_tank(speed, speed)
        print(motor_sensor_degrees.get_degrees_counted())
        #enlever le robot.stop() pour que ce soit progressif
    if stop_when_destination_reached:
        robot.stop()
    motor_sensor_degrees.set_degrees_counted(0)
    if distance_degrees < 0:
        print("ERREUR: LA VARIABLE DE LA DISTANCE NE DOIT PAS ETRE NEGATIVE(VOIR FONCTION move_until())")

# la fonction pour avancer une certaine distance fluidement avec un certain nombre de degrés
# le paramètre "robot" prends la MotorPair
# le paramètre "robot_sensor_degrees" prends la variable du moteur qui vaservir de capteur pour le nombre de degrés parcouru
# le paramère "degrees" prends le nombre de degrés que l'on va parcourrir
# le paramètre "speed" pends en compte la vitesse
#pour vaancer tout droit
def move_until_curve(robot,motor_sensor_degrees, distance_degrees,speed_motor_left,speed_motor_right,stop_when_destination_reached = False):
    while abs(motor_sensor_degrees.get_degrees_counted()) <= abs(distance_degrees):
        robot.start_tank(speed_motor_left, speed_motor_right)
        print(motor_sensor_degrees.get_degrees_counted())
    if stop_when_destination_reached:
        robot.stop()
    motor_sensor_degrees.set_degrees_counted(0)
    if distance_degrees < 0:
        print("ERREUR: LA VARIABLE DE LA DISTANCE NE DOIT PAS ETRE NEGATIVE(VOIR FONCTION move_until())")


def follow_line(color, distance,is_right = False, speed = 50):
    integral = 0
    lastError = 0
    k_fix = 0.5
    if is_right:
        k_fix = -0.5
    else:
        k_fix = 0.5
    left_motor.set_degrees_counted(0)

    while abs(left_motor.get_degrees_counted()) < distance:
        error = color.get_reflected_light() - 70
        P_fix = error * k_fix
        integral = integral + error # or integral+=error
        I_fix = integral * 0
        derivative = error - lastError
        lastError = error
        D_fix = derivative * 0
        correction = P_fix + I_fix + D_fix
        brain_bot.start_tank_at_power(int(speed+correction), speed)
    brain_bot.stop()

SPEED = 30
def hand():
    #20 pts
    brain_bot.move_tank(1750,'degrees', SPEED, SPEED)
    #120
    left_motor.run_for_degrees(-450, 35)
    brain_bot.move_tank(-350,'degrees', SPEED, SPEED)
    follow_line(color,450)
    brain_bot.move_tank(850,'degrees', 98, 100)
    #retour
    brain_bot.move_tank(-1200,'degrees', 100, 100)
    right_motor.run_for_degrees(500, 35)
    brain_bot.move_tank(2000,'degrees', 100, 100)
    brain_bot.stop()

# l'eolienne
def eolienne():
    brain_bot.move(400,'degrees',0,50)
    right_motor.run_for_degrees(125, 30)
    brain_bot.move(850,'degrees',0,50)
    left_motor.run_for_degrees(-350, 30)
    # essayer 4
    for i in range(3):
        brain_bot.move(700,'degrees',0,75)
        wait_for_seconds(0.75)
        brain_bot.move(-300,'degrees',0,25)
    # essayer avec 500
    brain_bot.move(400,'degrees',0,75)
    wait_for_seconds(0.75)
    brain_bot.move(-300,'degrees',0,100)
    left_motor.run_for_degrees(600, 75)
    brain_bot.move(-2000,'degrees',0,100)
    brain_bot.stop()
    '''
    # retour ne marche pas

    brain_bot.move(1250,'degrees',0,50)
    '''

#mission pétrolier
def oil_station():

    brain_bot.move_tank(45, 'cm', 30, 30)
    for i in range(4):
        brain_bot.move_tank(5, 'cm', 30, 30)
        wait_for_seconds(0.5)
        brain_bot.move_tank(-5, 'cm', 30, 30)
    brain_bot.move_tank(180, 'degrees', 30,0)
    brain_bot.move(5, 'cm')
    brain_bot.move_tank(-90, 'degrees', 0,30)
    brain_bot.move(-1000, 'degrees',0, 100)
    brain_bot.move(10, 'cm')
    brain_bot.move_tank(180, 'degrees', 0,100)
    brain_bot.move(-1250, 'degrees',0, 100)

# la mission "television"

def mission_television():
    move_until_straight(brain_bot,right_motor, 1000, 50)
    wait_for_seconds(1)
    move_until_straight(brain_bot,right_motor, 650, -100)
    brain_bot.stop()
#press_counter = 0
#missions = [
#mission_television()
#eolienne()

# oil_station
#]
#hub.write('0')

#eolienne()


'''

while press_counter != 4:
    """
    hub.left_button.wait_until_pressed()
    missions[press_counter]
    press_counter += 1
    hub.left_button.wait_until_released()
    print('press')
    """
    if hub.left_button.is_pressed():

    # Faire quelque chose.
        hub.speaker.beep()
        print(missions[press_counter])
        mission_to_execute = missions[press_counter]
        mission_to_execute()

        if press_counter == 0:
            print(0)
        elif press_counter == 1:
            pass
        elif press_counter == 2:
            pass
        elif press_counter == 3:
            pass
'''
'''
mission_counter = 0

def execute_mission_by_index(index):

    if index == 0:
        #television
        print('television')
        mission_television()
    elif index == 1:
        # eolienne
        print('eolienne')
        eolienne()
    elif index == 2:
        print('main')
        hand()
    elif index == 3:
        print('station_pétrolière')
        oil_station()

while mission_counter != 3:
    hub.light_matrix.write(str(mission_counter))
    if hub.left_button.is_pressed():
        hub.light_matrix.write(str(mission_counter))
        hub.speaker.beep()
        execute_mission_by_index(mission_counter)
        mission_counter += 1
    if hub.right_button.is_pressed():
        hub.light_matrix.write(str(mission_counter))
        mission_counter -= 1
        hub.speaker.beep()
        execute_mission_by_index(mission_counter)
        mission_counter += 1
'''
'''
    hub.left_button.wait_until_pressed()
    hub.speaker.beep()
    execute_mission_by_index(mission_counter)
    mission_counter += 1
'''


#oil_station()
