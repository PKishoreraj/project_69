from tkinter import *
from PLI import ImageTk,Image
fun=Tk()
fun.title("Working on a canvas using functions" )
fun.geometry("600x600")
color_label=Label(fun,text="Enter a color :")
color_label.place(relx=0.6,rely=0.9,anchor=CENTER)
input_box=Entry(fun)
input_box.insert(0,"black")
input_box.place(relx=0.8,rely=0.9,anchor=CENTER)
canvas=Canvas(fun,width=590,height=510,bg="white",highlightbackground="Lightgray")
img=ImageTk.PhotoImage(Image.open("start_point1.png"))
my_image=canvas.create_image(50,50,image=img)
direction=""
oldx=50
oldy=50
newx=50
newy=50
def right_dir():
    global direction
    global oldx
    global oldy
    global newx
    global newy
    oldx=newx
    oldy=newy
    newx=newx+5
    direction="right"
def left_dir():
    global direction
    global oldx
    global oldy
    global newx
    global newy
    oldx=newx
    newx=newx+5
    direction="left"
def up_dir():
    global direction
    global oldx
    global oldy
    global newx
    global newy
    oldy=newy
    newy=newy-5
    direction="up"
def down_dir():
    global direction
    global oldx
    global oldy
    global newx
    global newy
    oldy=newy
    newy=newy+5
    direction="down"
def draw(direction,oldx,oldy,newy,newx):
    fill_color=input_box.get()
    if(direction=="right"):
        right_line=canvas.create(oldx,oldy,newx,newy,width=3,fill=fill_color)
    if(direction=="left"):
        left_line=canvas.create(old,oldy,newx,newy,width=3,fill=fill_color)
    if(direction=="up"):
        up_line=canvas.create(oldx,oldy,newx,newy,width=3,fill=fill_color)
    if(direction=="down"):
        down_line=canvas.create(oldx,oldy,newx,newy,wdth=3,fill=fill)
canvas.pack
fun.bind("<Right>",right_dir)
fun.bind("<Left>",left_dir)
fun.bind("<Up>",up_dir)
fun.bind("<Down>",down_dir)
fun.mainloop