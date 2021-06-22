import tkinter as tk
from tkinter import ttk

def create_window():
    main_window = tk.Tk()
    menubar = tk.Menu(main_window)

    menubar.add_command(label="Quit", command=main_window.destroy)

    main_window.config(menu=menubar)
    return main_window
