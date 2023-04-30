from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt
import subprocess
import webbrowser
from pop import calculate_gpa
from pop import grade
from pop import percent
from tkinter import messagebox
def plot():
    data = pd.read_csv("C:/Users/DELL/Desktop/PPS Code projects/Final project/Student interface/namesnew.csv")
    with open("C:/Users/DELL/Desktop/PPS Code projects/Final project/Temp.txt", "r") as file1:
        roll_no=file1.read()
    student_data = data[data["Roll No."] == roll_no][["LADE","QSP","EOB","PEM"]]
    ax = student_data.plot(kind="bar")
    n=names_df.loc[roll_no,"Name"]
    l=names_df.loc[roll_no,"Last Name"]
    # Set the title and axis labels
    ax.set_title(f"{n} {l} Marks")
    ax.set_xlabel("Subject")
    ax.set_ylabel("Marks")
    ax.set_ylim([0, 50])
    # Display the graph
    plt.show()

#Home frame------------------------------------------------------------------------------------------------------

def create_home_frame(master, go_to_next_frame_func,go_chat_func,im1,im2,plot):
    home_frame = Frame(master, width=925,height=425)
    home_frame.place(x=0,y=75)
    home_frame.config(bg="white")

    def on_hover(event):
        home_button['background'] = '#9f1a1f'
        home_button['foreground'] = 'white'
        home_button['font'] = 'Bahnschrift 9 underline'
    
    # Function to change button color when not hovering
    def off_hover(event):
        home_button['background'] = '#d2232a'
        home_button['foreground'] = 'white'
        home_button['font'] = 'Bahnschrift 9'
        
    def butt():
      go_to_next_frame_func()
      plot()  

    
    home_button = Button(home_frame,width=20,pady=7, text="See Your report",bg='#d2232a',fg='white',border=0,cursor='hand2', command=butt)
    home_button.place(x=160, y=150)

    home_button.bind('<Enter>', on_hover)
    home_button.bind('<Leave>', off_hover)
    
    Label(home_frame,image=im1,bg="white").place(x=180,y=25)
    

    def on_hover2(event):
        home_button2['background'] = '#9f1a1f'
        home_button2['foreground'] = 'white'
        home_button2['font'] = 'Bahnschrift 9 underline'
    
    # Function to change button color when not hovering
    def off_hover2(event):
        home_button2['background'] = '#d2232a'
        home_button2['foreground'] = 'white'
        home_button2['font'] = 'Bahnschrift 9'


    home_button2 = Button(home_frame,width=20,pady=7, text="Chat with Mentors",bg='#d2232a',fg='white',border=0,cursor='hand2', command=go_chat_func)
    home_button2.place(x=390, y=150)
    
    home_button2.bind('<Enter>', on_hover2)
    home_button2.bind('<Leave>', off_hover2)    
    
    
    Label(home_frame,image=im2,bg="white").place(x=410,y=25)

    #notes

    def noteslink():
        webbrowser.open_new("https://drive.google.com/drive/u/1/folders/1Z9lZ-tZjlKEKiKGoHGt6QAx07W5cj1KA")
        

    def on_hover3(event):
        notes['background'] = '#9f1a1f'
        notes['foreground'] = 'white'
        notes['font'] = 'Bahnschrift 9 underline'
    
    # Function to change button color when not hovering
    def off_hover3(event):
        notes['background'] = '#d2232a'
        notes['foreground'] = 'white'
        notes['font'] = 'Bahnschrift 9'


    notes = Button(home_frame,width=20,pady=7, text="Lecture Notes",bg='#d2232a',fg='white',border=0,cursor='hand2', command=noteslink)
    notes.place(x=620, y=150)
    
    notes.bind('<Enter>', on_hover3)
    notes.bind('<Leave>', off_hover3)
    
    Label(home_frame,image=im5,bg="white").place(x=640,y=25) 
    
    #here is time table
    def ttlink():
        webbrowser.open_new("https://cdn.discordapp.com/attachments/1026538138203594793/1100841880075378768/9e4ad7d4-c31d-4b70-b41d-929aa9d0b4d6.png")
        

    def on_hover3(event):
        tt['background'] = '#9f1a1f'
        tt['foreground'] = 'white'
        tt['font'] = 'Bahnschrift 9 underline'
    
    # Function to change button color when not hovering
    def off_hover3(event):
        tt['background'] = '#d2232a'
        tt['foreground'] = 'white'
        tt['font'] = 'Bahnschrift 9'


    tt = Button(home_frame,width=20,pady=7, text="Class Time Table",bg='#d2232a',fg='white',border=0,cursor='hand2', command=ttlink)
    tt.place(x=270, y=350)
    
    tt.bind('<Enter>', on_hover3)
    tt.bind('<Leave>', off_hover3)
    
    Label(home_frame,image=im6,bg="white").place(x=290,y=225) 
    
    #here is handbook

    def hblink():
        webbrowser.open_new("https://svkmmumbai-my.sharepoint.com/personal/kasturi_shirodkar_nmims_edu/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fkasturi%5Fshirodkar%5Fnmims%5Fedu%2FDocuments%2FKasturi%20%2D%20MPSTME%2FStudent%20Information%20Handout%20A%2EY%2E%202022%20%2D23&ga=1")
        

    def on_hover3(event):
        hb['background'] = '#9f1a1f'
        hb['foreground'] = 'white'
        hb['font'] = 'Bahnschrift 9 underline'
    
    # Function to change button color when not hovering
    def off_hover3(event):
        hb['background'] = '#d2232a'
        hb['foreground'] = 'white'
        hb['font'] = 'Bahnschrift 9'


    hb = Button(home_frame,width=20,pady=7, text="Student Handbook",bg='#d2232a',fg='white',border=0,cursor='hand2', command=hblink)
    hb.place(x=510, y=350)
    
    hb.bind('<Enter>', on_hover3)
    hb.bind('<Leave>', off_hover3)
    
    Label(home_frame,image=im7,bg="white").place(x=530,y=225)        
    
    return home_frame

#second_frame------------------------------------------------------------------------

def create_second_frame(master, go_back_func,marks):

    
    second_frame = Frame(master, width=925,height=425)
    second_frame.config(bg="white")

    def on_hover(event):
        back_button['background'] = '#9f1a1f'
        back_button['foreground'] = 'white'
        back_button['font'] = 'Bahnschrift 12 bold'
    
    # Function to change button color when not hovering
    def off_hover(event):
        back_button['background'] = '#d2232a'
        back_button['foreground'] = 'white'
        back_button['font'] = 'Bahnschrift 12'
    
    back_button = Button(second_frame,padx=3,pady=1, text="<",font='Bahnschrift 12',bg='#d2232a',fg='white',border=0,cursor='hand2', command=go_back_func)
    back_button.place(x=1, y=1)

    back_button.bind('<Enter>', on_hover)
    back_button.bind('<Leave>', off_hover)
    Label(second_frame,text="Your Report Card ",fg='#d2232a',bg='white',font=('Bahnschrift',23,'bold')).place(x=350,y=40)
    Label(second_frame,text="LADE: "+str(marks[0]),bg='white',font=('Bahnschrift',15) ).place(x=350,y=80)
    Label(second_frame,text="QSP: "+str(marks[1]),bg='white',font=('Bahnschrift',15) ).place(x=350,y=120)
    Label(second_frame,text="EOB: "+str(marks[2]),bg='white',font=('Bahnschrift',15) ).place(x=350,y=160)
    Label(second_frame,text="PEM: "+str(marks[3]),bg='white',font=('Bahnschrift',15)).place(x=350,y=200)

    perc=percent(marks[0],marks[1],marks[2],marks[3])
    Label(second_frame,text="Percentage: "+perc,bg='white',font=('Bahnschrift',15)).place(x=350,y=240)

    gpa=calculate_gpa(marks[0],marks[1],marks[2],marks[3])
    g=str(gpa)
    Label(second_frame,text="Your GPA: "+g,bg='white',font=('Bahnschrift',15)).place(x=350,y=280)

    grd= grade(gpa)
    gg= Label(second_frame,text="Grade: "+grd,bg='white',font=('Bahnschrift',15))
    gg.place(x=500,y=280)
    if grd == "F" or grd == "D-" or grd == "D" or grd == "D+":
        gg['fg'] = '#d2232a'
    else:
        gg['fg'] = '#04e448'
    
    
    return second_frame

def go_back(second_frame, home_frame):
    second_frame.place_forget()
    home_frame.place(x=0,y=75)
def go_to_next_frame(home_frame, second_frame):
    home_frame.place_forget()
    second_frame.place(x=0,y=75)


#frame3------------------------------------------------------------------------------

def create_frame3(master, go_back_home_func):
    frame3 = Frame(master, width=925,height=425)
    frame3.config(bg="white")
    
    def on_hover(event):
        back_button['background'] = '#9f1a1f'
        back_button['foreground'] = 'white'
        back_button['font'] = 'Bahnschrift 12 bold'
    
    # Function to change button color when not hovering
    def off_hover(event):
        back_button['background'] = '#d2232a'
        back_button['foreground'] = 'white'
        back_button['font'] = 'Bahnschrift 12'

    back_button = Button(frame3,padx=3,pady=1, text="<",font='Bahnschrift 12',bg='#d2232a',fg='white',border=0,cursor='hand2', command=go_back_home_func)
    back_button.place(x=1, y=1)

    back_button.bind('<Enter>', on_hover)
    back_button.bind('<Leave>', off_hover)


    Label(frame3,image=im3,bg="white").place(x=250,y=100)

    def on_hoverl(event):
        launche['background'] = '#9f1a1f'
        launche['foreground'] = 'white'
        launche['font'] = 'Bahnschrift 9 underline'
    
    # Function to change button color when not hovering
    def off_hoverl(event):
        launche['background'] = '#d2232a'
        launche['foreground'] = 'white'
        launche['font'] = 'Bahnschrift 9'

    def on_hover2(event):
        start['background'] = '#9f1a1f'
        start['foreground'] = 'white'
        start['font'] = 'Bahnschrift 9 underline'
    
    # Function to change button color when not hovering
    def off_hover2(event):
        start['background'] = '#d2232a'
        start['foreground'] = 'white'
        start['font'] = 'Bahnschrift 9'
    

    def startchat():
        webbrowser.open_new("http://127.0.0.1:7860/")
    start = Button(frame3,width=20,pady=7, text="Start Chatting",bg='#d2232a',fg='white',border=0,cursor='hand2', command=startchat)
    start.bind('<Enter>', on_hover2)
    start.bind('<Leave>', off_hover2)



    def host():
        import time
        launche['text']="Hosting..."
        subprocess.Popen(["python", "C:/Users/DELL/Desktop/PPS Code projects/Final project/Chat/API Test.py"])
        time.sleep(10)
        launche.place_forget()
        start.place(x=230, y=225)
        

    launche = Button(frame3,width=20,pady=7, text="Chat with Mentors",bg='#d2232a',fg='white',border=0,cursor='hand2', command=host)
    launche.place(x=230, y=225)
    launche.bind('<Enter>', on_hoverl)
    launche.bind('<Leave>', off_hoverl)

    Label(frame3,image=im4,bg="white").place(x=585,y=100)

    def chatter():
        subprocess.Popen(["python", "C:/Users/DELL/Desktop/PPS Code projects/Final project/App/Chatroom.py"])

    def on_hoverl(event):
        talk['background'] = '#9f1a1f'
        talk['foreground'] = 'white'
        talk['font'] = 'Bahnschrift 9 underline'
    
    # Function to change button color when not hovering
    def off_hoverl(event):
        talk['background'] = '#d2232a'
        talk['foreground'] = 'white'
        talk['font'] = 'Bahnschrift 9'

    talk = Button(frame3,width=20,pady=7, text="Chat with others",bg='#d2232a',fg='white',border=0,cursor='hand2', command=chatter)
    talk.place(x=580, y=225)
    talk.bind('<Enter>', on_hoverl)
    talk.bind('<Leave>', off_hoverl)


    return frame3

def go_back_home(frame3, home_frame):
    frame3.place_forget()
    home_frame.place(x=0,y=75)

def go_chat(home_frame, frame3):
    home_frame.place_forget()
    frame3.place(x=0,y=75)

#Database load----------------------------------------------

# Define file names
password_file = "C:/Users/DELL/Desktop/PPS Code projects/Final project/Student interface/passwordsnew.csv"
name_file = "C:/Users/DELL/Desktop/PPS Code projects/Final project/Student interface/namesnew.csv"

# Load data from files
passwords_df = pd.read_csv(password_file, index_col="Roll No.")
names_df = pd.read_csv(name_file, index_col="Roll No.")
with open("C:/Users/DELL/Desktop/PPS Code projects/Final project/Temp.txt", "r") as file1:
    roll_no=file1.read()

marks=(names_df.loc[roll_no,"LADE"],names_df.loc[roll_no,"QSP"],names_df.loc[roll_no,"EOB"],names_df.loc[roll_no,"PEM"])
#Top bar Content------------------------------
import datetime

# Get the current time
now = datetime.datetime.now()

# Determine the greeting based on the time of day
if now.hour < 12:
    greeting = "Good morning, "
elif now.hour < 18:
    greeting = "Good afternoon, "
else:
    greeting = "Good evening, "

# Print the greeting
print(greeting)


app=Tk()
app.title("MPSTME Student Interface")
app.geometry('925x500+300+200')
app.resizable(False,False)

hi=Label(app,text=greeting+names_df.loc[roll_no, "Name"]+' '+names_df.loc[roll_no, "Last Name"],font=('Bahnschrift',20,'bold'))
hi.place(x=300,y=20)
img=PhotoImage(file='C:/Users/DELL/Desktop/PPS Code projects/Final project/App/log.png')
Label(app,image=img).place(x=25,y=10)


im1=PhotoImage(file='C:/Users/DELL/Desktop/PPS Code projects/Final project/App/report.png')
im2=PhotoImage(file='C:/Users/DELL/Desktop/PPS Code projects/Final project/App/speech.png')
im3=PhotoImage(file='C:/Users/DELL/Desktop/PPS Code projects/Final project/App/question.png')
im4=PhotoImage(file='C:/Users/DELL/Desktop/PPS Code projects/Final project/App/stuchat.png')
im5=PhotoImage(file='C:/Users/DELL/Desktop/PPS Code projects/Final project/App/books.png')
im6=PhotoImage(file='C:/Users/DELL/Desktop/PPS Code projects/Final project/App/timetable.png')
im7=PhotoImage(file='C:/Users/DELL/Desktop/PPS Code projects/Final project/App/information.png')
def create_marquee(window, text, width=400):
    # Define the marquee label
    marquee_label = Label(window, text=text,fg="#d2232a", font=('Bahnschrift', 8))
    marquee_label.pack(side=LEFT)

    # Define the marquee scrolling function
    def scroll_marquee():
        # Get the current position of the marquee label
        x, y = marquee_label.winfo_x(), marquee_label.winfo_y()
        
        # Check if the label is out of bounds
        if x < -marquee_label.winfo_width():
            x = window.winfo_width()

        # Move the label to the left
        marquee_label.place(x=x-width, y=57)
        marquee_label.after(120, scroll_marquee)

    # Start scrolling the marquee
    scroll_marquee()
with open("C:/Users/DELL/Desktop/PPS Code projects/Final project/App/Mar.txt", "r") as file1:
        txt=file1.read()



# Create the marquee
create_marquee(app,txt, 30)
home_frame = create_home_frame(app, lambda: go_to_next_frame(home_frame, second_frame),lambda:go_chat(home_frame, frame3),im1,im2,lambda:plot())
second_frame = create_second_frame(app, lambda: go_back(second_frame, home_frame),marks)
frame3= create_frame3(app,lambda:go_back_home(frame3, home_frame))

logs=open('C:/Users/DELL/Desktop/PPS Code projects/Final project/his.txt','a+')
now=datetime.datetime.now()
print(now)
logentry=str(now)+" Student: "+str(roll_no)+" has logged in\n"
print(logentry)
logs.write(logentry)
logs.close()

time=str(now)
role="Student"
activity="logged in"
logfile='C:/Users/DELL/Desktop/PPS Code projects/Final project/logs.csv'
log_df=pd.read_csv(logfile,index_col="Time")
log_df.loc[time]=[roll_no,role,activity]
log_df.to_csv(logfile)



def on_hover2(event):
    logout['background'] = '#9f1a1f'
    logout['foreground'] = 'white'
    logout['font'] = 'Bahnschrift 9 underline'
    
    # Function to change button color when not hovering
def off_hover2(event):
    logout['background'] = '#d2232a'
    logout['foreground'] = 'white'
    logout['font'] = 'Bahnschrift 9'

def loglogout():
    time=str(now)
    role="Student"
    activity="logged out"
    log_df.loc[time]=[roll_no,role,activity]
    log_df.to_csv(logfile)
    
    messagebox.showinfo("Logged out","Logged out successfully")
    app.withdraw()

    
    subprocess.Popen(["python", "C:/Users/DELL/Desktop/PPS Code projects/Final project/Python Ultimate Student interface.py"])
    

logout = Button(app,width=10,pady=2, text="Logout",bg='#d2232a',fg='white',border=0,cursor='hand2', command=loglogout)
logout.place(x=860, y=20)
    
logout.bind('<Enter>', on_hover2)
logout.bind('<Leave>', off_hover2)


app.mainloop()
subprocess.Popen(["python", "C:/Users/DELL/Desktop/PPS Code projects/Final project/Python Ultimate Student interface.py"])
