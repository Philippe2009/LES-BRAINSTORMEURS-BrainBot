# on importe les librairies nécessaires
# une librairie est un ensemble de fonctions déja faites
from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math


# C'est l'objet du hub
hub = MSHub()
# La variable (la référence/ l'objet) du capteur de couleur
color_sensor = ColorSensor('A') 
# la variable de couleur pour qu'on puisse connaitre la couleur
color = color_sensor.get_color()
# Pour avoir une "preuve" du lancement du programme
hub.speaker.beep()

# on déclare la fonction (le regroupement d'instruction) pour afficher la couleur sur le hub
# déclarer veut dire : "c'est ça CETE fonction"
def display_color():
    # je vais répéter cela 100 fois
    for i in range(100):
        # on revérifie la couleur détectée
        color = color_sensor.get_color()
        # on vérifie si une couleur est détectée
        if not_equal_to(color, None):
            # on allume le boutton du hub de la même couleur que celle détectée
            hub.status_light.on(color)
            # on affiche la couleur détectée 
            hub.light_matrix.write(color)
        # le "sinon" de la condition 
        else :
            # si on ne détécte pas de couleur, on l'affiche
            hub.light_matrix.write('No color detected')
    

# pour faire fonctionner une fonction, il faut l'appeler( car en effet, nous l'avons juste déclaré juste avant)
display_color()
