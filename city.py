from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import os
import sys




#name.pack()
font_tuple = ("Comic Sans MS",18, "bold")

# def city():
    
#New Window in Tkinter
top = Toplevel()
top.title("Can You Survive In The City!!!")
top.iconbitmap("C:\\Users\\Cybineer\\Desktop\\MyCode\\Survival_Game_GameOff2021\\Survive.ico")
top.geometry('1920x1080')




my_img =  ImageTk.PhotoImage(Image.open("cityblack.jpg"))
my_label = Label(top, image=my_img)
my_label.place(x=0,y=0, relwidth=1, relheight=1)

welcome_label = Label(top, text="YOU HAVE CHOSEN TO TRY AND SURVIVE IN A DARK CITY..... GOOD LUCK", pady=5, font=font_tuple)
welcome_label.pack()
name_label = Label(top, text="Enter your Name", bg="#FFEFDB", font=45)
name_label.pack()

# normal entry box
name = Entry(top, width=50,borderwidth=10, bg="#4D4D4D", fg="azure", font="ComicMS", justify="center")
name.pack()
#path_submit_button.pack_forget() #deletes chose your path button


global decision_1_submit_button

def game_start_1_function():
    game_line_1 = Label(top, font = ("Verdana", 11),  text="Welcome to the city of the lost. Here you will discover a deep dark secret and if you are lucky enough you will survive.")
    game_line_1.pack()
    game_line_2 = Label(top, font = ("Verdana", 11), text="As you start walking down the city street you see a piece of paper on the ground, at the same time you notice a flash coming from a dark alley")
    game_line_2.pack()
    game_line_3 = Label(top, font = ("Verdana", 11), text="Do you want to pick up the paper or head down the alley. Type alley or Type paper")
    game_line_3.pack()
    global user_decision_1
    global decision_1_submit_button
    global finishButton_1
    user_decision_1 = Entry(top, width=50,borderwidth=10, bg="#212121", fg="azure", font="ComicMS", justify="center")
    user_decision_1.pack()
    decision_1_submit_button = Button(top, text="Submit", bg="#228B22", fg="azure", command=game_start_2_function)
    decision_1_submit_button.pack()
    play_game_button.forget()
    finishButton_2.forget()
    finishButton_1 = Button(top, text="Click Here To QUIT Your Journey", command=top.quit, bg="#8B1A1A", fg="azure")
    finishButton_1.pack()
            

play_game_button = Button(top, text="Click To Enter The City", bg="#228B22", fg="azure", command=game_start_1_function)
play_game_button.pack()
finishButton_2 = Button(top, text="Click Here To QUIT Your Journey", command=top.quit, bg="#8B1A1A", fg="azure")
finishButton_2.pack()


# WORKING ON CHANGING FONT SIZE OF LABELS TO MAKE IT EASIER FOR PEOPLE TO SEE AND PLAY #####
def game_start_2_function():
    if user_decision_1.get().lower()  == "alley":
        game_line_4 = Label(top, font = ("Verdana", 11), text="As you head down the dark alley the light you saw quickly gets further and further away and you then notice 2 doors")
        game_line_4.pack()
        game_line_4 = Label(top, font = ("Verdana", 11), text="1 on your right side and 1 on your left side. Which door do you choose?")
        game_line_4.pack()
        game_line_4 = Label(top, font = ("Verdana", 11), text="Type Left or Right")
        game_line_4.pack()
        global user_decision_1_2
        global user_decision_1_1_submit
        global decision_1_submit_button
        global finishButton_2
        user_decision_1_2 = Entry(top, width=50,borderwidth=10, bg="#212121", fg="azure",font="ComicMS", justify="center")
        user_decision_1_2.pack()
        user_decision_1_1_submit = Button(top, text="Submit", bg="#228B22", fg="azure", command=game_start_4_function)
        user_decision_1_1_submit.pack()
        finishButton_2 = Button(top, text="Click Here To QUIT Your Journey", command=top.quit, bg="#8B1A1A", fg="azure")
        finishButton_2.pack()
        decision_1_submit_button.forget()
        finishButton_1.forget()


        

    elif user_decision_1.get().lower()  == "paper":
        game_line_5 = Label(top, font = ("Verdana", 11), text="You pick up the piece of paper and see that the note is written in blood.")
        game_line_5.pack()
        game_line_5 = Label(top, font = ("Verdana", 11), text="The note reads:  I KNOW WHO YOU ARE "+ name.get() + "... DO YOU KNOW WHY YOU ARE IN MY CITY. YOU WILL SOON FIND OUT.")
        game_line_5.pack()
        game_line_5 = Label(top, font = ("Verdana", 11), text="The note then gives you 2 direction to chose head into the 10 story building or continue down the street")
        game_line_5.pack()
        game_line_5 = Label(top, font = ("Verdana", 11), text="Type 'building'  or type 'street' ")
        game_line_5.pack()
        global user_decision_1_2_submit
        user_decision_1_2 = Entry(top, width=50,borderwidth=10, bg="#212121", fg="azure", font="ComicMS", justify="center")
        user_decision_1_2.pack()
        user_decision_1_2_submit = Button(top, text="Submit", bg="#228B22", fg="azure", command=game_start_3_function)
        user_decision_1_2_submit.pack()
        finishButton_2 = Button(top, text="Click Here To QUIT Your Journey", command=top.quit, bg="#8B1A1A", fg="azure")
        finishButton_2.pack()
        decision_1_submit_button.forget()
        finishButton_1.forget()
    


def game_start_3_function():
    if user_decision_1_2.get().lower()  == "building":
        game_line_5_1 = Label(top, font = ("Verdana", 11), text="Once you enter the building the door slams shut behind.")
        game_line_5_1.pack()
        game_line_5_1 = Label(top, font = ("Verdana", 11), text="The room turns red and you hear a robotic voice say: 'YOU HAVE MADE A BAD DECISION' " + name.get() +"!!!"+ " THIS BUILDING WILL BECOME YOUR TOMB")
        game_line_5_1.pack()
        game_line_5_1 = Label(top, font = ("Verdana", 11), text="The walls close in on you and you are crushed. You have died. YOU HAVE LOST THE GAME!!!")
        game_line_5_1.pack()
        game_over = Button(top, text="Game Over", command=top.quit,  bg="#8B1A1A", fg="azure", justify="center")
        game_over.pack()
        user_decision_1_2_submit.forget()
        finishButton_2.forget()


    elif user_decision_1_2.get().lower()  == "street":
        game_line_5_2 = Label(top, font = ("Verdana", 11), text="You continue walking down the street and you see a phone booth")
        game_line_5_2.pack()
        game_line_5_2 = Label(top, font = ("Verdana", 11), text="The phone inside the booth is ring")
        game_line_5_2.pack()
        game_line_5_2 = Label(top, font = ("Verdana", 11), text="You answer the phone and your hear on the other end:")
        game_line_5_2.pack()
        game_line_5_2 = Label(top, font = ("Verdana", 11), text=" " + name.get() + " " + name.get() + " You have chosen the correct path" )
        game_line_5_2.pack()
        game_line_5_2 = Label(top, font = ("Verdana", 11), text="Once you hang up this night mare will be over...")
        game_line_5_2.pack()
        game_line_5_2 = Label(top, font = ("Verdana", 11), text="...... HANG UP THE PHONE !!! ")
        game_line_5_2.pack()
        game_line_5_2 = Label(top, font = ("Verdana", 11), text="You hang up and you awake in your home.")
        game_line_5_2.pack()
        game_line_5_2 = Label(top, font = ("Verdana", 11), text="At your feet you see a pot of gold. ")
        game_line_5_2.pack()
        game_line_5_2 = Label(top, font = ("Verdana", 11), text="YOU HAVE SURVIVED THE GAME AND RECEIVED YOUR POT OF GOLD. ")
        game_line_5_2.pack()
        game_line_5_2 = Label(top, font = ("Verdana", 11), text = "YOU HAVE WON THE GAME ")
        game_line_5_2.pack()
        won_game= Button(top, text="You've Have One THe Game. Game Over", command=top.quit,  bg="#228B22", fg="azure")
        won_game.pack()
        user_decision_1_2_submit['state'] = DISABLED



def game_start_4_function():
    if user_decision_1_2.get().lower()  == "left":
        game_line_4_1 = Label(top, font = ("Verdana", 11), text="You think just because this path isn't as dark it is safer. But you may be in for a surprise?")
        game_line_4_1.pack()
        game_line_4_1 = Label(top, font = ("Verdana", 11), text="The door opens and you are faced with the brightest light you have ever seen. ")
        game_line_4_1.pack()  
        game_line_4_1 = Label(top, font = ("Verdana", 11), text="As your eyes try to adjust and you step inside. You feel these drips of something hitting the top of your head. You wipe your head and look into your hands")
        game_line_4_1.pack()
        game_line_4_1 = Label(top, font = ("Verdana", 11), text="You see your hands covered in blood. As you shield your eyes and look up you see the ceiling is covered in spikes.")
        game_line_4_1.pack()
        game_line_4_1 = Label(top, font = ("Verdana", 11), text="The spikes plunge from the ceiling and impale you.")
        game_line_4_1.pack()
        game_line_4_1 = Label(top, font = ("Verdana", 11), text="YOU HAVE MADE A BAD CHOICE {}, CHOOSING TO FOLLOW THE LIGHT. THAT LIGHT HAS COST YOU YOUR LIFE.".format(name.get()))
        game_line_4_1.pack()
        global game_over_1
        game_over_1 = Button(top, text="Game Over", command=top.quit,  bg="#8B1A1A", fg="azure")
        game_over_1.pack()
        user_decision_1_1_submit.forget()
        finishButton_2.forget()
        


    elif user_decision_1_2.get().lower()  == "right":
        game_line_4_2 = Label(top, font = ("Verdana", 11), text="You are headed down a dark path but the reward may be great!!")
        game_line_4_2.pack()
        game_line_4_2 = Label(top, font = ("Verdana", 11), text="As the door opens you see a knife and a bow/arrow on the table, you have a feeling you will need one of them but which do you choose.")
        game_line_4_2.pack()  
        game_line_4_2 = Label(top, font = ("Verdana", 11), text="Type Knife or Bow/Arrow to choose your weapon: ")
        game_line_4_2.pack()
        global user_decision_1_3
        global user_decision_1_3_submit
        user_decision_1_3 = Entry(top, width=50,borderwidth=10, bg="#212121", fg="azure", font="ComicMS", justify="center")
        user_decision_1_3.pack()
        user_decision_1_3_submit = Button(top, text="Submit", bg="#228B22", fg="azure", command=game_start_6_function)
        user_decision_1_3_submit.pack()
        game_over_1 = Button(top, text="Click Here To QUIT Your Journey", command=top.quit,  bg="#8B1A1A", fg="azure")
        game_over_1.pack()
        user_decision_1_1_submit.forget()
        finishButton_2.forget()
  


def game_start_6_function():

    if user_decision_1_3.get().lower()  == "knife":
        game_line_4_3 = Label(top, font = ("Verdana", 11), text="You pick up the knife and notice it already has dried blood on it. Who's blood is this you wonder.")
        game_line_4_3.pack()
        game_line_4_3 = Label(top, font = ("Verdana", 11), text="You head further into the dark room and you hear very faintly your name being called." + name.get() + " " + name.get() + " Please come help me")
        game_line_4_3.pack()  
        game_line_4_3 = Label(top, font = ("Verdana", 11), text="Type 'voice' to head towards the voice or Type 'room' to keep exploring the room: ")
        game_line_4_3.pack()
        global user_decision_1_4
        global user_decision_1_4_submit
        global game_over_3
        user_decision_1_4 = Entry(top, width=50,borderwidth=10, bg="#212121", fg="azure", font="ComicMS", justify="center")
        user_decision_1_4.pack()
        user_decision_1_4_submit = Button(top, text="Submit", bg="#228B22", fg="azure", command=game_start_7_function)
        user_decision_1_4_submit.pack()
        game_over_3 = Button(top, text="Click Here To QUIT Your Journey", command=top.quit,  bg="#8B1A1A", fg="azure")
        game_over_3.pack()
        user_decision_1_3_submit.forget()
        game_over_1.forget()



    elif user_decision_1_3.get().lower()  == "bow/arrow":
        game_line_4_4 = Label(top, font = ("Verdana", 11), text="Once you pick up the bow and arrow you see a note under the equipment on the table. ")
        game_line_4_4.pack()
        game_line_4_4 = Label(top, font = ("Verdana", 11), text="The note reads: The weapon you have chosen leads us to believe you may be the hero we have been searching for. There is also a key taped to the note. You take the key as well. ")
        game_line_4_4.pack()
        game_line_4_4 = Label(top, font = ("Verdana", 11), text="You only have 1 arrow. use it wisely. It just might save your life.")
        game_line_4_4.pack()  
        game_line_4_4 = Label(top, font = ("Verdana", 11), text=" While scanning the room you hear a voice calling your name  {}.... {}.... {}.....".format(name.get(), name.get(), name.get()))
        game_line_4_4.pack()  
        game_line_4_4 = Label(top, font = ("Verdana", 11), text="You head towards the sound and you see a stairwell. ")
        game_line_4_4.pack()  
        game_line_4_4 = Label(top, font = ("Verdana", 11), text="Time to decide. Do you want to head up the stairs or stay and explore.")
        game_line_4_4.pack()
        game_line_4_4 = Label(top, font = ("Verdana", 11), text="Type 'stairs' or Type 'explore' ")
        game_line_4_4.pack()
        global user_decision_1_5
        global user_decision_1_5_submit
        global game_over_2
        user_decision_1_5 = Entry(top, width=50,borderwidth=10, bg="#212121", fg="azure", font="ComicMS", justify="center")
        user_decision_1_5.pack()
        user_decision_1_5_submit = Button(top, text="Submit", bg="#228B22", fg="azure", command=game_start_8_function)
        user_decision_1_5_submit.pack()
        game_over_2 = Button(top, text="Click Here To QUIT Your Journey", command=top.quit,  bg="#8B1A1A", fg="azure")
        game_over_2.pack()
        user_decision_1_3_submit.forget()
        game_over_1.forget()

# voice or room story line
def game_start_7_function():
    if user_decision_1_4.get().lower()  == "voice":
        game_line_4_3_1 = Label(top, font = ("Verdana", 11), text="As you head up the stairs were you believe the voice is coming from all of a sudden the voice stops and the stairs start to shake beneath your feet. ")
        game_line_4_3_1.pack() 
        game_line_4_3_1 = Label(top, font = ("Verdana", 11), text="You start to fall. You finally land with a hard thud on a dirt floor.")
        game_line_4_3_1.pack() 
        game_line_4_3_1 = Label(top, font = ("Verdana", 11), text="You slowly lift your head and with the small sliver of light coming in the room you see a shadow standing above you.")
        game_line_4_3_1.pack() 
        game_line_4_3_1 = Label(top, font = ("Verdana", 11), text="As the shadow lunges towards you to shove the knife out in front of you.")
        game_line_4_3_1.pack() 
        game_line_4_3_1 = Label(top, font = ("Verdana", 11), text="The knife plunges deep into the shadowy figure and at that moment you realize.")
        game_line_4_3_1.pack() 
        game_line_4_3_1 = Label(top, font = ("Verdana", 11), text="You too have been stabbed.")
        game_line_4_3_1.pack()
        game_line_4_3_1 = Label(top, font = ("Verdana", 11), text="You were killed by the shadowy figure. In the end you chose the wrong weapon for this battle.")
        game_line_4_3_1.pack()
        game_line_4_3_1 = Label(top, font = ("Verdana", 11), text="YOU HAVE LOST THE GAME")
        game_line_4_3_1.pack()   
        game_over = Button(top, text="Game Over", command=top.quit,  bg="#8B1A1A", fg="azure")
        game_over.pack()
        user_decision_1_5_submit.forget()
        game_over_2.forget()




    elif user_decision_1_4.get().lower()  == "room":
        game_line_4_3_2 = Label(top, font = ("Verdana", 11), text="You continue to explore the room and you find a key. Hold on to this key. it may prove useful.")
        game_line_4_3_2.pack()
        game_line_4_3_2 = Label(top, font = ("Verdana", 11), text="You see a door with light coming from the bottom. The door is locked and you remember you have a key.")
        game_line_4_3_2.pack()
        game_line_4_3_2 = Label(top, font = ("Verdana", 11), text="You try the key and it opens the door.")
        game_line_4_3_2.pack()
        game_line_4_3_2 = Label(top, font = ("Verdana", 11), text="Once the door opens you find a pot of gold and a note. The note reads: ")
        game_line_4_3_2.pack()
        game_line_4_3_2 = Label(top, font = ("Verdana", 11), text="THE CHOICES YOU HAVE MADE THROUGHOUT THE GAME WERE THE RIGHT CHOICES")
        game_line_4_3_2.pack()
        game_line_4_3_2 = Label(top, font = ("Verdana", 11), text="YOU HAVE AVOIDED ALL THE DANGERS IN MY CITY. THE GOLD IS YOURS. YOU HAVE WON!!!")
        game_line_4_3_2.pack() 
        game_over = Button(top, text="Game Over. Click To Quit", command=top.quit,  bg="#228B22", fg="azure")
        game_over.pack()
        user_decision_1_4_submit.forget()
        game_over_3.forget()
        






#stairs or explore story line
def game_start_8_function():
    if user_decision_1_5.get().lower()  == "stairs":
        game_line_4_4_1 = Label(top, font = ("Verdana", 11), text="As you head up the stairs were you believe the voice is coming from all of a sudden the voice stops and the stairs start to shake beneath your feet.")
        game_line_4_4_1.pack()
        game_line_4_4_1 = Label(top, font = ("Verdana", 11), text="You start to turn to run back down the stair and all of a sudden the stairs open up and you begin to fall into an even darker hole.")
        game_line_4_4_1.pack()
        game_line_4_4_1 = Label(top, font = ("Verdana", 11), text="When you land, you slowly lift your head and with the small sliver of light coming in the room you see a shadow standing above you.")
        game_line_4_4_1.pack()
        game_line_4_4_1 = Label(top, font = ("Verdana", 11), text="The shadow lunges towards you.")
        game_line_4_4_1.pack()
        game_line_4_4_1 = Label(top, font = ("Verdana", 11), text="You fire your only arrow hitting the shadowy figure in the heart.")
        game_line_4_4_1.pack()
        game_line_4_4_1 = Label(top, font = ("Verdana", 11), text="As the figure slumps to the floor you see a door behind it. You head to the door.")
        game_line_4_4_1.pack()
        game_line_4_4_1 = Label(top, font = ("Verdana", 11), text="You use the key you picked up earlier and it unlocks the door.")
        game_line_4_4_1.pack()
        game_line_4_4_1 = Label(top, font = ("Verdana", 11), text="There you see a pot of gold and a note that reads: ")
        game_line_4_4_1.pack()
        game_line_4_4_1 = Label(top, font = ("Verdana", 11), text="You have killed the Guardian of my gold. This gold is yours.")
        game_line_4_4_1.pack()
        game_line_4_4_1 = Label(top, font = ("Verdana", 11), text="You Have Won The Game.")
        game_line_4_4_1.pack()        
        game_over = Button(top, text="Game Over. Click To Quit", command=top.quit,  bg="#228B22", fg="azure")
        game_over.pack()
        user_decision_1_5_submit.forget()
        game_over_2.forget()


    
    elif user_decision_1_5.get().lower()  == "explore":
        game_line_4_4_1 = Label(top, font = ("Verdana", 11), text="As you continue to explore the room, you start to feel really hot.")
        game_line_4_4_1.pack()
        game_line_4_4_1 = Label(top, font = ("Verdana", 11), text="You start to feel as if you skin is burning.")
        game_line_4_4_1.pack()
        game_line_4_4_1 = Label(top, font = ("Verdana", 11), text="The room a become so hot that you pass out.")
        game_line_4_4_1.pack()
        game_line_4_4_1 = Label(top, font = ("Verdana", 11), text="You have succumb to the heat in the room.")
        game_line_4_4_1.pack()
        game_line_4_4_1 = Label(top, font = ("Verdana", 11), text="YOU LOST THE GAME!!")
        game_line_4_4_1.pack()
        game_over = Button(top, text="Game Over", command=top.quit,  bg="#8B1A1A", fg="azure")
        game_over.pack()
        user_decision_1_5_submit.forget()
        game_over_2.forget()


top.mainloop()