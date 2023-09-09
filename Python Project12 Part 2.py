from tkinter import*
from PLI import ImageTk,Image
fun=Tk()
fun.title("Endless Dice Game")
fun.geomentry("600x400")
fun.configure(bacground="yellow2")
img=ImageTk.PhotoImage(Image.open("dice1.4.jpg")
player1=Label(fun,text="Player1",bg="royal blue",fg="white")
player1.place(relx=0.1,rely=0.3,anchor=CENTER)
player2=Label(fun,text="player2",bg="royal blue",fg="white")
player2.place(relx=0.9,rely=0.3,anchor=CENTER)
player1_score_label=(fun,text="Player1",bg="royal blue",fg="white")
player1_score_label.place(relx=0.1,rely=0.4,anchor=CENTER)
player2_score_label=Label(fun,text="player2",bg="royal blue",fg="white")
player2_score_label.(relx=0.9,rely=0.4,anchor=CENTER)
random_dice_label=Label(fun,bg="chocolate1",fg="white")
random_dice_label.place(relx=0.5,rely=0.5,anchor=CENTER)
player1_score=0
def player():
    global player1_score
    random_no=random.randit(1,6)
    random_dice_label["text"]="Player 1 Dice Random Number is:"+str(random_no)
    player1_score=player1_score+random_no
    player1_score_label["text"]=str(player1_score)
player1_btn=Button(fun,image=img,command= player1)
player1_btn.place(relx=0.1,rely=0.6,anchor=CENTER)
player2_score=0
def player2():
    global player2_score
    random_no=random.randit(1.6)
    random_dice_label["text"]="Player 2 Dice Random Number is :"+str(random_no)
    player2_score=player2_score+random_no
    player2_score_label["text"]=str(player2_score)
player2_btn=Button(fun,image=img,command=player2)
player2_btn.place(relx=0.9,rely=0.6,anchor=CENTER)
fun.mainloop()