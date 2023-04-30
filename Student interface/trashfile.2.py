import tkinter as tk
import subprocess

def run_script():
    # Replace "other_script.py" with the filename of the other Python script
    subprocess.Popen(["python", "C:/Users/DELL/Desktop/PPS Code projects/Final project/Python Ultimate Student interface.py"])

root = tk.Tk()

# Create a button with text "Run Script" and bind it to the run_script function
btn = tk.Button(root, text="Run Script", command=run_script)
btn.pack()

root.mainloop()
