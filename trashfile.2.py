import tkinter as tk
import subprocess

def run_script():
    # Replace "other_script.py" with the filename of the other Python script
    subprocess.Popen(["python", "C:/Users/DELL/Desktop/PPS Code projects/Final project/Python Ultimate Student interface.py"])

root = tk.Tk()

# Create a button with text "Run Script" and bind it to the run_script function
ab=tk.Button(root,width=39,pady=7,text='Open Programs',bg='#23aaf2',fg='white',border=0,cursor='hand2',command=run_script)
ab.pack(padx=5,pady=10)
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
# import_variable.py


root.mainloop()



