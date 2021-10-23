from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math


# Create your objects here.
hub = MSHub()

#variable des moteurs
pair = MotorPair('E','F')
#tourner à 90 degrés
#reset le yaw du gyro
hub.motion_sensor.reset_yaw_angle()
#variable de l'angle de destination
"""
val = 90
pair.start_tank(8, -8)
while hub.motion_sensor.get_yaw_angle() <= val:
    print(str(hub.motion_sensor.get_yaw_angle()))
    pass
pair.stop()
print(str(hub.motion_sensor.get_yaw_angle()))
"""

# la fonction pour tourner avec le gyro
# elle prend en paramètre la paire de moteurs et l'angle demandé
# il y environ 2 degrés de marge
def gyroTurn(motors, angle):
    #vérifie si la valeur est positiver est négative
    #divise angle par la valeur absolue de l'angle (si angle = -1 alors valeur absolue = 1 et à l'inverse si angle = 1 alors valeur absolue = -1)
    #si l'angle est négatif, l'angle = 1 et si ml'angle est positif, angle = -1
    direction = angle / math.fabs(angle)  
    print("direction:",direction)
    motors.start_tank(8*int(direction),-8*int(direction))
    print("direction:",direction)
    # example: -1*2 <= -1*-90
    # donc, si -2 <= 90
    while direction*hub.motion_sensor.get_yaw_angle() <= direction*angle:
        print(str(hub.motion_sensor.get_yaw_angle()))
        pass
    if angle > 0:
        # le robot tourne à droite
    
        # le robot tourne à gauche
    else:
        while hub.motion_sensor.get_yaw_angle() >= angle:
            print(str(hub.motion_sensor.get_yaw_angle()))
            pass
    motors.stop()
    print(str(hub.motion_sensor.get_yaw_angle()))
        
    
        
gyroTurn(pair,90)
