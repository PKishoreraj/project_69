from tkinter import *
fun=Tk()
fun.title("sales application")
fun.geometry("400x400")
 
def geranatemaxprofit:
    print("The maximum profit of"+str(max_profits)+"was recorded in the month of "+str(max_profits_month)

def geranateminprofit:
    print("The minimum profit of"+str(min_profits)+"was recorded in the month of "+str(min_profits_month)

month("Janurary","February","March","April","May","June","July","Augest","September","October","November","December")
profits(200000,450000,780000,970000,1200000,4562000,56000000,540000,100000,300000,900000)
max_profits=max(profits)
max_profits_index=profits.index(max_profits)
max_profits_month=month[max_profits_index]
      
min_profits=max(profits)
min_profits_index=profits.index(min_profits)
min_profits_month=month[min_profits_index]
      
print(month)
print(profits)

btn1=Button(fun)
btn1=Button(fun,text="Generate maximum profit",command=geranatemaxprofit)
btn1=place(relx=0.5,rely=0.5,anchor=CENTER)

btn1=Button(fun)
btn1=Button(fun,text="Generate minimum profit",command=geranateminprofit)
btn1=place(relx=0.5,rely=0.5,anchor=CENTER)

fun.mainloop

