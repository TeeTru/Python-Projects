# Python Ver:    3.10.4
#
# Author:        Teran Trujillo
#
# Purpose:       Student Tracking System Demo. Demonstrating OOP, Tkinter GUI module,
#                using Tkinter Parent and Child relationships
#
# Tested OS:     This code was written and tested to work with Windows 10.


from tkinter import *
import tkinter as tk
from tkinter import messagebox


#importing our other modules
#so we can have access to them
import studenttracker_gui
import studenttracker_func



# Frame is the Tkinter fram class that our class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define our master frame configuration
        self.master = master
        self.master.minsize(600,400) #(Height, Width)
        self.master.maxsize(600,400)
        # This CenterWindow method will center our app on the user's screen
        studenttracker_func.center_window(self,600,400)
        self.master.title("the Tkinter Student Tracker Demo")
        self.master.configure(bg="#F0F0F0")
        # This protocol method is a tkinter built-in method to catch if
        #the user clicks the upper corner, "X" on Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: studenttracker_func.ask_quit(self))
        arg = self.master

        # load in the GUI widget from a seperate module,
        # keeing your code comparmetnalized and clutter free
        studenttracker_gui.load_gui(self)

        
if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
