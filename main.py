from tkinter import *
from PIL import ImageTk, Image
import random

root = Tk()
root.geometry("1600x1600")
root.title("Pokemon")
root.configure(bg="palegreen")

Img1 = ImageTk.PhotoImage(Image.open("abra.jpg"))
Img2 = ImageTk.PhotoImage(Image.open("bulbasour.jpg"))
Img3 = ImageTk.PhotoImage(Image.open("charmender.jpg"))
Img4 = ImageTk.PhotoImage(Image.open("Iyvasour.jpg"))
Img5 = ImageTk.PhotoImage(Image.open("jigglypuff.jpg"))
Img6 = ImageTk.PhotoImage(Image.open("kadabra.jpg"))
Img7 = ImageTk.PhotoImage(Image.open("meowth.jpg"))
Img8 = ImageTk.PhotoImage(Image.open("nidoking.jpg"))
Img9 = ImageTk.PhotoImage(Image.open("paras.jpg"))
Img10 = ImageTk.PhotoImage(Image.open("persion.jpg"))
Img11 = ImageTk.PhotoImage(Image.open("pikachu.jpg"))
Img12 = ImageTk.PhotoImage(Image.open("ratata.jpg"))
Img13 = ImageTk.PhotoImage(Image.open("squirtle.jpg"))
button = ImageTk.PhotoImage(Image.open("button.jpg"))

Pokemons = [Img1, Img2, Img3, Img4, Img5, Img6, Img7, Img8, Img9, Img10, Img11, Img12, Img13]
powers = [30,60,50,100,70,70,60,90,40,70,200,40,50]

Player1 = Player1 = Label(
    root, text="Player 1", bg="pale turquoise", fg="black", font=("Arial", 30)
)
Player2 = Label(
    root, text="Player 2", bg="pale turquoise", fg="black", font=("Arial", 30)
)
HP_Player1 = Label(
    root, text="Score: 0", bg="pale turquoise", fg="black", font=("Arial", 25)
)
HP_Player2 = Label(
    root, text="Score: 0", bg="pale turquoise", fg="black", font=("Arial", 25)
)
ImageHolder = Label(root)
Player1.place(anchor=CENTER, relx=0.2, rely=0.2)
Player2.place(anchor=CENTER, relx=0.7, rely=0.2)
HP_Player1.place(anchor=CENTER, relx=0.2, rely=0.35)
HP_Player2.place(anchor=CENTER, relx=0.7, rely=0.35)
ImageHolder.place(anchor=CENTER, relx=0.45, rely=0.275)

player1score = 0

def Player1Function():
    global player1score
    random_pokemon = random.randint(0,12)
    ImageHolder["image"] = Pokemons[random_pokemon]
    player1score += powers[random_pokemon]
    HP_Player1['text'] = player1score

player2score = 0

def Player2Function():
    global player2score
    random_pokemon = random.randint(0,12)
    ImageHolder["image"] = Pokemons[random_pokemon]
    player2score += powers[random_pokemon]
    HP_Player2['text'] = player2score

TheBTN = Button(root, image=button, command=Player1Function)
TheBTN2 = Button(root, image=button, command=Player2Function)
TheBTN.place(anchor=CENTER, relx=0.2, rely=0.5)
TheBTN2.place(anchor=CENTER, relx=0.7, rely=0.5)

root.mainloop()
