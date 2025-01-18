""" Run this file to open the main apps dashboard """

import tkinter as tk
from tkinter import *

def run_app():
    # Create the main window
    window = Tk()

    menu = Menu(window)
    window.config(menu=menu)
    dash_menu = Menu(menu)
    menu.add_cascade(label="Dashboard", menu=dash_menu)

    # TODO: add command
    dash_menu.add_command(label="Open")
    

    dash_button = tk.Button(window, text="Dashboard", command=window.destroy)
    dash_button.pack()

    # Open the window
    window.mainloop()


if __name__ == "__main__":
    run_app()