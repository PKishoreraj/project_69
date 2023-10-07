from tkinter import *
rott= Tk()
root.title("Heart Report")
root.geometry("600x600")

question1_radioButton=StringVar("0")
Question1=Label(root,text="")
Question1.pack()
question1_r1=Radiobutton(root,text="yes",variable=question1_radioButton,value="yes")
question1_r1.pack()
question1_r2=Radiobutton(root,text="no",variable=question1_radioButton,value="no")
question1_r2.pack()

question2_radioButton=StringVar("0")
Question2=Label(root,text="")
Question2.pack()
question2_r1=Radiobutton(root,text="yes",variable=question1_radioButton,value="yes")
question2_r1.pack()
question2_r2=Radiobutton(root,text="no",variable=question1_radioButton,value="no")
question2_r2.pack()

question3_radioButton=StringVar("0")
Question3=Label(root,text="")
Question3.pack()
question3_r1=Radiobutton(root,text="yes",variable=question1_radioButton,value="yes")
question3_r1.pack()
question3_r2=Radiobutton(root,text="no",variable=question1_radioButton,value="no")
question3_r2.pack()

question4_radioButton=StringVar("0")
Question4=Label(root,text="")
Question4.pack()
question4_r1=Radiobutton(root,text="yes",variable=question1_radioButton,value="yes")
question4_r1.pack()
question4_r2=Radiobutton(root,text="no",variable=question1_radioButton,value="no")
question4_r2.pack()

def Heart_score():
    score=0
    if question1_radioButton.get()=="yes":
        score=score+20
        print(score)
    if question2_radioButton.get()=="yes":
        score=score+20
        print(score)
    if question3_radioButton.get()=="yes":
        score=score+20
        print(score)
    if question4_radioButton.get()=="yes":
        score=score+20
        print(score)
    if score<=20:
        messagebox.showinfo("Report","You don't need to visit a doctor")
    elif score>20 and score<=40:
        messagebox.showinfo("Report","You might need to visit a doctor")
    elif score>40 and score<=60:
        messagebox.showinfo("Report","You should visit a doctor")
    else:
        messagebox.showinfo("Report","You 100% should visit a doctor")
btn=Button(root,text="Click Me To See The Report",command=Heart_score)
btn.pack()