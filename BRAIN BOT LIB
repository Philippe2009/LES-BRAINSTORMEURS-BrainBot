from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math


# Create your objects here.
hub = MSHub()


# Write your program here.
hub.speaker.beep()
# la variable des moteurs du robot
brain_bot = MotorPair('B', 'C')
# moteur de droite
right_motor = Motor('C')
right_motor.set_degrees_counted(0)
# nous définissons que quand le robot s'arrête, il ne freine pas
brain_bot.set_stop_action('coast')

# la fonction pour avancer une certaine distance fluidement avec un certain nombre de degrés
# le paramètre "robot" prends la MotorPair
# le paramètre "robot_sensor_degrees" prends la variable du moteur qui va  servir de capteur pour le nombre de degrés parcouru
# le paramère "degrees" prends le nombre de degrés que l'on va parcourrir
# le paramètre "speed" pends en compte la vitesse
def move_until(robot,motor_sensor_degrees, degrees,speed):
    while motor_sensor_degrees.get_degrees_counted() <= degrees:
        robot.start_tank(speed, speed)
        print(motor_sensor_degrees.get_degrees_counted())
    robot.stop()
    motor_sensor_degrees.set_degrees_counted(0)
# le programme 
while  right_motor.get_degrees_counted() <= 1000:
    brain_bot.start_tank(50, 50)
    print(right_motor.get_degrees_counted())
brain_bot.stop()
right_motor.set_degrees_counted(0)
