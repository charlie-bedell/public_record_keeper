from tkinter import mainloop
from tkinter.messagebox import showinfo
from tkinter102 import MyGui

class CustomGui(MyGui):    # inherit init
    def reply(self):       # replace reply
        showinfo(title='popup', message='ouch!')

if __name__ == '__main__':
    # CustomGui().pack()      # this is the example in the book but it doesnt work, class must be instantiated first
    gui = CustomGui()
    gui.pack()
    mainloop()