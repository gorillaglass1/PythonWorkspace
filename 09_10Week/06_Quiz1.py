from tkinter import *

def process(x):
    global display
    if x == "=":
        temp = eval(display.get())
        display.delete(0, END)
        display.insert(0, str(temp))
    elif x == "C":
        display.delete(0, END)
    else :
        display.insert("end", x)


window = Tk()
window.title("My Calculator")

display = Entry(window, width=35, bg="yellow")
display.grid(row=0, column=0, columnspan=5)

button_list = [
    "7", "8", "9", "/", "C",
    "4", "5", "6", "*", " ",
    "1", "2", "3", "-", " ",
    "0", ".", "=", "+", " "
]

row_index = 1
col_index = 0

for i in range(len(button_list)):
    button = Button(window, text=button_list[i], width=5, height=2, command=(lambda x=button_list[i]:process(x)))
    button.grid(row=row_index, column=col_index)

    col_index += 1
    if col_index > 4:
        col_index = 0
        row_index += 1

window.mainloop()