from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math


# Create your objects here.
hub = MSHub()


# Write your program here.
hub.speaker.beep()
# la variable des moteurs
motors = MotorPair('E','F')

def gyroTurn(val,speed):
   hub.motion_sensor.reset_yaw_angle()
   if val > 0:
       #tourner à droite
       print("droite")
       while hub.motion_sensor.get_yaw_angle() >= val:
           motors.start(100,speed)  
   else:
       #tourner à gauche
       print("gauche")

gyroTurn(11,10)

 
