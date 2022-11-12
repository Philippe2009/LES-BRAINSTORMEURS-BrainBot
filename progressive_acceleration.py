from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

hub = PrimeHub()
robot = MotorPair('B','A')
leftMotor = Motor('B')
acceleration_distance = 200
max_speed = 75
distance = 1000
leftMotor.set_degrees_counted(1)
while leftMotor.get_degrees_counted() <= acceleration_distance:
    distanceParcourue = leftMotor.get_degrees_counted()
    speed = abs(int(distanceParcourue*(max_speed/acceleration_distance)))
    if speed < 10:
        speed = 10
        
    robot.start_tank(speed, speed)
    print(speed)
    print("speed:",str(speed))
robot.move_tank(distance-2*acceleration_distance,'degrees', max_speed,max_speed)
robot.stop()
