import customtkinter as ctk
import time


print("Timer: ")

exitRefreshTimer = False
resetVar = False
days = 0
hours = 0
minutes = 0
seconds = 0
total = seconds,"Seconds", minutes,"minutes", hours,"Hours", days,"days"

def pressedStartButton():
    global startTimer
    startTimer = True
    label.configure(text=total)
    isStartTimerTrue()

def pressedQuitButton():
    quit()
def pressedStopButton():
    global startTimer
    startTimer = False
def isStartTimerTrue():
     if startTimer == True:
        refreshTimer()

def resetTimer():
    global days, hours, minutes, seconds, total, exitRefreshTimer
    days = 0
    hours = 0
    minutes = 0
    seconds = 0
    label.configure(text=total)
    pressedStopButton()
    global startTimer
    startTimer = True
    label.configure(text=total)

def resetLoopCheck():
    global resetVar, total
    if resetVar == True:
        total = seconds,"Seconds", minutes,"minutes", hours,"Hours", days,"days"

def refreshTimer():
        if startTimer == False:
             return
        else:
            global days, hours, minutes, seconds, total
            total = seconds,"Seconds", minutes,"minutes", hours,"Hours", days,"days"
            label.configure(text=total)
            app.after(1000, refreshTimer)
            seconds = seconds + 1
            if seconds >= 60:
                minutes = minutes + 1
                seconds = 0
                 
            if minutes >= 60:
                hours += 1
                minutes = 0
                 
            if hours >= 24:
                days += 1
                hours = 0
            resetLoopCheck()

startTimer = False

app = ctk.CTk()
app.geometry("800x800")
app.title("Timer")

total = seconds,"Seconds:", minutes,"minutes:", hours,"Hours:", days,"days:"

customFont = ctk.CTkFont(family="Arial", size=30)
label = ctk.CTkLabel(app, text=total, fg_color="transparent", width=200, height=200, font=customFont)
label.pack()


startButton = ctk.CTkButton(app, text="Start Timer", width=200, height=100, font=customFont, command=pressedStartButton).pack(pady=10)
stopButton = ctk.CTkButton(app, text="Stop Timer", width=200, height=100, font=customFont, command=pressedStopButton).pack(pady=10)
resetButton = ctk.CTkButton(app, text="Reset Timer", width=200, height=100, font=customFont, command=resetTimer).pack(pady=10)
quitButton = ctk.CTkButton(app, text="Exit program", width=200, height=100, font=customFont, command=pressedQuitButton).pack(pady=10)


app.mainloop()