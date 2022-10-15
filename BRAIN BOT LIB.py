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
left_motor = Motor('B')
left_motor.set_degrees_counted(0)
#capteur de couleur de gauche
left_color_sensor = ColorSensor('A')
right_color_sensor = ColorSensor('D')
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
move_until_curve(brain_bot,right_motor,546 ,25,65)
move_until_straight(brain_bot,right_motor, 1050, 50)

move_until_curve(brain_bot,right_motor,260 ,65,25)
#move_until_straight(brain_bot,right_motor, 500, 50)
while right_color_sensor.get_reflected_light() <= 70:
    brain_bot.start_tank(30,30)
while left_color_sensor.get_reflected_light() >= 45 and right_color_sensor.get_reflected_light() >= 45:
    brain_bot.start_tank(50,50)

brain_bot.stop()
print("ligne noire")
#move_until_curve(brain_bot,right_motor,1910 ,66,55)
brain_bot.stop()

