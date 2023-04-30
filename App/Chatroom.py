import tkinter as tk
import datetime
import pandas as pd
name_file = "C:/Users/DELL/Desktop/PPS Code projects/Final project/Student interface/names -t.csv"
names_dft = pd.read_csv(name_file, index_col="Sapid")

name_file2 = "C:/Users/DELL/Desktop/PPS Code projects/Final project/Student interface/namesnew.csv"
names_df = pd.read_csv(name_file2, index_col="Roll No.")

class ChatroomWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.config(bg="#0b141a")
        self.root.title("Chatroom")

        # Create chat history text box
        self.chat_history = tk.Text(self.root, state="disabled",font=('Bahnschrift',12),bg="#0b141a",fg="White")
        self.chat_history.pack(side="top", fill="both", expand=True)

        # Create input box
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(side="bottom", fill="x")

        self.input_box = tk.Entry(self.input_frame, font=('Bahnschrift', 12))
        self.input_box.pack(side="left", fill="x", expand=True)
        self.input_box.bind("<Return>", self.send)

        def on_hover(event):
                self.button['background'] = '#0b8e32'
                self.button['foreground'] = 'white'
                
    
            # Function to change button color when not hovering
        def off_hover(event):
                self.button['background'] = '#04e448'
                self.button['foreground'] = 'white'
                

        self.button = tk.Button(self.input_frame, text="↪",font=('Bahnschrift', 12), bg="#04e448", fg="white",borderwidth=0, relief="solid", width=3, height=1,cursor='hand2',command=self.send)
        self.button.pack(side="left")

        self.button.bind("<Enter>",on_hover)
        self.button.bind("<Leave>",off_hover)


        self.chat_log = []  # initialize chat log list

        # Load chat history from file
        try:
            with open("C:/Users/DELL/Desktop/PPS Code projects/Final project/App/chat_history.txt", "r") as file:
                self.chat_log = file.readlines()
                self.chat_history.configure(state="normal")
                for line in self.chat_log:
                    self.chat_history.insert("end", line)
                self.chat_history.configure(state="disabled")
        except FileNotFoundError:
            print("wtf")
            pass

    def send(self, event=None):
        # Get message from input box
        message = self.input_box.get()

        # Create timestamp
        timestamp = datetime.datetime.now().strftime("[%d-%m] (%H:%M)")

        with open("C:/Users/DELL/Desktop/PPS Code projects/Final project/Temp.txt", "r") as file1:
            roll_no=file1.read()

        if roll_no in names_df.index:
             naam=names_df.loc[roll_no, "Name"]
        elif roll_no in names_dft.index:
             naam=names_dft.loc[roll_no, "Name"]

        # Add message to chat history
        self.chat_history.configure(state="normal")
        self.chat_history.insert("end", f"\n{timestamp}: {naam}: {message}")
        self.chat_history.configure(state="disabled")

        def write_to_file(msg):
            with open("C:/Users/DELL/Desktop/PPS Code projects/Final project/App/chat_history.txt", "a") as f:
                f.write(timestamp+": "+naam+": "+ msg + "\n")
        write_to_file(message)


        # Clear input box
        self.input_box.delete(0, "end")

    def run(self):
        self.root.mainloop()

chatroom = ChatroomWindow()

chatroom.run()
