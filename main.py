from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generate(): 
   from random import randint,choice,shuffle
   letter_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
   letter_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
   number= ['1','2','3','4','5','6','7','8','9','0']
   symbols = ['!','@','#','$','%','^','&','*']

   nr_letters = randint(2,4)
   nr_symbols = randint(2,4)
   nr_number = randint(1,2)

   password_list = []
   password_letters = [choice(letter_lower) for _ in range(nr_letters) ]
   password_number = [choice(number) for _ in range(nr_number)]
   password_symbol = [choice(symbols) for _ in range(nr_symbols)]

   password_list = password_letters + password_number + password_symbol
   shuffle(password_list)
   password = "".join(password_list)
   password_Entry.insert(0,password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def saverecords():
    website = name_entry.get()
    email = username_Entry.get()
    password = password_Entry.get()

    record_entry = {website : {"Email": email,"Password" : password}}
    
    if len(email) == 0 or len(password) == 0:
       messagebox.showinfo(title="Fields Empty", message="One of the fields \n is empty !! ")
    else :    
      try:
         with open("data.json","r") as data_file:
            data = json.load(data_file)
         
      except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(record_entry, data_file, indent=4)
      else:
             #Updating old data with new data
            data.update(record_entry)

            with open("data.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
                                 #old code using txt file
                           # is_ok = messagebox.askokcancel(title= record_entry[website][email], message= f"The details Entered are:\n Email :{email} \n Password: {password}\n Is it OK to Save ?")
                           # if is_ok:
                           #       with open("records.txt","a") as f:
                           #        f.writelines(record_entry)
      
      finally:
            name_entry.delete(0,END)
            password_Entry.delete(0,END)
    
#--------------------------------Search Password Feature -----------------------#
       
def searchPassword():
    
   search_Query = name_entry.get()
   try:
      with open("data.json","r") as data_file:
         data = json.load(data_file)
   except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
   else:
        if search_Query in data:
            email = data[search_Query]["Email"]
            password = data[search_Query]["Password"]
            messagebox.showinfo(title=search_Query, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {search_Query} exists.")
 

     

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.resizable(False,False)
window.config(width=300,height=500,padx=20,pady=50)
canvas = Canvas(height=200,width=300)
image_logo = PhotoImage(file= "logo.png")
canvas.create_image(100,100,image=image_logo)
canvas.grid(row=0,column=2,columnspan=2,sticky=EW)

name_label = Label(window,text="Website")
name_label.grid(column=1,row=1,padx=5,pady=5,sticky=E)

name_entry = Entry(window,width=35)
name_entry.grid(column=2,row=1,columnspan=2,padx=5,pady=5,sticky=W)

name_search = Button(window, text="Search",width=8,command=searchPassword)
name_search.grid(column = 3,row=1,pady=5,padx=10,sticky=E)

username_label = Label(window,text="Email/Username")
username_label.grid(column=1,row=2,padx=5,pady=5,sticky=E)

username_Entry = Entry(window,width=35)
username_Entry.insert(0,"advelestica.design@gmail.com")
username_Entry.grid(column=2,row=2,columnspan=2,padx=5,pady=5,sticky=W)

password_label = Label(window,text="Password")
password_label.grid(column=1,row=3,padx=5,pady=5,sticky=E)

password_Entry = Entry(window,width=25)
password_Entry.grid(column=2,row=3,columnspan=2,padx=5,pady=5,sticky=W)

generate_password = Button(text="Generate Password", width=15,command=password_generate)
generate_password.grid(column=3,row=3,padx=5,pady=5,sticky=E)

submit_button = Button(window,text="Submit",width=25,command=saverecords)
submit_button.grid(column=2,row=4,columnspan=2, padx=5,pady=10,sticky=W)

window.mainloop()