from tkinter import *
root=Tk()
root.title("imager viwer")
root.geometry("500x500")
root.configure(background="lightblue")
img=image
btn=Button(root,text="Open",command=Open)
btn.place(relx=0.5,rely=0.18,anchor=CENTER)
label_planet_image=Label(root,bg="gold2",heightthickness=5,borderwidth=2,bg="lightblue")
def Open():
    img=Image.open(image_path)
def Rotate():
    img.rotate(90)
btn=Button(root,text="Rotate",command=Rotate)
btn.place(relx=0.5,rely=0.18,anchor=CENTER)
root.mainloop()