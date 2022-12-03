from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math


# Create your objects here.
hub = MSHub()


# Write your program here.
hub.speaker.beep()


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

def follow_line(color, distance, power):
    integral = 0
    lastError = 0
    left_motor.set_degrees_counted(0)

    while abs(left_motor.get_degrees_counted()) < distance:
        error = color.get_reflected_light() - 70
        P_fix = error * 0.5
        integral = integral + error # or integral+=error
        I_fix = integral * 0
        derivative = error - lastError
        lastError = error
        D_fix = derivative * 0
        correction = P_fix + I_fix + D_fix
        brain_bot.start_tank_at_power(int(power+correction), power)
    brain_bot.stop()
SPEED = 30
def hand():
    brain_bot.move_tank(1750,'degrees', SPEED, SPEED)
    #120
    left_motor.run_for_degrees(-450, 35)
    brain_bot.move_tank(-350,'degrees', SPEED, SPEED)
    follow_line(color,450,30)
    brain_bot.move_tank(850,'degrees', 98, 100)
    #retour
    brain_bot.move_tank(-1200,'degrees', 100, 100)
    right_motor.run_for_degrees(500, 35)
    brain_bot.move_tank(2000,'degrees', 100, 100)

hand()
