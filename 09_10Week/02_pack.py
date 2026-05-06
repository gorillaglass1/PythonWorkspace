from tkinter import *

window = Tk()
Label(window, text="박스 #1", fg="white", bg="red").pack()
Label(window, text="박스 #2", fg="black", bg="green").pack()
Label(window, text="박스 #3", fg="white", bg="blue").pack()

Button(window, text="박스 #1", fg="black", bg="red").pack(side=LEFT)
Button(window, text="박스 #2", fg="black", bg="green").pack(side=LEFT)
Button(window, text="박스 #3", fg="black", bg="blue").pack(side=LEFT)

window.mainloop()