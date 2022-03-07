from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math


# Create your objects here.
hub = MSHub()

color_right = ColorSensor('B')
color_left = ColorSensor('A')
motor_pair = MotorPair('E', 'F')
motor_left = Motor('E')
motor_right = Motor('F')
motor_back = Motor('C')
motor_front = Motor('D')
motor_back.set_stop_action('coast')

# on attrappe la ligne
def catchline():
    motor_pair.set_stop_action('coast')
    motor_pair.move_tank(10, 'cm', 30, 30)
    motor_pair.move_tank(75, 'degrees', 30, 0)
    motor_pair.move_tank(15, 'cm', 30, 30)

def follow_line(color, distance):
    integral = 0
    lastError = 0
    motor_left.set_degrees_counted(0)

    while abs(motor_left.get_degrees_counted()) < distance:
        error = color.get_reflected_light() - 50
        P_fix = error * 0.2
        integral = integral + error # or integral+=error
        I_fix = integral * 0
        derivative = error - lastError
        lastError = error
        D_fix = derivative * 0
        correction = P_fix + I_fix + D_fix
        motor_pair.start_tank_at_power(int(30+correction), int(30-correction))
    motor_pair.stop()

# Tourne jusqu'à rencontrer une ligne
def turnToLine(color, power = 20): 
    motor_pair.start_tank(0, power)
    while color.get_color()!='black':
        pass
    motor_pair.stop()

# Avance jusqu'à rencontrer une ligne
def moveToLine(color):
    motor_pair.start_tank(30, 30)
    while color.get_color()!='black':
        pass
    motor_pair.stop()
    
# Programme principal
def grue():
    motor_front.run_for_degrees(180, 30)
    catchline()
    follow_line(color_right, 1350)
    motor_back.run_for_degrees(-90, 30)
    # on recule pour le camion
    motor_pair.move_tank(22, 'cm', -100, -100)
    motor_back.set_stop_action('brake')
    motor_back.run_for_degrees(120, 30)
    moveToLine(color_left)
    motor_pair.move_tank(-5, 'cm', 20, 20)
    motor_pair.move_tank(135, 'degrees', 0, 10)
    moveToLine(color_right)
    turnToLine(color_right)
    motor_pair.move_tank(9, 'cm', 30, 30)
    motor_pair.move_tank(90*1.5, 'degrees', 0, -30)
    motor_front.run_for_degrees(-250, 30)
    # on avance(comme des bourrins) au niveau de la grue
    motor_front.set_stop_action('hold')
    motor_pair.move_tank(30, 'cm', 70, 70)
    motor_pair.move_tank(-20, 'cm', 30, 30)
    motor_front.set_stop_action('coast')
    motor_front.run_for_degrees(180, 30)
    motor_pair.move_tank(40*1.5, 'degrees', 30, 0)
    motor_pair.move_tank(20, 'cm', 20, 20)
    moveToLine(color_left)
    turnToLine(color_right)
    follow_line(color_right, 500)
    moveToLine(color_left)
    # on est à l'hélicoptère
    motor_pair.move_tank(-1, 'cm', 30, 30)
    motor_pair.move_tank(1.5*1.5, 'cm', 20, 0)
    # on fait l'hélicoptère
    motor_pair.move_tank(3, 'cm', 50, 50)
    motor_pair.move_tank(-10, 'cm', 30, 30)
    motor_pair.move_tank(180, 'degrees', 20, -20)
    turnToLine(color_left,-20)
    motor_pair.move_tank(2, 'cm', 30, 0)
    motor_back.set_stop_action('brake')
    motor_back.run_for_degrees(-50, 20)
    motor_back.set_stop_action('coast')
    follow_line(color_left, 1500)
    motor_back.set_stop_action('brake')
    motor_back.run_for_degrees(90, 100)
    motor_pair.move_tank(20, 'cm', 50, 50)
    motor_back.set_stop_action('brake')
    motor_back.run_for_degrees(-70, 20)
    motor_back.set_stop_action('coast')
    motor_pair.move_tank(-15, 'cm', 70, 70)
    motor_back.set_stop_action('brake')
    motor_back.run_for_degrees(90, 100)
    motor_back.set_stop_action('coast')
    followLine(color_left, 500)
    motor_pair.move_tank(100, 'cm', 100, 100)
    """
    motor_pair.move_tank(140, 'degrees', 20, 0)
    motor_front.run_for_degrees(-210, 30)
    motor_pair.move_tank(25, 'cm', 50, 50)
    """
#grue()
motor_pair.move_tank(100, 'cm', 100, 100)


"""
séance du 05/03/2022
on a fait le pont , la grue , le camion, l'hélico

"""

