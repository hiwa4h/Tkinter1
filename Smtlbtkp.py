from tkinter.ttk import *
import tkinter as tk
import smtplib
import random
from tkinter import messagebox





def ligma_balls():
    global e1, b1, r
    
    try:
            
        chars = "1234567890"
        len = 6
        r = "".join(random.sample(chars, len))

        gmail = ""
        password = ""

        gmail_user = gmail
        gmail_password = password
        sent_from = gmail
        to = e.get()
        subject = "6 digit verfication code!"
        body = "code:" + r

        email_text = """
        From: %s
        To: %s
        Subject: %s

        %s
        """ % (sent_from, ", ".join(to), subject, body)



        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()
        
        
        
        
        l1 = Label(root, text='6 digit verfication code has been sent to your email')
        l1.place(x=180,y=210)
        e1 = Entry(root)
        e1.place(x=180, y=140)
        b1 = Button(root, text='subscribe', command=nigga_balls)
        b1.place(x=190, y=170)
    except smtplib.SMTPRecipientsRefused:
        messagebox.showerror('error', 'enter a valid  address')
        

def nigga_balls():
    if r in e1.get():
        messagebox.showinfo('Success', 'Successfully Subscribed')
    else:
        messagebox.showerror('Fail', 'Enter a Valid Code')
    

root = tk.Tk()
root.geometry('500x300')

l1 = tk.Label(root, text='Enter info to get subscription', font=('Bold', '24'))
l1.place(x=60, y=20)

e = Entry(root)
e.place(x=180, y=60)

l = Label(root, text='Email:')
l.place(x=140, y=60)

b = Button(root, text='send', command=ligma_balls)
b.place(x=200, y=100)



root.mainloop()
