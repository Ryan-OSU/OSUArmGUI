
import RPi.GPIO as GPIO
from time import sleep
import numpy
import robot_simulation

# Direction pin from controller
DIR = [10,10,10,10]
DIR1 = DIR[0]
DIR2 = DIR[1]
DIR3 = DIR[2]
DIR4 = DIR[3]
# Step pin from controller
STEP = [8,8,8,8]
STEP1 = STEP[0]
STEP2 = STEP[1]
STEP3 = STEP[2]
STEP4 = STEP[3]

# 0/1 used to signify clockwise or counterclockwise.
CW = 1
CCW = 0

# Setup pin layout on PI
GPIO.setmode(GPIO.BOARD)

# Establish Pins in software
GPIO.setup(DIR1, GPIO.OUT)
GPIO.setup(STEP1, GPIO.OUT)
GPIO.setup(DIR2, GPIO.OUT)
GPIO.setup(STEP2, GPIO.OUT)
GPIO.setup(DIR3, GPIO.OUT)
GPIO.setup(STEP3, GPIO.OUT)
GPIO.setup(DIR4, GPIO.OUT)
GPIO.setup(STEP4, GPIO.OUT)

# set up the system
arm = [16.965,14.565]
x = int(input("Enter target x position \n"))
y = int(input("ENter target y position \n"))
robot_system = robot_simulation.robot_simulate(arm,CW,CCW,DIR,STEP)
stopornot = input("Do you wish to continue \n")

# initial position
angle1 = -90   # degrees
angle3 = 90
angle4 = 45 
height = 10   # cm
target_position = [angle1, height, angle3, angle4]

while stopornot != "no":
    angle1 = target_position[0]
    height = target_position[1]
    angle3 = target_position[2]
    angle4 = target_position[3]

    target_position = robot_system.target_position(x,y)
    robot_system.simulate(angle1,height,angle3,angle4,target_position)
    stopornot = input("Do you wish to continue \n")
    if stopornot == "no":
        break
    x = int(input("Enter target x position \n"))
    y = int(input("ENter target y position \n"))