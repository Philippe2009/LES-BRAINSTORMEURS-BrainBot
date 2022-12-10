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
'''
def measure_degrees(motor_sensor):
    while True:
        measure = motor_sensor.set_degrees_counted(0)
        print(measure)
'''



"""
for i in range(3):
    brain_bot.move_tank(400, 'degrees', 50,50)
    brain_bot.move_tank(-400, 'degrees', 50,50)
"""


#measure_degrees(left_motor)
'''
brain_bot.move_tank(500, 'degrees', 50, 50)
follow_line(right_color_sensor, 450,True, 30)
left_motor.run_for_degrees(-300, 30)
brain_bot.move_tank(100, 'degrees', 50, 50)
left_motor.run_for_degrees(-150, 30)
follow_line(right_color_sensor,350, is_right = False,speed = 50 )

right_motor.run_for_degrees(200, -30)
left_motor.run_for_degrees(200, 30)
'''
for i in range(3):
    brain_bot.move_tank(-500, 'degrees', 50,50)
    brain_bot.move_tank(400, 'degrees', 50,50)
