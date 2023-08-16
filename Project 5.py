fun=Tk()
fun.title("Geouse the country")
fun.geometry("500x500")
enter_country=Entry(fun)
enter_country.place(relx=0.5,rely=0.2,anchor=CENTER)
country_list=Label(fun)
random_number_label=Label(fun)
lucky_friend=Label(fun)
list1=[]
def addcountry():
    country_name=enter_country.get()
    list1.append(country_name)
    friend_list["text"]="Your friendlist:"+str(list1)
def random_country():
    lenght=len(list1)
    random_no=random.randint(0,lenght-1)
    random_number_label["text"]="your lucky friend is :"+str(generated_random_number)
    btn=Button(fun,text="Add to the friend list",command=addcountry)
    btn.place(relx=0.5,rely=0.5,anchor=CENTER)
    random_number_label.place(relx=0.2,rely=0.6,anchor=CENTER)
    lucky_friend.place(relx=0.5,rely=0.7,anchor=CENTER)
fun.mainloop