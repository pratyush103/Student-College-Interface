#openai
#gradio
#custom tkinter
#SpeechRecognition
#pyttsx3
#pyaudio
#webbrowser
#threading
'''
Login page using tkinter 
first interface with greeting name based on data base
passing name to functions
each profiles greets with passed name (optional)
multiple profiles chatting with ui made with gradio
'''
'''import tkinter as tk
import gradio as gr

# Define the function that will be called when the button is clicked
def open_gradio_interface():
    # Define your gradio interface here, replacing the placeholders with your actual function, inputs, and outputs
    iface = gr.Interface(fn=my_gradio_function, inputs="my_input", outputs="my_output")
    # Launch the gradio interface
    iface.launch()

def my_gradio_function():
    print("Hello world")
# Create the tkinter window
window = tk.Tk()

# Create the button and add it to the window
button = tk.Button(window, text="Open Gradio Interface", command=open_gradio_interface)
button.pack()

# Start the tkinter event loop
window.mainloop()
'''
#---------------------------------------------------------------
'''
import gradio as gr
import webbrowser
import tkinter as tk
import threading

# Define the Gradio program
def greet(name):
    return "Hello, " + name + "!"

iface = gr.Interface(greet, "text", "text", title="Greeting App", description="Enter your name to get a greeting")

# Define the function that launches the Gradio program in a browser
def launch_gradio():
    def run_gradio():
        iface.launch()

    thread = threading.Thread(target=run_gradio)
    thread.start()
    print("Click")

# Create a Tkinter window with a button
window = tk.Tk()
window.title("Gradio Launcher")
button = tk.Button(window, text="Launch Gradio", command=launch_gradio)
button.pack()

# Start the Tkinter event loop
window.mainloop()
'''
#---------------------------------------------------------------
'''
import tkinter as tk
import gradio as gr
import webbrowser

def say_hello(name):
    return "Hello, " + name + "!"

def open_gradio():
    iface = gr.Interface(fn=say_hello, inputs="text", outputs="text", title="Gradio Hello Program")
    iface.launch(share=True)

root = tk.Tk()
root.title("Open Gradio Hello Program")

button = tk.Button(root, text="Open Gradio", command=open_gradio)
button.pack()

root.mainloop()
'''
'''
#-----------------------------------------------------------------------------------------------------------------
from tkinter import *
from tkinter import messagebox
import ast
#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-Login Database_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
import pandas as pd
# Define file names
password_file = "C:/Users/DELL/Desktop/PPS Code projects/Final project/Student interface/passwords.csv"
name_file = "C:/Users/DELL/Desktop/PPS Code projects/Final project/Student interface/names.csv"

# Load data from files
passwords_df = pd.read_csv(password_file, index_col="Roll No.")
names_df = pd.read_csv(name_file, index_col="Roll No.")

#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-Login Logic_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_

def login():
    roll_no = sapin.get()
    password = pw.get()
    print(roll_no,password)
    # Check if roll no. exists in passwords_df
   
    # Check if roll no. exists in passwords_df
    if roll_no not in passwords_df.index:
        print("Invalid Roll No.")
        messagebox.showerror("Invalid", "Invalid SAP ID entered")
        return

    # Check if password is correct
    if password != str(passwords_df.loc[roll_no, "Password"]):
        print("Invalid Password")
        messagebox.showerror("Invalid", "Invalid password entered")
        return

    # If login successful, print student name
    print("Login Successful. Welcome, ", names_df.loc[roll_no, "Name"])
    messagebox.showinfo("Success!", "Login successful")    
    app()


#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-App_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
def app():
   root.withdraw()
   roll_no = sapin.get()
   app=Toplevel(root)
   app.title("MPSTME Student Interface")
   app.geometry('925x500+300+200')
   app.config(bg="white")
   sapid=sapin.get()
   Label(app,text='Hello '+names_df.loc[roll_no, "Name"], bg='#fff',font=('Bahnschrift',43,'bold')).pack(expand=True)




#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-Login window UI_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
root=Tk()
root. title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root. resizable(False,False)
#Image-----------------------------------

img=PhotoImage(file='C:/Users/DELL/Desktop/PPS Code projects/Final project/Student interface/bbg.png')
Label(root,image=img,bg='white').place(x=0,y=0)
#Login Frame-----------------------------

frame=Frame(root,width=350,height=320,bg="white")
frame.place(x=520,y=100)
#Header Text-----------------------------

head=Label(frame,text='Sign In',fg='#d2232a',bg='white',font=('Bahnschrift',23,'bold'))
head.place(x=125,y=10 )
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
sapin.place(x=30,y=85)
sapin.insert(0,'SapID')
Frame(frame,width=295,height=2,bg='black').place(x=25,y=112)

#Password--------------------------------
def on_submit(e):
    # Execute function when Return key is pressed in the last Entry widget
    print("Function executed!")
    login()
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
pw.place(x=30,y=155)
pw.insert(0,'Password')



Frame(frame,width=295,height=2,bg='black').place(x=25,y=182)

#Buton-----------------------------------

Button(frame,width=39,pady=7,text='Sign in',bg='#d2232a',fg='white',border=0,cursor='hand2',command=login).place(x=35,y=209)

root.mainloop()'''