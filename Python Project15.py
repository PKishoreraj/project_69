from Tkinter import *
from PIL import ImageTk,Image
fun=Tk()
fun.minsize(650,650)
fun.maxsize(650,650)
open_img=ImageTk.PhotoImage(Image.open("open.png"))
save_img=ImageTk.PhotoImage(Image.open("save.png"))
exit_img=ImageTk.PhotoImage(Image.open("exit.jpg"))
label_file_name=Label(fun,text="File Name")
label_file_name.place(relx=0.28,re;y=0.03,anchor=CENTER)
input_file_name=Entry(fun)
input_file_name.place(relx=0.46,rely=0.03,anchor=CENTER)
my_text=Text(fun,height=35,width=80)
my_text.place(relx=0.5,rely=0.55,anchor=CENTER)
open_button=Button(fun,image=open_img,text="Open file",command=openfile)
open_button.place(relx=0.05,rely=0.03,anchor=CENTER)
fun.mainloop