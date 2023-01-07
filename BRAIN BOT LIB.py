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


# la mission "television"
def mission_television():
    move_until_straight(brain_bot,right_motor, 830, 50)
    move_until_straight(brain_bot,right_motor, 50, -10)
    move_until_straight(brain_bot,right_motor, 50, -30)
    move_until_straight(brain_bot,right_motor, 100, -50)
    move_until_straight(brain_bot,right_motor, 100, -40)
    move_until_straight(brain_bot,right_motor, 100, -30)
    brain_bot.stop()

"""
top_module.run_to_position(85,"shortest path", 75)
top_module.run_to_position(200, 'clockwise', 75)
"""
# la misision de la main
def mission_hand():
    brain_bot.move_tank(1500, 'degrees', 55, 75)
    brain_bot.move_tank(650, 'degrees', 75, 55)
    brain_bot.stop()
    top_module_motor.run_for_degrees(120, 30)

# la première run: mission_television + mission_hand.

def first_run():
    top_module_motor.run_for_degrees(60, 30)
    mission_television()
    mission_hand()
#first_run()
#first_run()

"""
# problèmes:
#main pas fiable
#fonctions marchents en s'arretant
"""

#mission_television()
"""
Main: NE MARCHE PAS
"""

#motor_pair.move_tank(90, 'degrees', -90, -90)

#move_until_straight(brain_bot,right_motor, 1550, 30)

#move_until_curve(brain_bot,right_motor,265 ,16,5)
#move_until_straight(brain_bot,right_motor, 600, 30)

#move_until_straight(top_module_motor, 400, 30)
#while right_color_sensor.get_reflected_light() <= 70:
 #brain_bot.start_tank(30,30)
#while left_color_sensor.get_reflected_light() >= 45 and right_color_sensor.get_reflected_light() >= 45:
 #brain_bot.start_tank(50,50)

#brain_bot.stop()
#print("ligne noire")
#move_until_curve(brain_bot,right_motor,1910 ,66,55)
#brain_bot.stop()

'''
brain_bot.move(72,'cm',0,50)
left_motor.run_for_degrees(-250, 50)
for i in range(4):
    brain_bot.move(-10,'cm',0,100)
    wait_for_seconds(1)
    brain_bot.move(20,'cm',0,100)
left_motor.run_for_degrees(250, 100)
brain_bot.move(-72,'cm',0,100)
'''
# l'eolienne
def eolienne():
    brain_bot.move(350,'degrees',0,50)
    right_motor.run_for_degrees(125, 30)
    brain_bot.move(900,'degrees',0,50)
    left_motor.run_for_degrees(-350, 30)
    # essayer 4
    for i in range(3):
        brain_bot.move(375,'degrees',0,100)
        wait_for_seconds(0.75)
        brain_bot.move(-300,'degrees',0,25)
    # essayer avec 500
    brain_bot.move(400,'degrees',0,75)
    wait_for_seconds(0.75)
    brain_bot.move(-300,'degrees',0,25)
    # retour ne marche pas
    left_motor.run_for_degrees(-450, 30)
    brain_bot.move(1250,'degrees',0,50)

SPEED = 30
def hand():
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

oil_station()

