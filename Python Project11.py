from tkinter import *
fun=Tk()
fun.geometry("400x400") 
fun.title("Random Background color")
colorlist1=["red","blue","green","red","pink","manganta","purple","cyan","light blue","lght red","orange"]
print(colorlist1)
random_color=random.randint(0,4)
color=colorlist1[random_color]
def color():
    print(color)
  btn1=Button(fun,text="rndom color",command=color)
  btn1=place(relx=0.5,rely=0.5,anchor=CENTER)
fun.mainloop