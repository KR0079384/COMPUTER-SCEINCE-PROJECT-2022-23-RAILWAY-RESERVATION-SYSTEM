from tkinter import *
import tkinter as tk
import mysql.connector as myc 
from tkinter import messagebox
import random
from tabulate import tabulate 
import os

#creating main window and title,gemoetr,bg of the window and also the icon for the window
root =tk.Tk()
root.title("RAILWAY MANAGEMENT SYSTEM")
root.iconbitmap("C:\Python\Computer Science project RAILWAY MANAGEMENT SYSTEM 2022-23\icon.ico")
root.config(bg="green")
root.geometry("1000x1000")

#background wallpaper for the window and frames
g=PhotoImage(file="C:\Python\Computer Science project RAILWAY MANAGEMENT SYSTEM 2022-23\wallpaperflare.com_wallpaper.png")
background_label=Label(root,image=g)
background_label.place(x=0,y=0,relwidth=1,relheight=1)

#title of the project as label 
main_lab=Label(root,text='RAILWAY RESERVATION SYSTEM',fg="Dark blue",bg="gray",font=("Italic",30))
main_lab.pack()

#frame for the main buttons
mainframe=Frame(root,bg="gray")
mainframe.place(x=350,y=90,height=350,width=600)

def fare():
    global fare_lab_N
    #fare label
    fare_label=Label(root,text="Fare of the tkt:",bg="lightgray",font=("Corbert Condensed Italic",18),fg="red")
    fare_label.place(x=675,y=500)

    fare_lab_N=Label(root,text="250",bg="lightgray",font=(18))
    fare_lab_N.place(x=675,y=540)

    if value_inside.get()== "Shatabdi":
        fare_lab_N.config(text="300")
    elif value_inside.get() == "Pallavan":
        fare_lab_N.config(text="350")
    elif value_inside.get()=="CSF Express":
        fare_lab_N.config(text="400")
    elif value_inside.get()=="Vaighai":
        fare_lab_N.config(text="450")
    elif value_inside.get()=="Hazrat Nizamuddin":
        fare_lab_N.config(text="500")
    else:
        print("ok")



#variables to store the data entered in textbox
def showop():
    global value_inside

    options_list = ["Shatbdi", "Pallavan", "CSF Express", "Vaighai","Hazrat Nizamuddin"]
    
  
# Variable to keep track of the option
# selected in OptionMenu
    value_inside = tk.StringVar(root)
  
# Set the default value of the variable
    value_inside.set("Select the train of your choice")
  
# Create the optionmenu widget and passing 
# the options_list and value_inside to it.
    question_menu = tk.OptionMenu(booktkt_frame, value_inside, *options_list)
    question_menu.config(fg="red",bg="yellow",font=('Helvetica',16))
    question_menu.place(x=350,y=145)

# function of the button for deleting the ticket from the database
def deltkt():
    tkt_del=delete_Entry.get()
    con=myc.connect(user="root",host="localhost",password="KR007@12345",database="irctc")
    cur=con.cursor()
    cur.execute(f"delete from train where PNR_No = '{tkt_del}'")
    print(cur.fetchall())
    con.commit()

    delete_Entry.delete("0","end")
    messagebox.showwarning("Deleted","Your ticket has been successfully deleted!!")

# function for the button to store it in the databse in MYSQL 
def booktkt1():
    if value_inside.get()=="select train of your choice" or Source_entry.get()=="" or destin_entry.get()=="" or namep_entry.get()=="" or gender_entry.get()=="":
        messagebox.showerror("Error","All fields are required")
    else:
        con=myc.connect(user="root",host="localhost",password="KR007@12345",database="irctc")
        cur=con.cursor()
        tkt_1=str(r)
        name=value_inside.get()
        source=Source_entry.get()
        destin=destin_entry.get()
        namep=namep_entry.get()
        gen=gender_entry.get()
        fare=str(fare_lab_N)
         
        cur.execute(f"INSERT INTO train values('{tkt_1}','{name}','{source}','{destin}','{namep}','{gen}','{fare}')")
        con.commit()

         

        cur.execute("select PNR_No from train")
        T=cur.fetchall()
        print(T)
        buffer=[]
        for i in T:
            buffer.append(i[0])
        print(buffer)
        state = True 
        while state:
            s=str(random.randint(6098900,6099900))
            if s not in buffer:
                buffer.append(s)
                state=False
            else:
                state=True
            print(s)
        
        tkt_PNR_Lab.config(text=str(s))
        Source_entry.delete("0","end")
        destin_entry.delete("0","end")
        namep_entry.delete("0","end")
        gender_entry.delete("0","end")

        messagebox.showinfo("Done!!","Your ticket has been successfully saved to the database")
        
# tabulate function in python is used to tabulate the records and keep a track of the records
        table=[['PNR of yout tkt',s],['Source Station',source],['Name of the train',name],['Destination',destin],['Name of the passenger',namep],['gender_entry',gen]]
        print(tabulate(table))

# The frame to book ticket and the labels and entries for the details  
def booktkt():
    global r,booktkt_frame
    con=myc.connect(user="root",host="localhost",password="KR007@12345",database="irctc")
    cur=con.cursor()
    cur.execute("create table if not exists train(PNR_No varchar(30),Train_name varchar(50),Source varchar(30),destination varchar(30),name_of_passenger varchar(30),gender char (1),fare varchar(30))")
    con.commit()

    global tkt_entry,Name_entry,Source_entry,destin_entry,namep_entry,gender_entry,tkt_PNR_Lab
    
    mainframe.destroy()
    booktkt_frame=tk.Frame(root,bg="orange")
    booktkt_frame.place(x=450,y=90,width=700,height=700)
    
    label1=Label(root,text="Enter your details here:",font=("Italic",18),fg="pink",bg="black")
    label1.place(x=525,y=100)

    #PNR_No
    r=random.randint(6969200,6969700)
    tkt_label=Label(root,text="PNR No:",bg="lightgray",font=("Corbert Condensed Italic",18),fg="red")
    tkt_label.place(x=475,y=200)

    tkt_PNR_Lab=Label(root,text=r,bg="lightgray",font=(18))
    tkt_PNR_Lab.place(x=475,y=240)


    #Train_Name
    Name_label=Label(root,text="Train Name:",bg="lightgray",font=("Corbert Condensed Italic",18),fg="red")
    Name_label.place(x=800,y=200)
    showop()
    
    # Name_entry=Entry(root,font=("Corbert Condensed Italic",16),bg="lightgray")
    # Name_entry.place(x=800,y=240)

    #Gender
    Source_label=Label(root,text="Source:",bg="lightgray",font=("Corbert COndensed Italic",18),fg="red")
    Source_label.place(x=475,y=300)

    Source_entry=Entry(root,font=("Corbert Condensed Italic",16),bg="lightgray")
    Source_entry.place(x=475,y=340)

    #Destination
    destin_label=Label(root,text="Destination:",bg="lightgray",font=("Corbert COndensed Italic",18),fg="red")
    destin_label.place(x=800,y=300)

    destin_entry=Entry(root,font=("Corbert Condensed Italic",16),bg="lightgray")
    destin_entry.place(x=800,y=340)

    #Name_of_passernger
    namep_label=Label(root,text="Name of the passenger:",bg="lightgray",font=("Corbert Condensed Italic",18),fg="red")
    namep_label.place(x=475,y=400)
    
    namep_entry=Entry(root,font=("Corbert Condensed Italic",16),bg="lightgray",width=25)
    namep_entry.place(x=475,y=440)

    #Gender
    gender_label=Label(root,text="Gender:",bg="lightgray",font=("Corbert Condensed Italic",18),fg="red")
    gender_label.place(x=800,y=400)

    gender_entry=Entry(root,font=("Corbert Condensed Italic",16),bg="lightgray")
    gender_entry.place(x=800,y=440)

    #signup button
    input_btn=Button(root,text="Book your ticket",bg="Yellow",fg="Red",font=("Corbert Condensed Italic",18),padx=15,pady=15,command=booktkt1)
    input_btn.place(x=900,y=600)

    #show fare btn
    show_fare=Button(root,text="Show fare for the train",padx=5,pady=15,font=("Helvetica",18),fg="Skyblue",bg="Indigo",command=fare)
    show_fare.place(x=500,y=600)


# the main function for deleting ticket from the table and the frame for it 
def cantkt():
    global delete_Entry
    mainframe.destroy()
    deltkt_frame=tk.Frame(root,bg="pink")
    deltkt_frame.place(x=400,y=90,height=400,width=800)

    delete_btn=Label(root,text="Enter your PNR_No to delete yout ticket:",bg="Yellow",fg="Red",font=("Corbert Condessed Italic",18))
    delete_btn.place(x=550,y=200)

    delete_Entry=Entry(root,font=("Corbert Condensed Italic",18),bg="lightgray",)
    delete_Entry.place(x=550,y=250)

    del_btn=Button(root,text="Delete your ticket",bg="red",fg="skyblue",padx=25,pady=25,font=('Helvetica',16),command=deltkt)
    del_btn.place(x=800,y=300)

# The main buttons for the main functions 
book_tkt_btn=Button(mainframe,text="Book your ticket by clicking here !!",font=("Century Gothic",20),fg="Indigo",bg="light green",command=booktkt)
delete_tkt_btn=Button(mainframe,text="Cancel your ticket !!!",font=("Century Gothic",20),fg="Indigo",bg="light green",command=cantkt)

# Placing of the buttons at their respective pixels
book_tkt_btn.place(x=45,y=25)
delete_tkt_btn.place(x=45,y=100)

 


# The Main function the is required to loop the program till the prg ends
root.mainloop()
