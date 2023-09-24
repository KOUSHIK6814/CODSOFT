from tkinter import *
from random import randint
import tkinter.messagebox

root = Tk()
root.title("PASSWORD GENERATOR")
root.geometry("500x500")


def new_rand():
    pw_entry.delete(0, END)
    pw_length = int(my_entry.get())
    my_password = ""
    for x in range(pw_length):
        my_password += chr(randint(33, 126))

    pw_entry.insert(0, my_password)


def clipper():
    print("Hello " + str(my_name.get()) + " This is Your password " + str(pw_entry.get()))
    root.clipboard_clear()
    root.clipboard_append(pw_entry.get())
    tkinter.messagebox.showinfo("PassWord", "The PassWord Copied")


name = LabelFrame(root, text="Your Name Please")
name.pack(pady=20)

my_name = Entry(name, font=("Helvetica", 24))
my_name.pack(pady=20, padx=20)

lf = LabelFrame(root, text="How many Characters?: ")
lf.pack(pady=20)

my_entry = Entry(lf, font=("Helvetica", 24))
my_entry.pack(pady=20, padx=20)

pw_entry = Entry(root, text="", font=("Helvetica", 24), bd=0, bg="systembuttonface")
pw_entry.pack(pady=20)

my_frame = Frame(root)
my_frame.pack(pady=20)

my_button = Button(my_frame, text="Generate Strong Password", command=new_rand)
my_button.grid(row=0, column=0, padx=10)

clip_button = Button(my_frame, text="Copy To Clipboard", command=clipper)
clip_button.grid(row=0, column=1, padx=10)
root.mainloop()
