from tkinter import *

root = Tk()
root.geometry("200x200")

class Person:
    def __init__(self, email, password):
        self.email    = email
        self.password = password

m_one = Person("hiwa@gmail.com", "hiw20")
e = Entry(root)
e.pack()

n = Entry(root)
n.pack()

def new_window():
    top = Toplevel()


def main():
    global e, n
    if e.get() == m_one.email:
        Label(root, text="drsta", bg="green").pack()
    else:
        Label(root, text="xalata", bg="red").pack()
    if n.get() == m_one.password:
        Label(root, text="drsta", bg="green").pack()
        new_window()
    else:
        Label(root, text="xalata", bg="red").pack()
        



b = Button(root, text="submit", command=main)
b.pack()

root.mainloop()
