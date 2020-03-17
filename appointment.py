#import modules
from tkinter import *
import sqlite3
import tkinter.messagebox

#connect to database
conn = sqlite3.connect('database.db')
print("Sucessfully connected ")

#cursor to move around database
c = conn.cursor()

#Empty list to later append
ids =[]

#tkinter window
class Application:
    def __init__(self, master):
        self.master = master

        #creating the frames in master
        self.left = Frame(master, width = 800, height = 720, bg = 'lightgreen')
        self.left.pack(side=LEFT)

        self.right = Frame(master, width = 400, height = 720, bg = 'darkblue')
        self.right.pack(side=RIGHT)

        #Label the window
        self.heading = Label(self.left, text="Saturn hospital Appointment's", font = ('TimesNewRoman 40 bold italic'), fg='black',bg='lightblue')
        self.heading.place(x=0, y=0)

        #Patient's details

        #Patient's Name

        self.name = Label(self.left, text="Patient's Name",  font = ('TimesNewRoman 18 bold'), fg='black',bg='lightgreen')
        self.name.place(x=0, y=100)

        #Patient's Age
        self.age = Label(self.left, text="Age",  font = ('TimesNewRoman 18 bold'), fg='black',bg='lightgreen')
        self.age.place(x=0, y=140)

        #Gender
        self.gender = Label(self.left, text="Gender",  font = ('TimesNewRoman 18 bold'), fg='black',bg='lightgreen')
        self.gender.place(x=0, y=180)

        #Address
        self.location = Label(self.left, text="Address",  font = ('TimesNewRoman 18 bold'), fg='black',bg='lightgreen')
        self.location.place(x=0, y=220)

        #appointment time
        self.time = Label(self.left, text="Apppointment time",  font = ('TimesNewRoman 18 bold'), fg='black',bg='lightgreen')
        self.time.place(x=0, y=260)

        #Creating Entries for labels

        self.name_ent = Entry(self.left, width=30)
        self.name_ent.place(x=250, y=100)

        self.age_ent = Entry(self.left, width=30)
        self.age_ent.place(x=250, y=140)

        self.gender_ent = Entry(self.left, width=30)
        self.gender_ent.place(x=250, y=180)

        self.location_ent = Entry(self.left, width=30)
        self.location_ent.place(x=250, y=220)

        self.time_ent = Entry(self.left, width=30)
        self.time_ent.place(x=250, y=260)

        
        #To see the number of appointment fixed in a log
        sql2 = "SELECT ID FROM appointment"
        self.result = c.execute(sql2)
        for self.row in self.result:
            self.id = self.row[0]
            ids.append(self.id)

        #ordering
        self.new = sorted(ids)
        self.final_id = self.new[len(ids)-1]

        #FOR displaying log in right frame
        
        
        self.box = Text(self.right, width=40, height=40)
        self.box.place(x=30,y=30)
        self.box.insert(END, "Total appointment till now: " + str(self.final_id) )

        #function to call when add appointment button is clicked

        def add_appointment():            
            #getting the user input
            self.val1 = self.name_ent.get()
            self.val2 = self.age_ent.get()
            self.val3 = self.gender_ent.get()
            self.val4 = self.location_ent.get()
            self.val5 = self.time_ent.get()

            #To alert user to fill all the details 
            if self.val1 == "" or  self.val2 == "" or self.val3 == "" or self.val4 == "" or self.val5 == "" :
                tkinter.messagebox.showinfo("Warning","Please Fill all the details")
            else:
                #Now we add into database
                sql = "INSERT INTO 'appointment' (name, age, gender, location, Schedule_time) VALUES(?,?,?,?,?)"
                c.execute(sql,(self.val1,self.val2,self.val3,self.val4,self.val5))
                conn.commit()
                tkinter.messagebox.showinfo("Success","Appointment for " +str(self.val1) + " has been created")

                self.box.insert(END, ' Appointment Fixed for ' + str(self.val1) + ' at ' + str(self.val5))
            

        #Creating submit button
        self.submit = Button(self.left, text= 'Add appointment', width=20, height=2, bg='steelblue', command= add_appointment)
        self.submit.place(x=300, y=300)

        

        

       

#creating object
root =Tk()
b = Application(root)

#resolution of the window
root.geometry("1200x700+0+0")

