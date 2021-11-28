from tkinter import *
from PIL import ImageTk, Image
import os
import sys




root = Tk()
root.title("Can You Survive")
root.iconbitmap("C:\\Users\\Cybineer\\Desktop\\MyCode\\Text_Adventure_Game_GUI\\Survive.ico")
root.geometry('1920x1080')



# # Add image file
bg = ImageTk.PhotoImage(file = "start4.jpg")


my_img =  ImageTk.PhotoImage(Image.open("start4.jpg"))
my_label = Label(root, image=my_img)
my_label.place(x=0,y=0, relwidth=1, relheight=1)


global name


def path():
    path_label = Label(root, text="Welcome To The World Of The Unknown, Where Would You Like To Start Your Journey? Choose your path city or forest", padx=20, pady=20, font=50, bg="#5C5C5C", fg="#F0FFFF")
    path_label.pack()
    global world2
    world2 = Entry(root, width=50,borderwidth=10, bg="#212121", fg="azure", font="ComicMS", justify="center")
    world2.pack()
    global path_submit_button
    global name_submit_button
    path_submit_button = Button(root, text="Enter", command=game_start_0_function, font=24)
    path_submit_button.pack()
    finishButton = Button(root, text="Click Here To QUIT Your Journey", command=root.quit, bg="#8B1A1A", fg="azure")
    finishButton.pack()
    name_submit_button.pack_forget()
    finishButton_1.pack_forget()



def game_start_0_function():
    world = str(world2.get().lower())

    if world == "city":
        import city

        
    elif world == "forest":
        import forest




name_submit_button = Button(root, text="Start Your Adventure", command=path, bg="#66CD00", padx=25,pady=25)
name_submit_button.pack(padx=200,pady=200)

finishButton_1 = Button(root, text="Click Here To QUIT Your Journey", command=root.quit, bg="#8B1A1A", fg="azure", padx=25,pady=25)
finishButton_1.pack(padx=205,pady=205)





root.mainloop()