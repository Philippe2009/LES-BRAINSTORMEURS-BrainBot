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
motor_back = Motor('C')
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

catchline()
follow_line(color_right, 1350)
motor_back.run_for_degrees(-90, 30)
motor_pair.move_tank(17, 'cm', -70, -70)
motor_back.run_for_degrees(90, 30)
motor_pair.start_tank(30, 30)
while color_left.get_color()!='black':
    pass
motor_pair.stop()
motor_pair.move_tank(135, 'degrees', 0, 10)
motor_pair.move_tank(7, 'cm', 20, 20)
motor_pair.move_tank(135, 'degrees', 10, 0)
motor_back.run_for_degrees(-20, 30)
motor_pair.move_tank(25, 'cm', 50, 50)
