import tkinter as tk
import json
import smtplib
from email.mime.text import MIMEText
#import tkinter as ttk
#from ttk import *
mail_list = []
def send_emails(b_group):
    f = open("students.json")
    data = json.load(f)

    for i in data:
        if i['b'] == b_group:
            mail_list.append(i['u']+"iitk.ac.in")
    
    s = smtplib.SMTP('smtp.cc.iitk.ac.in',25)
    s.starttls()
    s.login('blah','12345')
    recipients = ", ".join(mail_list)
    email_message = "URGENT: There is an urgent need of blood group "+b_group+" Please visit HC to donate"
    username = 'blah'
    s.sendmail(username, recipients, email_message)

    print("Emails Sent to students with "+b_group)

if __name__ == '__main__':

    root = tk.Tk()
    root.title("Mailing System for Blood Donation")

    # Add a grid
    mainframe = tk.Frame(root)
    mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
    mainframe.columnconfigure(0, weight = 1)
    mainframe.rowconfigure(0, weight = 1)
    mainframe.pack(pady = 150, padx = 150)

    # Create a Tkinter variable
    tkvar = StringVar(root)

    # Dictionary with options
    choices = { 'A+','B+','O+','AB+','A-','B-','O-','AB-'}
    tkvar.set(' ') # set the default option

    popupMenu = OptionMenu(mainframe, tkvar, *choices)
    Label(mainframe, text="Choose Blood Group").grid(row = 1, column = 1)
    popupMenu.grid(row = 2, column =1)

    # on change dropdown value
    def change_dropdown(*args):
        print( tkvar.get() )

    send_emails(tkvar.get)
    # link function to change dropdown
    tkvar.trace('w', change_dropdown)

    button = Button(window, text = 'Send Emails', command = send_emails(tkvar.get))
    root.mainloop()
