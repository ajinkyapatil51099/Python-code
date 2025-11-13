from tkinter import *


def ok_button_handler():
    print('OK BUTTON IS CLICKED')

root_window = Tk()
root_window.title('Push Button demo')
root_window.geometry('700x500')


ok_button = Button(root_window)
ok_button.configure(text = 'Ok', command=ok_button_handler)
ok_button.grid(row=0, column=0)

print('ATA CONTROL FLOW root_window.mainloop() MADHE JAT AHE')
root_window.mainloop()
print('MALA TERMINATE HO  - ASHI ADNYA ALI')
