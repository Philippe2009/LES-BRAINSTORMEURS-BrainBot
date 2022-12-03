from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math


# Create your objects here.
hub = MSHub()
color = ColorSensor('A')
motor_left = Motor('B')
motor_pair = MotorPair('B','C')
# Write your program here.
hub.speaker.beep()

def follow_line(color, distance):
    integral = 0
    lastError = 0
    motor_left.set_degrees_counted(0)

    while abs(motor_left.get_degrees_counted()) < distance:
        error = color.get_reflected_light() - 70
        P_fix = error * 0.5
        integral = integral + error # or integral+=error
        I_fix = integral * 0
        derivative = error - lastError
        lastError = error
        D_fix = derivative * 0
        correction = P_fix + I_fix + D_fix
        motor_pair.start_tank_at_power(int(50+correction), 50)
    motor_pair.stop()

follow_line(color, 10000)
