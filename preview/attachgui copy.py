from tkinter import *
from tkinter102 import MyGui

#main app winow
mainwin = Tk()
Label(mainwin, text=__name__).pack()

# popup window
popup = Toplevel()
Label(popup, text='Attach').pack(side=LEFT)
MyGui(popup).pack(side=RIGHT)                # attach my frame
mainwin.mainloop()