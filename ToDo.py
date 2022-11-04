#creating a to do app
from tkinter import *
from tkinter import messagebox
import datetime
import time
import winsound


root = Tk()
root.title("Andrew -  To Do ")
root.iconbitmap("favicon.ico")
root.geometry("400x400+300+300")
root.resizable(0,0)

#Creating frames
eFrame =LabelFrame(root,bg="green")
eFrame.pack(fill="both")

nFrame =LabelFrame(root,bg="green")
nFrame.pack(fill="both")

bFrame = LabelFrame(root,bg="#ccccff")
bFrame.pack(expand=True,fill="both")

# Creating Entry
e = Entry(eFrame,width=400)
e.insert(0,"Activity")
e.grid(row=1,column=0,columnspan=3,rowspan=1,ipadx=10)

#setAlarm function
def setAlarm():
    clock = Toplevel()
    clock.geometry("250x150")
    clock.resizable(0,0)
    clock.title("Set time frame")
    clock.iconbitmap("favicon.ico")

    frame1 = LabelFrame(clock,bg="#e2ffaa")
    frame1.pack(fill="both",expand=True)
    frame2 = LabelFrame(clock,bg="#ffbffe")
    frame2.pack(fill="both",expand=True)
    #labels
    addTime = Label(frame1,text = "Hour    Min     Sec",font=10,bg="#e2ffaa").place(x = 110)
    setYourAlarm = Label(frame1,text = "Alarm time",fg="black",bg="#e2ffaa",font=("Calibri (Body)",11)).place(x=0, y=29)
    time_format = Label(frame2,text="Please input time in 24 hours format",bg="#ffbffe").pack(side="bottom")

    def alarm(set_alarm_timer):
        while True:
            time.sleep(1)
            current_time = datetime.datetime.now()
            now = current_time.strftime("%H:%M:%S")
            date = current_time.strftime("%d/%m/%Y")
            #Some logic
            if now == set_alarm_timer:                                                                
                winsound.PlaySound("1715.mp3",winsound.SND_ASYNC)
                response = messagebox.showinfo("Alarm","Alarm ended!")
                clock.destroy() 
                break

    def actual_time():
        messagebox.showinfo("Alarm","Started your alarm")
        set_alarm_timer = f"{hour.get()}:{mins.get()}:{sec.get()}"
        alarm(set_alarm_timer)

    
    #creating text variable
    hour = StringVar()
    mins = StringVar()
    sec = StringVar()

    #creating time entry
    hourTime= Entry(frame1,textvariable = hour,bg = "#ffcccc",width = 15).place(x=110,y=30)
    minTime= Entry(frame1,textvariable = mins,bg = "#ffcccc",width = 15).place(x=150,y=30)
    secTime = Entry(frame1,textvariable = sec,bg = "#ffcccc",width = 15).place(x=200,y=30)

    #creating alarm button
    btn = Button(frame2,text="Set Alarm",relief="flat",bg="#ffbffe",command=actual_time)
    btn.pack()

    clock.mainloop()

#Definig button function
def click():
    var = StringVar()
    task =  Checkbutton(bFrame,text=e.get(),variable=var,bg="#ccccff",font=("Bahnschrift Condensed",10))
    task.pack()
    

    

#Defining function that deletes tasks
btn = Button(bFrame,text="Add time frame",bg="#ccccff",relief="flat",command=setAlarm)
btn.pack()
    #dell = Button(bFrame,text="delete").pack(side="right")
    


#Creating add task button
add = Button(nFrame,text="ADD TASK",command=click,fg="blue")
add.pack(side="left")

#defining self deatruct function
def close():
    response = messagebox.askyesno("Close","Close app?,your data will be lost")
    if response == True:
        root.quit()

#Creating self destruct button  //create different frame for this widget
close = Button(bFrame,text="close",bg="#ccccff",relief="flat",command=close)
close.pack(side="bottom")


root.mainloop()