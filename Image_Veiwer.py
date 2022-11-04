from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title("Andrew - Image Veiwer")
#root.geometry("320x250+300+300")
root.resizable()

#root.icon("image.ico")
#Frames 1


my_img0 = ImageTk.PhotoImage(Image.open("Images/helicop.jpg"))
my_img1 = ImageTk.PhotoImage(Image.open("Images/alex_rifle.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("Images/paki_f17.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("Images/second.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("Images/chengdu.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("Images/helicop.jpg"))


img_list = [my_img0,my_img1,my_img2,my_img3,my_img4,my_img5]

my_label = Label(image = my_img0)
my_label.grid(row=0,column=0,columnspan=3)




def forward(img_num):
    global my_label
    global button_forward
    global button_back
    #creating logic for moving the pictures 
    my_label.grid_forget()
    my_label = Label(image=img_list[img_num-1])
    my_label.grid(row=0,column=0,columnspan=3)
    button_forward = Button(root,text="next>>",command=lambda:forward(img_num+1)).grid(row=1,column=2)
    button_back = Button(root,text="prev<<",command=lambda:previous(img_num-1)).grid(row=1,column=0)
    #disable button using an if statement
    if img_num == 5:
        button_forward = Button(root,text="next>>",state=DISABLED).grid(row=1,column=2)

    status = Label(root,text="Image " + str(img_num) + " of " +str(len(img_list)),bd=1,relief=SUNKEN,anchor=E)
    status.grid(row=2,column=0,columnspan=3,sticky=N+E+W+S)


def previous(img_num):
    global my_label
    global button_forward
    global button_back
    my_label.grid_forget()
    my_label = Label(image=img_list[img_num-1])
    my_label.grid(row=0,column=0,columnspan=3)
    button_forward = Button(root,text="next>>",command=lambda:forward(img_num+1)).grid(row=1,column=2)
    button_back = Button(root,text="prev<<",command=lambda:previous(img_num-1)).grid(row=1,column=0)

    if img_num == 1:
        button_back = Button(root,text="prev<<",state=DISABLED).grid(row=1,column=0)

    status = Label(root,text="Image " + str(img_num) + " of " +str(len(img_list)),bd=1,relief=SUNKEN,anchor=E)
    status.grid(row=2,column=0,columnspan=3,sticky=N+E+W+S)

    





button_forward = Button(root,text="next>>",command=lambda:forward(2)).grid(row=1,column=2)
button_exit = Button(root,text="exit",command=root.quit,pady=1).grid(row=1,column=1)
button_back = Button(root,text="prev<<",command=previous).grid(row=1,column=0)

status = Label(root,text="Image 1 of "+str(len(img_list)),bd=1,relief=SUNKEN,anchor=E)
status.grid(row=2,column=0,columnspan=3,sticky=N+E+W+S)




root.mainloop()