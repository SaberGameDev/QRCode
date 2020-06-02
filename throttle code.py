#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_IMPORTS-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_

import time
import termios
import sys
import tty
import RPi.GPIO as GPi

#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-PIN SETUPS-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_

GPi.setmode(GPi.BOARD) #how to set physical pins... yeah. Pull up a pinup table and name pins based on their numerical order (left->right,top->bottom)
GPi.setwarnings(False)
GPi.setup(12,GPi.OUT) #pin for servo. officially named "GPIO 18", physically pin 13
GPi.setup(13,GPi.OUT) #pin for throttle. officially named "GPIO 17", physically pin 11
GPi.setup(7, GPi.OUT) #pin for throttle. officially named "GPIO 4", physically pin 7
GPi.setup(15, GPi.OUT)#pin for throttle (enabler). officially named "GPIO 22", physically pin 15
pulse=GPi.PWM(12,50) #sets PWM modulation OUTPUT for pin 13, with a frequency of 50 Hz
pulse.start(2.5) #AND we start the PWM
pulse2 = GPi.PWM(15,100)
pulse2.start(0)

#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-DEFINED FUNCTIONS-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_

def getch():  #this entire thing basically defines the listener. Getch() cab actually be used in a library called
    #msvcrt, but Linux can't run it, and this ver. of python is too old to run it properly
    file_desc = sys.stdin.fileno()
    init_set = termios.tcgetattr(file_desc)
    tty.setraw(file_desc)
    
    char = sys.stdin.read(1)
    
    termios.tcsetattr(file_desc, termios.TCSADRAIN, init_set)
    return char

def servo_calc(angle): #conversion from angle to signal duration
    absolut = abs(angle)
    pwm = .056*absolut + 2.5
    pulse.ChangeDutyCycle(pwm)

def W_Fwd(): #forward command
    GPi.output(15, False)
    GPi.output(7, False)
    GPi.output(13, True)
    pulse2.ChangeDutyCycle(100)
    GPi.output(15, True)

def S_Bcwd(): #backward command
    GPi.output(15, False)
    GPi.output(7, True)
    GPi.output(13, False)
    pulse2.ChangeDutyCycle(100)
    GPi.output(15, True)

def Throt_STOP(): #keeps the programs from running with uni_var1 as 0; stops car
    GPi.output(7, False)
    GPi.output(13, False)


#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_DEFINING VARIABLES-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
uni_var2 = int(90)

#                                      Defined in CC due to while loop
#                                                   |
#                                                   |
#                                                   |
#                                                   |
#                                                   |
#                                                   |
#                                                   V
##-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_CENTRAL COMMANDS-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
while True:
    getch1 = getch()
    if getch1 == 'w':
        W_Fwd()
    elif getch1 == 's':
        S_Bcwd()
    elif getch1 == 'e':
        Throt_STOP()
    if getch1 == 'a':
        uni_var2 = uni_var2 - 5
        if uni_var2 > 30:
            uni_var2 = 30
        servo_calc(uni_var2)
    elif getch1 == 'd':
        uni_var2 = uni_var2 + 5
        if uni_var2 < 150:
            uni_var2 = 150
        servo_calc(uni_var2)
            
print("Cleaning and Quitting...")
GPi.cleanup()

