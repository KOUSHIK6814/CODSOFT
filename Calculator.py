from tkinter import *


def button_press(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)


def equals():
    global equation_text
    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total

    except SyntaxError:
        equation_label.set("Syntax Error")
        equation_text = ""

    except ZeroDivisionError:
        equation_label.set("Arithmetic Error")
        equation_text = ""


def clear():
    global equation_text
    equation_label.set("")
    equation_text = ""


window = Tk()
window.title("GUI CALCULATOR")
window.geometry("800x800")
window.config(bg="black")
photo = PhotoImage(file="codsoft_image1.png")
codsoft_photo = Label(image=photo)
codsoft_photo.pack(padx=20, pady=5)
equation_text = ""
equation_label = StringVar()
label = Label(window, textvariable=equation_label, bg="white",
              font=("consolas", 20), width=24, height=2)
label.pack(pady=15)

frame = Frame(window)
frame.pack()

button1 = Button(frame, text=1, height=4, width=9, font=35,
                 command=lambda: button_press(1), fg="red", bg="#87CEEB")
button1.grid(row=0, column=0)
button2 = Button(frame, text=2, height=4, width=9, font=35,
                 command=lambda: button_press(2), fg="red", bg="#87CEEB")
button2.grid(row=0, column=1)
button3 = Button(frame, text=3, height=4, width=9, font=35,
                 command=lambda: button_press(3), fg="red", bg="#87CEEB")
button3.grid(row=0, column=2)
button4 = Button(frame, text=4, height=4, width=9, font=35,
                 command=lambda: button_press(4), fg="red", bg="#87CEEB")
button4.grid(row=1, column=0)
button5 = Button(frame, text=5, height=4, width=9, font=35,
                 command=lambda: button_press(5), fg="red", bg="#87CEEB")
button5.grid(row=1, column=1)
button6 = Button(frame, text=6, height=4, width=9, font=35,
                 command=lambda: button_press(6), fg="red", bg="#87CEEB")
button6.grid(row=1, column=2)
button7 = Button(frame, text=7, height=4, width=9, font=35,
                 command=lambda: button_press(7), fg="red", bg="#87CEEB")
button7.grid(row=2, column=0)
button8 = Button(frame, text=8, height=4, width=9, font=35,
                 command=lambda: button_press(8), fg="red", bg="#87CEEB")
button8.grid(row=2, column=1)
button9 = Button(frame, text=9, height=4, width=9, font=35,
                 command=lambda: button_press(9), fg="red", bg="#87CEEB")
button9.grid(row=2, column=2)
button0 = Button(frame, text=0, height=4, width=9, font=35,
                 command=lambda: button_press(0), fg="red", bg="#87CEEB")
button0.grid(row=3, column=0)
plus = Button(frame, text="+", height=4, width=9, font=35,
              command=lambda: button_press("+"), fg="red", bg="#87CEEB")
plus.grid(row=0, column=3)
minus = Button(frame, text="-", height=4, width=9, font=35,
               command=lambda: button_press("-"), fg="red", bg="#87CEEB")
minus.grid(row=1, column=3)
multiply = Button(frame, text="*", height=4, width=9, font=35,
                  command=lambda: button_press("*"), fg="red", bg="#87CEEB")
multiply.grid(row=2, column=3)
divide = Button(frame, text="/", height=4, width=9, font=35,
                command=lambda: button_press("/"), fg="red", bg="#87CEEB")
divide.grid(row=3, column=3)

equal = Button(frame, text="=", height=4, width=9, font=35,
               command=equals, fg="red", bg="#87CEEB")
equal.grid(row=3, column=2)
decimal = Button(frame, text=".", height=4, width=9, font=35,
                 command=lambda: button_press("."), fg="red", bg="#87CEEB")
decimal.grid(row=3, column=1)

clear = Button(window, text="clear", height=4, width=12, font=35,
               command=clear, fg="red", bg="#87CEEB")
clear.pack(pady=10)
window.mainloop()
