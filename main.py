from tkinter import *
from PIL import ImageTk, Image

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

root.mainloop()
