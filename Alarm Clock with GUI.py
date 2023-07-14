from tkinter import *
import datetime
import time
import winsound

def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%d/%m/%Y %H:%M:%S")
        print(now)
        if now == set_alarm_timer:
            print("Time to Wake up")
            winsound.PlaySound("_02_maa ka phone aaya - Ring Mummy",winsound.SND_ASYNC)
            break
        elif now > set_alarm_timer:
            print("Time passed. Stopping alarm.")
            break

def actual_time():
    set_alarm_timer = f"{day.get()}/{month.get()}/{year.get()} {hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)

clock = Tk()
clock.title("Alarm Clock")
clock.geometry("500x200")
time_format=Label(clock, text= "Enter time in 24 hour format!", fg="white",bg="black",font="Arial").place(x=130,y=150)
addTime = Label(clock,text = " Day    Month    Year       Hour   Min    Sec",fg="black", font=("Arial", 14)).place(x = 110, y = 10)

# The Variables we require to set the alarm(initialization):
day = StringVar()
month = StringVar()
year = StringVar()
hour = StringVar()
min = StringVar()
sec = StringVar()

#Time required to set the alarm clock:
dayTime = Entry(clock,textvariable = day,bg = "pink",width = 5).place(x = 120, y = 70)
monthTime = Entry(clock,textvariable = month,bg = "pink",width = 5).place(x = 180, y = 70)
yearTime = Entry(clock,textvariable = year,bg = "pink",width = 7).place(x = 240, y = 70)
hourTime= Entry(clock,textvariable = hour,bg = "pink",width = 5).place(x = 320,y = 70)
minTime= Entry(clock,textvariable = min,bg = "pink",width = 5).place(x = 370,y = 70)
secTime = Entry(clock,textvariable = sec,bg = "pink",width = 5).place(x = 420,y = 70)

#To take the time input by user:
submit = Button(clock,text = "Set Alarm",fg="red",width = 10,command = actual_time).place(x =190,y = 110)

clock.mainloop()
