from cx_Freeze import setup, Executable
import sys
import pygame
from pygame.locals import *
from pygame import font
import time
import random

includes = ["pygame", "time", "sys", "random"]

includefiles = [
"oiseau_mort-removebg-preview.png", "oiseau_v12.png", "oiseau_v22.png", "tueur-removebg-preview.png","Fast Forward.ttf", "game_over.ttf", "nge.png", "nuagez.jpg", "j_perdu2.mp3", "music_arcade.mp3"
]

executables = [
Executable("flappy.py")
]

 
# On appelle la fonction setup
 
setup(
    name = "Flappy",
    version = "1.7",
    description = "Flappy Bird codé en Python", 
    options = {'build_exe' : {'include_files':includefiles, 'includes': includes}},
    executables = executables,
)