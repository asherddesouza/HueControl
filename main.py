from phue import Bridge
import tkinter as tk
from tkinter import *
from tkinter.font import Font
import time

br = Bridge('192.168.1.30')
# br.connect()
# br.get_api()


# br.set_light(5,'on', False)
# checks if a certain light has been switched on
# lightOn = br.get_light(5, 'on')
# print(lightOn)

# sets brightness to a certain level
# br.set_light(5, 'bri', 254)

# br.set_light(5, 'bri', 254, transitiontime=50)

app = tk.Tk()

app.title('HueControl')
app.wm_iconbitmap('C:/Users/ashth/Downloads/hueLogo.ico')
app.geometry("500x500")
app.resizable(False, False)
app.configure(bg='mint cream')
#defining the fonts
introFont = Font(family="Ubuntu", size=20)
appFont = Font(family="Ubuntu", size=10)

def getInput():
    lightSelection = int(lightInputField.get())
    return lightSelection

def powerOn():
    br.set_light(getInput(), 'on', True)

def powerOff():
    br.set_light(getInput(), 'on', False)

def setBrightness(var):
    lightSelection = int(lightInputField.get())
    lightBrightness = int(brightSlider.get())
    br.set_light(lightSelection, 'bri',lightBrightness)

def gettingStarted():
    pass

def troubleshooting():
    pass

def fadeToFull():
    lightSelection = int(lightInputField.get())
    br.set_light(lightSelection, 'bri', 0)
    time.sleep(5)
    br.set_light(lightSelection, 'bri', 254, transitiontime=50)

def rainbow():
    lightSelection = int(lightInputField.get())

    for i in range(3):
        br.set_light(lightSelection, 'xy', [0.675,0.322])#red
        time.sleep(1)
        br.set_light(lightSelection, 'xy', [0.6,0.35])#orange
        time.sleep(1)
        br.set_light(lightSelection, 'xy', [0.56,0.4])#yellow
        time.sleep(1)
        br.set_light(lightSelection, 'xy', [0.2,0.5])#green
        time.sleep(1)
        br.set_light(lightSelection, 'xy', [0.2,0.2])#blue
        time.sleep(1)
        br.set_light(lightSelection, 'xy', [0.13,0.1])#indigo
        time.sleep(1)
        br.set_light(lightSelection, 'xy', [0.23,0.04])#violet
        time.sleep(1)

    br.set_light(lightSelection, 'xy', [0.35, 0.35])



def alert():
    lightSelection = int(lightInputField.get())
    br.set_light(lightSelection, 'xy',[0.35,0.35])#sets light to white
    br.set_light(lightSelection, 'bri', 254, transitiontime=50)
    time.sleep(5)
    br.set_light(lightSelection, "xy", [0.675, 0.322])
    time.sleep(1)
    for i in range(10):
        time.sleep(0.5)
        br.set_light(getInput(), 'on', False)
        time.sleep(0.5)
        br.set_light(getInput(), 'on', True)
        time.sleep(0.5)
        br.set_light(getInput(), 'on', False)
        time.sleep(0.5)
        br.set_light(getInput(), 'on', True)
    br.set_light(lightSelection, 'xy', [0.35, 0.35])


def white():
    lightSelection = int(lightInputField.get())
    br.set_light(lightSelection, 'xy', [0.35, 0.35])
    br.set_light(lightSelection, 'bri', 254)

def greenlights():
    lightSelection = int(lightInputField.get())
    for i in range(5):
        time.sleep(1)
        br.set_light(lightSelection, 'xy', [0.2, 0.4])
        time.sleep(1)
        br.set_light(lightSelection, 'xy', [0.3, 0.5])
        time.sleep(1)
        br.set_light(lightSelection, 'xy', [0.25, 0.5])
        time.sleep(1)
        br.set_light(lightSelection, 'xy', [0.2, 0.45])



def effect6():
    pass
def effect7():
    pass
def effect8():
    pass
def effect9():
    pass
def effect10():
    pass

#creating the dropdown menus
mainMenu = Menu(app)
app.config(menu=mainMenu)

helpMenu = Menu(mainMenu, tearoff=0)
mainMenu.add_cascade(label="Help",menu=helpMenu)
helpMenu.add_command(label="Getting Started", command=gettingStarted)
helpMenu.add_command(label="Troubleshooting", command=troubleshooting)
#brightness slider
brightSlider = Scale(app,
                     from_=0,
                     to=254,
                     relief="ridge",
                     borderwidth="3",
                     orient=HORIZONTAL,
                     command=setBrightness, width=10, fg='blue4',troughcolor='dark slate gray', font=appFont, bg='sky blue', length=250)
brightSlider.set(254)
#Frames holding groups of elements
lightSelectionF = tk.Frame(relief="ridge", borderwidth="3")
lightToggleF = tk.Frame(relief="raised", borderwidth="3")
effectsF = tk.Frame(relief="ridge", borderwidth="3")


introduction = tk.Label(text="Welcome to HueControl!", fg="dark slate gray", borderwidth="5", font=introFont, bg='mint cream')

lightInputField = tk.Entry(master=lightSelectionF, bg="azure", fg="gray21", width="40", font=appFont)
lightInputField.insert(0, "5")
#lightInputField.insert(0, "Enter IDs of the lights you want to control.")
confirmLights = tk.Button(master=lightSelectionF, height=1, width=2, text="✔", bg="dark slate gray",fg="yellow", command=getInput, font=appFont)
#toggle controls
onButton = tk.Button(master=lightToggleF, height=1, width=10, text="On", bg="dark slate gray", fg="yellow",command=powerOn, font=appFont)
offButton = tk.Button(master=lightToggleF, height=1, width=10, text="Off", bg="dark slate gray", fg="yellow", command=powerOff, font=appFont)

#Effects
effect1 = tk.Button(master=effectsF, height=4, width=8, text="brightRise", bg="light cyan", command=fadeToFull, font=appFont)
effect2 = tk.Button(master=effectsF, height=4, width=8, text="Rainbow", bg="gold", command=rainbow, font=appFont)
effect3 = tk.Button(master=effectsF, height=4, width=8, text="Alert!", bg="firebrick1", command=alert, font=appFont)
effect4 = tk.Button(master=effectsF, height=4, width=8, text="White", bg="ghost white", command=white, font=appFont)
effect5 = tk.Button(master=effectsF, height=4, width=8, text="GreenLights", bg="spring green", command=greenlights, font=appFont)
#effect6 = tk.Button(master=effectsF, height=4, width=8, text="Effect 6", bg="powder blue", command=effect6, font=appFont)
#effect7 = tk.Button(master=effectsF, height=4, width=8, text="Effect 7", bg="powder blue", command=effect7, font=appFont)
#effect8 = tk.Button(master=effectsF, height=4, width=8, text="Effect 8", bg="powder blue", command=effect8, font=appFont)
##effect9 = tk.Button(master=effectsF, height=4, width=8, text="Effect 9", bg="powder blue", command=effect9, font=appFont)
#effect10 = tk.Button(master=effectsF, height=4, width=8, text="Effect 10", bg="powder blue", command=effect10, font=appFont)



introduction.grid(row=0, column=0, padx=100, pady=10)

lightSelectionF.grid(row=1, column=0)
lightInputField.grid(row=1, column=0, ipady=4)
confirmLights.grid(row=1, column=1)

lightToggleF.grid(row=2, column=0,pady=5)
onButton.grid(row=2, column=0)
offButton.grid(row=2, column=1)

brightSlider.grid(row=3, column=0,pady=5)

effectsF.grid(row=4,column=0)
effect1.grid(row=0,column=0)
effect2.grid(row=0,column=1)
effect3.grid(row=0,column=2)
effect4.grid(row=0,column=3)
effect5.grid(row=0,column=4)
#effect6.grid(row=1,column=0)
#effect7.grid(row=1,column=1)
#effect8.grid(row=1,column=2)
#effect9.grid(row=1,column=3)
#effect10.grid(row=1,column=4)









#introduction.pack()
#lightSelectionF.pack()
#lightToggleF.pack()
#lightInputField.pack()
#confirmLights.pack()
#onButton.pack()
#offButton.pack()

app.mainloop()
