from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import ttk
import os
import sys


global main_frame



#name.pack()
font_tuple = ("Comic Sans MS",18, "bold")

top = Toplevel()
top.title("Can You Survive In The Forest!!!")
top.iconbitmap("C:\\Users\\Cybineer\\Desktop\\MyCode\\Survival_Game_GameOff2021\\Survive.ico")
top.geometry('1920x1080')


my_img =  ImageTk.PhotoImage(Image.open("forest2.jpg"))
my_label = Label(top, image=my_img)
my_label.place(x=0,y=0, relwidth=1, relheight=1)



welcome_label = Label(top, text="YOU HAVE CHOSEN TO TRY AND SURVIVE IN A MAGICAL MYSTICAL FOREST.... GOOD LUCK", pady=5, font=font_tuple)
welcome_label.pack()

name_label = Label(top, text="Enter your Name", bg="#FFEFDB", font=45)
name_label.pack()

# normal entry box
name = Entry(top, width=50,borderwidth=10, bg="#4D4D4D", fg="azure", font="ComicMS", justify="center")
name.pack()
#path_submit_button.pack_forget() #deletes chose your path button


global decision_1_submit_button


def game_start_1_function():
    game_line_1 = Label(top, font = ("Verdana", 11),  text="Welcome {}, to the magical mystical forest were nothing is as it seems".format(name.get()))
    game_line_1.pack()
    game_line_2 = Label(top, font = ("Verdana", 11), text="How you got to the forest is unknown and how to leave the forest is even more of a mystery")
    game_line_2.pack()
    game_line_3 = Label(top, font = ("Verdana", 11), text="Time for your first choice of the game weather it is day or night. Be aware the time of day may or may not affect the creatures you run into")
    game_line_3.pack()
    game_line_4 = Label(top, font = ("Verdana", 11), text="Type 'Day' or Type 'Night' to choose when you entered the forest.")
    game_line_4.pack()
    global user_decision_1
    user_decision_1 = Entry(top, width=50,borderwidth=10, bg="#212121", fg="azure", font="ComicMS", justify="center")
    user_decision_1.pack()
    global decision_1_submit_button
    global finishButton_1
    decision_1_submit_button = Button(top, text="Submit", bg="#228B22",  fg="azure", command=game_start_2_function)
    decision_1_submit_button.pack()
    play_game_button.forget()
    finishButton_2.forget()
    finishButton_1 = Button(top, text="Click Here To QUIT Your Journey", command=top.quit, bg="#8B1A1A", fg="azure")
    finishButton_1.pack()


play_game_button = Button(top, text="Click To Enter The Forest", bg="#228B22", fg="azure", command=game_start_1_function)
play_game_button.pack()
finishButton_2 = Button(top, text="Click Here To QUIT Your Journey", command=top.quit, bg="#8B1A1A", fg="azure")
finishButton_2.pack()


# All story lines for day are even numbered functions. 
# All story lines for night are odd numbered functions
            
def game_start_2_function():
    if user_decision_1.get().lower() == "day":
        global game_line_5
        game_line_5 = Label(top, font = ("Verdana", 11), text="As you walk through the thick lush forest you noticed all the pretty flowers, the lovely smell of a fresh rain.")
        game_line_5.pack()
        game_line_5 = Label(top, font = ("Verdana", 11), text="You also notice what looks to be a weird shaped foot print in the wet dirt.")
        game_line_5.pack()
        game_line_5 = Label(top, font = ("Verdana", 11), text="At the same time you see what you could swear was a fairy fly past you saying you name. {}.... {}.... Follow Me!!!!!!".format(name.get(), name.get()))
        game_line_5.pack()
        game_line_5 = Label(top, font = ("Verdana", 11), text="Follow the fairy or examine the foot print. Type fairy or Type foot print: ")
        game_line_5.pack()
        global user_decision_1_2
        global user_decision_1_1_submit
        global decision_1_submit_button 
        global user_decision_1_1_button
        global finishButton_3      
        user_decision_1_2 = Entry(top, width=50,borderwidth=10, bg="#212121", fg="azure", font="ComicMS", justify="center")
        user_decision_1_2.pack()
        user_decision_1_1_button = Button(top, text="Submit", bg="#228B22",  fg="azure", command=game_start_4_function)
        user_decision_1_1_button.pack()
        finishButton_3 = Button(top, text="Click Here To QUIT Your Journey", command=top.quit, bg="#8B1A1A", fg="azure")
        finishButton_3.pack()
        #decision_1_submit_button['state'] = DISABLED #disables button once function runs
        finishButton_1.forget()
        decision_1_submit_button.forget()

        
#### WORKING ON NIGHT STORY LNE #######
    elif user_decision_1.get().lower()  == "night":
        game_line_6 = Label(top, font = ("Verdana", 11), text="Why would anyone want to be in a spooky forest at night. ")
        game_line_6.pack()
        game_line_6 = Label(top, font = ("Verdana", 11), text="You must be a brave and wise hero to enter this forest night.")
        game_line_6.pack()
        game_line_6 = Label(top, font = ("Verdana", 11), text="As you slowly walk into the dense forest you see a weird glow off in the distance.")
        game_line_6.pack()
        game_line_6 = Label(top, font = ("Verdana", 11), text="At the same time you see the glow you also hear what sounds like a waterfall.")
        game_line_6.pack()
        game_line_6 = Label(top, font = ("Verdana", 11), text="Time to decide, do you want to head towards the glow or the waterfall. ")
        game_line_6.pack()
        game_line_6 = Label(top, font = ("Verdana", 11), text="Type 'Glow' or Type 'Waterfall' ")
        game_line_6.pack()
        global user_decision_2_1
        global finishButton_2
        user_decision_2_1 = Entry(top, width=50,borderwidth=10, bg="#212121", fg="azure", font="ComicMS", justify="center")
        user_decision_2_1.pack()
        user_decision_1_1_button = Button(top, text="Submit", bg="#228B22",  fg="azure", command=game_start_3_function)
        user_decision_1_1_button.pack()
        finishButton_2 = Button(top, text="Click Here To QUIT Your Journey", command=top.quit, bg="#8B1A1A", fg="azure")
        finishButton_2.pack()
        finishButton_1.forget()
        decision_1_submit_button.forget()


def game_start_3_function():
    if user_decision_2_1.get().lower() == "glow":
        game_line_6_1 = Label(top, font = ("Verdana", 11), text="As you head towards the glow you realize this")
        game_line_6_1.pack()
        game_line_6_1 = Label(top, font = ("Verdana", 11), text="could be the biggest mistake you have made. You slowly")
        game_line_6_1.pack()
        game_line_6_1 = Label(top, font = ("Verdana", 11), text="walk up to the glow. It's so bright you really can't make out what the glow is.")
        game_line_6_1.pack()
        game_line_6_1 = Label(top, font = ("Verdana", 11), text="As you shield your eyes and reach out for the glow you suddenly feel something crawling on you")
        game_line_6_1.pack()
        game_line_6_1 = Label(top, font = ("Verdana", 11), text="you have been covered by a swarm of mystical bees. They have lured you to their hive")
        game_line_6_1.pack()
        game_line_6_1 = Label(top, font = ("Verdana", 11), text="by the glow of their honey. You have fell for their trap and have died. ")
        game_line_6_1.pack()
        game_line_6_1 = Label(top, font = ("Verdana", 11), text="tHIS FOREST IS NO PLACE TO BE AT NIGHT!!")
        game_line_6_1.pack()
        game_line_6_1 = Label(top, font = ("Verdana", 11), text="YOU LOST THE GAME!!")
        game_line_6_1.pack()
        game_over = Button(top, text="Game Over", command=top.quit,  bg="#8B1A1A", fg="azure")
        game_over.pack()
        user_decision_1_1_button.forget()
        finishButton_2.forget()


    
    elif user_decision_2_1.get().lower() == "waterfall":
        game_line_6_2 = Label(top, font = ("Verdana", 11), text="You would think that this waterfall is a normal waterfall but it is not ")
        game_line_6_2.pack()
        game_line_6_2 = Label(top, font = ("Verdana", 11), text="As you had towards the base of the waterfall and look up you see something shimmering")
        game_line_6_2.pack()
        game_line_6_2 = Label(top, font = ("Verdana", 11), text="You take a few steps into the water to get a closer look and realize you steped on something")
        game_line_6_2.pack()
        game_line_6_2 = Label(top, font = ("Verdana", 11), text="You look down to see what is was a notice something is wrapping itself around you")
        game_line_6_2.pack()
        game_line_6_2 = Label(top, font = ("Verdana", 11), text="You have stepped on the serpent of the waterfall before you could react  ")
        game_line_6_2.pack()
        game_line_6_2 = Label(top, font = ("Verdana", 11), text="You are swallowed whole. ")
        game_line_6_2.pack()
        game_line_6_2 = Label(top, font = ("Verdana", 11), text="tHIS FOREST IS NO PLACE TO BE AT NIGHT!!")
        game_line_6_2.pack()
        game_line_6_2 = Label(top, font = ("Verdana", 11), text="YOU LOST THE GAME!!")
        game_line_6_2.pack()
        game_over = Button(top, text="Game Over", command=top.quit,  bg="#8B1A1A", fg="azure")
        game_over.pack()
        user_decision_1_1_button.forget()
        finishButton_2.forget()





def game_start_4_function():
    game_line_5.forget()
    
    if user_decision_1_2.get().lower()  == "fairy":
        game_line_5_1 = Label(top, font = ("Verdana", 11), text="You start to follow the fairy and as she flies past the leaves and ")
        game_line_5_1.pack()
        game_line_5_1 = Label(top, font = ("Verdana", 11), text="the grass the glitter that follows her starts to turn everything into a brighter color of what it original was.")
        game_line_5_1.pack()
        game_line_5_1 = Label(top, font = ("Verdana", 11), text="The colors catch your attention and you notice that her glitter is also revealing a path. You decide to reach out and touch the glitter.")
        game_line_5_1.pack()
        game_line_5_1 = Label(top, font = ("Verdana", 11), text="Instantly your fingers begins to burn. You notice a lake to your right and the fairy starts to fly to the left.")
        game_line_5_1.pack()
        game_line_5_1 = Label(top, font = ("Verdana", 11), text="As you walk through the thick lush forest you noticed all the pretty flowers, the lovely smell of a fresh rain.")
        game_line_5_1.pack()
        game_line_5_1 = Label(top, font = ("Verdana", 11), text="Time to decide. Do you head towards the lake to sooth your burning hand and risk losing sight of the fairy or \n do you continue to follow the fairy and risky what ever may happen to your hand.")
        game_line_5_1.pack()
        game_line_5_1 = Label(top, font = ("Verdana", 11), text="Type 'Follow' to follow the fairy or Type 'Lake' to head towards the lake:")
        game_line_5_1.pack()
        global user_decision_1_3
        global user_decision_1_1_button
        global user_decision_1_3_1_button
        global finishButton_4
        user_decision_1_3 = Entry(top, width=50,borderwidth=10, bg="#212121", fg="azure", font="ComicMS", justify="center")
        user_decision_1_3.pack()
        user_decision_1_3_1_button = Button(top, text="Submit", bg="#228B22",  fg="azure", command=game_start_6_function)
        user_decision_1_3_1_button.pack()
        finishButton_4 = Button(top, text="Click Here To QUIT Your Journey", command=top.quit, bg="#8B1A1A", fg="azure")
        finishButton_4.pack()
        user_decision_1_1_button.forget()
        finishButton_3.forget()
 
  


    elif user_decision_1_2.get().lower()  == "foot print":
        game_line_5_1_1 = Label(top, font = ("Verdana", 11), text="While looking at the footprint you fail to notice Goblin that snuck up behind you.")
        game_line_5_1_1.pack()
        game_line_5_1_1 = Label(top, font = ("Verdana", 11), text="As you turn around he impales you with the horn protruding from his chest.")
        game_line_5_1_1.pack()
        game_line_5_1_1 = Label(top, font = ("Verdana", 11), text="You have died")
        game_line_5_1_1.pack()
        game_line_5_1_1 = Label(top, font = ("Verdana", 11), text="GAME OVER")
        game_line_5_1_1.pack()
        game_over = Button(top, text="Game Over", command=top.quit,  bg="#8B1A1A", fg="azure")
        game_over.pack()
        user_decision_1_1_button.forget()
        finishButton_3.forget()







def game_start_6_function():
    if user_decision_1_3.get().lower() == "follow":
        game_line_5_2 = Label(top, font = ("Verdana", 11), text="Your curiosity could lead you to great rewards.")
        game_line_5_2.pack()
        game_line_5_2 = Label(top, font = ("Verdana", 11), text="Even though your hand/arm is burning you have chosen to follow the fairy.")
        game_line_5_2.pack()
        game_line_5_2 = Label(top, font = ("Verdana", 11), text="You're so intent on following the fairy that you don't realize you are so deep in the forest that you cannot even see the path behind you")
        game_line_5_2.pack()
        game_line_5_2 = Label(top, font = ("Verdana", 11), text="The fairy is leading somewhere in a hurry. ")
        game_line_5_2.pack()
        game_line_5_2 = Label(top, font = ("Verdana", 11), text="You still feel your arm and hand burning and you are so temped to turn and run towards the water you see off in the distance.")
        game_line_5_2.pack()
        game_line_5_2 = Label(top, font = ("Verdana", 11), text="But just like early even though your pain in your arm is BUGGING you")
        game_line_5_2.pack()
        game_line_5_2 = Label(top, font = ("Verdana", 11), text="You continue to follow the fairy and she finally leads you")
        game_line_5_2.pack()
        game_line_5_2 = Label(top, font = ("Verdana", 11), text="Out of the forest to a huge chest with the follow words written on the side")
        game_line_5_2.pack()
        game_line_5_2 = Label(top, font = ("Verdana", 11), text="'YOU HAVE SURVIVED AND MADE IT THROUGH MY FOREST, WHAT IS IN THE CHEST IS YOURS TO KEEP'")
        game_line_5_2.pack()
        game_line_5_2 = Label(top, font = ("Verdana", 11), text="YOU'VE WON THE GAME")
        game_line_5_2.pack()
        game_over = Button(top, text="YOU WON....Game Over. Click To Quit", command=top.quit,  bg="#228B22", fg="azure")
        game_over.pack()
        user_decision_1_3_1_button.forget()
        finishButton_4.forget()
        
        

    elif user_decision_1_3.get().lower() == "lake":
        game_line_5_3 = Label(top, font = ("Verdana", 11), text="You head towards the lake as fast as you can.")
        game_line_5_3.pack()
        game_line_5_3 = Label(top, font = ("Verdana", 11), text="You plunge your arm into the glowing water.")
        game_line_5_3.pack()
        game_line_5_3 = Label(top, font = ("Verdana", 11), text="Instantly your arm tops burning and you see a rope at the bottom of the water")
        game_line_5_3.pack()
        game_line_5_3 = Label(top, font = ("Verdana", 11), text="You pull at the rope and realize there is something heavy at the end of the rope ")
        game_line_5_3.pack()
        game_line_5_3 = Label(top, font = ("Verdana", 11), text="You step into the water and pull hard on the rope and you notice bubbles coming up as you pull more \n and more of the rope out of the water")
        game_line_5_3.pack()
        game_line_5_3 = Label(top, font = ("Verdana", 11), text="You think you see the end of the rope and give it one last hard tug with all your strength")
        game_line_5_3.pack()
        game_line_5_3 = Label(top, font = ("Verdana", 11), text="As you pull this huge beast emerges from the water. With the head of a great white shark and the body of a what looks like a prehistoric crocodile this beast is mad.")
        game_line_5_3.pack()
        game_line_5_3 = Label(top, font = ("Verdana", 11), text="You try to run but slip in the mud and you are eatten in one bite from this creature")
        game_line_5_3.pack()
        game_line_5_3 = Label(top, font = ("Verdana", 11), text="You have lost the game because you were unwilling to risk pain and see where your curiosity would have led you.")
        game_line_5_3.pack()
        game_line_5_3 = Label(top, font = ("Verdana", 11), text="GAME OVER")
        game_line_5_3.pack()
        game_over = Button(top, text="Game Over", command=top.quit,  bg="#8B1A1A", fg="azure")
        game_over.pack()
        user_decision_1_3_1_button.forget()
        finishButton_4.forget()



top.mainloop()