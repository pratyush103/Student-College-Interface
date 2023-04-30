from tkinter import *
from tkinter import messagebox
import ast

#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-Login Database_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
import pandas as pd
# Define file names
password_file = "C:/Users/DELL/Desktop/PPS Code projects/Final project/Student interface/passwords -t.csv"
name_file = "C:/Users/DELL/Desktop/PPS Code projects/Final project/Student interface/names -t.csv"

# Load data from files
passwords_df = pd.read_csv(password_file, index_col="Sapid")
names_df = pd.read_csv(name_file, index_col="Sapid")

#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-Signup logic_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
import subprocess
def run_script():
    root.withdraw()
    # Replace "other_script.py" with the filename of the other Python script
    subprocess.Popen(["python", "C:/Users/DELL/Desktop/PPS Code projects/Final project/Python Ultimate Student interface.py"])
def signup():
    # Get user input    
    name = n.get()
    Sapid = sapin.get()
    password = pw.get()
    

    # Check if roll_no already exists in the file
    if Sapid in passwords_df.index:
        messagebox.showerror("Invalid", "Account for this SAP ID already exists")
        print("Roll No. already exists. Please try again.")
        return

    # Add new student to dataframes
    passwords_df.loc[Sapid] = password
    names_df.loc[Sapid] = name

    # Save data to files
    passwords_df.to_csv(password_file)
    names_df.to_csv(name_file)

    print("Signup Successful. Welcome, ", name)
    messagebox.showinfo("Account Created", "Now head onto login page to proceed")
    run_script()



root=Tk()
root. title('Teacher Sign Up')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root. resizable(False,False)
#Image-----------------------------------

img=PhotoImage(file='C:/Users/DELL/Desktop/PPS Code projects/Final project/Student interface/bgt.png')
Label(root,image=img,bg='white').place(x=0,y=0)
#Login Frame-----------------------------

frame=Frame(root,width=350,height=350,bg="white")
frame.place(x=520,y=80)
#Header Text-----------------------------

head=Label(frame,text='Sign Up',fg='#23aaf2',bg='white',font=('Bahnschrift',23,'bold'))
head.place(x=125,y=10 )
#Name-------------------------------------
def on_enter(e):
    # Move focus to next Entry widget
    e.widget.tk_focusNext().focus()

def on_focus_in_sap(event):
       n = event.widget
       if n.get() == 'Name':
        n.delete(0, 'end')

def on_focus_out_sap(event):
    sapin=event.widget
    if n.get() =="" :
     n.insert(0, 'Name')
     n.config(show="")

n=Entry(frame, width=25, fg="black", border=0, bg="white", font=('Bahnschrift',12))
n.bind("<FocusIn>", on_focus_in_sap)
n.bind("<FocusOut>", on_focus_out_sap)
n.bind("<Return>", on_enter)
n.place(x=30,y=85)
n.insert(0,'Name')
Frame(frame,width=295,height=2,bg='black').place(x=25,y=112)
#SapID-----------------------------------
def on_enter(e):
    # Move focus to next Entry widget
    e.widget.tk_focusNext().focus()

def on_focus_in_sap(event):
       sapin = event.widget
       if sapin.get() == 'SapID':
        sapin.delete(0, 'end')

def on_focus_out_sap(event):
    pw=event.widget
    if sapin.get() =="" :
     sapin.insert(0, 'SapID')
     sapin.config(show="")

sapin=Entry(frame, width=25, fg="black", border=0, bg="white", font=('Bahnschrift',12))
sapin.bind("<FocusIn>", on_focus_in_sap)
sapin.bind("<FocusOut>", on_focus_out_sap)
sapin.bind("<Return>", on_enter)
sapin.place(x=30,y=155)
sapin.insert(0,'SapID')
Frame(frame,width=295,height=2,bg='black').place(x=25,y=182)

#Password--------------------------------
def on_submit(e):
    # Execute function when Return key is pressed in the last Entry widget
    print("Function executed!")
    signup()
def on_focus_in(event):
       pw = event.widget
       if pw.get() == 'Password':
        pw.delete(0, 'end')
        pw.config(show='*')

def on_focus_out(event):
    pw=event.widget
    if pw.get() =="" :
     pw.insert(0, 'Password')
     pw.config(show="")

pw=Entry(frame, width=25, fg="black", border=0, bg="white", font=('Bahnschrift',12))
pw.bind("<FocusIn>", on_focus_in)
pw.bind("<FocusOut>", on_focus_out)
pw.bind("<Return>", on_submit)
pw.place(x=30,y=225)
pw.insert(0,'Password')



Frame(frame,width=295,height=2,bg='black').place(x=25,y=252)

#Buton-----------------------------------

ab=Button(frame,width=39,pady=7,text='Sign up',bg='#23aaf2',fg='white',border=0,cursor='hand2',command=signup)
ab.place(x=35,y=279)
# Function to change button color on hover
def on_hover(event):
    ab['background'] = '#1b86bf'
    ab['foreground'] = 'white'
    ab['font'] = 'Bahnschrift 9 underline'
    
# Function to change button color when not hovering
def off_hover(event):
    ab['background'] = '#23aaf2'
    ab['foreground'] = 'white'
    ab['font'] = 'Bahnschrift 9'
    

# Bind hover events to button
ab.bind('<Enter>', on_hover)
ab.bind('<Leave>', off_hover)


root.mainloop()
subprocess.Popen(["python", "C:/Users/DELL/Desktop/PPS Code projects/Final project/Python Ultimate Student interface.py"])