from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
import math


# Create your objects here.
hub = PrimeHub()

#variable des moteurs
pair = MotorPair('C','B')
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
def gyroTurn(motors, angle,speed = 8):
    hub.motion_sensor.reset_yaw_angle()
    #vérifie si la valeur est positiver est négative
    #divise angle par la valeur absolue de l'angle (si angle = -1 alors valeur absolue = 1 et à l'inverse si angle = 1 alors valeur absolue = -1)
    #si l'angle est négatif, l'angle = 1 et si ml'angle est positif, angle = -1
    direction = angle / math.fabs(angle)
    print("direction:",direction)
    motors.start_tank(speed*int(direction),-speed*int(direction))
    print("direction:",direction)
    # example: -1*2 <= -1*-90
    # donc, si -2 <= 90
    while direction*hub.motion_sensor.get_yaw_angle() <= direction*angle:
        print(str(hub.motion_sensor.get_yaw_angle()))
        pass
    motors.stop()
    print(str(hub.motion_sensor.get_yaw_angle()))

#carré
def square(speed,gyroSpeed = 10):
    pair.set_stop_action('coast')
    for i in range(4):
        pair.move_tank(10, 'cm', speed, speed)
        gyroTurn(pair,-90,gyroSpeed)

# fonction qui retourne un tour de roue
# cette fonction prnd en paramètre le type de roue("little" pour petit et "big" pour gros)
def setWheelType(whell = "big"):
    # vérifie si le paramètre est égal à "small"
    if whell == "small":
        #le diamètre des roues
        rotation = 5.6 * math.pi
        pair.set_motor_rotation(rotation, 'cm')
    else:
        # ici, dans tous les cas, le paramètre estv égal à small
        rotation = 8.8 * math.pi
        pair.set_motor_rotation(rotation, 'cm')

#fonction pour afficher simplement du texte sur le HUB
def hubPrint(hubVar,text = "LES BRAINSTORMEURS C'EST LES MEILLEURS !!!"):
    hubVar.light_matrix.write(str(text))

def moveForward():
    pass



#pas besoin de renseigner de paramètre car la valeur par défaut est "big"
setWheelType()
for i in range(10):
    square(50,50)
hubPrint(hub)