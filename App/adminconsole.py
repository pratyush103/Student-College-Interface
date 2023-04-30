import tkinter as tk
import subprocess

# Define the colors
bg_color = "#36393F"
button_bg_off = "#5865f2"
button_bg_on = "#4752c4"
button_fg = "white"

def studata():
    subprocess.call(['start', '', "C:/Users/DELL/Desktop/PPS Code projects/Final project/Student interface/namesnew.csv"], shell=True)

def studatapass():
    subprocess.call(['start', '', "C:/Users/DELL/Desktop/PPS Code projects/Final project/Student interface/passwordsnew.csv"], shell=True)

def teadata():
    subprocess.call(['start', '', "C:/Users/DELL/Desktop/PPS Code projects/Final project/Student interface/names -t.csv"], shell=True)

def teadatapass():
    subprocess.call(['start', '', "C:/Users/DELL/Desktop/PPS Code projects/Final project/Student interface/passwords -t.csv"], shell=True)

def useract():
    subprocess.call(['start', '', "C:/Users/DELL/Desktop/PPS Code projects/Final project/logs.csv"], shell=True)

def chistory():
    subprocess.call(['start', '', "C:/Users/DELL/Desktop/PPS Code projects/Final project/App/chat_history.txt"], shell=True)


# Define the functions for button events
def on_hover(event):
    event.widget.config(bg=button_bg_on)

def off_hover(event):
    event.widget.config(bg=button_bg_off)

# Create the tkinter window
root = tk.Tk()
root.title("Admin Console")
root.config(bg=bg_color)
root.geometry("+560+240")

frm=tk.Frame(root,bg="#2b2d31")

# Create the buttons
button1 = tk.Button(root,pady=5, text="Open Student Data", bg=button_bg_off, fg=button_fg,border=0,cursor='hand2',command=studata)
button1.bind("<Enter>", on_hover)
button1.bind("<Leave>", off_hover)

button2 = tk.Button(root,pady=1, text="Open Student Login Data", bg=button_bg_off, fg=button_fg,border=0,cursor='hand2',command=studatapass)
button2.bind("<Enter>", on_hover)
button2.bind("<Leave>", off_hover)

button3 = tk.Button(root,pady=5, text="Open Teacher Data", bg=button_bg_off, fg=button_fg,border=0,cursor='hand2',command=teadata)
button3.bind("<Enter>", on_hover)
button3.bind("<Leave>", off_hover)

button4 = tk.Button(root,pady=5, text="Open Teacher Login Data", bg=button_bg_off, fg=button_fg,border=0,cursor='hand2',command=teadatapass)
button4.bind("<Enter>", on_hover)
button4.bind("<Leave>", off_hover)

button5 = tk.Button(root,pady=5, text="Open User activity logs", bg=button_bg_off, fg=button_fg,border=0,cursor='hand2',command=useract)
button5.bind("<Enter>", on_hover)
button5.bind("<Leave>", off_hover)

button6 = tk.Button(root,pady=5, text="Open Chatroom History", bg=button_bg_off, fg=button_fg,border=0,cursor='hand2',command=chistory)
button6.bind("<Enter>", on_hover)
button6.bind("<Leave>", off_hover)

im=tk.PhotoImage(file="C:/Users/DELL/Desktop/PPS Code projects/Final project/App/Admin.png")
labl=tk.Label(image=im,bg="#36393F")
labl.grid(row=0, column=0, pady=10)

Head=tk.Label(text="Admin Console",bg="#36393F",fg="white", font=('Bauhaus 93',20))
Head.grid(row=0, column=1, pady=10)

# Display the buttons in the window
button1.grid(row=1, column=0, padx=10, pady=10,sticky=tk.N+tk.S+tk.E+tk.W)
button2.grid(row=1, column=1, padx=10,pady=10,sticky=tk.N+tk.S+tk.E+tk.W)
button3.grid(row=2, column=0, padx=10, pady=10,sticky=tk.N+tk.S+tk.E+tk.W)
button4.grid(row=2, column=1, padx=10,pady=10,sticky=tk.N+tk.S+tk.E+tk.W)
button5.grid(row=3, column=0, padx=10, pady=10,sticky=tk.N+tk.S+tk.E+tk.W)
button6.grid(row=3, column=1, padx=10,pady=10,sticky=tk.N+tk.S+tk.E+tk.W)

# Run the tkinter event loop
root.mainloop()
subprocess.Popen(["python", "C:/Users/DELL/Desktop/PPS Code projects/Final project/Python Ultimate Student interface.py"])