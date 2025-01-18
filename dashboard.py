""" Run this file to open the main apps dashboard """

import tkinter as tk
from tkinter import *

def run_app():
    # Create the main window
    window = Tk()
    window.state("zoomed")              # set the window to fullscreen

    # Add the menu
    menu = Menu(window)
    window.config(menu=menu)
    file_menu = Menu(menu)
    menu.add_cascade(label="File", menu=file_menu)
    view_menu = Menu(menu)
    menu.add_cascade(label="View", menu=view_menu)
    
    # TODO: add command to redirect to dashboard
    file_menu.add_command(label="Import CSV")
    file_menu.add_command(label="Close App", command=window.destroy)

    # TODO: add command to redirect to dashboard
    view_menu.add_command(label="Dashboard")
    

    dash_button = tk.Button(window, text="Dashboard", command=window.destroy)
    dash_button.pack()

    # Open the window
    window.mainloop()


if __name__ == "__main__":
    run_app()