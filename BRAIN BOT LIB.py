from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math

# THE LIBRARY FOR THE BRAIN BOT 2.0

# Create your objects here.
hub = MSHub()
# Write your program here.
hub.speaker.beep()
# la variable des moteurs du robot
brain_bot = MotorPair('B', 'C')
# moteur de droite
right_motor = Motor('C')
right_motor.set_degrees_counted(0)
#le moteur du module du haut
top_module_motor = Motor('E')
# nous définissons que quand le robot s'arrête, il ne freine pas
brain_bot.set_stop_action('coast')

# la fonction pour avancer une certaine distance fluidement avec un certain nombre de degrés
# le paramètre "robot" prends la MotorPair
# le paramètre "robot_sensor_degrees" prends la variable du moteur qui vaservir de capteur pour le nombre de degrés parcouru
# le paramère "degrees" prends le nombre de degrés que l'on va parcourrir
# le paramètre "speed" pends en compte la vitesse
#pour avancer tout droit
def move_until_straight(robot,motor_sensor_degrees, distance_degrees,speed):
    while abs(motor_sensor_degrees.get_degrees_counted()) <= abs(distance_degrees):
        robot.start_tank(speed, speed)
        print(motor_sensor_degrees.get_degrees_counted())
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
def move_until_curve(robot,motor_sensor_degrees, distance_degrees,speed_motor_left,speed_motor_right):
    while abs(motor_sensor_degrees.get_degrees_counted()) <= abs(distance_degrees):
        robot.start_tank(speed_motor_left, speed_motor_right)
        print(motor_sensor_degrees.get_degrees_counted())
    robot.stop()
    motor_sensor_degrees.set_degrees_counted(0)
    if distance_degrees < 0:
        print("ERREUR: LA VARIABLE DE LA DISTANCE NE DOIT PAS ETRE NEGATIVE(VOIR FONCTION move_until())")



# la mission "television"
def mission_television():
    move_until_straight(brain_bot,right_motor, 1250, 50)
    move_until_straight(brain_bot,right_motor, 400, -60)
    
"""
top_module.run_to_position(85,"shortest path", 75)
top_module.run_to_position(200, 'clockwise', 75)
"""
# la misision de la main
def mission_hand():
    brain_bot.move_tank(1500, 'degrees', 55, 75)
    brain_bot.move_tank(650, 'degrees', 75, 55)
    top_module_motor.run_for_degrees(120, 30)

# la première run: mission_television + mission_hand.

def first_run():
    top_module_motor.run_for_degrees(60, 30)
    mission_television()
    mission_hand()
#first_run()

move_until_straight(brain_bot,right_motor, 300,50)
move_until_curve(brain_bot,right_motor, 300,50,75)
"""
# problèmes: 
#main pas fiable
fonctions marchent en s'arretant
"""