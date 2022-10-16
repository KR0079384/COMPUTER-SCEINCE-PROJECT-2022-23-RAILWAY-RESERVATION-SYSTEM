from re import T
from tkinter import *
import tkinter as tk
import mysql.connector as myc 
from tkinter import messagebox
import random

root =tk.Tk()
root.title("RAILWAY MANAGEMENT SYSTEM")
root.iconbitmap("C:\Python\Computer Science project RAILWAY MANAGEMENT SYSTEM 2022-23\icon.ico")
root.config(bg="green")
root.geometry("1000x1000")

mainframe=Frame(root,bg="gray")
mainframe.place(x=375,y=85,height=350,width=600)



#variables to store the data entered in textbox


def deltkt():
    tkt_del=delete_Entry.get()
    con=myc.connect(user="root",host="localhost",password="KR007@12345",database="irctc")
    cur=con.cursor()
    cur.execute(f"delete from train where PNR_No = '{tkt_del}'")
    print(cur.fetchall())
    con.commit()

    delete_Entry.delete("0","end")

    messagebox.showwarning("Deleted","Your ticket has been successfully deleted!!")

def booktkt1():
    if Name_entry.get()=="" or Source_entry.get()=="" or destin_entry.get()=="" or namep_entry.get()=="" or gender_entry.get()=="":
        messagebox.showerror("Error","All fields are required")
    else:
        con=myc.connect(user="root",host="localhost",password="KR007@12345",database="irctc")
        cur=con.cursor()
        tkt_1=str(r)
        name=Name_entry.get()
        source=Source_entry.get()
        destin=destin_entry.get()
        namep=namep_entry.get()
        gen=gender_entry.get()
         
        cur.execute(f"INSERT INTO train values('{tkt_1}','{name}','{source}','{destin}','{namep}','{gen}')")
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
        Name_entry.delete("0","end")
        destin_entry.delete("0","end")
        namep_entry.delete("0","end")
        gender_entry.delete("0","end")

        messagebox.showinfo("Done!!","Your ticket has been successfully saved to the database")

def booktkt():
    global r 
    con=myc.connect(user="root",host="localhost",password="KR007@12345",database="irctc")
    cur=con.cursor()
    cur.execute("create table if not exists train(PNR_No varchar(30),Train_name varchar(50),Source varchar(30),destination varchar(30),name_of_passenger varchar(30),gender char (1))")
    con.commit()

    global tkt_entry,Name_entry,Source_entry,destin_entry,namep_entry,gender_entry,tkt_PNR_Lab
    
    mainframe.destroy()
    booktkt_frame=tk.Frame(root,bg="orange")
    booktkt_frame.place(x=450,y=90,width=700,height=500)
    
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
    
    Name_entry=Entry(root,font=("Corbert Condensed Italic",16),bg="lightgray")
    Name_entry.place(x=800,y=240)

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
    input_btn.place(x=900,y=500)


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

    


book_tkt_btn=Button(mainframe,text="Book your ticket by clicking here !!",font=("Century Gothic",20),fg="red",bg="black",command=booktkt)

delete_tkt_btn=Button(mainframe,text="Cancel your ticket !!!",font=("Century Gothic",20),fg="red",bg="black",command=cantkt)

book_tkt_btn.place(x=45,y=25)
delete_tkt_btn.place(x=45,y=100)

 


 

root.mainloop()

