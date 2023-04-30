from tkinter import *
from tkinter import messagebox
import ast
import subprocess
from pop import calculate_gpa
from pop import percent
from pop import grade
#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-Login Database_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
import pandas as pd
import csv

#Home frame------------------------------------------------------------------------------------------------------

def create_home_frame(master, go_to_next_frame_func,go_chat_func,im1,im2):
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

    
    home_button = Button(home_frame,width=20,pady=7, text="View Student Data",bg='#d2232a',fg='white',border=0,cursor='hand2', command=butt)
    home_button.place(x=230, y=225)

    home_button.bind('<Enter>', on_hover)
    home_button.bind('<Leave>', off_hover)
    

    

    def on_hover2(event):
        home_button2['background'] = '#9f1a1f'
        home_button2['foreground'] = 'white'
        home_button2['font'] = 'Bahnschrift 9 underline'
    
    # Function to change button color when not hovering
    def off_hover2(event):
        home_button2['background'] = '#d2232a'
        home_button2['foreground'] = 'white'
        home_button2['font'] = 'Bahnschrift 9'


    home_button2 = Button(home_frame,width=20,pady=7, text="Update Noticeboard",bg='#d2232a',fg='white',border=0,cursor='hand2', command=go_chat_func)
    home_button2.place(x=570, y=225)
    
    home_button2.bind('<Enter>', on_hover2)
    home_button2.bind('<Leave>', off_hover2)
    
    Label(home_frame,image=im1,bg="white").place(x=250,y=100)
    
    Label(home_frame,image=im2,bg="white").place(x=600,y=100)

    def openchat():        
        subprocess.Popen(["python", "C:/Users/DELL/Desktop/PPS Code projects/Final project/App/Chatroom.py"])

    def on_hover(event):
        chatr['image'] = chatroom2
    
    # Function to change button color when not hovering
    def off_hover(event):
        chatr['image'] = chatroom1
        
    def butt():
      go_to_next_frame_func()  

    
    chatr = Button(home_frame,border=0,bg="white",image=chatroom1,cursor='hand2', command=openchat)
    chatr.place(x=850, y=350)

    chatr.bind('<Enter>', on_hover)
    chatr.bind('<Leave>', off_hover)
    
    return home_frame

#second_frame------------------------------------------------------------------------

def create_second_frame(master, go_back_func):
    second_frame = Frame(master, width=925,height=425)
    second_frame.config(bg="white")

    name_file = "C:/Users/DELL/Desktop/PPS Code projects/Final project/Student interface/namesnew.csv"
    df = pd.read_csv(name_file, index_col="Roll No.")

    def on_hover(event):
        back_button['background'] = '#9f1a1f'
        back_button['foreground'] = 'white'
        back_button['font'] = 'Bahnschrift 15 bold'
    
    # Function to change button color when not hovering
    def off_hover(event):
        back_button['background'] = '#d2232a'
        back_button['foreground'] = 'white'
        back_button['font'] = 'Bahnschrift 15'

    def clear():
        Name['text'] = ' '
        sapidi['text'] = ' '
        subject['text'] = ' '
        score['text'] = ' '
        lade['text'] = ' '
        ladesc['text'] = ' '
        qsp['text'] = ' '
        qspsc['text'] = ' '
        eob['text'] = ' '
        eobsc['text'] = ' '
        pem['text'] = ' '
        pemsc['text'] = ' '
        perc['text'] = ' '
        gpa['text'] = ' '
        grd['text'] = ' '
        editor.place_forget()
        ledit.place_forget()
        qedit.place_forget()
        eedit.place_forget()
        pedit.place_forget()
        savebutton.place_forget()


    def back():
        go_back_func()
        clear()



    Name=Label(second_frame,text=" ",font=('Bahnschrift',12),bg="White")
    Name.place(x=250,y=100)    
    
    sapidi=Label(second_frame,text=" ",font=('Bahnschrift',12),bg="White")
    sapidi.place(x=500,y=100)
    
    subject=Label(second_frame,text=" ",font=('Bahnschrift',12),bg="White")
    subject.place(x=300,y=140)
    
    score=Label(second_frame,text=" ",font=('Bahnschrift',12),bg="White")
    score.place(x=550,y=140)
    
    lade=Label(second_frame,text=" ",font=('Bahnschrift',12),bg="White")
    lade.place(x=300,y=180)
    ladesc=Label(second_frame,text=" ",font=('Bahnschrift',12),bg="White")
    ladesc.place(x=560,y=180)
    
    qsp=Label(second_frame,text=" ",font=('Bahnschrift',12),bg="White")
    qsp.place(x=300,y=200)
    qspsc=Label(second_frame,text=" ",font=('Bahnschrift',12),bg="White")
    qspsc.place(x=560,y=200)
    
    eob=Label(second_frame,text=" ",font=('Bahnschrift',12),bg="White")
    eob.place(x=300,y=220)
    eobsc=Label(second_frame,text=" ",font=('Bahnschrift',12),bg="White")
    eobsc.place(x=560,y=220)
    
    pem=Label(second_frame,text=" ",font=('Bahnschrift',12),bg="White")
    pem.place(x=300,y=240)
    pemsc=Label(second_frame,text=" ",font=('Bahnschrift',12),bg="White")
    pemsc.place(x=560,y=240)

    perc=Label(second_frame,text=" ",font=('Bahnschrift',12),bg="White")
    perc.place(x=300,y=260)

    gpa=Label(second_frame,text=" ",font=('Bahnschrift',12),bg="White")
    gpa.place(x=300,y=280)

    grd=Label(second_frame,text=" ",font=('Bahnschrift',12),bg="White")
    grd.place(x=380,y=280)    
    


    back_button = Button(second_frame,width=3,pady=1, text="<",font='Bahnschrift 15',bg='#d2232a',fg='white',border=0,cursor='hand2', command=back)
    back_button.place(x=1, y=1)

    back_button.bind('<Enter>', on_hover)
    back_button.bind('<Leave>', off_hover)

    ledit=Entry(second_frame, width=2, fg="black", border=1, bg="white", font=('Bahnschrift',12))    
    qedit=Entry(second_frame, width=2, fg="black", border=1, bg="white", font=('Bahnschrift',12))    
    eedit=Entry(second_frame, width=2, fg="black", border=1, bg="white", font=('Bahnschrift',12))    
    pedit=Entry(second_frame, width=2, fg="black", border=1, bg="white", font=('Bahnschrift',12))
    
    def flower():
        ledit.lower()
        qedit.lower()
        eedit.lower()
        pedit.lower()
    def flift():
        ledit.lift()
        qedit.lift()
        eedit.lift()
        pedit.lift()


    

    def on_enter(e):
        # Move focus to next Entry widget
        search()

    def on_focus_in_sap(event):
           sapin = event.widget
           if sapin.get() == 'SapID':
            sapin.delete(0, 'end')

    def on_focus_out_sap(event):
        pw=event.widget
        if sapin.get() =="" :
         sapin.insert(0, 'SapID')
         sapin.config(show="")

    sapin=Entry(second_frame, width=32, fg="black", border=1, bg="white", font=('Bahnschrift',12))
    sapin.bind("<FocusIn>", on_focus_in_sap)
    sapin.bind("<FocusOut>", on_focus_out_sap)
    sapin.bind("<Return>", on_enter)
    sapin.place(x=400,y=65)
    sapin.insert(0,'SapID')
    Frame(second_frame,width=295,height=2,bg='black').place(x=400,y=89)
    Label(second_frame,text="Enter Student SapID to view details",font=('Bahnschrift',12),bg="white").place(x=120,y=65)    
    def search():
        clear()
        flower()
        editbut()
        roll_no=sapin.get()
        if roll_no not in df.index:
            messagebox.showerror("Invalid", "Entered SapID does not exist")
            return
        else:
            
            Name['text'] = str('Name: ' + df.loc[roll_no, "Name"]+" "+df.loc[roll_no, "Last Name"])
            sapidi['text'] = "SapID: "+roll_no
            subject['text'] = "Subject"
            score['text'] = "Score"
            lade['text'] = 'LADE'
            ladesc['text'] = df.loc[roll_no, "LADE"]
            qsp['text'] = 'QSP'
            qspsc['text'] = df.loc[roll_no, "QSP"]
            eob['text'] = 'EOB'
            eobsc['text'] = df.loc[roll_no, "EOB"]
            pem['text'] = 'PEM'
            pemsc['text'] = df.loc[roll_no, "PEM"]
            
            pc= percent(df.loc[roll_no, "LADE"],df.loc[roll_no, "QSP"],df.loc[roll_no, "EOB"],df.loc[roll_no, "PEM"])
            perc['text'] = 'Percentage: '+pc

            ggp= calculate_gpa(df.loc[roll_no, "LADE"],df.loc[roll_no, "QSP"],df.loc[roll_no, "EOB"],df.loc[roll_no, "PEM"])
            gp= str(ggp)
            gpa['text'] = 'GPA: '+gp

            ggr= grade(ggp)
            grd['text'] = 'Grade: '+ggr
    
    

    def on_hoverf(event):
        find['background'] = '#9f1a1f'
        find['foreground'] = 'white'
        find['font'] = 'Bahnschrift 9 underline'
    
    # Function to change button color when not hovering
    def off_hoverf(event):
       find['background'] = '#d2232a'
       find['foreground'] = 'white'
       find['font'] = 'Bahnschrift 9' 

    
    find = Button(second_frame,width=8,pady=4, text="Search",fg="white",bg='#d2232a',border=0,cursor='hand2', command=search)
    find.place(x=700,y=65)
    find.bind('<Enter>', on_hoverf)
    find.bind('<Leave>', off_hoverf)
    
    def savechanges():
        roll_no=sapin.get()
        
        try:
            lmarks=int(ledit.get())
            qmarks=int(qedit.get())
            emarks=int(eedit.get())
            pmarks=int(pedit.get())
            if lmarks>50 or qmarks>50 or emarks>50 or pmarks>50:
                messagebox.showerror("Invalid Marks", "Only Enter Marks out 50")
                return
            
            else:
                
                confirmed = messagebox.askyesno("Confirmation", "Are you sure you want to save changes?")
                if confirmed:
                    messagebox.showwarning("Warning","This will change the marks of students")
                    print(lmarks+qmarks+emarks+pmarks)
                                
                    df.loc[roll_no, "LADE"] = lmarks
                    df.loc[roll_no, "QSP"] = qmarks
                    df.loc[roll_no, "EOB"] = emarks
                    df.loc[roll_no, "PEM"] = pmarks
                    df.to_csv(name_file)
                    messagebox.showinfo("Success","Changes Saved successfully")
                    
                    time=str(now)
                    role="Teacher"
                    activity="Changed marks of Student "+roll_no                    
                    with open(logfile, mode='a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow([time, Sapid, role, activity])
                    flower()
                    savebutton.place_forget()
                    editor.place(x=700,y=100)
                    ladesc['text'] = df.loc[roll_no, "LADE"]
                    qspsc['text'] = df.loc[roll_no, "QSP"]
                    eobsc['text'] = df.loc[roll_no, "EOB"]
                    pemsc['text'] = df.loc[roll_no, "PEM"]

                    pc= percent(df.loc[roll_no, "LADE"],df.loc[roll_no, "QSP"],df.loc[roll_no, "EOB"],df.loc[roll_no, "PEM"])
                    perc['text'] = 'Percentage: '+pc

                    ggp= calculate_gpa(df.loc[roll_no, "LADE"],df.loc[roll_no, "QSP"],df.loc[roll_no, "EOB"],df.loc[roll_no, "PEM"])
                    gp= str(ggp)
                    gpa['text'] = 'GPA: '+gp

                    ggr= grade(ggp)
                    grd['text'] = 'Grade: '+ggr
                else:
                    return

                    

        except ValueError:
            messagebox.showerror("Invalid", "Enter only Integers for Marks")
            return

        print("botton")

    savebutton= Button(second_frame,width=12,pady=4, text="Save Changes",fg="white",bg='#d2232a',border=0,cursor='hand2', command=savechanges)
    def edit():
        flift()
        editor.place_forget()

        roll_no=sapin.get()
        
        ledit.place(x=560,y=180)
        ledit.delete(0,'end')
        ledit.insert(0,df.loc[roll_no, "LADE"])
        
        qedit.place(x=560,y=200)
        qedit.delete(0,'end')
        qedit.insert(0,df.loc[roll_no, "QSP"])
        
        eedit.place(x=560,y=220)
        eedit.delete(0,'end')
        eedit.insert(0,df.loc[roll_no, "EOB"])

        pedit.place(x=560,y=240)
        pedit.delete(0,'end')
        pedit.insert(0,df.loc[roll_no, "PEM"])

        
        def on_hovere(event):
            savebutton['background'] = '#9f1a1f'
            savebutton['foreground'] = 'white'
            savebutton['font'] = 'Bahnschrift 9 underline'
    
        # Function to change button color when not hovering
        def off_hovere(event):
           savebutton['background'] = '#d2232a'
           savebutton['foreground'] = 'white'
           savebutton['font'] = 'Bahnschrift 9' 

    
        
        savebutton.place(x=700,y=100)
        savebutton.bind('<Enter>', on_hovere)
        savebutton.bind('<Leave>', off_hovere)

    
    editor = Button(second_frame,width=8,pady=4, text="Edit",fg="white",bg='#d2232a',border=0,cursor='hand2', command=edit)
    def editbut():
        def on_hovere(event):
            editor['background'] = '#9f1a1f'
            editor['foreground'] = 'white'
            editor['font'] = 'Bahnschrift 9 underline'
    
        # Function to change button color when not hovering
        def off_hovere(event):
           editor['background'] = '#d2232a'
           editor['foreground'] = 'white'
           editor['font'] = 'Bahnschrift 9' 

    
        
        editor.place(x=700,y=100)
        editor.bind('<Enter>', on_hovere)
        editor.bind('<Leave>', off_hovere)





    
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
        back_button['font'] = 'Bahnschrift 15 bold'
    
    # Function to change button color when not hovering
    def off_hover(event):
        back_button['background'] = '#d2232a'
        back_button['foreground'] = 'white'
        back_button['font'] = 'Bahnschrift 15'

    back_button = Button(frame3,width=3,pady=1, text="<",font='Bahnschrift 15',bg='#d2232a',fg='white',border=0,cursor='hand2', command=go_back_home_func)
    back_button.place(x=1, y=1)

    back_button.bind('<Enter>', on_hover)
    back_button.bind('<Leave>', off_hover)
    
    with open("C:/Users/DELL/Desktop/PPS Code projects/Final project/App/Mar.txt", "r") as file1:
        txt=file1.read()

    Noticeb=Text(frame3,border=2,height=6, width=50,font='Bahnschrift 12')
    Noticeb.place(x=250,y=100)
    Noticeb.insert("1.0",txt)
    
    


    def savenb():

        confirmed = messagebox.askyesno("Confirmation", "Are you sure you want to save changes?")
        if confirmed:    
            messagebox.showwarning("Warning","This will Update the Notice board with new message")      
        
            nb=Noticeb.get("1.0", "end")
                    
            time=str(now)
            role="Teacher"
            activity="Updated Noticeboard "                    
            with open(logfile, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([time, Sapid, role, activity])

            nbfile=open('C:/Users/DELL/Desktop/PPS Code projects/Final project/App/Mar.txt','w+')
            nbfile.write(nb)
            nbfile.close
            messagebox.showinfo("Success","Changes Saved successfully")
        else:
            return


    def on_hover(event):
        saveit['background'] = '#9f1a1f'
        saveit['foreground'] = 'white'
        saveit['font'] = 'Bahnschrift 12 underline'
    
    # Function to change button color when not hovering
    def off_hover(event):
        saveit['background'] = '#d2232a'
        saveit['foreground'] = 'white'
        saveit['font'] = 'Bahnschrift 12'

    saveit = Button(frame3,padx=3,pady=1, text="Save Message",font='Bahnschrift 12',bg='#d2232a',fg='white',border=0,cursor='hand2', command=savenb)
    saveit.place(x=325, y=250)

    saveit.bind('<Enter>', on_hover)
    saveit.bind('<Leave>', off_hover)
    return frame3

def go_back_home(frame3, home_frame):
    frame3.place_forget()
    home_frame.place(x=0,y=75)

def go_chat(home_frame, frame3):
    home_frame.place_forget()
    frame3.place(x=0,y=75)

#Database load----------------------------------------------

# Define file names
password_file = "C:/Users/DELL/Desktop/PPS Code projects/Final project/Student interface/passwords -t.csv"
name_file = "C:/Users/DELL/Desktop/PPS Code projects/Final project/Student interface/names -t.csv"

# Load data from files
passwords_df = pd.read_csv(password_file, index_col="Sapid")
names_df = pd.read_csv(name_file, index_col="Sapid")
with open("C:/Users/DELL/Desktop/PPS Code projects/Final project/Temp.txt", "r") as file1:
    Sapid=file1.read()


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
app.title("MPSTME Faculty Interface")
app.geometry('925x500+300+200')
app.resizable(False,False)

hi=Label(app,text=greeting+names_df.loc[Sapid, "Name"],font=('Bahnschrift',20,'bold')) # Add '+names_df.loc[Sapid, "Last Name"]
hi.place(x=300,y=20)
img=PhotoImage(file='C:/Users/DELL/Desktop/PPS Code projects/Final project/App/log.png')
Label(app,image=img).place(x=25,y=10)


im1=PhotoImage(file='C:/Users/DELL/Desktop/PPS Code projects/Final project/App/graduated.png')
im2=PhotoImage(file='C:/Users/DELL/Desktop/PPS Code projects/Final project/App/notice.png')
chatroom1=PhotoImage(file='C:/Users/DELL/Desktop/PPS Code projects/Final project/App/Chatoff.png')
chatroom2=PhotoImage(file='C:/Users/DELL/Desktop/PPS Code projects/Final project/App/chaton.png')


home_frame = create_home_frame(app, lambda: go_to_next_frame(home_frame, second_frame),lambda:go_chat(home_frame, frame3),im1,im2)
second_frame = create_second_frame(app, lambda: go_back(second_frame, home_frame))
frame3= create_frame3(app,lambda:go_back_home(frame3, home_frame))

logs=open('C:/Users/DELL/Desktop/PPS Code projects/Final project/his.txt','a+')
now=datetime.datetime.now()

logentry=str(now)+" Teacher: [ "+str(Sapid)+" ] has logged in\n"
print(logentry)
logs.write(logentry)
logs.close()


logfile='C:/Users/DELL/Desktop/PPS Code projects/Final project/logs.csv'
time = str(now)
role = "Teacher"
activity = "logged in"

with open(logfile, mode='a', newline='') as file:
  writer = csv.writer(file)
  writer.writerow([time, Sapid, role, activity])


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
    time = str(now)
    role = "Teacher"
    activity = "logged out"

    with open(logfile, mode='a', newline='') as file:
      writer = csv.writer(file)
      writer.writerow([time, Sapid, role, activity])
    
    
    messagebox.showinfo("Logged out","Logged out successfully")
    app.withdraw()

    
    subprocess.Popen(["python", "C:/Users/DELL/Desktop/PPS Code projects/Final project/Python Ultimate Student interface.py"])
    

logout = Button(app,width=10,pady=2, text="Logout",bg='#d2232a',fg='white',border=0,cursor='hand2', command=loglogout)
logout.place(x=860, y=20)
    
logout.bind('<Enter>', on_hover2)
logout.bind('<Leave>', off_hover2)

app.mainloop()
subprocess.Popen(["python", "C:/Users/DELL/Desktop/PPS Code projects/Final project/Python Ultimate Student interface.py"])
'''# Load data from files
passwords_df = pd.read_csv(password_file, index_col="Sapid")
names_df = pd.read_csv(name_file, index_col="Sapid")
with open("C:/Users/DELL/Desktop/PPS Code projects/Final project/Temp.txt", "r") as file1:
    Sapid=file1.read()
    

app=Tk()
app.title("MPSTME Teacher Interface")
app.geometry('925x500+300+200')
app.config(bg="white")
app.resizable(False,False)
Label(app,text='Hello '+names_df.loc[Sapid, "Name"], bg='#fff',font=('Bahnschrift',43,'bold')).pack(expand=True)
app.mainloop()
file1.close()'''