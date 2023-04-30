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
#-----------------------------------------------------------------------------------------------------------------
from tkinter import *
from tkinter import messagebox
import ast
import datetime
#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-Login Database_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
import pandas as pd
# Define file names
password_file = "C:/Users/DELL/Desktop/PPS Code projects/Final project/Student interface/passwordsnew.csv"
name_file = "C:/Users/DELL/Desktop/PPS Code projects/Final project/Student interface/namesnew.csv"

# Load data from files
passwords_df = pd.read_csv(password_file, index_col="Roll No.")
names_df = pd.read_csv(name_file, index_col="Roll No.")

# Define file names
password_file = "C:/Users/DELL/Desktop/PPS Code projects/Final project/Student interface/passwords -t.csv"
name_file = "C:/Users/DELL/Desktop/PPS Code projects/Final project/Student interface/names -t.csv"

# Load data from files
passwords_dft = pd.read_csv(password_file, index_col="Sapid")
names_dft = pd.read_csv(name_file, index_col="Sapid")

#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-Login Logic_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
def teacherlog():
    Sapid = sapin.get()
    password = pw.get()

    # Check if password is correct
    if password != str(passwords_dft.loc[Sapid, "Password"]):
        print("Invalid Password")
        messagebox.showerror("Invalid", "Invalid password entered")
        return
    

    # If login successful, print student name-----------------------------
    print("Login Successful. Welcome, ", names_dft.loc[Sapid, "Name"])
    messagebox.showinfo("Success!", "Login successful")
    f=open('C:/Users/DELL/Desktop/PPS Code projects/Final project/Temp.txt','w+')
    f.write(Sapid)
    f.close()

    
    appt()


def login():
    roll_no = sapin.get()
    password = pw.get()
    print(roll_no,password)
    # Check if roll no. exists in passwords_df
    
    if roll_no=="admin" and password=="admin123":
        root.withdraw()
        subprocess.Popen(["python", "C:/Users/DELL/Desktop/PPS Code projects/Final project/App/adminconsole.py"])
    
    elif roll_no in passwords_dft.index:
        teacherlog()
    # Check if roll no. exists in passwords_df
    elif roll_no not in passwords_df.index and roll_no not in passwords_dft.index:
        print("Invalid Roll No.")
        messagebox.showerror("Invalid", "Invalid SAP ID entered")
        return
    

    

    # Check if password is correct
    elif password != str(passwords_df.loc[roll_no, "Password"]):
        print("Invalid Password")
        messagebox.showerror("Invalid", "Invalid password entered")
        return
    

    # If login successful, print student name-----------------------------
    print("Login Successful. Welcome, ", names_df.loc[roll_no, "Name"])
    messagebox.showinfo("Success!", "Login successful")
    f=open('C:/Users/DELL/Desktop/PPS Code projects/Final project/Temp.txt','w+')
    f.write(roll_no)
    f.close()

    app()
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-Signup Query_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
import subprocess

def run_script(): 
       
    root.withdraw()

    # Replace "other_script.py" with the filename of the other Python script
    subprocess.Popen(["python", "C:/Users/DELL/Desktop/PPS Code projects/Final project/Signup window/Signup_stu.py"])

#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-Admin Authenticate_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
def run_scriptt(): 
       
    root.withdraw()

    # Replace "other_script.py" with the filename of the other Python script
    subprocess.Popen(["python", "C:/Users/DELL/Desktop/PPS Code projects/Final project/Signup window/Signup_tea.py"])

def login_prompt():
    # Create the login window
    login_window = Tk()
    login_window.title("Admin Authorization")
    login_window.geometry("+600+400")
    login_window.config(bg="white")
    login_window. resizable(False,False)
    
    h=Label(login_window,text='Authenticate',fg='#d2232a',bg='white',font=('Bahnschrift',19,'bold'))
    h.grid(row=0, column=0, padx=0, pady=10)
    def on_entry(e):
        # Move focus to next Entry widget
        e.widget.tk_focusNext().focus()

    def on_focus(event):
           username_entry = event.widget
           if username_entry.get() == 'Username':
            username_entry.delete(0, 'end')

    def on_focus_o(event):
        password_entry=event.widget
        if username_entry.get() =="" :
         username_entry.insert(0, 'Username')
         username_entry.config(show="")

    # Create the username and password labels and entry fields
    username_entry = Entry(login_window,width=25, fg="black", border=0, bg="white", font=('Bahnschrift',10))
    username_entry.grid(row=1, column=0, padx=10, pady=0)
    username_entry.bind("<FocusIn>", on_focus)
    username_entry.bind("<FocusOut>", on_focus_o)
    username_entry.bind("<Return>", on_entry)
    username_entry.insert(0,'Username')
    Frame(login_window,width=200,height=2,bg='black').grid(row=2, column=0, padx=5, pady=0)
    def on_enter(e):
        # Execute function when Return key is pressed in the last Entry widget
        print("Function executed!")
        submit_login()

    def onto_focus(event):
           pw = event.widget
           if pw.get() == 'Password':
            pw.delete(0, 'end')
            pw.config(show='*')

    def out_focus(event):
        pw=event.widget
        if pw.get() =="" :
         pw.insert(0, 'Password')
         pw.config(show="")
    
    Frame(login_window,width=200,height=2,bg='white').grid(row=3, column=0, padx=5, pady=10)


    password_entry = Entry(login_window, width=25, fg="black", border=0, bg="white", font=('Bahnschrift',10))
    password_entry.grid(row=4, column=0, padx=0, pady=0)
    password_entry.insert(0,'Password')
    password_entry.bind("<FocusIn>", onto_focus)
    password_entry.bind("<FocusOut>", out_focus)
    password_entry.bind("<Return>", on_enter)    
    Frame(login_window,width=200,height=2,bg='black').grid(row=5, column=0, padx=5, pady=0)

   

    # Create the submit button
    def submit_login():
        username = username_entry.get()
        password = password_entry.get()

        if username == "admin" and password == "admin123":
            print("Login successful!")
            messagebox.showinfo("Authorized", "Authentication Successful")
            login_window.destroy()
            run_scriptt()
        else:
            messagebox.showerror("Unauthorized", "Authentication Failed")
            print("Authentication Failed")
            return

    

    submit_button = Button(login_window,width=29,pady=7,text='Authorize',bg='#d2232a',fg='white',border=0,cursor='hand2', command=submit_login)
    submit_button.grid(row=6, column=0, columnspan=2, padx=5, pady=10)
    
    # Function to change button color on hover
    def on_hover(event):
        submit_button['background'] = '#9f1a1f'
        submit_button['foreground'] = 'white'
        submit_button['font'] = 'Bahnschrift 9 underline'
    
    # Function to change button color when not hovering
    def off_hover(event):
        submit_button['background'] = '#d2232a'
        submit_button['foreground'] = 'white'
        submit_button['font'] = 'Bahnschrift 9'
    

    # Bind hover events to button
    submit_button.bind('<Enter>', on_hover)
    submit_button.bind('<Leave>', off_hover)

    # Run the login window
    login_window.mainloop()

'''def open_window():
    # Create a new window
    new_window = Toplevel(root)
    new_window.config(bg='white')    
        
    # Create label and buttons
    label = Label(new_window,text='Are you a',fg='#d2232a',bg='white',font=('Bahnschrift',13,'bold'))
    label.pack(padx=10, pady=5)

    a1=Button(new_window,width=29,pady=7,text='Teacher',bg='#d2232a',fg='white',border=0,cursor='hand2')
    a1.pack(padx=5,pady=10)
    # Function to change button color on hover
    def on_hover(event):
        a1['background'] = '#9f1a1f'
        a1['foreground'] = 'white'
        a1['font'] = 'Bahnschrift 9 underline'
    
    # Function to change button color when not hovering
    def off_hover(event):
        a1['background'] = '#d2232a'
        a1['foreground'] = 'white'
        a1['font'] = 'Bahnschrift 9'
    

    # Bind hover events to button
    a1.bind('<Enter>', on_hover)
    a1.bind('<Leave>', off_hover)

    label = Label(new_window, text="OR",bg="white")
    label.pack(padx=10, pady=5)
    
    #Close query window---------------------------------

    def close_window():
        new_window.withdraw()    

    a2=Button(new_window,width=29,pady=7,text='Student',bg='#d2232a',fg='white',border=0,cursor='hand2',command=run_script)
    a2.config(command=lambda: (close_window(), run_script()))
    a2.pack(padx=5,pady=10)
    # Function to change button color on hover
    def on_hover(event):
        a2['background'] = '#9f1a1f'
        a2['foreground'] = 'white'
        a2['font'] = 'Bahnschrift 9 underline'
    
    # Function to change button color when not hovering
    def off_hover(event):
        a2['background'] = '#d2232a'
        a2['foreground'] = 'white'
        a2['font'] = 'Bahnschrift 9'
    

    # Bind hover events to button
    a2.bind('<Enter>', on_hover)
    a2.bind('<Leave>', off_hover)'''

def open_window():
    
    frme=Frame(root,width=350,height=320,bg="white")
    frme.place(x=560,y=180)     
    

    
    
    # Create label and buttons
    label = Label(frme,text='Are you a',fg='#d2232a',bg='white',font=('Bahnschrift',13,'bold'))
    label.pack(padx=10, pady=5)

    a1=Button(frme,width=29,pady=7,text='Teacher',bg='#d2232a',fg='white',border=0,cursor='hand2',command=login_prompt)
    a1.pack(padx=5,pady=10)
    # Function to change button color on hover
    def on_hover(event):
        a1['background'] = '#9f1a1f'
        a1['foreground'] = 'white'
        a1['font'] = 'Bahnschrift 9 underline'
    
    # Function to change button color when not hovering
    def off_hover(event):
        a1['background'] = '#d2232a'
        a1['foreground'] = 'white'
        a1['font'] = 'Bahnschrift 9'
    

    # Bind hover events to button
    a1.bind('<Enter>', on_hover)
    a1.bind('<Leave>', off_hover)

    
    label2 = Label(frame, text="",bg="#5a5d5d",font=('Bahnschrift',1))
    label2.pack(padx=0, pady=0)

    label = Label(frme, text="OR",bg="white")
    label.pack(padx=10, pady=5)
    
    #Close query window---------------------------------

    def close_window():
        root.withdraw()    

    a2=Button(frme,width=29,pady=7,text='Student',bg='#d2232a',fg='white',border=0,cursor='hand2',command=run_script)
    a2.config(command=lambda: (close_window(), run_script()))
    a2.pack(padx=5,pady=10)

    # Function to change button color on hover
    def on_hover(event):
        a2['background'] = '#9f1a1f'
        a2['foreground'] = 'white'
        a2['font'] = 'Bahnschrift 9 underline'
    
    # Function to change button color when not hovering
    def off_hover(event):
        a2['background'] = '#d2232a'
        a2['foreground'] = 'white'
        a2['font'] = 'Bahnschrift 9'
    

    # Bind hover events to button
    a2.bind('<Enter>', on_hover)
    a2.bind('<Leave>', off_hover)
    
    
    
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-App_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
'''def app():
   root.withdraw()
   roll_no = sapin.get()
   app=Toplevel(root)
   app.title("MPSTME Student Interface")
   app.geometry('925x500+300+200')
   app.config(bg="white")
   sapid=sapin.get()
   Label(app,text='Hello '+names_df.loc[roll_no, "Name"], bg='#fff',font=('Bahnschrift',43,'bold')).pack(expand=True)'''

def app():     
       
    root.withdraw()

    # Replace "other_script.py" with the filename of the other Python script
    subprocess.Popen(["python", "C:/Users/DELL/Desktop/PPS Code projects/Final project/App/App_Stu.py"])

def appt():     
       
    root.withdraw()

    # Replace "other_script.py" with the filename of the other Python script
    subprocess.Popen(["python", "C:/Users/DELL/Desktop/PPS Code projects/Final project/App/App_Tea.py"])


#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-Login window UI_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
root=Tk()
root. title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root. resizable(False,False)
#Image-----------------------------------

img=PhotoImage(file='C:/Users/DELL/Desktop/PPS Code projects/Final project/Student interface/bg login.png')
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

ab=Button(frame,width=39,pady=7,text='Sign in',bg='#d2232a',fg='white',border=0,cursor='hand2',command=login)
ab.place(x=35,y=209)
# Function to change button color on hover
def on_hover(event):
    ab['background'] = '#9f1a1f'
    ab['foreground'] = 'white'
    ab['font'] = 'Bahnschrift 9 underline'
    
# Function to change button color when not hovering
def off_hover(event):
    ab['background'] = '#d2232a'
    ab['foreground'] = 'white'
    ab['font'] = 'Bahnschrift 9'
    

# Bind hover events to button
ab.bind('<Enter>', on_hover)
ab.bind('<Leave>', off_hover)
#Signup----------------------------------

# Create the hyperlink text
# Create the hyperlink-like label

def on_enter(e):
    text.config(font=("Bahnschrift Underline", 10, "underline"), fg="#85161a")

def on_leave(e):
    text.config(font=("Bahnschrift Underline", 10), fg="#d2232a")

text = Label(frame, text="Signup for a new account", font=("Bahnschrift Underline", 10), height=1, cursor="hand2", fg="#d2232a",bg="white")
text.place(x=25, y=260)

# Bind the hyperlink text to open a new window when clicked
text.bind("<Enter>", on_enter)
text.bind("<Leave>", on_leave)
text.bind("<Button-1>", lambda event: open_window())


root.mainloop()
