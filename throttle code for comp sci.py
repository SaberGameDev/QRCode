import sys #Have to use sys, tty, and termios for event capture bc Pi can't handle msvcrt
import tty
import termios
import RPi.GPIO as GPi #general pin configuration library for RBP
import tkinter as tk #tkinter for GUI
from tkinter import colorchooser 

GPi.setmode(GPi.BOARD) #board setup for reading pins
GPi.setup(12, GPi.OUT) #pin configuration
GPi.setup(7, GPi.OUT)
GPi.setup(13, GPi.OUT)
GPi.setup(15, GPi.OUT)
pulse=GPi.PWM(12, 50) #Pulse width mod configuration for pin 12 at 50 hertz
pulse2 =GPi.PWM(15,100)
pulse.start(7.5) #And we start PWM at 7.5 duty cycle, or 90 degrees
pulse2.start(0)

def getch(): #character reader for pi. it can't handle new libraries that do it automatically
    file_disc = sys.stdin.fileno()
    old_settings = termios.tcgetattr(file_disc)
    tty.setraw(sys.stdin.fileno())

    char = sys.stdin.read(1)

    termios.tcsetattr(file_disc, termios.TCSADRAIN, old_settings)

    return char

def servo_calc(angle): #angle calculator
    absolut = abs(angle)
    pwm = .056*absolut+2.5
    pulse.ChangeDutyCycle(pwm)

def W_Fwd(): #forward command
    GPi.output(15, False)
    pulse2.ChangeDutyCycle(90)
    GPi.output(7, False)
    GPi.output(13, True)
    GPi.output(15, True)

def S_Bcwd(): #backward command
    GPi.output(15, False)
    pulse2.ChangeDutyCycle(90)
    GPi.output(7, True)
    GPi.output(13, False)
    GPi.output(15, True)

def Throt_STOP(): #stop it
    GPi.output(7, False)
    GPi.output(13, False)

def Logic_Table(): #logic table for motor function in button
    import turtle
    win = turtle.Screen()
    tortuga = turtle.Turtle()
    tortuga.speed()

    def turt_rec(x, y, z, l):
        tortuga.up()
        tortuga.setpos(z, l)
        tortuga.down()
        for i in range(2):
            tortuga.fd(x)
            tortuga.rt(90)
            tortuga.fd(y)
            tortuga.rt(90)

    turt_rec(450, 295, -200, 165)

    tortuga.up()
    tortuga.setpos(-87.5, 165)
    tortuga.down()
    tortuga.seth(270)
    tortuga.forward(295)

    tortuga.up()
    tortuga.setpos(25, 165)
    tortuga.down()
    tortuga.seth(270)
    tortuga.forward(295)

    tortuga.up()
    tortuga.setpos(137.5, 165)
    tortuga.down()
    tortuga.seth(270)
    tortuga.forward(295)

    tortuga.up()
    tortuga.setpos(-200, 115.7)
    tortuga.down()
    tortuga.seth(0)
    tortuga.forward(450)

    tortuga.up()
    tortuga.setpos(-200, 66.4)
    tortuga.down()
    tortuga.seth(0)
    tortuga.forward(450)

    tortuga.up()
    tortuga.setpos(-200, 17.1)
    tortuga.down()
    tortuga.seth(0)
    tortuga.forward(450)

    tortuga.up()
    tortuga.setpos(-200, -32.2)
    tortuga.down()
    tortuga.seth(0)
    tortuga.forward(450)

    tortuga.up()
    tortuga.setpos(-200, -81.5)
    tortuga.down()
    tortuga.seth(0)
    tortuga.forward(450)

    tortuga.up()
    tortuga.setpos(-165, 135)
    tortuga.down()
    tortuga.write("Enabler 1", 'middle')

    tortuga.up()
    tortuga.setpos(-37.5, 135)
    tortuga.down()
    tortuga.write("1A", 'middle')

    tortuga.up()
    tortuga.setpos(75, 135)
    tortuga.down()
    tortuga.write("2A", 'middle')

    tortuga.up()
    tortuga.setpos(165, 135)
    tortuga.down()
    tortuga.write("Motor Action", 'middle')

    tortuga.color("green")
    tortuga.up()
    tortuga.setpos(-150, 85.7)
    tortuga.down()
    tortuga.write("ON", 'middle')

    tortuga.up()
    tortuga.setpos(-150, 36.4)
    tortuga.down()
    tortuga.write("ON", 'middle')

    tortuga.up()
    tortuga.setpos(-150, -12.9)
    tortuga.down()
    tortuga.write("ON", 'middle')

    tortuga.up()
    tortuga.setpos(-150, -62.2)
    tortuga.down()
    tortuga.write("ON", 'middle')

    tortuga.color("red")
    tortuga.up()
    tortuga.setpos(-150, -111.5)
    tortuga.down()
    tortuga.write("OFF", 'middle')

    tortuga.up()
    tortuga.setpos(-37.5, 85.7)
    tortuga.down()
    tortuga.write("0", 'middle')

    tortuga.color("green")
    tortuga.up()
    tortuga.setpos(-37.5, 36.4)
    tortuga.down()
    tortuga.write("1", 'middle')

    tortuga.up()
    tortuga.setpos(-37.5, -12.9)
    tortuga.down()
    tortuga.write("1", 'middle')

    tortuga.color("red")
    tortuga.up()
    tortuga.setpos(-37.5, -62.2)
    tortuga.down()
    tortuga.write("0", 'middle')

    tortuga.color('black')
    tortuga.up()
    tortuga.setpos(-37.5, -111.5)
    tortuga.down()
    tortuga.write("N/A", 'middle')

    tortuga.color('green')
    tortuga.up()
    tortuga.setpos(75, 85.7)
    tortuga.down()
    tortuga.write("1", 'middle')

    tortuga.color('red')
    tortuga.up()
    tortuga.setpos(75, 36.4)
    tortuga.down()
    tortuga.write("0", 'middle')

    tortuga.color('green')
    tortuga.up()
    tortuga.setpos(75, -12.9)
    tortuga.down()
    tortuga.write("1", 'middle')

    tortuga.color('red')
    tortuga.up()
    tortuga.setpos(75, -62.2)
    tortuga.down()
    tortuga.write("0", 'middle')

    tortuga.color('black')
    tortuga.up()
    tortuga.setpos(75, -111.5)
    tortuga.down()
    tortuga.write("N/A", 'middle')

    tortuga.color('green')
    tortuga.up()
    tortuga.setpos(175, 85.7)
    tortuga.down()
    tortuga.write("Forward", 'middle')

    tortuga.color('red')
    tortuga.up()
    tortuga.setpos(170, 36.4)
    tortuga.down()
    tortuga.write("Backward", 'middle')

    tortuga.color('black')
    tortuga.up()
    tortuga.setpos(185, -12.9)
    tortuga.down()
    tortuga.write("Stop", 'middle')

    tortuga.up()
    tortuga.setpos(185, -62.2)
    tortuga.down()
    tortuga.write("Stop", 'middle')

    tortuga.up()
    tortuga.setpos(185, -111.5)
    tortuga.down()
    tortuga.write("Stop", 'middle')

def vid_feed(): #automatically press a button to access video feed (only usable after starting stream file, which is not included)
    import socket
    import webbrowser
    a = socket.gethostbyname(socket.gethostname())
    webbrowser.open_new_browser('https://'+a+':8000/')
    
def color(): #color picker for button background
    rgb_color = colorchooser.askcolor()[0] #actual tkinter color chooser
    lista = list(rgb_color)
    tuples = []
    for i in lista:
        tuples.append(int(i))
    bel = tuple(tuples)
    global hexa #return variable is global for use in fore_color 
    hexa = '#%02x%02x%02x' % bel
    return hexa #hexa for color

def fore_color(): #color picker for button text
    h = hexa.lstrip('#')
    tup = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    if tup[0] < 140 and tup[1] < 140 and tup[2] < 140:
        return '#FFFFFF' #chooses between light and dark depending on background color
    else:
        return '#000000'
    
def directional(): #tells user direction with labels
    dir_text = ""
    if event.char == 'w':
        dir_text = "Moving forward"
    elif event.char == 's':
        dir_text = "Moving backward"
    elif event.char == 'a':
        dir_text = "turning left"
    elif event.char == 'd':
        dir_text = "turning right"
    elif event.char == 'e':
        dir_text = "Stopped"
    myLabel = Label(scrn, text=dir_text)
    myLabel.grid(row=2, column=3)

def callback(event): #click button first to start pressing the buttons
    labeller_butt.focus_set()


scrn = tk.Tk() #tkinter stuff
scrn.title('Visual Command Board')
scrn['padx'] = 25
scrn['pady'] = 25
turtle_butt = Button(scrn, text='Logic Chart', bg=color(), fg=fore_color(), command = Logic_Table)
turtle_butt.grid(row=1, column=2)
IP_button = Button(scrn, text="Video Feed", bg= color(), fg=fore_color())
IP_button.grid(row=1, column=3)
labeller_butt = Button(scrn, text='Direction', bg=color(), fg=fore_color())
labeller_butt.bind("<Key>", directional)
labeller_butt.bind("<Button-1>", callback)
labeller_butt.grid(row=1,column=4)

scrn.mainloop

uni_var2 = int(90)
getch1 = getch()

while True:
    if getch1 == 'w':
        W_Fwd()
    elif getch1 == 's':
        S_Bcwd()
    elif getch1 == 'e':
        Throt_STOP()
    if getch1 = 'a':
        uni_var2 = uni_var2 - 5
        if uni_var2 < 30:
            uni_var2 = 30
        servo_calc(uni_var2)
    elif getch1 = 'd':
        uni_var2 = uni_var2 + 5
        if uni_var > 150:
            uni_var2 = 150
        servo_calc(uni_var2)

