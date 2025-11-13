from tkinter import *

root_window = Tk()
root_window.geometry('300x200')
root_window.title('My first Window')

msg = Label(root_window, text='PY50025_Ajinkya Patil')
msg.grid(row=0, column=0)

root_window.mainloop()

