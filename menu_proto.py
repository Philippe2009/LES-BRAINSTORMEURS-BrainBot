
from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

brain_bot = PrimeHub()

brain_bot.light_matrix.show_image('HAPPY')

def mission_1():
    print('mission 1')
def mission_2():
    print('mission 2')
def execute_mission(mission_index):
    if mission_index == 1:
        mission_1()
    elif mission_index == 2:
        mission_2()
    else:
        print('ERROR: in def execute_mission(mission_index) non-valid index')


mission_index = 0

while mission_index <= 3:
    #print(mission_index)
    brain_bot.light_matrix.write(str(mission_index))
    if brain_bot.left_button.is_pressed():
        if mission_index == 0:
          execute_mission(1) 
          mission_index += 1 
        else:
            brain_bot.speaker.beep()
            mission_index += 1
            print(mission_index)
            brain_bot.light_matrix.write(str(mission_index))
            execute_mission(mission_index)

    if brain_bot.right_button.is_pressed():
        if mission_index-1== 0:
            brain_bot.speaker.beep()
            execute_mission(1)
        else:
            brain_bot.speaker.beep()
            mission_index -= 1
            print(mission_index)
            brain_bot.light_matrix.write(str(mission_index))
            execute_mission(mission_index)
            
        


        


    '''
    a = input()
    if a == 'd':
        mission_index += 1
        print(mission_index)
    elif a == 'q':
        mission_index -= 1
        print(mission_index)
    elif a == 's':
        execute_mission(mission_index)*
        '''
'''
def mission_1():
    print('mission 1')
def mission_2():
    print('mission 2')
def execute_mission(mission_index):
    if mission_index == 0:
        mission_1()
    elif mission_index == 1:
        mission_2()
    else:
        print('error')
        

mission_index = -1

while mission_index < 2:
    print('mission index')
    a = input()
    if a == 'd':
        mission_index += 1
        execute_mission(mission_index)
        print(mission_index)
    elif a == 'q':
        mission_index -= 1
        print(mission_index)
        execute_mission(mission_index)
    elif a == 's':
        execute_mission(mission_index)
'''  
