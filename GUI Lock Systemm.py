from tkinter import *
import os

def encrypt():
    import PyPDF2
    theFile = open(file2, "rb")

    reader = PyPDF2.PdfFileReader(theFile)
    PageNo = reader.getNumPages()
    page = reader.getPage(0)
    text = page.extractText()

    def vigenerecipher(otext, keyword):

        key = keyword
        kl = list(keyword)
        text = "".join(otext.split())

        if len(text) != len(keyword):
            for i in range(len(text) - len(keyword)):
                key = key + kl[i]
                kl.append(kl[i])

        cipheredtext = ""
        letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                   "t", "u", "v",
                   "w", "x", "y", "z"]

        for i in range(len(text)):
            cipher = 0
            ltpos = 0
            lkpos = 0
            if text[i].isalpha() == True:
                if text[i].islower() == True:
                    for j in range(len(letters)):
                        if text[i] == letters[j]:
                            ltpos = j
                        if key[i] == letters[j]:
                            lkpos = j
                    cipher = ltpos + lkpos
                    cipher = cipher % 26
                    cipheredtext = cipheredtext + letters[cipher]
                elif text[i].isupper() == True:
                    for q in range(len(letters)):
                        letters[q] = letters[q].upper()
                    for j in range(len(letters)):
                        if text[i] == letters[j]:
                            ltpos = j
                        if key[i] == letters[j]:
                            lkpos = j
                    cipher = ltpos + lkpos
                    cipher = cipher % 26
                    cipheredtext = cipheredtext + letters[cipher]
            else:
                cipheredtext = cipheredtext + text[i]
        for i in range(len(otext)):
            if otext[i] == " ":
                cipheredtext = cipheredtext[:i] + " " + cipheredtext[i:]

        print(cipheredtext)

    vigenerecipher(text, password1)



def browse_file():
    global f3
    global file2
    from tkinter import filedialog
    file1= filedialog.askopenfile()
    file2= file1.name
    f3= open(file2)


def lock():
    sc5=Toplevel(sc4)
    sc5.geometry("400x300")
    sc5.title("Lock Files")
    Label(sc5,text="Browse Files from your device",width="400",height="2",bg="Light Blue",font=("Calibri","20")).pack()
    Label(sc5,text="").pack()
    Label(sc5, text="").pack()
    Button(sc5,text="Browse Files",width="30",height="1",activebackground="Yellow",activeforeground="Blue",command=browse_file).pack()
    Button(sc5,text="Lock it!!!",width="38",height="1",activebackground="Yellow",activeforeground="Blue",command=encrypt).pack()


def nextpage():
    global sc4
    sc3.destroy()
    sc2.destroy()
    sc4=Toplevel(sc)
    sc4.geometry("400x300")
    sc4.title("Secure it!")
    Label(sc4,text="Choose to Lock or Unlock",bg="Grey",width="400",height="4").pack()
    Label(sc4,text="").pack()
    Label(sc4, text="").pack()
    Button(sc4,text="Lock",width="10",height="2",activebackground="Grey",activeforeground="blue",command=lock).pack()
    Label(sc4,text="").pack()
    Label(sc4, text="").pack()
    Button(sc4,text="Unlock",width="10",height="2",activebackground="Grey",activeforeground="blue").pack()

def login_success():
    global sc3
    sc3=Toplevel(sc2)
    sc3.geometry("300x150")
    sc3.title("Login Success")
    Label(sc3,text="").pack()
    Label(sc3,text="You've Logged in successfully",font=("calibri","12")).pack()
    Label(sc3,text="").pack()
    Button(sc3,text="Proceed",command=nextpage).pack()

def login_fail():
    Label(sc2,text="Wrong Password, Please try again").pack()

def login_no_username():
    Label(sc2,text="Username not found")


def logged_in():
    global password1
    username1=username_verify.get()
    password1=password_verify.get()

    username_entry1.delete(0,END)
    password_entry1.delete(0,END)

    array_of_files=os.listdir()
    if username1 in array_of_files:
        f1=open(username1,"r")
        check=f1.read().splitlines()
        if password1 in check:
            login_success()
        else:
            login_fail()
    else:
        login_no_username()


def signed():
    name_details=Name.get()
    username_details=username.get()
    password_details=password.get()

    f=open(username_details,"w")
    f.write(name_details+"\n")
    f.write(username_details+"\n")
    f.write(password_details)
    f.close()

    name_entry.delete(0,END)
    username_entry.delete(0,END)
    password_entry.delete(0,END)

    Label(sc1,text="Your Registration is successfull",font=("calibri","12")).pack()

def login():
    global sc2
    global username_verify
    global password_verify
    global username_entry1
    global password_entry1

    sc2=Toplevel(sc)
    sc2.geometry("400x250")
    sc2.title("Login")

    username_verify=StringVar()
    password_verify=StringVar()

    Label(sc2, text="Secure your files in seconds", bg="Maroon", width="400", height="3", font=("calibri", "12")).pack()
    Label(sc2,text="").pack()
    Label(sc2, text="Username: ").pack()
    username_entry1=Entry(sc2, textvariable=username_verify)
    username_entry1.pack()
    Label(sc2, text="Password: ").pack()
    password_entry1 = Entry(sc2, textvariable=password_verify)
    password_entry1.pack()
    Label(sc2, text="").pack()
    Button(sc2, text="Login", width="10", height="1", command=logged_in ).pack()




def signup():

    global username
    global Name
    global password
    global name_entry
    global username_entry
    global password_entry
    global sc1
    sc1=Toplevel(sc)
    sc1.title("Sign Up")
    sc1.geometry("400x300")

    Name=StringVar()
    username=StringVar()
    password=StringVar()

    Label(sc1,text="Secure your files in seconds",bg="Maroon",width="400",height="3",font=("calibri","12")).pack()
    Label(sc1,text="").pack()
    Label(sc1,text="Name: ").pack()
    name_entry=Entry(sc1,textvariable=Name)
    name_entry.pack()
    Label(sc1,text="Username: ").pack()
    username_entry=Entry(sc1,textvariable=username)
    username_entry.pack()
    Label(sc1,text="Password: ").pack()
    password_entry=Entry(sc1,textvariable=password)
    password_entry.pack()
    Label(sc1,text="").pack()
    Button(sc1,text="Register",width="10",height="1",command=signed ).pack()




def first_screen():
    global sc

    sc=Tk()
    sc.geometry("500x350")
    sc.title("Urmp Lock System")
    Label(text="U R M P",bg="Gold",width="400",height="3",font=("calibri","20")).pack()
    Label(text="").pack()
    Label(text="").pack()
    Button(text="Login",height="3",width="15",activebackground="Grey",activeforeground="Purple",command=login ).pack()
    Label(text="").pack()
    Label(text="").pack()
    Button(text="Sign up",height="3",width="15",activebackground="Grey",activeforeground="Purple",command=signup ).pack()



    sc.mainloop()
first_screen()
