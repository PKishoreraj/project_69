from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
fun=Tk()
fun.title("Country Flags")
fun.geometry("600x400")
fun.configure(background="lightblue")
get_input = Entry(fun)
show_label = Label(fun)
india_map = ImageTk.PhotoImage(Image.open ("India.jpg"))
america_map = ImageTk.PhotoImage(Image.open ("America.jpg"))
australia_map = ImageTk.PhotoImage(Image.open ("Australia.png"))
philippines_map = ImageTk.PhotoImage(Image.open ("Philippines.png"))
japan_map = ImageTk.PhotoImage(Image.open ("Japan.jpg"))
maps_dictionary = { "India" : india_map , 
                    "America" : america_map ,
                    "Australia" : australia_map ,
                    "Philippines" : philippines_map,
                    "Japan" : japan_map,}
def showMaps():
    try:
        map_name = get_input.get()
        show_label['image'] = maps_dictionary[map_name]
    except:
        messagebox.showinfo("Error","The country you have typed is not in our system")
btn = Button(fun,text="Show Map",bg="green",command=showMaps)
get_input.place(relx=0.5,rely=0.1,anchor=CENTER)
btn.place(relx=0.5,rely=0.2,anchor=CENTER)
show_label.place(relx=0.5,rely=0.6,anchor=CENTER)
fun.mainloop()