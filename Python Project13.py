from tkinter import *
fun=Tk()
fun.title("Credit card cheak")
fun.geometry("00x400")
pin=1456
input_box=Entry(root)
input_box.pack()
place(rely=0.5,relx=0.5,anchor=CENTER)
get_input=input_box.get()
def cheak:
    if:
        get_input=pin
        Messagebox.showinfo("Congralutations your pin number is accepted")
    else:
        Messagebox.showinfo("Error","Your pin number is not accepted try again")
fun.mainloop