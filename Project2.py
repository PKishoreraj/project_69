from tkinter import *
fun=Tk()
fun.geomentry("900x600")
fun.title("GUI Elements")
class GUIElements:
    def __init__(self):
        print("This is GUIElements Class")
    def CreateGUIElements():
        label=Label(fun,text="This is a label created using a class",fg="blue")
        label.pack()
        btn=Button(fun,text="Button",command=self.message)
        btn.pack(padx=20,pady=10)
    def message(self):
        messagebox.showinfo("showinfo","You have clicked on a button that has been created using class")
object_GUIElements=GUIElements()
btn=Button(fun,text="Click to create GUI Elements",command=object_GUIElements.GUIElements)
btn.pack(padx=20,pady=10)
fun.mainloop()